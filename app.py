import numpy as np
import pandas as pd
from flask import Flask, render_template, request, jsonify
from keras.models import load_model
from sklearn.preprocessing import LabelEncoder
from nltk.stem import PorterStemmer

# Load the datasets
train = pd.read_csv('Training.csv')
symptom_columns = train.columns[:-1]  # All symptom columns except the last (diagnosis)
diagnoses = train['prognosis'].unique()

# Initialize the Flask app
app = Flask(__name__)

# Load the trained model and label encoder
model = load_model('medical_diagnosis_bot.h5')
label_encoder = LabelEncoder()
label_encoder.classes_ = np.load('classes.npy', allow_pickle=True)

# Initialize the stemmer
stemmer = PorterStemmer()

# Function to encode symptoms into a vector
def encode_symptoms(symptoms, symptom_columns):
    symptoms_vector = np.zeros(len(symptom_columns))
    recognized_symptoms = []
    
    for symptom in symptoms:
        # We assume the input symptom should match the dataset column names
        if symptom in symptom_columns:
            index = list(symptom_columns).index(symptom)
            symptoms_vector[index] = 1
            recognized_symptoms.append(symptom)
        else:
            print(f"Warning: Symptom '{symptom}' not recognized.")
    
    return symptoms_vector, recognized_symptoms

# Prediction function
def predict_diagnosis(symptoms):
    symptoms_list = [symptom.strip().lower() for symptom in symptoms.split(",")]
    
    # Encode symptoms and get the recognized symptoms
    symptoms_vector, recognized_symptoms = encode_symptoms(symptoms_list, symptom_columns)
    
    # If no valid symptoms are found, return an error
    if len(recognized_symptoms) == 0:
        return "Error: No valid symptoms recognized. Please check your input."
    
    # Make prediction if valid symptoms are recognized
    prediction = model.predict(np.array([symptoms_vector]))
    predicted_label = label_encoder.inverse_transform([np.argmax(prediction)])
    
    return predicted_label[0]

# Routes
@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    symptoms = request.json.get('symptoms')
    try:
        diagnosis = predict_diagnosis(symptoms)
        return jsonify({'diagnosis': diagnosis})
    except Exception as e:
        return jsonify({'error': str(e)}), 400

if __name__ == '__main__':
    app.run(debug=True)

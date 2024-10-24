# Medical Diagnosis Bot

The **Medical Diagnosis Bot** is a machine learning-powered web application that predicts possible medical diagnoses based on symptoms provided by the user. The project uses a trained neural network model for diagnosis prediction and is deployed as a Flask web application.

## Features

- Predict medical diagnosis based on user-provided symptoms.
- Interactive web interface for entering symptoms and receiving diagnosis.
- Flask backend with a trained model and label encoder.
- Validation of symptoms input.
- Displays error messages for unrecognized symptoms.
- Clean and modern web interface with animations and buttons for navigation.

## Tech Stack

- **Backend**: Flask (Python)
- **Frontend**: HTML, CSS, JavaScript
- **Model**: Keras Sequential Model (trained on `Training.csv` dataset)
- **Data**: Training and testing datasets for symptom and diagnosis prediction.
- **Libraries**: 
  - Keras
  - Numpy
  - Pandas
  - Scikit-learn
  - NLTK (for stemming user input symptoms)

## Prerequisites

Before you begin, ensure you have the following installed:

- Python 3.12.4
- Flask
- Keras
- Numpy
- Pandas
- Scikit-learn
- NLTK

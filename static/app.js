// document.getElementById('diagnosis-form').addEventListener('submit', function(event) {
//     event.preventDefault();

//     const symptoms = document.getElementById('symptoms').value;
//     const resultDiv = document.getElementById('result');
//     resultDiv.innerHTML = "Processing...";  // Show a message while the diagnosis is being processed

//     fetch('/predict', {
//         method: 'POST',
//         headers: {
//             'Content-Type': 'application/json'
//         },
//         body: JSON.stringify({ symptoms: symptoms })
//     })
//     .then(response => response.json())
//     .then(data => {
//         resultDiv.innerHTML = `Diagnosis: <span style="color:#007BFF;">${data.diagnosis}</span>`;
//     })
//     .catch(error => {
//         console.error('Error:', error);
//         resultDiv.innerHTML = '<span style="color: red;">Error in getting the diagnosis. Please try again.</span>';
//     });
// });
document.getElementById('diagnosis-form').addEventListener('submit', function(event) {
    event.preventDefault();

    const symptoms = document.getElementById('symptoms').value;
    const resultDiv = document.getElementById('result');
    
    // Show a loading animation during the processing
    resultDiv.innerHTML = '<span class="loading">Processing...</span>';

    fetch('/predict', {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json'
        },
        body: JSON.stringify({ symptoms: symptoms })
    })
    .then(response => response.json())
    .then(data => {
        resultDiv.innerHTML = `Diagnosis: <span style="color:#007BFF;">${data.diagnosis}</span>`;
    })
    .catch(error => {
        console.error('Error:', error);
        resultDiv.innerHTML = '<span style="color: red;">Error in getting the diagnosis. Please try again.</span>';
    });
});

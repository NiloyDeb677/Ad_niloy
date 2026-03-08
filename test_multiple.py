import requests

url = "http://127.0.0.1:5000/predict"
data = {
    "name": "Test Patient",
    "age": 45,
    "sex": "male",
    "cp": "Non-anginal pain",
    "trestbps": 130,
    "chol": 250,
    "fbs": "Yes",
    "restecg": "ST-T Wave abnormality",
    "thalach": 187,
    "exang": "Yes",
    "oldpeak": 2.0,
    "slope": "Downsloping: signs of unhealthy heart",
    "ca": 2,
    "thal": "normal"
}

for i in range(25):
    try:
        response = requests.post(url, data=data)
        print(f"Request {i+1}: {response.status_code}")
    except Exception as e:
        print(f"Error on request {i+1}: {e}")

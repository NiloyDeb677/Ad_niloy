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
try:
    response = requests.post(url, data=data)
    print("Status Code:", response.status_code)
    if "result" in response.text.lower() or "predict" in response.text.lower():
        print("SUCCESS: prediction page returned successfully")
    elif response.status_code != 200:
        print("ERROR:", response.text[:200])
except Exception as e:
    print("Error during request:", e)

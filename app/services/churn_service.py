import joblib
import pandas as pd

MODEL_PATH = "models/churn_model.pkl"

model = joblib.load(MODEL_PATH)

def predict_churn(request):
    data = pd.DataFrame([request.dict()])

    prediction = model.predict(data)

    print("Input:")
    print(data)

    print("Prediction:")
    print(prediction)

    return {
        "prediction": str(prediction[0])
    }
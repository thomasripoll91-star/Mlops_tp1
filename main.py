from fastapi import FastAPI
from pydantic import BaseModel
import joblib

app = FastAPI()
model = joblib.load("regression.joblib")

class HouseData(BaseModel):
    taille: float
    chambres: int
    jardin: int

# @app.get("/predict")
# def predict_get():
#     return {"y_pred": 2}

@app.post("/predict")
def predict_model(data: HouseData):
    prediction = model.predict([[data.taille, data.chambres, data.jardin]])
    return {"y_pred": float(prediction[0])}
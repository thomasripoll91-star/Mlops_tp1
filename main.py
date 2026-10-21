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
    # La prédiction renvoie généralement un tableau numpy, on récupère le premier élément
    prediction = model.predict([[data.taille, data.chambres, data.jardin]])
    
    # On stocke la valeur dans une variable pour éviter d'appeler float() deux fois
    valeur_predite = float(prediction[0])
    
    return {
        "y_pred": valeur_predite,
        "commentaire": f"La valeur du bien est estimée à {valeur_predite}"
    }
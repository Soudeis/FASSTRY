from fastapi import FastAPI
from dateutil.relativedelta import relativedelta
from datetime import datetime

app = FastAPI()

# Route principale
@app.get("/")
def bonjour():
    return {"message": "Bonjour"}

# Nouvelle fonction utilisant dateutil
@app.get("/jours_restants")
def jours_restants_fin_annee():
    aujourd_hui = datetime.now()
    fin_annee = datetime(aujourd_hui.year, 12, 31)
    difference = relativedelta(fin_annee, aujourd_hui)
    return {
        "jours_restants": difference.days,
        "mois_restants": difference.months
    }

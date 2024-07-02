import os
from fastapi import FastAPI
from salary_ranges.registry import load_model, preprocess_data
app = FastAPI()
model = load_model()

@app.get("/")
def index():
    return {"ok": True}

@app.get("/predict")
def predict(input:str):

    input_ids, attention_mask = preprocess_data(input)
    y_pred = model.predict([input_ids, attention_mask])
    range_min = int(round(y_pred[0][0] / 1000))
    range_max = int(round(y_pred[0][1] / 1000))

    return {"range_min": range_min, "range_max": range_max}

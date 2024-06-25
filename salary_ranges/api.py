import tensorflow as tf
from fastapi import FastAPI
from transformers import AutoTokenizer, TFAutoModel

app = FastAPI()

@app.get("/")
def index():
    return {"ok": True}

model_path = "../models/model.keras"

model = tf.keras.load_model(model_path)
base_model_type = "deepset/gbert-base"

tokenizer = AutoTokenizer.from_pretrained(base_model_type, padding="right")

def preprocess_data(input:str):
    """Tokenizes and encodes input text.

    Parameters
    ----------
    input : str
        Text to encode

    Returns
    -------
    input_ids
    attention_mask
    """
    encodings = tokenizer(
        input,
        max_length=512,
        truncation=True,
        padding="max_length",
        return_tensors="tf"
        )

    input_ids = encodings["input_ids"]
    attention_mask = encodings["attention_mask"]

    return input_ids, attention_mask

@app.get("/predict")
def predict(input:str):
    input_ids, attention_mask = preprocess_data(input)
    y_pred = model.predict([input_ids, attention_mask])

    return y_pred

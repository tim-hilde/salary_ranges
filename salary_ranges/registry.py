import os
import tensorflow as tf
from tensorflow import keras
from transformers import AutoTokenizer, TFAutoModel

os.environ["TF_USE_LEGACY_KERAS"]="0"

tokenizer = AutoTokenizer.from_pretrained("deepset/gbert-base", padding="right")
base_model = TFAutoModel.from_pretrained("deepset/gbert-base", from_pt=True)

def load_model():
    model = tf.keras.saving.load_model("models/base_line.keras")
    # weights_path = "models/deepset_gbert-base_AdamW.weights.h5"

    # # creating model

    # # Eingangsdimensionen definieren
    # input_ids = tf.keras.layers.Input(shape=(512,),
    #                                 dtype=tf.int32,
    #                                 name="input_ids")
    # attention_mask = tf.keras.layers.Input(shape=(512,),
    #                                     dtype=tf.int32,
    #                                     name="attention_mask")

    # outputs = base_model(input_ids, attention_mask=attention_mask)
    # hidden_states = outputs.last_hidden_state
    # pooled_output = tf.reduce_mean(hidden_states, axis=1)

    # regression_output = tf.keras.layers.Dense(2,
    #                                         activation='linear',
    #                                         name='regression_output')(pooled_output)
    # model = tf.keras.Model(
    #     inputs=[input_ids, attention_mask],
    #     outputs=regression_output
    # )
    # model.load_weights(weights_path)

    return model


def preprocess_data(input:str):
    """Tokenizes and encodes input text.

    Parameters
    ----------
    input : str
        Text to encode
    base_model_name : str
        Base Model name to load tokenizer

    Returns
    -------
    input_ids: Any
    attention_mask: Any
    """

    # creating encodings
    encodings = tokenizer(
        input,
        max_length=512,
        truncation=True,
        padding="max_length",
        return_tensors="tf"
        )

    emb = base_model.predict(encodings)

    return emb["last_hidden_state"][:, 0, :]

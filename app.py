import os
import json
import librosa
import cv2
import numpy as np
import tensorflow as tf
import streamlit as st
from streamlit_extras.add_vertical_space import add_vertical_space
import sounddevice as sd
import wavio
from warnings import filterwarnings

filterwarnings('ignore')

# Load your pre-trained model once
model = tf.keras.models.load_model('model.h5')

# Load prediction mapping
with open('prediction.json', 'r') as f:
    prediction_dict = json.load(f)

def streamlit_config():
    st.set_page_config(
        page_title='Bird Sound Classification',
        page_icon='https://upload.wikimedia.org/wikipedia/commons/thumb/2/29/American_Robin.jpg/512px-American_Robin.jpg',
        layout='centered'
    )
    st.markdown("""
    <style>
    [data-testid="stHeader"] {
        background: rgba(0,0,0,0);
    }
    </style>
    """, unsafe_allow_html=True)
    st.markdown(
        """
        <div style="display: flex; align-items: center; justify-content: center;">
            <img src="https://is5-ssl.mzstatic.com/image/thumb/Purple117/v4/2d/38/05/2d380587-7a1a-6367-8216-ea7f79fc1731/source/512x512bb.jpg" style="width: 100px; height: 100px; margin-right: 10px;">
            <h1 style="text-align: center;">Bird Sound Classification</h1>
        </div>
        """,
        unsafe_allow_html=True
    )
    add_vertical_space(4)

def record_audio(duration=5, fs=44100):
    recording = sd.rec(int(duration * fs), samplerate=fs, channels=2)
    sd.wait()
    wavio.write("recorded_audio.wav", recording, fs, sampwidth=2)
    return "recorded_audio.wav"

def prediction(audio_file):
    audio, sr = librosa.load(audio_file, sr=22050)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=40)
    mfcc_mean = np.mean(mfcc, axis=1)
    mfcc_input = np.expand_dims(mfcc_mean, axis=0)  # shape (1, 40)
    mfcc_input = np.expand_dims(mfcc_input, axis=2)   # shape (1, 40, 1)
    mfcc_tensors = tf.convert_to_tensor(mfcc_input, dtype=tf.float32)
    
    pred = model.predict(mfcc_tensors)
    target_index = np.argmax(pred)
    predicted_class = prediction_dict.get(str(target_index), "Unknown")
    
    # Display the corresponding image
    image_path = os.path.join('Inference_Images', f'{predicted_class}.jpg')
    if os.path.exists(image_path):
        img = cv2.imread(image_path, cv2.IMREAD_COLOR)
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        img = cv2.resize(img, (350, 300))
        _, col2, _ = st.columns([0.1, 0.8, 0.1])
        with col2:
            st.image(img)
    else:
        st.error(f"Image for '{predicted_class}' not found.")
    
    st.markdown(f'<h3 style="text-align: center; color: green;">{predicted_class}</h3>', unsafe_allow_html=True)
    
    return predicted_class

# --- Streamlit App ---
streamlit_config()

_, col2, _ = st.columns([0.1, 0.9, 0.1])
with col2:
    input_audio = st.file_uploader("Upload a bird audio file", type=["mp3", "wav", "ogg"])
    record_button = st.button("Record Audio", key="record_button")

if record_button:
    recorded_file = record_audio()
    prediction(recorded_file)

if input_audio is not None:
    _, col2, _ = st.columns([0.2, 0.8, 0.2])
    with col2:
        prediction(input_audio)

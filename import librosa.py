import librosa
import numpy as np

def extract_mfcc(audio_file, n_mfcc=40):
    audio, sr = librosa.load(audio_file, sr=22050)
    mfcc = librosa.feature.mfcc(y=audio, sr=sr, n_mfcc=n_mfcc)
    mfcc_mean = np.mean(mfcc, axis=1)
    return mfcc_mean

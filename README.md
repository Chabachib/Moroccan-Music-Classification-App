# ![Morocco](frontend/public/morocco.ico) Moroccan Music Classification App

![Status](https://img.shields.io/badge/status-Production--Ready-brightgreen)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

A Full-stack AI system for classifying Moroccan music genres from
uploaded audio clips. The project combines deep learning (LSTM-based
sequence modeling), MFCC feature extraction, and a containerized Flask
inference API with a React frontend for real-time predictions.

Supports 7 Moroccan genres:
**Gnawa • Chaabi • Andalusian • Rai • Imazighn • Rap • Pop**

------------------------------------------------------------------------

# 📌 Overview

This project demonstrates:

-   End-to-end ML pipeline (data collection → preprocessing → training →
    deployment)
-   Sequence modeling using LSTM networks
-   Audio feature engineering using MFCC
-   REST API deployment for inference
-   Dockerized backend for reproducibility
-   Modular preprocessing pipeline for future extensibility

------------------------------------------------------------------------

# 🧠 Model Details

## Input Pipeline

-   Audio preprocessing, normalization and conversion to WAV
-   Segmentation into fixed-length windows (3 seconds)
-   MFCC feature extraction
-   Feature tensor fed into LSTM network

## Model Architecture

-   LSTM-based sequential model
-   Dropout regularization
-   Fully connected dense layer
-   Softmax output layer (7 classes)

Loss: Categorical Crossentropy
Optimizer: Adam

------------------------------------------------------------------------

# 📊 Model Performance

-   Dataset size: ~5,000+ audio clips
-   Classes: 7
-   Train/Test Split: 80/20
-   Final Test Accuracy: ~92-98%

------------------------------------------------------------------------

# ⚡ Inference Performance

-   Model loaded once at API startup
-   Average inference latency: \~100--200 ms per 3s segment
-   Segment-level predictions aggregated via majority voting
-   Supports audio files up to 100 MB

------------------------------------------------------------------------

# 🛠 Tech Stack

## AI & Data

-   TensorFlow / Keras (LSTM modeling)
-   Librosa (MFCC extraction)
-   Scikit-learn (evaluation metrics)
-   NumPy / Pandas (data handling)

## Backend

-   Flask (REST API)
-   CORS-enabled for frontend integration

## Frontend

-   React (Single-page application)

## DevOps

-   Docker (containerized backend)
-   Virtual environments
-   Modular project structure

------------------------------------------------------------------------

## Project Structure

```
Moroccan-Music-Classification-App/
├─ backend/
│  ├─ main.py
│  ├─ constants.py
│  ├─ requirements.txt
│  └─ Dockerfile
├─ frontend/
│  ├─ public/
│  ├─ src/
│  └─ package.json
└─ notebooks/
   ├─ download-songs.ipynb
   ├─ scrap-artists-names.ipynb
   ├─ scrap-artists-songs.ipynb
   ├─ trim-audio-and-convert-to-wav.ipynb
   └─ model-training.ipynb
```

------------------------------------------------------------------------

# 🔌 Backend API

### POST `/predict`

**Request** - multipart/form-data - Field: `file` - Supported formats:
wav, mp3, aac, flac

**Response Example** { "class": "gnawa" }

Error Example { "error": "File type not allowed" }

------------------------------------------------------------------------

# 🐳 Docker Deployment

cd backend\
docker build -t moroccan-music-backend .\
docker run -p 8989:8989 moroccan-music-backend

Backend runs at: http://127.0.0.1:8989

------------------------------------------------------------------------

```{=html}
<p align="center">
```
Built with ❤️ --- Chabachib
```{=html}
</p>
```

# Moroccan Music Genre Classification System

![Status](https://img.shields.io/badge/status-Production--Ready-brightgreen)
![Python](https://img.shields.io/badge/python-3.11+-blue)
![TensorFlow](https://img.shields.io/badge/TensorFlow-DeepLearning-orange)
![Docker](https://img.shields.io/badge/Docker-Containerized-blue)

A full-stack AI system for classifying Moroccan music genres from
uploaded audio clips. The system combines deep learning (LSTM-based
sequence modeling), MFCC feature extraction, and a containerized Flask
inference API with a React frontend for real-time predictions.

Supported genres:
**Gnawa • Chaabi • Andalusian • Rai • Imazighn • Rap • Pop**

------------------------------------------------------------------------

# Overview

This project demonstrates:

-   End-to-end ML pipeline (data collection → preprocessing → training →
    deployment)
-   Temporal sequence modeling using LSTM networks
-   Audio feature engineering using MFCC
-   REST API deployment for inference
-   Dockerized backend for reproducibility
-   Modular preprocessing pipeline for extensibility

------------------------------------------------------------------------

# System Architecture

User\
↓\
React Frontend (File Upload UI)\
↓\
Flask REST API (/predict)\
↓\
Audio Segmentation (3s windows)\
↓\
MFCC Feature Extraction\
↓\
LSTM Model Inference\
↓\
Segment Aggregation (Majority Vote)\
↓\
Predicted Genre

------------------------------------------------------------------------

# Features Used in Training

## Mel-Frequency Cepstral Coefficients (MFCC)

### What is MFCC?

MFCC (Mel-Frequency Cepstral Coefficients) is a representation of the
short-term power spectrum of a sound, computed via a linear cosine
transform of a log power spectrum on a nonlinear mel frequency scale.

### Why MFCC?

-   Approximates human auditory perception
-   Captures timbral texture critical for genre discrimination
-   Reduces dimensionality while preserving relevant frequency
    characteristics
-   More robust to noise compared to raw waveform input

### MFCC Parameters

-   `num_mfcc = 40`
-   `n_fft = 2048`
-   `hop_length = 512`
-   `num_segment = 10`

Each audio file is segmented into 3-second windows to capture temporal
variations and increase training sample diversity.

------------------------------------------------------------------------

# Model Architecture

The model is built using a Sequential architecture.

## LSTM Layers

### Layer 1

`LSTM(64, return_sequences=True)`

-   64 memory units
-   Outputs full sequence for stacking
-   Captures temporal dependencies across MFCC frames

### Layer 2

`LSTM(64)`

-   Further refines temporal feature extraction
-   Outputs condensed sequence representation

## Dense Layers

### Dense Layer

`Dense(64, activation='relu')`

-   Introduces non-linearity
-   Learns higher-level feature combinations

### Output Layer

`Dense(7, activation='softmax')`

-   7 units corresponding to 7 genres
-   Produces probability distribution across classes

------------------------------------------------------------------------

# Compilation & Training

-   Optimizer: `Adam(learning_rate=0.001)`
-   Loss Function: `sparse_categorical_crossentropy`
-   Metrics: `accuracy`

Training Configuration:

-   Batch Size: 32
-   Epochs: 60
-   Validation Split used to monitor generalization

------------------------------------------------------------------------

# Model Performance

-   Classes: 7
-   Train/Test Split: 80/20
-   Evaluation performed using Scikit-learn metrics
-   Accuracy and validation metrics available in `model-training.ipynb`

------------------------------------------------------------------------

# Inference Performance

-   Model loaded once at API startup
-   Segmented prediction aggregated via majority voting
-   Supports audio files up to 100MB

------------------------------------------------------------------------

# Tech Stack

## AI & Data

-   TensorFlow / Keras
-   Librosa
-   Scikit-learn
-   NumPy / Pandas

## Backend

-   Flask (REST API)
-   CORS enabled

## Frontend

-   React

## DevOps

-   Docker
-   Virtual environments

------------------------------------------------------------------------

# Project Structure

Moroccan-Music-Classification-App/ ├─ backend/ │ ├─ main.py │ ├─
constants.py │ ├─ requirements.txt │ └─ Dockerfile ├─ frontend/ │ ├─
public/ │ ├─ src/ │ └─ package.json └─ notebooks/ ├─
scrap-artists-names.ipynb ├─ scrap-artists-songs.ipynb ├─
download-songs.ipynb ├─ trim-audio-and-convert-to-wav.ipynb └─
model-training.ipynb

------------------------------------------------------------------------

# Backend API

## POST `/predict`

Request: - multipart/form-data - Field: `file` - Supported formats: wav,
mp3, aac, flac

Response Example: { "class": "gnawa" }

Error Example: { "error": "File type not allowed" }

------------------------------------------------------------------------

# Docker Deployment

cd backend\
docker build -t moroccan-music-backend .\
docker run -p 8989:8989 moroccan-music-backend

Backend runs at: http://127.0.0.1:8989

---
<p align="center">
  Developed with ❤️ from Chabachib
</p>

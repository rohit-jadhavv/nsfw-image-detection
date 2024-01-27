# NSFW Image Detection Chrome Extension and Flask Server

This project combines a Chrome extension for extracting image URLs from web pages and a Flask server for NSFW (Not Safe For Work) image detection using a trained model.

## Overview

The project aims to provide a solution for identifying NSFW images on web pages. It consists of a Chrome extension that extracts image URLs and sends them to a Flask server. The Flask server processes the images and uses a trained NSFW image detection model to classify them into categories such as hentai, sexy, porn, or neutral.

## Features

- NSFW image detection using a TensorFlow and Keras-based model.
- Chrome extension for seamless extraction of image URLs.
- Flask server for processing and predicting NSFW content.

## Prerequisites

Before getting started, ensure you have the following installed:

- Python 3.10 or above
- TensorFlow
- Flask
- Chrome browser

## Installation

1. Clone the repository:

    ```bash
    git clone https://github.com/yourusername/nsfw-image-detection.git
    ```

2. Install Python dependencies:

    ```bash
    cd nsfw-image-detection
    pip install -r requirements.txt
    ```

3. Set up the Chrome extension:
    - Open Chrome and go to `chrome://extensions/`.
    - Enable "Developer mode" in the top-right corner.
    - Click "Load unpacked" and select the `chrome-extension` folder from the cloned repository.

4. Run the Flask server:

    ```bash
    python app.py
    ```

5. Open the Chrome extension on a webpage and start extracting image URLs.

## Usage

1. **Extracting Image URLs:**
   - Navigate to a webpage with images.
   - Click on the Chrome extension icon.
   - The extension will extract image URLs and send them to the Flask server.

2. **Flask Server:**
   - The Flask server receives image URLs and processes them.
   - The NSFW image detection model predicts the content category.
   - Results are returned to the Chrome extension for display.

## Model Training

The NSFW image detection model is trained using TensorFlow and Keras. Here's a summary of the training process:

1. **Data Loading and Preprocessing:**
   - Image datasets for training (`train_ds`) and validation (`val_ds`) are created using `image_dataset_from_directory`.
   - The data is split into training and validation sets (80% training, 20% validation).
   - Class names are extracted from the dataset.

2. **Model Definition:**
   - A Sequential model is built with convolutional and max-pooling layers for feature extraction.
   - Dense layers with ReLU activation functions are added for classification.
   - The final layer has units equal to the number of classes.

3. **Model Compilation:**
   - The model is compiled using the Adam optimizer and sparse categorical cross-entropy loss function.
   - Accuracy is chosen as the evaluation metric.

4. **Model Training:**
   - The model is trained for 10 epochs on the training dataset with validation on the validation dataset.
   - Training progress, including loss and accuracy metrics, is monitored.

Adjustments to the model architecture and hyperparameters can be made based on performance evaluation.

## Chrome Extension

The Chrome extension serves as a convenient tool for extracting image URLs from web pages, facilitating the process of collecting data for NSFW image detection. Here's how it works:

1. **Installation:**
   - Navigate to `chrome://extensions/` in your Chrome browser.
   - Enable "Developer mode" in the top-right corner.
   - Click "Load unpacked" and select the `chrome-extension` folder from the cloned repository.

2. **Usage:**
   - Visit a webpage containing images you want to analyze for NSFW content.
   - Click on the Chrome extension icon in the browser toolbar.
   - The extension will extract image URLs from the page and send them to the Flask server for processing.

## Flask Server
The Flask server acts as an intermediary between the Chrome extension and the NSFW image detection model.


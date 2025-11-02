"""
AI-Driven Price Prediction using Bidirectional LSTM

This Python script provides a reference implementation for training and using
a Bi-directional LSTM model for price prediction.

To use this model in production:
1. Install dependencies: pip install tensorflow numpy pandas scikit-learn
2. Collect historical price data for training
3. Train the model with your data
4. Save the trained model
5. Deploy as a REST API using Flask or FastAPI
6. Update the Edge Function to call this API instead of using simple prediction

Note: The current implementation uses a simple prediction algorithm in the
Edge Function. This Python code is provided for future enhancement.
"""

import numpy as np
import pandas as pd
from tensorflow.keras.models import Sequential, load_model
from tensorflow.keras.layers import LSTM, Bidirectional, Dense, Dropout
from sklearn.preprocessing import MinMaxScaler
import os


class PricePredictionModel:
    def __init__(self, sequence_length=60):
        self.sequence_length = sequence_length
        self.scaler = MinMaxScaler(feature_range=(0, 1))
        self.model = None

    def build_model(self, input_shape):
        """Build Bidirectional LSTM model"""
        model = Sequential([
            Bidirectional(LSTM(128, return_sequences=True), input_shape=input_shape),
            Dropout(0.2),
            Bidirectional(LSTM(64, return_sequences=True)),
            Dropout(0.2),
            Bidirectional(LSTM(32, return_sequences=False)),
            Dropout(0.2),
            Dense(16, activation='relu'),
            Dense(1)
        ])

        model.compile(optimizer='adam', loss='mean_squared_error', metrics=['mae'])
        self.model = model
        return model

    def prepare_data(self, prices):
        """Prepare sequences for training"""
        scaled_data = self.scaler.fit_transform(np.array(prices).reshape(-1, 1))

        X, y = [], []
        for i in range(self.sequence_length, len(scaled_data)):
            X.append(scaled_data[i-self.sequence_length:i, 0])
            y.append(scaled_data[i, 0])

        X, y = np.array(X), np.array(y)
        X = np.reshape(X, (X.shape[0], X.shape[1], 1))

        return X, y

    def train(self, prices, epochs=50, batch_size=32, validation_split=0.2):
        """Train the model on historical price data"""
        X, y = self.prepare_data(prices)

        if self.model is None:
            self.build_model((X.shape[1], 1))

        history = self.model.fit(
            X, y,
            epochs=epochs,
            batch_size=batch_size,
            validation_split=validation_split,
            verbose=1
        )

        return history

    def predict(self, recent_prices):
        """Predict next price based on recent price history"""
        if len(recent_prices) < self.sequence_length:
            raise ValueError(f"Need at least {self.sequence_length} price points")

        # Use last sequence_length prices
        input_data = recent_prices[-self.sequence_length:]
        scaled_input = self.scaler.transform(np.array(input_data).reshape(-1, 1))

        X = np.reshape(scaled_input, (1, self.sequence_length, 1))

        # Make prediction
        scaled_prediction = self.model.predict(X, verbose=0)
        prediction = self.scaler.inverse_transform(scaled_prediction)

        return float(prediction[0][0])

    def save_model(self, filepath='bilstm_price_model.h5'):
        """Save trained model to file"""
        if self.model is not None:
            self.model.save(filepath)
            print(f"Model saved to {filepath}")

    def load_model(self, filepath='bilstm_price_model.h5'):
        """Load trained model from file"""
        if os.path.exists(filepath):
            self.model = load_model(filepath)
            print(f"Model loaded from {filepath}")
        else:
            raise FileNotFoundError(f"Model file not found: {filepath}")


def example_usage():
    """Example of how to use the model"""

    # Generate sample price data (in real usage, load from database)
    sample_prices = [100 + np.sin(i/10) * 10 + np.random.randn() * 2
                     for i in range(200)]

    # Initialize and train model
    model = PricePredictionModel(sequence_length=60)
    model.train(sample_prices, epochs=20)

    # Save the trained model
    model.save_model('bilstm_price_model.h5')

    # Make a prediction
    recent_prices = sample_prices[-60:]
    predicted_price = model.predict(recent_prices)
    print(f"Current price: ${sample_prices[-1]:.2f}")
    print(f"Predicted next price: ${predicted_price:.2f}")

    return model


# Flask API Example (for deployment)
"""
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load model at startup
predictor = PricePredictionModel()
try:
    predictor.load_model('bilstm_price_model.h5')
except:
    print("No pre-trained model found. Train a model first.")

@app.route('/predict', methods=['POST'])
def predict_price():
    data = request.json
    product_id = data.get('productId')
    prices = data.get('prices')

    if not prices or len(prices) < 60:
        return jsonify({'error': 'Need at least 60 historical prices'}), 400

    try:
        predicted_price = predictor.predict(prices)
        return jsonify({
            'productId': product_id,
            'predictedPrice': predicted_price
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/train', methods=['POST'])
def train_model():
    data = request.json
    prices = data.get('prices')

    if not prices or len(prices) < 100:
        return jsonify({'error': 'Need at least 100 prices for training'}), 400

    try:
        predictor.train(prices)
        predictor.save_model()
        return jsonify({'success': True, 'message': 'Model trained successfully'})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
"""


if __name__ == '__main__':
    print("BILSTM Price Prediction Model")
    print("This is a reference implementation.")
    print("Run example_usage() to see how to use the model.")

    # Uncomment to run example
    # example_usage()

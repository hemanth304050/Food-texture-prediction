from flask import Flask, render_template, request, jsonify
import pandas as pd
import numpy as np
import joblib
import os

app = Flask(__name__)

# Load model and scaler
model = joblib.load('model.pkl')
scaler = joblib.load('scaler.pkl')

LABELS = {0: 'Good', 1: 'Bad', 2: 'Worst'}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['GET', 'POST'])
def predict():
    if request.method == 'POST':
        try:
            # Get 6 inputs
            force = float(request.form['force'])
            vib_freq = float(request.form['vib_freq'])
            vib_amp = float(request.form['vib_amp'])
            sound_int = float(request.form['sound_int'])
            sound_freq = float(request.form['sound_freq'])
            moisture = float(request.form['moisture'])
            
            # Prepare input for prediction with correct feature names
            input_df = pd.DataFrame([[force, vib_freq, vib_amp, sound_int, sound_freq, moisture]], 
                                    columns=['Force', 'Vib_Freq', 'Vib_Amp', 'Sound_Int', 'Sound_Freq', 'Moisture'])
            input_scaled = scaler.transform(input_df)
            
            # Predict
            prediction = model.predict(input_scaled)[0]
            result = LABELS[prediction]
            
            return render_template('predict.html', result=result, inputs=request.form)
        except Exception as e:
            return render_template('predict.html', error=str(e))
            
    return render_template('predict.html')

@app.route('/dashboard')
def dashboard():
    # Load dataset details for display
    df = pd.read_csv('food_texture_data.csv')
    dataset_info = {
        'total_samples': len(df),
        'cols': list(df.columns),
        'head': df.head(10).to_dict(orient='records'),
        'counts': df['Label'].value_counts().to_dict()
    }
    
    # Map label counts to names
    dataset_info['counts'] = {LABELS[int(k)]: int(v) for k, v in dataset_info['counts'].items()}
    
    return render_template('dashboard.html', data_info=dataset_info)

if __name__ == '__main__':
    app.run(debug=True, port=5000)

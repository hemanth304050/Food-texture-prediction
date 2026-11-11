
<div align="center">🍎 FOOD TEXTURE PREDICTION SYSTEM

Food Texture Prediction Using Multiple Measurement and Template Data

🤖 An AI & Machine Learning Based Food Quality Prediction Web Application

<p>
  <img src="https://img.shields.io/badge/Python-3.10+-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/Flask-Web%20Framework-black?logo=flask" />
  <img src="https://img.shields.io/badge/Machine-Learning-orange" />
  <img src="https://img.shields.io/badge/Scikit--Learn-ML-red?logo=scikitlearn" />
  <img src="https://img.shields.io/badge/Status-Developed-success" />
</p><img src="assets/banner.gif" width="100%" alt="Food Texture Prediction Animated Banner" />🔗 Live Repository

""GitHub" (https://img.shields.io/badge/GitHub-Food--Texture--Prediction-181717?logo=github)" (https://github.com/hemanth304050/Food-texture-prediction)

"View Source Code" (https://github.com/hemanth304050/Food-texture-prediction)

</div>---

📌 About The Project

Food texture is an important factor in determining food quality, freshness, and consumer acceptability.

Traditional food quality evaluation methods often depend on manual observation and subjective judgment. To address this challenge, this project introduces an intelligent Food Texture Prediction System Using Multiple Measurement and Template Data.

This project uses multiple food measurement parameters and machine learning techniques to predict food quality categories.

The system is developed using Python, Flask, Pandas, NumPy, Scikit-learn, and Gaussian Process Classification.

It provides a web-based interface where users can enter measurement values and receive predicted food quality results.

🎯 Main Objectives

- Analyze food characteristics using multiple measurements.
- Develop a machine learning-based prediction model.
- Apply data preprocessing and feature scaling.
- Classify food quality into different categories.
- Provide a simple web interface for predictions.
- Display dataset information and model performance.

---

✨ Key Features

Feature| Description
📥 Multiple Measurements| Accepts six food measurement inputs
🧹 Data Preprocessing| Processes and scales input data
🤖 Machine Learning| Gaussian Process Classification
🔍 Prediction| Predicts Good, Bad or Worst
🌐 Web Application| Flask-based application
📊 Dashboard| Displays dataset information
📈 Model Evaluation| Accuracy, F1-score and Recall
📉 Confusion Matrix| Visualizes classification performance

---

🏗️ System Architecture

             🍎 FOOD SAMPLE
                   |
                   ▼
          📥 MEASUREMENT INPUT
                   |
                   ▼
        📊 MULTIPLE PARAMETERS
                   |
                   ▼
          🧹 DATA PREPROCESSING
                   |
                   ▼
           ⚙️ FEATURE SCALING
                   |
                   ▼
       🤖 GAUSSIAN PROCESS CLASSIFIER
                   |
                   ▼
           📊 MODEL PREDICTION
                   |
          ┌────────┼────────┐
          ▼        ▼        ▼
        GOOD      BAD     WORST
          |        |        |
          └────────┼────────┘
                   |
                   ▼
          🌐 FLASK WEB APPLICATION
                   |
                   ▼
             📑 FINAL RESULT

---

🎬 Project Demonstration

<div align="center"><img src="assets/demo.gif" width="850" alt="Food Texture Prediction Project Demonstration" />🚀 Food Measurement → Data Processing → AI Prediction → Final Result

</div>Add your actual application recording as "assets/demo.gif".

---

🔬 Working Methodology

1. 📥 Data Collection

The application accepts six measurement parameters:

Input Parameter| Description
Force| Applied force measurement
Vib_Freq| Vibration frequency
Vib_Amp| Vibration amplitude
Sound_Int| Sound intensity
Sound_Freq| Sound frequency
Moisture| Moisture measurement

2. 🧹 Data Preprocessing

The collected measurement values are converted into a structured DataFrame using Pandas.

The input data is processed using the same feature order as the training dataset.

3. ⚙️ Feature Scaling

The project uses "StandardScaler" from Scikit-learn to standardize input features before prediction.

4. 🤖 Machine Learning Model

The project uses:

Gaussian Process Classifier (GPC)

Kernel:

Radial Basis Function (RBF)

The model learns patterns from the training dataset and predicts one of three food quality categories.

5. 📊 Prediction Results

The model produces one of the following categories:

- 🟢 GOOD
- 🟡 BAD
- 🔴 WORST

6. 📈 Model Evaluation

The training script evaluates the model using:

- Accuracy Score
- Weighted F1-Score
- Weighted Recall
- Confusion Matrix

---

🛠️ Technologies Used

Technology| Purpose
🐍 Python| Core programming
Flask| Backend web framework
HTML5| Web page structure
CSS3| User interface styling
JavaScript| Frontend interactions
Pandas| Data manipulation
NumPy| Numerical computations
Scikit-learn| Machine learning
Gaussian Process Classifier| Food quality classification
RBF Kernel| Machine learning kernel
StandardScaler| Feature scaling
Matplotlib| Graph visualization
Seaborn| Statistical visualization
Joblib| Model and scaler serialization
Git & GitHub| Version control

---

📂 Project Structure

Food-texture-prediction/
│
├── Static/
│   ├── accuracy_graph.png
│   └── confusion_matrix.png
│
├── Templates/
│   ├── index.html
│   ├── predict.html
│   └── dashboard.html
│
├── assets/
│   ├── banner.gif
│   ├── demo.gif
│   ├── prediction.gif
│   └── dashboard.gif
│
├── app.py
├── train.py
├── food_texture_data.csv
├── example_values.csv
├── model.pkl
├── scaler.pkl
├── requirements.txt
└── README.md

The assets folder and some generated files may need to be added. Keep the actual folder names and their capitalization consistent with the application code.

---

⚙️ Installation & Setup

Step 1: Clone Repository

git clone https://github.com/hemanth304050/Food-texture-prediction.git

Step 2: Navigate to Project

cd Food-texture-prediction

Step 3: Create Virtual Environment

python -m venv venv

Step 4: Activate Environment

Windows:

venv\Scripts\activate

Step 5: Install Dependencies

pip install -r requirements.txt

Step 6: Train Machine Learning Model

python train.py

This generates the trained model and scaler files.

Step 7: Run Flask Application

python app.py

Step 8: Open Browser

http://127.0.0.1:5000/

🎉 Your Food Texture Prediction Web Application is ready!

---

📊 Dataset Information

The project uses a CSV dataset containing multiple food measurement parameters and their corresponding quality labels.

Dataset Features

- Force
- Vib_Freq
- Vib_Amp
- Sound_Int
- Sound_Freq
- Moisture
- Label

Target Classes

Label| Prediction
0| Good
1| Bad
2| Worst

Sample Dataset Structure

Force,Vib_Freq,Vib_Amp,Sound_Int,Sound_Freq,Moisture,Label

Refer to the actual "food_texture_data.csv" file for the dataset values.

---

📈 Model Training & Evaluation

The training process includes:

1. Loading the food texture dataset.
2. Separating input features and target labels.
3. Splitting data into training and testing sets.
4. Applying StandardScaler.
5. Training Gaussian Process Classifier.
6. Predicting test dataset labels.
7. Calculating performance metrics.
8. Generating model evaluation graphs.
9. Saving the trained model using Joblib.

Model Configuration

Parameter| Configuration
Algorithm| Gaussian Process Classifier
Kernel| RBF
Test Size| 20%
Random State| 42
Training Subset| Up to 5,000 samples
Feature Scaling| StandardScaler

Actual model performance should be taken from your training output rather than assumed.

---

📸 Application Screenshots

🖥️ Main Interface

<img src="assets/main-interface.png" width="850" alt="Food Texture Application Interface" />📊 Dashboard

<img src="assets/dashboard.png" width="850" alt="Food Texture Dashboard" />🤖 Prediction Result

<img src="assets/prediction-result.png" width="850" alt="Food Quality Prediction Result" />---

🎞️ Animated GIF Demonstrations

🍎 Food Analysis

<img src="assets/food-analysis.gif" width="750" alt="Food Analysis Animation" />🤖 AI Prediction

<img src="assets/prediction.gif" width="750" alt="AI Prediction Animation" />📊 Dashboard Visualization

<img src="assets/dashboard.gif" width="750" alt="Dashboard Animation" />Upload your actual GIF files into the assets folder for these animations to display.

---

🌟 Advantages

- Automated food quality classification.
- Multiple measurement-based analysis.
- Machine learning-based prediction.
- Easy-to-use web application.
- Dataset visualization.
- Model performance evaluation.
- Extendable architecture.

⚠️ Limitations

- Prediction quality depends on dataset quality.
- Sensor calibration affects measurement reliability.
- Different food products may require different training data.
- Gaussian Process Classification may be computationally expensive for large datasets.
- Real-world validation is required before industrial use.

---

🚀 Future Enhancements

- 📷 Computer vision-based food texture analysis.
- 🔌 Real-time sensor integration.
- 🌐 Cloud-based deployment.
- 📱 Mobile application.
- 📊 Advanced analytics dashboard.
- 🤖 Comparison with additional classification algorithms.
- 🔍 Dynamic Time Warping-based time-series template matching.
- 📑 Automated food quality reports.

---

👨‍💻 About The Developer

<div align="center">Dhannodi Hemanth Kumar

B.Tech Computer Science & Engineering Student | Python Developer | Full Stack Developer | Data Analytics Enthusiast

<img src="https://img.shields.io/badge/Computer%20Science-Engineering-blue" />
<img src="https://img.shields.io/badge/Python-Developer-yellow?logo=python" />
<img src="https://img.shields.io/badge/Full%20Stack-Development-green" />
<img src="https://img.shields.io/badge/Data-Analytics-orange" /></div>🎓 Education

Qualification| Institution| Year
B.Tech – Computer Science & Engineering| Sri Venkateswara College of Engineering, Kadapa| 2022–2026
Intermediate – MPC| Board of Intermediate Education| —
SSC| Sri Chaitanya Techno School| 2019–2020

B.Tech CGPA: 7.6/10

💻 Technical Skills

Programming Languages

- Python
- Java
- SQL
- JavaScript

Frontend Development

- HTML5
- CSS3
- React.js

Backend Development

- Node.js
- Express.js
- Flask

Database

- MySQL
- MongoDB

Data Analytics

- Tableau
- Excel
- Pandas
- NumPy

Tools

- Git & GitHub
- VS Code
- Eclipse
- Jupyter Notebook

Core Computer Science

- Object-Oriented Programming
- Database Management Systems
- REST APIs
- Data Structures Fundamentals

💼 Internship Experience

1. Software Development Internship – KodNest Technologies

- Gained practical exposure to software development.
- Worked on programming and application development concepts.
- Improved technical problem-solving skills.

2. Data Analytics with Tableau – SmartBridge × APSCHE

- Learned data analytics fundamentals.
- Worked with Tableau-based data visualization.
- Gained exposure to data analysis and reporting.

📜 Certifications

- IBM – Python for Data Science.
- SmartBridge – Data Analytics with Tableau.
- ExcelR – Java Full Stack.
- AWS – Prompt Engineer.
- Quantum Fundamentals Program.

🚀 Other Projects

Project| Technologies
DHK FOODIES – AI-Powered Food Delivery Application| MERN Stack
Personal Portfolio Website| HTML, CSS, JavaScript
E-Learning Platform| Web Development
Food Texture Prediction| Python, Flask, Machine Learning

---

📬 Connect With Me

<p align="center"><a href="https://github.com/hemanth304050">
<img src="https://img.shields.io/badge/GitHub-hemanth304050-181717?style=for-the-badge&logo=github" />
</a><a href="https://www.linkedin.com/in/dhannodi-hemanth-kumar-5b758b258/">
<img src="https://img.shields.io/badge/LinkedIn-Connect-blue?style=for-the-badge&logo=linkedin" />
</a><a href="https://dhkmyportfolio.netlify.app/">
<img src="https://img.shields.io/badge/Portfolio-Visit-orange?style=for-the-badge&logo=googlechrome" />
</a><a href="mailto:hemanthheman86@gmail.com">
<img src="https://img.shields.io/badge/Email-Contact-red?style=for-the-badge&logo=gmail" />
</a></p>---

🤝 Contributing

Contributions, suggestions, and improvements are welcome.

1. Fork this repository.
2. Create a new branch.
3. Make your changes.
4. Submit a pull request.

📜 License

This project can be distributed under the MIT License. Add a LICENSE file if you choose this license.

---

<div align="center">⭐ If You Like This Project, Give It a Star!

🍎 Making Food Quality Prediction Smarter with Artificial Intelligence 🤖

Developed by Dhannodi Hemanth Kumar

</div>

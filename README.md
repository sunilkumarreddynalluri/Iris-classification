# Iris-classification
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Iris Species Classification Web Application</title>
</head>
<body>

<h1>Iris Species Classification Web Application</h1>

<h2>Project Overview</h2>
<p>
This is a <strong>Flask-based web application</strong> that classifies Iris flower species using
<strong>K-Nearest Neighbors (KNN)</strong> and <strong>Naive Bayes</strong> machine learning algorithms.
The application provides an interactive dashboard where users can input flower measurements and get
real-time predictions along with model performance metrics.
</p>

<hr>

<h2>Features</h2>

<h3>1. Interactive Prediction Interface</h3>
<ul>
    <li>Input fields for four flower measurements:
        <ul>
            <li>Sepal Length (cm)</li>
            <li>Sepal Width (cm)</li>
            <li>Petal Length (cm)</li>
            <li>Petal Width (cm)</li>
        </ul>
    </li>
    <li>Toggle between KNN and Naive Bayes models</li>
    <li>Real-time species prediction (Setosa, Versicolor, Virginica)</li>
</ul>

<h3>2. Model Performance Dashboard</h3>
<p><strong>Training Results:</strong></p>
<ul>
    <li>Accuracy score</li>
    <li>Classification report (Precision, Recall, F1-score, Support)</li>
    <li>Confusion matrix</li>
</ul>

<p><strong>Testing Results:</strong></p>
<ul>
    <li>Same comprehensive metrics for test data</li>
    <li>Dynamic display based on selected model</li>
</ul>

<h3>3. Visual Design</h3>
<ul>
    <li>Modern glass-morphism UI with gradient background</li>
    <li>Responsive design (mobile & desktop)</li>
    <li>Smooth animations and hover effects</li>
    <li>Color-coded buttons and interactive elements</li>
</ul>

<hr>

<h2>Architecture</h2>

<h3>Frontend</h3>
<ul>
    <li>HTML / CSS / JavaScript</li>
    <li>Bootstrap 5 for responsive layout</li>
    <li>Custom CSS with glass-morphism effects</li>
    <li>JavaScript for model selection and animations</li>
</ul>

<h3>Backend</h3>
<ul>
    <li>Python Flask framework</li>
    <li>Pickle for model loading</li>
    <li>JSON for metrics storage</li>
    <li>Jinja2 templating</li>
</ul>

<hr>

<h2>Machine Learning Models</h2>
<ul>
    <li>KNN Classifier (k = 3)</li>
    <li>Gaussian Naive Bayes Classifier</li>
    <li>Trained on Iris dataset (150 samples, 4 features)</li>
</ul>

<hr>

<h2>Dataset Information</h2>

<h3>Source</h3>
<p>Iris Dataset from Kaggle / UCI Machine Learning Repository</p>

<h3>Features</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Feature</th>
        <th>Description</th>
        <th>Range</th>
    </tr>
    <tr>
        <td>Sepal Length</td>
        <td>Length of sepal in cm</td>
        <td>4.3 – 7.9</td>
    </tr>
    <tr>
        <td>Sepal Width</td>
        <td>Width of sepal in cm</td>
        <td>2.0 – 4.4</td>
    </tr>
    <tr>
        <td>Petal Length</td>
        <td>Length of petal in cm</td>
        <td>1.0 – 6.9</td>
    </tr>
    <tr>
        <td>Petal Width</td>
        <td>Width of petal in cm</td>
        <td>0.1 – 2.5</td>
    </tr>
</table>

<h3>Target Classes</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Class</th>
        <th>Label</th>
        <th>Samples</th>
    </tr>
    <tr>
        <td>Iris Setosa</td>
        <td>0</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Iris Versicolor</td>
        <td>1</td>
        <td>50</td>
    </tr>
    <tr>
        <td>Iris Virginica</td>
        <td>2</td>
        <td>50</td>
    </tr>
</table>

<hr>

<h2>Model Performance</h2>

<h3>K-Nearest Neighbors (KNN)</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Metric</th>
        <th>Training</th>
        <th>Testing</th>
    </tr>
    <tr>
        <td>Accuracy</td>
        <td>95%</td>
        <td>100%</td>
    </tr>
    <tr>
        <td>Setosa F1-Score</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Versicolor F1-Score</td>
        <td>0.93</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Virginica F1-Score</td>
        <td>0.92</td>
        <td>1.00</td>
    </tr>
</table>

<h3>Naive Bayes (Gaussian)</h3>
<table border="1" cellpadding="5">
    <tr>
        <th>Metric</th>
        <th>Training</th>
        <th>Testing</th>
    </tr>
    <tr>
        <td>Accuracy</td>
        <td>95%</td>
        <td>100%</td>
    </tr>
    <tr>
        <td>Setosa F1-Score</td>
        <td>1.00</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Versicolor F1-Score</td>
        <td>0.93</td>
        <td>1.00</td>
    </tr>
    <tr>
        <td>Virginica F1-Score</td>
        <td>0.92</td>
        <td>1.00</td>
    </tr>
</table>

<hr>

<h2>File Structure</h2>
<pre>
iris-classifier/
├── app.py
├── requirements.txt
├── Procfile
├── templates/
│   └── index.html
├── KNN.pkl
├── Navis.pkl
├── train_knn.json
├── test_knn.json
├── train_Navia.json
└── test_Navia.json
</pre>

<hr>

<h2>Live Demo & Repository</h2>
<p>
Live Application:
<a href="https://iris-classification-xz67.onrender.com/" target="_blank">
https://iris-classification-xz67.onrender.com/
</a>
</p>

<p>
GitHub Repository:
<a href="https://github.com/sunilkumarreddynalluri/Iris-classification.git" target="_blank">
https://github.com/sunilkumarreddynalluri/Iris-classification.git
</a>
</p>

<hr>

<h2>Contact</h2>
<p>Email: sunilkumarreddy736@gmail.com</p>

<hr>

<h2>License</h2>
<p>
This project is open-source and available for educational and commercial use.
</p>

<hr>

<p><strong>Created by Sunil Reddy</strong></p>

</body>
</html>

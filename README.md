# SENTIMENT-ANALYSIS-WITH-NLP

**Company:** Codtech It Solutions

**Name:** Lalit Kumar

**Intern Id:** CT4MWZ33

**Domain:** Machine Learning

**Duration:** 16 Weeeks

**Mentor:** Neela Santhosh Kumar

# Sentiment Analysis with NLP and Flask Web App

## 🎜️ Overview

This project implements a movie review sentiment analysis system using Natural Language Processing (NLP) and machine learning. The application classifies user-written reviews as **positive** or **negative** and is deployed through a Flask web interface.

## 📊 Dataset

We use the `movie_reviews` dataset from the NLTK corpus. It contains 2,000 movie reviews labeled as `pos` or `neg`, evenly split for binary classification.

## 📘 Technologies Used

* **Python**
* **NLTK** for accessing the dataset
* **scikit-learn** for vectorization and model training
* **Joblib** for model persistence
* **Flask** for the web application
* **HTML/CSS** for frontend styling

## ✅ Features

* Loads and preprocesses movie reviews
* Converts text data using TF-IDF vectorization
* Trains a Logistic Regression model
* Evaluates performance with accuracy, confusion matrix, and classification report
* Saves the model and vectorizer
* Deploys a web form to input new reviews and display predicted sentiment

## ⚙️ How It Works

1. **Load and Shuffle Data**:

   * Reviews and labels are loaded from `movie_reviews`
   * Labels are converted to 0 (negative) and 1 (positive)

2. **Data Preprocessing**:

   * Train/test split using `train_test_split`
   * Vectorization using `TfidfVectorizer`

3. **Model Training**:

   * Logistic Regression with `max_iter=1000`
   * Fit model on TF-IDF transformed training data

4. **Evaluation**:

   * Uses accuracy score, confusion matrix, and classification report

5. **Saving Model**:

   * Trained model and TF-IDF vectorizer are saved using `joblib`

6. **Flask App**:

   * Loads saved model and vectorizer
   * Accepts review input via web form
   * Displays result with styled feedback (positive or negative sentiment)

## 🌐 Web Application

* The web app provides a user-friendly interface.
* Enter a movie review and receive immediate feedback.
* Result is displayed in styled boxes using HTML and CSS.

## 🚀 Getting Started

### Prerequisites

Ensure you have Python and pip installed. Then install required packages:

```bash
pip install -r requirements.txt
```

### Run Locally

```bash
python app.py
```

Visit `http://127.0.0.1:5000` in your browser.

## 🔄 Example

Input:

```
I absolutely loved the movie! It was fantastic and inspiring.
```

Output:

```
Positive
```

## 📈 Model Performance

* **Accuracy**: \~81%
* **Confusion Matrix**:

  ```
  ```

\[\[165  51]
\[ 25 159]]

```
- **Precision/Recall**:
- Precision (positive): 0.76
- Recall (positive): 0.86
- F1-score (positive): 0.81

## 🚀 Future Work
- Use advanced NLP methods (lemmatization, POS tagging)
- Integrate deep learning models (e.g., BERT)
- Deploy app on cloud platforms like Heroku or AWS
- Allow batch review uploads for sentiment analysis

## 📖 License
This project is open-source and free to use under the MIT License.

---

Made with ❤️ using Python and Flask.

```

# Output
![image](https://github.com/user-attachments/assets/a8fdbcb5-06ee-4caa-bd37-54a16310fa7d)

![image](https://github.com/user-attachments/assets/8a80f522-c8af-478b-9143-af0d7a8b510b)


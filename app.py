from flask import Flask, request, render_template_string
import joblib

# Load trained model and vectorizer
model = joblib.load("sentiment_model.pkl")
tfidf = joblib.load("tfidf_vectorizer.pkl")

app = Flask(__name__)

HTML_TEMPLATE = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Sentiment Analysis</title>
    <style>
        body {
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background: linear-gradient(to right, #f0f2f5, #d9e2ec);
            padding: 40px;
            margin: 0;
        }
        .container {
            background: white;
            max-width: 700px;
            margin: auto;
            padding: 30px 40px;
            border-radius: 12px;
            box-shadow: 0px 8px 20px rgba(0,0,0,0.1);
        }
        h2 {
            color: #2c3e50;
            text-align: center;
        }
        textarea {
            width: 100%;
            font-size: 16px;
            padding: 12px;
            border: 1px solid #ccc;
            border-radius: 6px;
            resize: vertical;
            margin-top: 10px;
        }
        input[type="submit"] {
            background-color: #3498db;
            color: white;
            border: none;
            padding: 12px 25px;
            font-size: 16px;
            border-radius: 6px;
            cursor: pointer;
            transition: background-color 0.3s ease;
            margin-top: 15px;
        }
        input[type="submit"]:hover {
            background-color: #2980b9;
        }
        .result {
            margin-top: 25px;
            font-size: 20px;
            font-weight: bold;
            padding: 12px;
            border-radius: 8px;
            text-align: center;
        }
        .positive {
            background-color: #e6f4ea;
            color: #2e7d32;
        }
        .negative {
            background-color: #fdecea;
            color: #c0392b;
        }
    </style>
</head>
<body>
    <div class="container">
        <h2>🎬 Movie Review Sentiment Analyzer</h2>
        <form method="post">
            <textarea name="review" rows="6" placeholder="Enter your movie review here..." required></textarea><br>
            <input type="submit" value="Analyze Sentiment">
        </form>
        {% if prediction is not none %}
            <div class="result {{ 'positive' if prediction == 1 else 'negative' }}">
                {{ 'Positive' if prediction == 1 else 'Negative' }}
            </div>
        {% endif %}
    </div>
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = None
    if request.method == "POST":
        review = request.form["review"]
        if review.strip():
            review_vector = tfidf.transform([review])
            prediction = model.predict(review_vector)[0]
    return render_template_string(HTML_TEMPLATE, prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)

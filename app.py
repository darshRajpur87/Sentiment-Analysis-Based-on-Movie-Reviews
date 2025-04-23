from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("sentiment_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/predict', methods=['POST'])
def predict():
    review = request.form['review']
    review_vec = vectorizer.transform([review])
    pred = model.predict(review_vec)[0]
    sentiment = "👍 Positive" if pred == 1 else "👎 Negative"
    return render_template("index.html", review=review, sentiment=sentiment)

if __name__ == '__main__':
    app.run(debug=True)

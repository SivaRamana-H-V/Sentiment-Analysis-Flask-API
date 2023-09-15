from flask import Flask, request, jsonify
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import nltk

app = Flask(__name__)

output = {}

def sentiment(sentence):
    nltk.download('vader_lexicon')
    sid = SentimentIntensityAnalyzer()
    score = sid.polarity_scores(sentence)['compound']
    if score > 0:
        return "Positive"
    else:
        return "Negative"

@app.route("/", methods=["GET", "POST"])
def sentimentRequest():
    if request.method == "POST" or request.method == "GET":
        sentence = request.args.get('q')
        sent = sentiment(sentence)
        output['sentiment'] = sent
        return jsonify(output)
    else:
        return jsonify({'error': 'Invalid request method'}), 400

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)

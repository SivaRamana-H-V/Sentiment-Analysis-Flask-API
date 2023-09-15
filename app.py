# from flask import Flask, request, jsonify
# import nltk
# from nltk.sentiment.vader import SentimentIntensityAnalyzer

# app = Flask(__name__)

# output = {}

# def sentiment(sentence):

#     nltk.download('vader_lexicon')
#     sid = SentimentIntensityAnalyzer()
#     score = sid.polarity_scores(sentence)['compound']
#     if(score>0):
#         return "Positive"
#     else:
#         return "Negative"

# @app.route("/", methods = ["GET","POST"])
# def sentimentRequest():
#     if request.method == "POST":
#         sentence = request.form['q']
#         sent = sentiment(sentence)
#         output['sentiment'] = sent
#         return jsonify(output)
#     else:
#         sentence = request.args.get('q')
#         sent = sentiment(sentence)
#         print(sentence)
#         output['sentiment'] = sent
#         return jsonify(output)

# if __name__ == "__main__":
#     app.run(host='0.0.0.0.0',debug=True)

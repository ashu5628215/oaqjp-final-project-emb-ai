'''
Flask application to get analyse statement and predicte emotions.
'''
from flask import Flask, render_template, request
from EmotionDetection.emotion_detection import emotion_detector

app = Flask("Emotion Detector")
@app.route("/emotionDetector")
def sent_analyzer():
    '''
    Call emotion detector
    '''
    text_to_analyze = request.args.get('textToAnalyze')
    result = emotion_detector(text_to_analyze)

    if result is None:
        return "Invalid input! Try again."
    if result['dominant_emotion'] is None:
        return "Invalid text! Please try again!."

    return (f"For the given statement, the system response is 'anger': {result['anger']}, "
            f"'disgust': {result['disgust']}, 'fear': {result['fear']}"
            f"'joy': {result['joy']} and "
            f"'sadness': {result['sadness']}. The dominant emotion"
            f" is {result['dominant_emotion']}.")
@app.route("/")
def render_index_page():
    '''
    Render index.html
    '''
    return render_template('index.html')

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

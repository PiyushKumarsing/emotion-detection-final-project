"""
Flask web application for Emotion Detection using Watson NLP Library.

This app provides a web interface where users can input text and receive
emotion analysis results (anger, disgust, fear, joy, sadness) along with
the dominant emotion.
"""

from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)
@app.route("/", methods=['GET'])
def home():
    """
    Main route handler.

    Retrieves text from the 'textToAnalyze' query parameter, analyzes it
    for emotions using the emotion_detector function, and renders the
    result on the page.

    Handles empty input and API errors by displaying an invalid message.

    Returns:
        Rendered index.html template with input text and result.
    """
    text = request.args.get('textToAnalyze', '').strip()
    
    response = emotion_detector(text)
    
    if response['anger'] is None or not text:
        result = "Invalid input! Please enter some text."
    else:
        result = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']:.6f}, 'disgust': {response['disgust']:.6f}, "
            f"'fear': {response['fear']:.6f}, 'joy': {response['joy']:.6f}, "
            f"'sadness': {response['sadness']:.6f}. "
            f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>."
        )
    
    return render_template('index.html', input_text=text, result=result)


if __name__ == "__main__":
    """
    Run the Flask development server.
    
    Binds to 0.0.0.0 to be accessible from outside the container.
    """
    app.run(host="0.0.0.0", port=5000)
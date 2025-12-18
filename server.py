from flask import Flask, render_template, request
from EmotionDetection import emotion_detector

app = Flask(__name__)

@app.route("/emotionDetector")
def emotion_detector_route():
    text_to_analyze = request.args.get("textToAnalyze")
    if not text_to_analyze:
        return "Invalid input!", 400

    result = emotion_detector(text_to_analyze)
    
    formatted = (
        f"For the given statement, the system response is "
        f"'anger': {result['anger']:.6f}, 'disgust': {result['disgust']:.6f}, "
        f"'fear': {result['fear']:.6f}, 'joy': {result['joy']:.6f}, "
        f"'sadness': {result['sadness']:.6f}. "
        f"The dominant emotion is <strong>{result['dominant_emotion']}</strong>."
    )
    return formatted
    
@app.route("/", methods=['GET'])
def home():
    text = request.args.get('textToAnalyze', '').strip()
    
    response = emotion_detector(text)
    
    # If anger is None → means either empty input or API error
    if response['anger'] is None:
        result = "Invalid input! Please enter some text."
    else:
        result = (
            f"For the given statement, the system response is "
            f"'anger': {response['anger']:.6f}, "
            f"'disgust': {response['disgust']:.6f}, "
            f"'fear': {response['fear']:.6f}, "
            f"'joy': {response['joy']:.6f}, "
            f"'sadness': {response['sadness']:.6f}. "
            f"The dominant emotion is <strong>{response['dominant_emotion']}</strong>."
        )

    return render_template(
        'index.html',
        input_text=text_to_analyze,
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
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
    text_to_analyze = request.args.get('textToAnalyze', '').strip()
    result = None

    if text_to_analyze:
        response = emotion_detector(text_to_analyze)
        anger = response['anger']
        disgust = response['disgust']
        fear = response['fear']
        joy = response['joy']
        sadness = response['sadness']
        dominant = response['dominant_emotion']

        result = (
            f"For the given statement, the system response is "
            f"'anger': {anger:.6f}, 'disgust': {disgust:.6f}, 'fear': {fear:.6f}, "
            f"'joy': {joy:.6f}, 'sadness': {sadness:.6f}. "
            f"The dominant emotion is <strong>{dominant}</strong>."
        )
    elif text_to_analyze == "":
        result = "Invalid input! Please enter some text."

    return render_template(
        'index.html',
        input_text=text_to_analyze,
        result=result
    )

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
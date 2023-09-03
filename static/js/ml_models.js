// Digit Classifier
function DigitClassifier() {
    // var url = "{{ digit_classifier_url }}";  // Use the URL variable
    // window.location.href = url;
    window.location.href = '{{ url_for("digitClassifier") }}';
}

//Titanic Prediction
function TitanicPrediction() {
    window.location.href = "{{ url_for('titanicPrediction') }}";
}

//Email Classifier
function EmailClassifier() {
    window.location.href = "{{ url_for('emailClassifier') }}";
}

//Speech Sentiment
function SpeechSentiment() {
    window.location.href = "{{ url_for('speechSentiment') }}";
}

//Spoof Detection
function SpoofDetection() {
    window.location.href = "{{ url_for('spoofDetection') }}";
}
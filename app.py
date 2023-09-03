from flask import Flask, render_template, url_for, request, redirect

from mlModels import titanic

app = Flask(__name__)

@app.route('/')
def Welcome():
    return render_template("index.html",)

# @app.route("/t")
# def fun():
#     return render_template(url_for("digitClassifier"))

@app.route('/digitClassifier')
def digitClassifier():
    return render_template('Projects/ML_Projects/Digit Classification.html')
    # digit_classifier_url = url_for('digitClassifier')  # Generate the URL on the server-side
    # return render_template('Projects/ML_Projects/Digit Classification.html', digit_classifier_url=digit_classifier_url)

@app.route('/titanicPrediction')
def titanicPrediction():
    return render_template('Projects/ML_Projects/Titanic Prediction.html')


@app.route('/emailClassifier')
def emailClassifier():
    return render_template('Projects/ML_Projects/Email Classifier.html')


@app.route('/speechSentiment')
def speechSentiment():
    return render_template('Projects/ML_Projects/Speech Sentiment.html')

@app.route('/spoofDetection')
def spoofDetection():
    return render_template('Projects/ML_Projects/Spoof Detection.html')

@app.route('/mylink/')

@app.route('/titanic', methods=["GET", 'POST'])
def fun():
    if request.method == "POST":
        pid = int(request.form['pid'])
        pclass = int(request.form['pclass'])
        name = str(request.form['name'])
        sex = str(request.form['sex'])
        age = int(request.form['age'])
        sib = int(request.form['sib'])
        par = int(request.form['par'])
        tict = str(request.form['tict'])
        fare = float(request.form['fare'])
        cabin = str(request.form['cabin'])
        emb = str(request.form['emb'])
        
        print(pid, pclass, name, sex, age, sib, par, tict, fare, cabin, emb)
        # print('output ' ,sex)
        
        output = titanic.predict(pid, pclass, name, sex, age, sib, par, tict, fare, cabin, emb)
        
        return render_template("Projects/ML_Projects/Titanic Prediction.html", output = output)
        
    else:
        return "<h2>method is not post</h2>"

if __name__=='__main__':
    app.run(debug=True)
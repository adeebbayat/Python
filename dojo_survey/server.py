from flask import Flask, render_template, request, redirect,session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



@app.route('/',methods=["POST"])
def index():

    return render_template("index.html")

@app.route('/process', methods=['POST'])
def form_submit():
    print("Got Post Info")
    session["name"] = request.form["textBox1"]
    session["location"] = request.form["Locations"]
    session["language"] = request.form["Language"]
    session["comment"] = request.form["textBox"]

    return redirect('/result')

@app.route('/result')
def form_result():
    return render_template("result.html", name_on_template=session["name"],
    location_on_template=session["location"],language_on_template=session["language"],
    comment_on_template=session["comment"])



if __name__ == "__main__":
    app.run(debug=True)
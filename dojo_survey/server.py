from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes



@app.route('/')
def index():

    return render_template("index.html")

@app.route('/process' method="post")
def form_submit(textBox1,Locations,Languages,textBox):
    print("Got Post Info")
    print(request.form)


    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
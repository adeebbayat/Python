from flask import Flask, render_template, request, redirect, session

app = Flask(__name__)
app.secret_key = 'keep it secret, keep it safe' # set a secret key for security purposes


count = 0
@app.route('/')
def index():
    global count
    count += 1
    return render_template("index.html", count = count)

@app.route('/destroy_session')
def destroy():
    global count
    count = 0
    return redirect('/')


if __name__ == "__main__":
    app.run(debug=True)
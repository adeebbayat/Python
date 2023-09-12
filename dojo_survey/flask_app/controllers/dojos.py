from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.dojo import Dojo



@app.route('/')
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

@app.route('/create', methods=['POST'])
def create_dojo():
    # if there are errors:
    # We call the staticmethod on Burger model to validate
    if not Dojo.validate_dojo(request.form):
        # redirect to the route where the burger form is rendered.
        return redirect('/')
    # else no errors:
    Dojo.save(request.form)
    return redirect("/process")

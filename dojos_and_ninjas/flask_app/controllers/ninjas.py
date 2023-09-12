from flask_app import app
from flask import render_template,redirect,request,session,flash
from flask_app.models.ninja import Ninja
from flask_app.models.dojo import Dojo

@app.route('/')
def index():
    return redirect('/ninjas')

@app.route('/dojos/create',methods=['POST'])
def create_dojo():
    Dojo.save(request.form)
    return redirect('/dojos')

@app.route('/ninjas/create',methods=['POST'])
def create_ninja():
    print(request.form)
    Ninja.save(request.form)
    return redirect('/dojos')

@app.route('/ninjas')
def ninjas():
    dojo=Dojo.get_all_no_data()
    print(dojo)
    return render_template("ninjas.html",ninjas=Ninja.get_all(),dojo=dojo)

@app.route('/dojos')
def dojos():
    dojo=Dojo.get_all_no_data()
    print(dojo)
    return render_template("dojos.html",dojo=dojo)

@app.route('/dojos/<int:id>')
def dojo_list(id):
    data ={ 
        "id":id
    }
    return render_template("dojo_list.html",dojo=Dojo.get_all(data))


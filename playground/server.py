from flask import Flask, render_template  # added render_template!
app = Flask(__name__)                     


@app.route('/play')
def index():
    return render_template('index.html')  

@app.route('/play/<name>')                           
def name(name):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', times = int(name), text = name)  
    


@app.route('/play/<name>/<color>')                           
def color(name,color):
    # Instead of returning a string, 
    # we'll return the result of the render_template method, passing in the name of our HTML file
    return render_template('index.html', times = int(name), text = name,color=color)  
    
if __name__=="__main__":
    app.run(debug=True)  
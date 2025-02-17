from flask import Flask, render_template, request, redirect, url_for
app = Flask(__name__)
from com.okyunsu.models.titanic.titanic_controller import TitanicController
from com.okyunsu.models.matzip.matzip_controller import MatzipController



@app.route("/")
def index():
    
    controller = TitanicController()
    controller.modeling("train.csv", "test.csv")


    return render_template("index.html")

@app.route("/titanic") 
def titanic():

    controller = MatzipController()
    controller.modelling("matzip.csv")
    remove = request.form.get("remove")

    return render_template("titanic.html")






if __name__ == '__main__':  
    app.run('0.0.0.0',port=5000,debug=True)

app.config['TEMPLATES_AUTO_RELOAD'] = True  
 
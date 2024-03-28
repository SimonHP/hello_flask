from flask import Flask, render_template



app = Flask(__name__)
##python -m flask run --host=0.0.0.0 --port=80
@app.route("/")
def index():
    first_name = "John"
    pizzalist = ["tomateo", "curry"," hawain" , "vegetarian"]
    return render_template("index.html", first_name = first_name, pizzalist = pizzalist)
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)


##if __name__=='__main__':
  ##  app.run(host= '0.0.0.0', port= 5000, debug=True)
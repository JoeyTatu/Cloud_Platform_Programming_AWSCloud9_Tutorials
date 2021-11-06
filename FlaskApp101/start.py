from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)


@app.route("/")
def home():
    #return "Hello! This is the main page <h1> Hello </h1> "
    return render_template("index.html")
    
@app.route("/<name>")
def user(name):
    #return f"Hello {name}!"
    return render_template("index.html", content=name, r=1776)

#redirect to the home page when reaching admin endpoint 
# Both redirect and url_for must be import above before recognized by compiler
@app.route("/admin/")
def admin():
    return redirect(url_for("user", name="admin!"))


# We need to state this below due to our C9 Env
if __name__ == "__main__":
    app.run(host='0.0.0.0', port=8080, debug=True)

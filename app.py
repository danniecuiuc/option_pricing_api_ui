import call
from call import barrier_bs, black_scholes
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html", context = "Testing")

@app.route("/european")
def european():
    return render_template("europeancall.html")

@app.route("/american")
def american():
    return render_template("american.html")

@app.route("/barrier")
def barrier():
    return render_template("barrier.html")

@app.route("/vertical")
def vertical():
    return render_template("vertical.html")

@app.route("/butterfly")
def butterfly():
    return render_template("butterfly.html")

@app.route("/condor")
def condor():
    return render_template("condor.html")

def main():
    sigma = inputjlakjs
    bar_value = call.barrier_bs(sigma, 12, 0.1, 0.05, 0.02, 0.1, 1)
    print(bar_value)
    print("Hello Main")

if __name__ == "__main__":
    app.run(debug = True)

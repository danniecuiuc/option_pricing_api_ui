import call
from call import barrier_bs, black_scholes
from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("europeancall.html", context = "Testing")

@app.route("/barrier")
def barrier():
    return render_template("barrier.html")

def main():
    sigma = inputjlakjs
    bar_value = call.barrier_bs(sigma, 12, 0.1, 0.05, 0.02, 0.1, 1)
    print(bar_value)
    print("Hello Main")

if __name__ == "__main__":
    app.run(debug = True)

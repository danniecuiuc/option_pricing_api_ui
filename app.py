import call
from call import black_scholes, CRRA_model, barrier_bs, CRRB_model, ver_spread, butterfly_euro, condor_euro 
from flask import Flask, redirect, url_for, render_template, request

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template("home.html")

@app.route("/european")
def european():
    return render_template("europeancall.html")

@app.route('/send', methods=['POST'])
def send(sum=sum):
    if request.method == 'POST':
        S0 = request.form['S0']
        K = request.form['K']
        T = request.form['T']
        r = request.form['r']
        div = request.form['div']
        sigma = request.form['sigma']
        operation = request.form['operation']

        if operation == 'black_scholes':
            sum = black_scholes(float(S0), float(K), float(T), float(r), float(div), float(sigma))
            return render_template('europeancall.html', sum=sum)
        else:
            return render_template('europeancall.html')

@app.route("/american")
def american():
    return render_template("american.html")

@app.route('/senda', methods=['POST'])
def senda(sum=sum):
    if request.method == 'POST':
        S0 = request.form['S0']
        K = request.form['K']
        T = request.form['T']
        r = request.form['r']
        div = request.form['div']
        sigma = request.form['sigma']
        N = request.form['N']
        operation = request.form['operation']

        if operation == 'binomial':
            sum = CRRA_model(float(S0), float(K), float(T), float(r), float(div), float(sigma), int(N))
            return render_template('american.html', sum=sum)
        else:
            return render_template('american.html')


@app.route("/barrier")
def barrier():
    return render_template("barrier.html")

@app.route('/sendb', methods=['POST'])
def sendb(sum=sum):
    if request.method == 'POST':
        S0 = request.form['S0']
        K = request.form['K']
        B = request.form['B']
        T = request.form['T']
        r = request.form['r']
        div = request.form['div']
        sigma = request.form['sigma']
        N = request.form['N']
        operation = request.form['operation']

        if operation == 'binomial':
            sum = CRRB_model(float(S0), float(K), float(B), float(T), float(r), float(div), float(sigma), int(N))
            return render_template('barrier.html', sum=sum)
        elif operation == 'blacksholes':
            sum = barrier_bs(float(B), float(S0), float(K), float(T), float(r), float(div), float(sigma))
            return render_template('barrier.html', sum=sum)
        else:
            return render_template('barrier.html')

@app.route("/vertical")
def vertical():
    return render_template("vertical.html")

@app.route('/sendver', methods=['POST'])
def sendver(sum=sum):
    if request.method == 'POST':
        S0 = request.form['S0']
        K1 = request.form['K1']
        K2 = request.form['K2']
        T = request.form['T']
        r = request.form['r']
        div = request.form['div']
        sigma = request.form['sigma']
        operation = request.form['operation']

        if operation == 'black_scholes':
            sum = ver_spread(float(S0), float(K1), float(K2), float(T), float(r), float(div), float(sigma))
            return render_template('vertical.html', sum=sum)
        else:
            return render_template('vertical.html')

@app.route("/butterfly")
def butterfly():
    return render_template("butterfly.html")

@app.route('/sendbut', methods=['POST'])
def sendbut(sum=sum):
    if request.method == 'POST':
        S0 = request.form['S0']
        K1 = request.form['K1']
        K2 = request.form['K2']
        K3 = request.form['K3']
        T = request.form['T']
        r = request.form['r']
        div = request.form['div']
        sigma = request.form['sigma']
        operation = request.form['operation']

        if operation == 'black_scholes':
            sum = butterfly_euro(float(S0), float(K1), float(K2), float(K3), float(T), float(r), float(div), float(sigma))
            return render_template('butterfly.html', sum=sum)
        else:
            return render_template('butterfly.html')

@app.route("/condor")
def condor():
    return render_template("condor.html")

@app.route('/sendc', methods=['POST'])
def sendc(sum=sum):
    if request.method == 'POST':
        S0 = request.form['S0']
        K1 = request.form['K1']
        K2 = request.form['K2']
        K3 = request.form['K3']
        K4 = request.form['K4']
        T = request.form['T']
        r = request.form['r']
        div = request.form['div']
        sigma = request.form['sigma']
        operation = request.form['operation']

        if operation == 'black_scholes':
            sum = condor_euro(float(S0), float(K1), float(K2), float(K3), float(K4), float(T), float(r), float(div), float(sigma))
            return render_template('condor.html', sum=sum)
        else:
            return render_template('condor.html')

def main():
    sigma = inputjlakjs
    bar_value = call.barrier_bs(sigma, 12, 0.1, 0.05, 0.02, 0.1, 1)
    print(bar_value)
    print("Hello Main")

if __name__ == "__main__":
    app.run(debug = True)

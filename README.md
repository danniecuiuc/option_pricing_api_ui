# Derivatives Pricing App
 - By Dannie Che€ý,n€ý,

## a. Description
This repo contains an API and UI to price different types of call options and call spreads. The tool used is Python flask.
## b. Installation
First make sure that you have python3 and pip3 installed.
<br/>Next, install virtualenv if you haven't.
```python
$ pip3 install virtualenv 
```
In project folder, run
```python
$ virtualenv -p python3 venv
```
to initialize python virtual environment.
<br/>Activate virtual environment with:
```python
$ source ./venv/bin/activate
```
Install flask in venv
```python
(venv)$ pip3 install flask
```
App is ready to run:
```python
(venv)$ python3 app.py
```
Visit http://127.0.0.1:5000 to view the Web UI locally.

## c. Project requirements
Create a secure API and UI using certain tools and languages to quickly price a call option and a call spread.
## d. Usage
First, select the product that you want to price in the navigation bar. 
<br/>  
![Alt text](/home.png?raw=true "home page")
<br/>  
Then, provide all the inputs needed for each model in the blocks.
<br/>  
![Alt text](/barrier.png?raw=true "pricing page")
<br/>  
Finally, you can see the calculation result in the green bar. (in $)
<br/>  
![Alt text](/result.png?raw=true "output")
### Pricing Models Used 
- Binomial Tree (for American Call, Down-and-out Barrier Call, Vertical Call Spread, Butterfly, and Condor)
- Black Scholes Fomula (for European Call, Down-and-out Barrier Call, Vertical Call Spread, Butterfly, and Condor)
## e. endpoint map
### The base path
All URLs referenced in the documentation have the base path http://127.0.0.1:5000/. 
### The endpoint paths and required parameters
Parameters should be included in the request for each endpoint path. In a request, you will replace the placeholders with real values.
- European Call
    <br/>http://127.0.0.1:5000/european
    <br/>http://127.0.0.1:5000/send (HTTP POST method)
    <br/>Required Parameters:
    - S0: Original price of underlying asset (e.g. If the underlying stock price is $100, put "100" into the placeholder. )
    - K: Exercise pice of the option
    - T: Time to maturity (In Years): T
    - r: Annualized Continously Compounded Risk-free Rate:
    - div: Continuous Dividend Yield (If asset pays no divident, put 0 here): div
    - sigma: Annualized (Future) Volatility of Stock Price Returns (In Black Scholes Model, we assume the volatility is constant)
    - operation: Black Scholes only for now (future plan: add Heston Model here)
- American Call
    <br/>http://127.0.0.1:5000/american
    <br/>http://127.0.0.1:5000/senda (HTTP POST method)
    <br/>Required parameters: 
    - S0, K, T, r, div, sigma (same as european call)
    - N: Number of Steps in the Binomial Tree, should be larger to reduce errors, but if larger number of steps chosen, it might take some time to calculate the price
    - operation: Binomial Trees only for now (future plan: add Monte Carlo Simulation Methods here) 
- Down-and-out Barrier Call Option (European) 
    <br/>http://127.0.0.1:5000/barrier
    <br/>http://127.0.0.1:5000/sendb (HTTP POST method)
    <br/>Required parameters: 
    - S0, K, T, r, div, sigma (same as european call)
    - If Binomial Tree Model Chosen: additional input N - Number of Steps in the Binomial Tree, should be larger to reduce errors (e.g. suggest to choose 1000 here) 
    - If Black Scholes Chosen: no need to input N 
    - operation: Binomial Trees or Black Scholes 
- Vertical Call Spread (European)
    <br/>http://127.0.0.1:5000/vertical
    <br/>http://127.0.0.1:5000/sendver (HTTP POST method)
    <br/>Required parameters: 
    - S0, T, r, div, sigma (same as european call)
    - K1: The long-position call's strike price, should be smaller than K2
    - K2: The short-position call's strike price, should be larger than K1
    - operation: Black Scholes only for now (future plan: add Heston Model here) 
- Butterfly (European)
    <br/>http://127.0.0.1:5000/butterfly
    <br/>http://127.0.0.1:5000/sendbut
    <br/>Required parameters: 
    - S0, T, r, div, sigma (same as european call)
    - K1: The long-position call's strike price, should be smaller than K2 and K3
    - K2: The short-position call's strike price, should be larger than K1, but smaller than K3
    - K3: The long-position call's strike price, should be larger than K1 and K2 
    - operation: Black Scholes only for now (future plan: add Heston Model here)
- Condor(European)
    <br/>http://127.0.0.1:5000/condor
    <br/>http://127.0.0.1:5000/sendc
    <br/>Required parameters: 
    - S0, T, r, div, sigma (same as european call)
    - K1: The long-position call's strike price, should be smaller than K2, K3, and K4
    - K2: The short-position call's strike price, should be larger than K1, but smaller than K3 and K4
    - K3: The short-position call's strike price, should be larger than K1 and K2, but smaller than K4
    - K4: The long-position call's strike price, should be larger than K1, K2, K3, and K4
    - operation: Black Scholes only for now (future plan: add Heston Model here)
## f. Fufure Release Planning
- Add other pricing models (e.g. Heston SV model, Monte Carlo Simulation) to price call options;
- Add pages for more advanced and complex derivatives (e.g. discrete barrier callable notes, derivatives with path dependency features);
- Add visualization (e.g. line graphs) for price changes of each derivative as expiration nears;
- Make the User Interface more aesthetically pleasing.
## g. Authors and acknowledgment
I thank Mr. Barton for his guidance throughout this project and for his help in writing the documentation.

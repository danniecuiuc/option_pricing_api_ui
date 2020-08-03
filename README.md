# Derivatives Pricing App
 - By Dannie Chen and Trey Barton

## a. Description
This repo contains an API and UI to price different types of call options and call spreads. The backend and frontend can be found in this repository. The tool used to build the webserver and web UI is Python flask.
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
- Binomial Tree (for American Call, Down-and-out Barrier Call, Call Spreads)
- Black Scholes Fomula (for European Call, Down-and-out Barrier Call, Call Spreads)
## e. Fufure Release Planning
- Add other pricing models (e.g. Heston SV model, Monte Carlo Simulation) to price call options;
- Add pages for more advanced and complex derivatives (e.g. discrete barrier callable notes, derivatives with path dependency features);
- Add visualization (e.g. line graphs) for price changes of each derivative as expiration nears;
- Make the User Interface more aesthetically pleasing.
## f. endpoint map
### The base path
http://127.0.0.1:5000/
All URLs referenced in the documentation have the base path https://api.mapbox.com. This base path goes before the endpoint path.
### The endpoint paths and required parameters
These parameters should be included in a request. In a request, you will replace the placeholders with real values.
- European Call
    Urls:
    - http://127.0.0.1:5000/european
    - http://127.0.0.1:5000/send (HTTP POST method)
    Required parameters: 
    - S0: Original Price of Underlying Asset, for example, if the underlying stock price is $100, put "100" into the placeholder 
    - K
- http://127.0.0.1:5000/american
    Urls:
    - http://127.0.0.1:5000/european
    - http://127.0.0.1:5000/send (HTTP POST method)
    Required parameters: 
    - S0
    - K
- http://127.0.0.1:5000/senda
- http://127.0.0.1:5000/barrier
- http://127.0.0.1:5000/sendb
- http://127.0.0.1:5000/vertical
- http://127.0.0.1:5000/sendver
- http://127.0.0.1:5000/butterfly
- http://127.0.0.1:5000/sendbut
- http://127.0.0.1:5000/condor
- http://127.0.0.1:5000/sendc
## g. Authors and acknowledgment
I thank Mr. Barton for his guidance throughout this project and for his help in writing the documentation.

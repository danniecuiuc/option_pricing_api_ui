import numpy as np
import scipy.stats as st
import math

# 1.European Calls Pricing
def black_scholes(S0, K, T, r, div, sigma):
    """
    Function to calcuslates the value of an European Call Option using Black Scholes 

    S0: Original Stock Price
    K: Excercise Price of Call Option
    T: Time Length of Option in which to Exercise (In Years)
    r: Annualized Continously Compounded Risk-free Rate
    div: Rate of continuous dividend paying asset
    sigma: Annualized (Future) Volatility of Stock Price Returns

    """

    cdf_mean = 0.0
    cdf_sd = 1.0

    d1 = (np.log(S0 / K) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    value = S0 * np.exp(-div * T) * st.norm.cdf(d1, cdf_mean, cdf_sd) 
    value = value - K * np.exp(-r * T) * st.norm.cdf(d2, cdf_mean, cdf_sd) 

    return value

# 2. American Call Option (Binomial Tree Model & Monte Carlo Simulations)
def CRRA_model(S0, K, T, r, div, sigma, N):
    """
    Function to calculates the value of an American Call Option using the CRR Binomial Model 

    S0: Original Stock Price
    K: Excercise Price of Call Option
    T: Time Length of Option in which to Exercise (In Years)
    r: Annualized Continously Compounded Risk-free Rate
    sigma: Annualized (Future) Volatility of Stock Price Rckwardeturns
    N: Number of time steps

    """     
    crra_result = []
    option_value = np.zeros([N+1, N+1])
    stock_value = np.zeros([N+1, N+1])    

    delta = T / N
    u = np.exp(sigma * (delta)**0.5)
    d = 1 / u
    qu = (np.exp((r-div) * delta) - d) / (u - d)
    qd = 1 - qu

    for i in range(0, N):    
        stock_value[N, i] = S0 * (u**i) * (d**(N - i))
        option_value[N, i] = np.maximum(stock_value[N, i] - K, 0)

        for j in range(N-1, -1, -1):
            for i in range(j, -1, -1):
                stock_value[j, i] = S0 * (u**i) * (d**(j - i))
                pv = np.exp(-r * delta) * (qu * option_value[j + 1, i + 1] + qd * option_value[j + 1, i])
                option_value[j, i] = np.maximum(pv, stock_value[j, i] - K)
    output = option_value[0,0]

    return output


# 3. European Barrier Option - Down-and-out Call(continuous barrier)
def barrier_bs(B, S0, K, T, r, div, sigma):
    """ 
    --- Black Scholes Model ---
    Function to calculates the value of a European Down-and-out Call Option using Black Scholes 

    B: Barrier Level - option ceases to exit if the stock price hits a particular level during or at a certain time period.
    S0: Original Stock Price
    K: Excercise Price of Call Option
    T: Time Length of Option in which to Exercise (In Years)
    r: Annualized Continously Compounded Risk-free Rate
    div: Rate of continuous dividend paying asset
    sigma: Annualized (Future) Volatility of Stock Price Returns

    """

    cdf_mean = 0.0
    cdf_sd = 1.0
    
    d1 = (np.log(S0 / K) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    h1 = (np.log(B**2 / (K*S0)) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    h2 = h1 - sigma * np.sqrt(T)

    value = S0 * np.exp(-div * T) * st.norm.cdf(d1, cdf_mean, cdf_sd) 
    value = value - K * np.exp(-r * T) * st.norm.cdf(d2, cdf_mean, cdf_sd)
    value = value - (B / S0)** (1 + 2 * (r - div) / sigma ** 2) * S0 * np.exp(-div * T) * st.norm.cdf(h1, cdf_mean, cdf_sd) 
    value = value + (B / S0)** (-1 + 2 * (r - div) / sigma ** 2) * K * np.exp(-r * T) * st.norm.cdf(h2, cdf_mean, cdf_sd)

    return value

def CRRB_model(S0, K, B, T, r, div, sigma, N):
    """
    --- Binomial Model ---
    Function to calculates the value of a European Put Option using the CRR Binomial Model 

    B: Barrier Level - option ceases to exit if the stock price hits a particular level during or at a certain time period.
    S0: Original Stock Price
    K: Excercise Price of Call Option
    T: Time Length of Option in which to Exercise (In Years)
    r: Annualized Continously Compounded Risk-free Rate
    div: Rate of continuous dividend paying asset
    sigma: Annualized (Future) Volatility of Stock Price Returns
    N: Number of time steps

    """    

    crrb_result = []
    option_value = np.zeros([N+1, N+1])
    stock_value = np.zeros([N+1, N+1])    

    delta = T / N
    u = np.exp(sigma * (delta)**0.5)
    d = 1 / u
    qu = (np.exp((r-div) * delta) - d) / (u - d)
    qd = 1 - qu

    for i in range(0, N):    
        stock_value[N, i] = S0 * (u**i) * (d**(N - i))
        option_value[N, i] = np.maximum(stock_value[N, i]-K, 0)

        if stock_value[N, i] < B:
            sd = stock_value[N, i]

    for j in range(N-1, -1, -1):
        for i in range(j, -1, -1):
            pv = np.exp(-r * delta) * (qu * option_value[j + 1, i + 1] + qd * option_value[j + 1, i])
            option_value[j, i] = pv
            stock_value[j, i] = S0 * (u**i) * (d**(j - i))
            if stock_value[j, i] < B:
                option_value[j, i] = 0

        output = option_value[0,0]

    return output

# 4. European Vertical Call - Bull Call Spread - same time to maturity
def ver_spread(S0, K1, K2, T, r, div, sigma):

    cdf_mean = 0.0
    cdf_sd = 1.0

    d1 = (np.log(S0 / K1) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K1) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    d3 = (np.log(S0 / K2) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d4 = (np.log(S0 / K2) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    value1 = S0 * np.exp(-div * T) * st.norm.cdf(d1, cdf_mean, cdf_sd) 
    value1 = value1 - K1 * np.exp(-r * T) * st.norm.cdf(d2, cdf_mean, cdf_sd) 

    value2 = S0 * np.exp(-div * T) * st.norm.cdf(d3, cdf_mean, cdf_sd) 
    value2 = value2 - K2 * np.exp(-r * T) * st.norm.cdf(d4, cdf_mean, cdf_sd) 

    value = value1 - value2
     
    return value

# 5. butterfly - 3 calls
def butterfly_euro(S0, K1, K2, K3, T, r, div, sigma):

    cdf_mean = 0.0
    cdf_sd = 1.0

    d1 = (np.log(S0 / K1) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K1) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    d3 = (np.log(S0 / K2) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d4 = (np.log(S0 / K2) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    d5 = (np.log(S0 / K3) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d6 = (np.log(S0 / K3) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    value1 = S0 * np.exp(-div * T) * st.norm.cdf(d1, cdf_mean, cdf_sd) 
    value1 = value1 - K1 * np.exp(-r * T) * st.norm.cdf(d2, cdf_mean, cdf_sd) 

    value2 = S0 * np.exp(-div * T) * st.norm.cdf(d3, cdf_mean, cdf_sd) 
    value2 = value2 - K2 * np.exp(-r * T) * st.norm.cdf(d4, cdf_mean, cdf_sd) 

    value3 = S0 * np.exp(-div * T) * st.norm.cdf(d5, cdf_mean, cdf_sd) 
    value3 = value3 - K3 * np.exp(-r * T) * st.norm.cdf(d6, cdf_mean, cdf_sd) 

    value = value1 - 2 * value2 + value3

    return value


# 6. Condor - 4 calls
def condor_euro(S0, K1, K2, K3, K4, T, r, div, sigma):

    cdf_mean = 0.0
    cdf_sd = 1.0

    d1 = (np.log(S0 / K1) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d2 = (np.log(S0 / K1) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    d3 = (np.log(S0 / K2) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d4 = (np.log(S0 / K2) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))

    d5 = (np.log(S0 / K3) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d6 = (np.log(S0 / K3) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    
    d7 = (np.log(S0 / K4) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    d8 = (np.log(S0 / K4) + (r - div - 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))


    value1 = S0 * np.exp(-div * T) * st.norm.cdf(d1, cdf_mean, cdf_sd) 
    value1 = value1 - K1 * np.exp(-r * T) * st.norm.cdf(d2, cdf_mean, cdf_sd) 

    value2 = S0 * np.exp(-div * T) * st.norm.cdf(d3, cdf_mean, cdf_sd) 
    value2 = value2 - K2 * np.exp(-r * T) * st.norm.cdf(d4, cdf_mean, cdf_sd) 

    value3 = S0 * np.exp(-div * T) * st.norm.cdf(d5, cdf_mean, cdf_sd) 
    value3 = value3 - K3 * np.exp(-r * T) * st.norm.cdf(d6, cdf_mean, cdf_sd) 

    value4 = S0 * np.exp(-div * T) * st.norm.cdf(d7, cdf_mean, cdf_sd) 
    value4 = value4 - K4 * np.exp(-r * T) * st.norm.cdf(d8, cdf_mean, cdf_sd) 

    value = value1 - value2 - value3 + value4

    return value


# Test Cases
if __name__ == "__main__":
    euro_call_value = black_scholes(100, 100, 0.2, 0.1, 0.05, 0.3)
    print(euro_call_value)   # Tested OK
    american_value = CRRA_model(100, 95, 0.2, 0.1, 0, 0.3, 50)
    print(american_value) #  Tested OK
    barrier = barrier_bs(95, 100, 100, 0.2, 0.1, 0, 0.3)
    print(barrier)  # Tested OK, result shout be 4.670342933300565
    barrier_binomial = CRRB_model(100, 100, 95, 0.2, 0.1, 0, 0.3, 50)
    print(barrier_binomial) # Tested OK, result shout be 4.397502559962934
    ver_bull = ver_spread(98, 95, 100, 0.2, 0.1, 0, 0.3)
    print(ver_bull)    # Tested OK
    butterfly_test= butterfly_euro(98, 90, 95, 100, 0.2, 0.1, 0, 0.3)
    print(butterfly_test)    # Tested OK
    condor_test = condor_euro(100, 95, 98, 102, 105, 0.2, 0.1, 0, 0.3)
    print(condor_test)   # Tested OK

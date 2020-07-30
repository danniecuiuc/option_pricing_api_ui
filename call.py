import numpy as np
import scipy.stats as st
import math

# European Calls Pricing
def black_scholes(S0, K, T, r, div, sigma):
    """
    Function to calcuslates the value of a European Call Option using Black Scholes 

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

# European Barrier Option - Down-and-out Call(continuous barrier)
def barrier_bs(B, S0, K, T, r, div, sigma):
    """ 
    Function to calculates the value of a European Autocall Call Option using Black Scholes 

    B: Barrier Level - if the stock p rice hits a p articular level durin g or at a certain time p eriod.
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
    h1 = (np.log(B ** 2 / K * S0) + (r - div + 0.5 * sigma ** 2) * T) / (sigma * np.sqrt(T))
    h2 = h1 - sigma * np.sqrt(T)

    value = S0 * np.exp(-div * T) * st.norm.cdf(d1, cdf_mean, cdf_sd) 
    value = value - K * np.exp(-r * T) * st.norm.cdf(d2, cdf_mean, cdf_sd)
    value = value - (B / S0)** (1 + 2 * (r - div) / sigma ** 2) * S0 * np.exp(-div * T) * st.norm.cdf(h1, cdf_mean, cdf_sd) 
    value = value + (B / S0)** (-1 + 2 * (r - div) / sigma ** 2) * K * np.exp(-r * T) * st.norm.cdf(h2, cdf_mean, cdf_sd)

    return value


if __name__ == "__main__":
    euro_call_value = black_scholes(100, 100, 0.2, 0.1, 0.05, 0.3)
    print(euro_call_value)
    barrier = barrier_bs(30, 100, 90, 2, 0.05, 0.03, 0.2)
    print(barrier)


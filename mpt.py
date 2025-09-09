**IMPORTS**

%pip install pyportfolioopt
from pypfopt.expected_returns import mean_historical_return
from pypfopt.risk_models import CovarianceShrinkage, sample_cov
from pypfopt import plotting
import matplotlib.pyplot as plt
import yfinance as yf

from datetime import datetime, timedelta
from pypfopt.efficient_frontier import EfficientFrontier
import numpy as np

**INSERT TICKERS**

tickers = []
print('Please input your tickers (press Enter to finish)')

while True:
    ticker = input(f"Enter ticker #{len(tickers) + 1}: ").strip().upper()
    if ticker == '':
        if len(tickers) >= 2:
            break
        print("Please enter at least 2 tickers.")
        continue

    if ticker not in tickers:
        tickers.append(ticker)
        print(f"Added {ticker}")
    else:
        print(f"{ticker} already added.")

start_date = (datetime.now() - timedelta(days=3*365)).strftime('%Y-%m-%d')
data = yf.download(tickers, start=start_date, auto_adjust=True)['Close']
data = data.dropna()


**Calculating Historical Returns + (Co)Variance**

mu = mean_historical_return(data)
S = CovarianceShrinkage(data).ledoit_wolf()
plotting.plot_covariance(S, plot_correlation=True)
plt.show()

**MIN VARIANCE**

EF = EfficientFrontier(mu, S)
EF.min_volatility()
weights = EF.clean_weights()
display(weights)
EF.portfolio_performance(verbose=True)

**MAX SHARPE**

EF = EfficientFrontier(mu, S)

EF.max_sharpe()
weights = EF.clean_weights()
display(weights)
EF.portfolio_performance(verbose=True)

**TARGET RETURNS**

target_return = float(input('Enter your target return in decimal format: '))
EF_target = EfficientFrontier(mu, S) # Create a new instance
EF_target.efficient_return(target_return)
weights = EF_target.clean_weights()
display(weights)
EF_target.portfolio_performance(verbose=True)

**PLOTTING THE EFFICIENT FRONTIER**

# Create a new EfficientFrontier instance for plotting
EF_plot = EfficientFrontier(mu, S)

fig, ax = plt.subplots()
plotting.plot_efficient_frontier(EF_plot, ax=ax, show_assets=True)

# Add tangent portfolio
EF_tangent = EfficientFrontier(mu, S)
EF_tangent.max_sharpe()
tangent_perf = EF_tangent.portfolio_performance(verbose=False)
ax.scatter(tangent_perf[1], tangent_perf[0], marker='+', s=150, c='red',
           label='Tangent Portfolio')

# Add Target Return
EF_target_plot = EfficientFrontier(mu, S)
EF_target_plot.efficient_return(target_return)
target_perf = EF_target_plot.portfolio_performance(verbose=False)
ax.scatter(target_perf[1], target_perf[0], marker='x', s=150, c='blue',
           label='Target Portfolio')

# Add labels for individual assets
for i, (ticker, ret, vol) in enumerate(zip(mu.index, mu, np.sqrt(np.diag(S)))):
    ax.text(vol, ret, ticker, fontsize=9, ha='right')

ax.legend()
plt.show()

# Modern Portfolio Theory Optimiser

A Python implementation of Modern Portfolio Theory (MPT) for optimal portfolio allocation using the Markowitz mean-variance optimisation framework.

## Features

- **Portfolio Optimisation**: Calculate optimal asset allocations using Maximum Sharpe Ratio and Minimum Volatility strategies
- **Real-time Data**: Automatic stock data retrieval via Yahoo Finance API
- **Risk Analysis**: Covariance matrix calculation using Ledoit-Wolf shrinkage estimator
- **Interactive Visualizations**: 
  - Asset correlation heatmap
  - Efficient frontier with tangent portfolio
  - Capital Allocation Line (CAL)
- **Performance Metrics**: Expected returns, volatility, and Sharpe ratios

## Installation

### Prerequisites
- Python 3.7 or higher
- pip package manager

### Setup
1. **Clone the repository:**
   ```bash
   git clone https://github.com/raihan-noor/Portfolio_Optimisation.git
   cd Portfolio_Optimisation
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Run the optimiser:**
   ```bash
   python mpt.py
   ```
## Usage

### Basic Usage

1. Run the script:
   ```bash
   python mpt.py
   ```

2. Enter stock tickers when prompted (e.g., AAPL, MSFT, GOOGL, TSLA)

3. The program will:
   - Download 3 years of historical data
   - Calculate expected returns and risk metrics
   - Display correlation matrix
   - Optimise for minimum volatility and maximum Sharpe ratio
   - Generate efficient frontier visualisation with tangent portfolio

### Example Output

```
Expected Annual Returns:
  AAPL: 12.3%
  MSFT: 15.7%
  GOOGL: 11.2%
  TSLA: 23.8%

MAXIMUM SHARPE RATIO PORTFOLIO
==============================
Expected annual return: 16.2%
Annual volatility: 18.5%
Sharpe Ratio: 0.78

Optimal Weights:
  AAPL: 25.4%
  MSFT: 41.2%
  GOOGL: 18.9%
  TSLA: 14.5%
```

## Visualization

The tool generates several key visualisations:

- **Asset Correlation Matrix**: Shows how different assets move relative to each other
- **Efficient Frontier**: Displays the optimal risk-return trade-off
- **Tangent Portfolio**: Highlights the maximum Sharpe ratio portfolio (red star)

## Technical Details

### Methodology
- **Expected Returns**: Historical mean return over the specified period
- **Risk Model**: Ledoit-Wolf shrinkage covariance estimator
- **Optimisation**: Scipy-based convex optimisation for portfolio weights
- **Risk-Free Rate**: Assumed at 2% (configurable)

### Key Libraries
- `PyPortfolioOpt`: Portfolio optimisation algorithms
- `yfinance`: Real-time financial data
- `matplotlib`: Data visualisation
- `pandas/numpy`: Data manipulation and numerical computations

## File Structure

```
portfolio-optimizer/
├── mpt.py              # Main portfolio optimisation script
├── requirements.txt    # Python dependencies
├── README.md          # Project documentation
└── examples/          # Example outputs and screenshots
```

## Configuration

You can modify key parameters in the script:

```python
# Data period (default: 3 years)
start_date = (datetime.now() - timedelta(days=3*365)).strftime('%Y-%m-%d')

# Risk-free rate for Sharpe ratio calculation (default: 2%)
# In the code, simply rewrite the EF variables as EF = EfficientFrontier(mu, S, risk_free_rate = _) for example
```

## Limitations

- Historical data may not predict future performance
- Assumes normal distribution of returns
- No transaction costs or market constraints considered
- Requires at least 2 assets for diversification

## Acknowledgments

- Built using the [PyPortfolioOpt](https://github.com/robertmartin8/PyPortfolioOpt) library
- Data provided by [Yahoo Finance](https://finance.yahoo.com/)
- Based on Harry Markowitz's Modern Portfolio Theory

## Contact

- **Author**: Raihan Noor
- **Email**: raihannoor361@gmail.com
- **LinkedIn**: www.linkedin.com/in/raihan-noor-7b3606293
---

# Py-Fundamentals

This library utilizes Financial Modeling Prep endpoints to return objects representing
stock fundamentals.

## Installation

Clone this GitHub repo and use the below within the root directory:
```commandline
pip install .
```


# Fundamentals & Stock Fundamentals
Fundamentals and StockFundamentals are interfaces used to return JSON objects for two
different use cases.

### Fundamentals 
Used as a general data reader to return fundamentals for different stocks, meaning 
each cash flow, income statement or balance sheet call needs a 'symbol' param passed.

```python
from fundamentals import Fundamentals

# Instantiating Fundamentals (no 'symbol' param passed).
fundamentals_factory = Fundamentals(api_key="abc123")

# Symbol param MUST be passed during income statement call.
msft_inc_stmts = fundamentals_factory.income_statement(symbol="MSFT",
                                                       period="annual",
                                                       limit=5)
```

### StockFundamentals 
Used to persist a constant stock symbol (passed during instantiation) across all
cash flow, income statement and balance sheet calls.

```python
from fundamentals import StockFundamentals

# Standard fundamentals factory ('symbol' param IS passed).
aapl_fundamentals_factory = StockFundamentals(symbol="AAPL", api_key="abc123")

# No need to pass symbol param during balance sheet call.
aapl_bal_sheets = aapl_fundamentals_factory.balance_sheet(period="quarter",
                                                          limit=15)
```

# FundamentalsFactory & StockFundamentalsFactory

Factories are used to return dataclass objects (defined in fundamentals/dclasses.py)
instead of JSON objects from the classes defined directly above this section.

### FundamentalsFactory

Used to return dataclasses from standard Fundamentals class described above.

```python
from fundamentals import FundamentalsFactory

# Standard fundamentals factory (no 'symbol' param passed).
fundamentals_factory = FundamentalsFactory(api_key="abc123")

# Symbol param MUST be passed during cash flow call.
amzn_cash_flows = fundamentals_factory.cash_flow(symbol="AMZN",
                                                 period="quarter",
                                                 limit=15)
```

### StockFundamentalsFactory

Used to return dataclasses from StockFundamentals class described above.

```python
from fundamentals import StockFundamentalsFactory

# Stock fundamentals factory ('symbol' param IS passed).
aapl_fundamentals_factory = StockFundamentalsFactory(symbol="AAPL", api_key="abc123")

# No need to pass symbol during balance sheet call.
aapl_bal_sheets = aapl_fundamentals_factory.balance_sheet(period="quarter",
                                                          limit=15)
```

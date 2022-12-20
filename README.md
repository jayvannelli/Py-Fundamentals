# Py-Fundamentals

This library utilizes Financial Modeling Prep endpoints to return objects representing
stock fundamentals.

## Usage

Currently, the fundamentals module can be used with one of the below:

### FundamentalsReader
Returns JSON response containing data.

### FundamentalsFactory
Returns list of IncomeStatement, CashFlowStatement and/or 
BalanceSheetStatement objects containing data.

```python
from fundamentals.reader import FundamentalsReader
from fundamentals.factory import FundamentalsFactory

reader = FundamentalsReader(api_key="abc123") # Reader.
factory = FundamentalsFactory(api_key="abc123") # Factory.

SYMBOL: str = "AAPL"
PERIOD: str = "quarter"
LIMIT: int = 2

print(reader is factory) # False
print(reader == factory) # False

reader_cash_flows = reader.cash_flow(SYMBOL, PERIOD, LIMIT)
factory_cash_flows = factory.cash_flow(SYMBOL, PERIOD, LIMIT)

for (r_cash_flow, f_cash_flow) in (reader_cash_flows, factory_cash_flows):
    print(type(r_cash_flow)) # <class 'dict'> <class 'dict'>
    print(type(f_cash_flow)) # <class 'fundamentals.dclasses.CashFlowStatement'> 
    ...                      # <class 'fundamentals.dclasses.CashFlowStatement'>
```

### Compare
Compare allows you to return fundamental data for two stocks given their symbols upon instantiation.
CompareFundamentals currently uses FundamentalFactory to return data.
```python
from fundamentals.compare import CompareFundamentals

comparison = CompareFundamentals(symbol_one="MSFT", symbol_two="AMZN", api_key="abc123")

# You can return two list objects.
msft_cf, amzn_cf = comparison.cash_flow(period="quarter", limit=30)

# Or the one tuple object containing the two lists.
cash_flows = comparison.cash_flow(period="annual", limit=15)
```

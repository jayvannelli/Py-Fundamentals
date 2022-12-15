# Py-Fundamentals

This library utilizes Financial Modeling Prep endpoints to return objects representing
stock fundamentals.

### Usage
```python
from fundamentals.reader import FundamentalsReader

fundamentals = FundamentalsReader(api_key="abc123") # FMP api key.

# Creates list of CashFlowStatement, IncomeStatement & BalanceSheetStatement.
amzn_cash_flows = fundamentals.cash_flow("amzn", "quarter", 5)
tsla_income_statements = fundamentals.income_statement("tsla", "annual", 10)
aapl_balance_sheet_statements = fundamentals.balance_sheet("aapl", "quarter", 50)

# You can access the returned fundamentals by using the following syntax:
for cash_flow_statement in amzn_cash_flows:
    print(cash_flow_statement)
    print(cash_flow_statement.symbol)
    fcf = cash_flow_statement.freeCashFlow
    ocf = cash_flow_statement.operatingCashFlow
    ...
```
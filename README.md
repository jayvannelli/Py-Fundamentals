# Py-Fundamentals

### Usage
```python
from fundamentals.reader import FundamentalsReader

fundamentals = FundamentalsReader(api_key="abc123")

# Creates list of CashFlowStatement, Incomestatement & BalanceSheetStatement dataclasses
amzn_cash_flows = fundamentals.cash_flow("amzn", "quarter", 50)
tsla_income_statements = fundamentals.income_statement("tsla", "annual", 10)
aapl_balance_sheet_statements = fundamentals.balance_sheet("aapl", "quarter", 15)
```
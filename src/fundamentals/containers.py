from dataclasses import dataclass
from .dclasses import BalanceSheetStatement, CashFlowStatement, IncomeStatement


@dataclass
class BalanceSheetsContainer:
    symbol: str
    period: str
    limit: int

    balance_sheets: list[BalanceSheetStatement]


@dataclass
class IncomeStatementsContainer:
    symbol: str
    period: str
    limit: int

    income_statements: list[IncomeStatement]


@dataclass
class CashFlowsContainer:
    symbol: str
    period: str
    limit: int

    cash_flows: list[CashFlowStatement]


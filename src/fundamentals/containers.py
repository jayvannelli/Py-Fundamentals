from dataclasses import dataclass
from .dclasses import BalanceSheetStatement, CashFlowStatement, IncomeStatement


@dataclass
class BalanceSheetContainer:
    symbol: str
    period: str
    limit: int

    balance_sheets: list[BalanceSheetStatement]


@dataclass
class IncomeStatementContainer:
    symbol: str
    period: str
    limit: int

    income_statements: list[IncomeStatement]


@dataclass
class CashFlowContainer:
    symbol: str
    period: str
    limit: int

    cash_flows: list[CashFlowStatement]


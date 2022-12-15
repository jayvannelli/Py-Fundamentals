from .base import Base
from ._utils import _validate_period, _validate_limit
from .dclasses import CashFlowStatement, IncomeStatement, BalanceSheetStatement


class FundamentalsReader(Base):

    def cash_flow(self, symbol: str, period: str, limit: int) -> list[CashFlowStatement]:
        response = self.data(
            url=f"{self._URL_V3}/cash-flow-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )
        return [CashFlowStatement(**i) for i in response]

    def income_statement(self, symbol: str, period: str, limit: int) -> list[IncomeStatement]:
        response = self.data(
            url=f"{self._URL_V3}/income-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )
        return [IncomeStatement(**i) for i in response]

    def balance_sheet(self, symbol: str, period: str, limit: int) -> list[BalanceSheetStatement]:
        response = self.data(
            url=f"{self._URL_V3}/balance-sheet-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )
        return [BalanceSheetStatement(**i) for i in response]

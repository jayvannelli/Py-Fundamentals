from src.fmp import FmpBase
from ._utils import _validate_period, _validate_limit


class FundamentalsReader(FmpBase):

    def cash_flow(self, symbol: str, period: str, limit: int):
        return self.data(
            url=f"{self._URL_V3}/cash-flow-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

    def income_statement(self, symbol: str, period: str, limit: int):
        return self.data(
            url=f"{self._URL_V3}/income-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

    def balance_sheet(self, symbol: str, period: str, limit: int):
        return self.data(
            url=f"{self._URL_V3}/balance-sheet-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

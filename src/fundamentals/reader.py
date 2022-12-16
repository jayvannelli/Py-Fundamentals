from .fmp import FmpBase
from ._utils import _validate_period, _validate_limit


class FundamentalsReader(FmpBase):

    def cash_flow(self, symbol: str, period: str, limit: int):
        """*JSON VERSION*

        Obtain list of stock Cash Flow Statements using FMP endpoint.

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[dict]
        """
        return self.data(
            url=f"{self._URL_V3}/cash-flow-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

    def income_statement(self, symbol: str, period: str, limit: int):
        """*JSON VERSION*

        Obtain list of stock Income Statements using FMP endpoint.

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[dict]
        """
        return self.data(
            url=f"{self._URL_V3}/income-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

    def balance_sheet(self, symbol: str, period: str, limit: int):
        """*JSON VERSION*

        Obtain list of stock Balance Sheet Statements using FMP endpoint.

        Parameters
         ----------
        symbol : str
            Stock ticker symbol.
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[dict]
        """
        return self.data(
            url=f"{self._URL_V3}/balance-sheet-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

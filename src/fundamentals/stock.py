from .readers import FmpSymbolReader
from ._utils import _validate_period, _validate_limit


class StockFundamentals(FmpSymbolReader):
    """Establishes Fundamentals interface for specific stock (given a symbol)."""

    def cash_flow(self, period: str, limit: int):
        """*JSON VERSION*

        Obtain list of stock Cash Flow Statements using FMP endpoint.

        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[dict]
        """
        return self._data(
            url_version="v3",
            path=f"cash-flow-statement/{self.symbol}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

    def income_statement(self, period: str, limit: int):
        """*JSON VERSION*

        Obtain list of stock Income Statements using FMP endpoint.

        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[dict]
        """
        return self._data(
            url_version="v3",
            path=f"income-statement/{self.symbol}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

    def balance_sheet(self, period: str, limit: int):
        """*JSON VERSION*

        Obtain list of stock Balance Sheet Statements using FMP endpoint.

        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[dict]
        """
        return self._data(
            url_version="v3",
            path=f"balance-sheet-statement/{self.symbol}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )

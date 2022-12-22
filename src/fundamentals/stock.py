from .reader import FmpReader
from ._utils import _validate_period, _validate_limit


class StockFundamentals(FmpReader):
    """Establishes Fundamentals interface for specific stock (given a symbol)."""

    def __init__(self, symbol: str, api_key: str, session=None):
        """Interface for Fmp stock reader classes.

        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        api_key: str
            Financial Modeling Prep (FMP) Api Token.
        session: requests.Session
            Requests session object.
        """
        super().__init__(api_key=api_key, session=session)

        self._symbol = symbol.upper()

    @property
    def symbol(self):
        """Symbol getter."""
        return self._symbol

    @symbol.setter
    def symbol(self, new_symbol: str):
        """Symbol setter."""
        self._symbol = new_symbol.upper()

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

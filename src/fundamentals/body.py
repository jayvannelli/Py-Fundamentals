from .reader import FmpReader
from ._utils import _validate_period, _validate_limit


class Fundamentals(FmpReader):
    """Establishes standard Fundamentals interface."""
    def __init__(self, api_key: str, session=None):
        """Interface for standard Fmp reader classes.

        Parameters
        ----------
        api_key: str
            Financial Modeling Prep (FMP) Api Token.
        session: requests.Session
            Requests session object.
        """
        super().__init__(api_key=api_key, session=session)

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
        return self._data(
            url_version="v3",
            path=f"cash-flow-statement/{symbol.upper()}",
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
        return self._data(
            url_version="v3",
            path=f"income-statement/{symbol.upper()}",
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
        return self._data(
            url_version="v3",
            path=f"balance-sheet-statement/{symbol.upper()}",
            params={"period": _validate_period(period), "limit": _validate_limit(limit)}
        )


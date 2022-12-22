from .dclasses import CashFlowStatement, IncomeStatement, BalanceSheetStatement
from .body import Fundamentals
from .stock import StockFundamentals


class FundamentalsFactory(Fundamentals):
    """Factory for standard Fundamentals reader."""

    def cash_flow(self, symbol: str, period: str, limit: int) -> list[CashFlowStatement]:
        """*FACTORY VERSION*

        Obtain list of stock Cash Flow Statements using FMP endpoint.


        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[CashFlowStatement]
        """
        response = super().cash_flow(symbol, period, limit)
        return [CashFlowStatement(**i) for i in response]

    def income_statement(self, symbol: str, period: str, limit: int) -> list[IncomeStatement]:
        """*FACTORY VERSION*

        Obtain list of stock Income Statements using FMP endpoint.


        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[IncomeStatement]
        """
        response = super().income_statement(symbol, period, limit)
        return [IncomeStatement(**i) for i in response]

    def balance_sheet(self, symbol: str, period: str, limit: int) -> list[BalanceSheetStatement]:
        """*FACTORY VERSION*

        Obtain list of stock Cash Balance Sheet Statements using FMP endpoint.


        Parameters
        ----------
        symbol : str
            Stock ticker symbol.
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[BalanceSheetStatement]
        """
        response = super().balance_sheet(symbol, period, limit)
        return [BalanceSheetStatement(**i) for i in response]


class StockFundamentalsFactory(StockFundamentals):
    """Factory for Stock Fundamentals reader (given its symbol upon instantiation)."""

    def cash_flow(self, period: str, limit: int) -> list[CashFlowStatement]:
        """*FACTORY VERSION*

        Obtain list of stock Cash Flow Statements using FMP endpoint.


        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[CashFlowStatement]
        """
        response = super().cash_flow(period, limit)
        return [CashFlowStatement(**i) for i in response]

    def income_statement(self, period: str, limit: int) -> list[IncomeStatement]:
        """*FACTORY VERSION*

        Obtain list of stock Income Statements using FMP endpoint.


        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[IncomeStatement]
        """
        response = super().income_statement(period, limit)
        return [IncomeStatement(**i) for i in response]

    def balance_sheet(self, period: str, limit: int) -> list[BalanceSheetStatement]:
        """*FACTORY VERSION*

        Obtain list of stock Cash Balance Sheet Statements using FMP endpoint.


        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: list[BalanceSheetStatement]
        """
        response = super().balance_sheet(period, limit)
        return [BalanceSheetStatement(**i) for i in response]

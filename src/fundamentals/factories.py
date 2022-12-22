from .body import Fundamentals
from .stock import StockFundamentals

from .dclasses import BalanceSheetStatement, CashFlowStatement, IncomeStatement
from .containers import BalanceSheetsContainer, CashFlowsContainer, IncomeStatementsContainer


class FundamentalsFactory(Fundamentals):
    """Factory for standard Fundamentals reader."""

    def cash_flow(self, symbol: str, period: str, limit: int) -> CashFlowsContainer:
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

        :return: CashFlowsContainer
        """
        response = super().cash_flow(symbol, period, limit)
        cash_flows = [CashFlowStatement(**i) for i in response]
        return CashFlowsContainer(
            symbol=symbol, period=period, limit=limit, cash_flows=cash_flows
        )

    def income_statement(self, symbol: str, period: str, limit: int) -> IncomeStatementsContainer:
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

        :return: IncomeStatementsContainer
        """
        response = super().income_statement(symbol, period, limit)
        income_statements = [IncomeStatement(**i) for i in response]
        return IncomeStatementsContainer(
            symbol=symbol, period=period, limit=limit, income_statements=income_statements
        )

    def balance_sheet(self, symbol: str, period: str, limit: int) -> BalanceSheetsContainer:
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

        :return: BalanceSheetsContainer
        """
        response = super().balance_sheet(symbol, period, limit)
        balance_sheets = [BalanceSheetStatement(**i) for i in response]
        return BalanceSheetsContainer(
            symbol=symbol, period=period, limit=limit, balance_sheets=balance_sheets
        )


class StockFundamentalsFactory(StockFundamentals):
    """Factory for Stock Fundamentals reader (given its symbol upon instantiation)."""

    def cash_flow(self, period: str, limit: int) -> CashFlowsContainer:
        """*FACTORY VERSION*

        Obtain list of stock Cash Flow Statements using FMP endpoint.


        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: CashFlowsContainer
        """
        response = super().cash_flow(period, limit)
        cash_flows = [CashFlowStatement(**i) for i in response]
        return CashFlowsContainer(
            self.symbol, period=period, limit=limit, cash_flows=cash_flows
        )

    def income_statement(self, period: str, limit: int) -> IncomeStatementsContainer:
        """*FACTORY VERSION*

        Obtain list of stock Income Statements using FMP endpoint.


        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: IncomeStatementsContainer
        """
        response = super().income_statement(period, limit)
        income_statements = [IncomeStatement(**i) for i in response]
        return IncomeStatementsContainer(
            symbol=self.symbol, period=period, limit=limit, income_statements=income_statements
        )

    def balance_sheet(self, period: str, limit: int) -> BalanceSheetsContainer:
        """*FACTORY VERSION*

        Obtain list of stock Cash Balance Sheet Statements using FMP endpoint.


        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :return: BalanceSheetsContainer
        """
        response = super().balance_sheet(period, limit)
        balance_sheets = [BalanceSheetStatement(**i) for i in response]
        return BalanceSheetsContainer(
            symbol=self.symbol, period=period, limit=limit, balance_sheets=balance_sheets
        )

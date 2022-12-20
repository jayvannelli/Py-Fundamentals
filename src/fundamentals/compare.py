from .dclasses import CashFlowStatement, IncomeStatement, BalanceSheetStatement
from .factory import FundamentalsFactory


class CompareFundamentals(FundamentalsFactory):
    def __init__(self, symbol_one: str, symbol_two: str, api_key: str, session=None):
        super().__init__(api_key=api_key, session=session)

        if not isinstance(symbol_one, str) or not isinstance(symbol_two, str):
            raise TypeError("Both symbols must be of type: str.")

        self.symbol_one = symbol_one.upper()
        self.symbol_two = symbol_two.upper()

    def cash_flow(self, period: str, limit: int) -> tuple[list[CashFlowStatement], list[CashFlowStatement]]:
        """*COMPARE VERSION*

        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :returns: (list[CashFlowStatement], list[CashFlowStatement])
        """
        s1 = super().cash_flow(self.symbol_one, period=period, limit=limit)
        s2 = super().cash_flow(self.symbol_two, period=period, limit=limit)
        return s1, s2

    def income_statement(self, period: str, limit: int) -> tuple[list[IncomeStatement], list[IncomeStatement]]:
        """*COMPARE VERSION*

        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :returns: (list[IncomeStatement], list[IncomeStatement])
        """
        s1 = super().income_statement(self.symbol_one, period=period, limit=limit)
        s2 = super().income_statement(self.symbol_two, period=period, limit=limit)
        return s1, s2

    def balance_sheet(self, period: str, limit: int) -> tuple[list[BalanceSheetStatement], list[BalanceSheetStatement]]:
        """*COMPARE VERSION*

        Parameters
        ----------
        period : str
            Reporting period ('quarter' or 'annual').
        limit : int
            Number of rows to return.

        :returns: (list[BalanceSheetStatement], list[BalanceSheetStatement])
        """
        s1 = super().balance_sheet(self.symbol_one, period=period, limit=limit)
        s2 = super().balance_sheet(self.symbol_two, period=period, limit=limit)
        return s1, s2

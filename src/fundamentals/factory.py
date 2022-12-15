from .dclasses import CashFlowStatement, IncomeStatement, BalanceSheetStatement
from .reader import FundamentalsReader


class FundamentalsFactory(FundamentalsReader):

    def cash_flow(self, symbol: str, period: str, limit: int) -> list[CashFlowStatement]:
        response = super().cash_flow(symbol, period, limit)
        return [CashFlowStatement(**i) for i in response]

    def income_statement(self, symbol: str, period: str, limit: int) -> list[IncomeStatement]:
        response = super().income_statement(symbol, period, limit)
        return [IncomeStatement(**i) for i in response]

    def balance_sheet(self, symbol: str, period: str, limit: int) -> list[BalanceSheetStatement]:
        response = super().balance_sheet(symbol, period, limit)
        return [BalanceSheetStatement(**i) for i in response]

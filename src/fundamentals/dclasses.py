from dataclasses import dataclass


@dataclass(frozen=True, eq=True, repr=False, slots=True)
class CashFlowStatement:
    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    fillingDate: str
    acceptedDate: str
    calendarYear: str
    period: str
    netIncome: int
    depreciationAndAmortization: int
    deferredIncomeTax: float
    stockBasedCompensation: float
    changeInWorkingCapital: int
    accountsReceivables: float
    inventory: int
    accountsPayables: int
    otherWorkingCapital: float
    otherNonCashItems: float
    netCashProvidedByOperatingActivities: int
    investmentsInPropertyPlantAndEquipment: int
    acquisitionsNet: float
    purchasesOfInvestments: int
    salesMaturitiesOfInvestments: int
    otherInvestingActivites: float
    netCashUsedForInvestingActivites: int
    debtRepayment: float
    commonStockIssued: float
    commonStockRepurchased: float
    dividendsPaid: float
    otherFinancingActivites: float
    netCashUsedProvidedByFinancingActivities: int
    effectOfForexChangesOnCash: float
    netChangeInCash: int
    cashAtEndOfPeriod: int
    cashAtBeginningOfPeriod: int
    operatingCashFlow: int
    capitalExpenditure: int
    freeCashFlow: int
    link: str
    finalLink: str

    def __repr__(self):
        return f"{self.symbol} Cash Flow Statement: {self.date}"


@dataclass(frozen=True, eq=True, repr=False, slots=True)
class IncomeStatement:
    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    fillingDate: str
    acceptedDate: str
    calendarYear: str
    period: str
    revenue: int
    costOfRevenue: int
    grossProfit: int
    grossProfitRatio: float
    researchAndDevelopmentExpenses: int
    generalAndAdministrativeExpenses: float
    sellingAndMarketingExpenses: float
    sellingGeneralAndAdministrativeExpenses: int
    otherExpenses: float
    operatingExpenses: int
    costAndExpenses: int
    interestIncome: int
    interestExpense: int
    depreciationAndAmortization: int
    ebitda: int
    ebitdaratio: float
    operatingIncome: int
    operatingIncomeRatio: float
    totalOtherIncomeExpensesNet: int
    incomeBeforeTax: int
    incomeBeforeTaxRatio: float
    incomeTaxExpense: int
    netIncome: int
    netIncomeRatio: float
    eps: float
    epsdiluted: float
    weightedAverageShsOut: int
    weightedAverageShsOutDil: int
    link: str
    finalLink: str

    def __repr__(self):
        return f"{self.symbol} Income Statement: {self.date}"


@dataclass(frozen=True, eq=True, repr=False, slots=True)
class BalanceSheetStatement:
    date: str
    symbol: str
    reportedCurrency: str
    cik: str
    fillingDate: str
    acceptedDate: str
    calendarYear: str
    period: str
    cashAndCashEquivalents: int
    shortTermInvestments: int
    cashAndShortTermInvestments: int
    netReceivables: int
    inventory: int
    otherCurrentAssets: int
    totalCurrentAssets: int
    propertyPlantEquipmentNet: int
    goodwill: int
    intangibleAssets: int
    goodwillAndIntangibleAssets: int
    longTermInvestments: int
    taxAssets: int
    otherNonCurrentAssets: int
    totalNonCurrentAssets: int
    otherAssets: float
    totalAssets: int
    accountPayables: int
    shortTermDebt: int
    taxPayables: int
    deferredRevenue: int
    otherCurrentLiabilities: int
    totalCurrentLiabilities: int
    longTermDebt: int
    deferredRevenueNonCurrent: float
    deferredTaxLiabilitiesNonCurrent: int
    otherNonCurrentLiabilities: int
    totalNonCurrentLiabilities: int
    otherLiabilities: float
    capitalLeaseObligations: int
    totalLiabilities: int
    preferredStock: float
    commonStock: float
    retainedEarnings: int
    accumulatedOtherComprehensiveIncomeLoss: int
    othertotalStockholdersEquity: int
    totalStockholdersEquity: int
    totalLiabilitiesAndStockholdersEquity: int
    minorityInterest: int
    totalEquity: int
    totalLiabilitiesAndTotalEquity: int
    totalInvestments: int
    totalDebt: int
    netDebt: int
    link: str
    finalLink: str

    def __repr__(self):
        return f"{self.symbol} Income Statement: {self.date}"

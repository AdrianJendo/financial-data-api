from app import db


class ReportModel(db.Model):
    __tablename__ = "reports"
    report_id = db.Column(
        db.Integer,
    )
    symbol = db.Column(db.String, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date, primary_key=True)
    # filing_date = db.Column(db.Date)
    income_statement = db.relationship(
        "IncomeStatementModel",
        uselist=False,
        backref="reports",
        cascade="all, delete-orphan",
    )
    balance_sheet = db.relationship(
        "BalanceSheetModel",
        uselist=False,
        backref="reports",
        cascade="all, delete-orphan",
    )
    cash_flow = db.relationship(
        "CashFlowModel",
        uselist=False,
        backref="reports",
        cascade="all, delete-orphan",
    )

    def __init__(
        self,
        report_id,
        symbol,
        start_date,
        end_date,
    ):
        self.report_id = report_id
        self.symbol = symbol
        self.start_date = start_date
        self.end_date = end_date

    def to_json(self):
        return {
            "report_id": self.report_id,
            "symbol": self.symbol,
            "start_date": self.start_date.strftime("%Y-%m-%d"),
            "end_date": self.end_date.strftime("%Y-%m-%d"),
            "income_statement": self.income_statement.to_json()
            if self.income_statement
            else None,
            "balance_sheet": self.balance_sheet.to_json()
            if self.balance_sheet
            else None,
            "cash_flow": self.cash_flow.to_json() if self.cash_flow else None,
        }

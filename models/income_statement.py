from app import db


class IncomeStatementModel(db.Model):
    __tablename__ = "income_statement"
    report_id = db.Column(db.Integer, db.ForeignKey("reports.report_id"), primary_key=True)
    revenue = db.Column(db.Integer)
    cost_of_sales = db.Column(db.Integer)
    gross_profit = db.Column(db.Integer)
    # r_and_d = db.Colum(db.Integer)
    # g_and_a = db.Colum(db.Integer)
    # interest_expense = db.Colum(db.Integer)
    # operating_income = db.Colum(db.Integer)
    # operating_expenses = db.Colum(db.Integer)
    # income_before_taxes = db.Colum(db.Integer)
    # taxes_paid = db.Colum(db.Integer)
    # net_income = db.Colum(db.Integer)
    # basic_shares_outstanding = db.Colum(db.Integer)
    # diluted_shares_outstanding = db.Colum(db.Integer)

    def __init__(
        self,
        revenue,
        cost_of_sales,
        gross_profit,
        # r_and_d,
        # g_and_a,
        # interest_expense,
        # operating_income,
        # operating_expenses,
        # income_before_taxes,
        # taxes_paid,
        # net_income,
        # basic_shares_outstanding,
        # diluted_shares_outstanding,
    ):
        self.revenue = revenue
        self.cost_of_sales = cost_of_sales
        self.gross_profit = gross_profit
        # self.r_and_d = r_and_d
        # self.g_and_a = g_and_a
        # self.interest_expense = interest_expense
        # self.operating_income = operating_income
        # self.operating_expenses = operating_expenses
        # self.income_before_taxes = income_before_taxes
        # self.taxes_paid = taxes_paid
        # self.net_income = net_income
        # self.basic_shares_outstanding = basic_shares_outstanding
        # self.diluted_shares_outstanding = diluted_shares_outstanding

    def to_json(self):
        return {
            "revenue": self.revenue,
            "cost_of_sales": self.cost_of_sales,
            "gross_profit": self.gross_profit,
            # "r_and_d": self.r_and_d,
            # "g_and_a": self.g_and_a,
            # "interest_expense": self.interest_expense,
            # "operating_income": self.operating_income,
            # "operating_expenses": self.operating_expenses,
            # "income_before_taxes": self.income_before_taxes,
            # "taxes_paid": self.taxes_paid,
            # "net_income": self.net_income,
            # "basic_shares_outstanding": self.basic_shares_outstanding,
            # "diluted_shares_outstanding": self.diluted_shares_outstanding,
        }

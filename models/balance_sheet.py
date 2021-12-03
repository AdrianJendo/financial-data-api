from app import db


class BalanceSheetModel(db.Model):
    __tablename__ = "balance_sheet"
    report_id = db.Column(
        db.Integer, db.ForeignKey("reports.report_id"), primary_key=True
    )
    cash = db.Column(db.Integer)
    marketable_securities = db.Column(db.Integer)
    accounts_receivable = db.Column(db.Integer)
    inventories = db.Column(db.Integer)
    # property_plant_equipment = db.Column(db.Integer)
    # goodwill = db.Column(db.Integer)
    # intangibles = db.Column(db.Integer)
    # total_assets = db.Column(db.Integer)
    # current_assets = db.Column(db.Integer)
    # short_term_debt = db.Column(db.Integer)
    # long_term_debt = db.Column(db.Integer)
    # accounts_payable = db.Column(db.Integer)
    # accrued_expenses = db.Column(db.Integer)
    # deferred_revenue = db.Column(db.Integer)
    # current_liabilties = db.Column(db.Integer)
    # total_liabilities = db.Column(db.Integer)
    # equity = db.Column(db.Integer)
    # retained_earnings = db.Column(db.Integer)

    def __init__(
        self,
        report_id,
        cash,
        marketable_securities,
        accounts_receivable,
        inventories,
        # property_plant_equipment,
        # goodwill,
        # intangibles,
        # total_assets,
        # current_assets,
        # short_term_debt,
        # long_term_debt,
        # accounts_payable,
        # accrued_expenses,
        # deferred_revenue,
        # current_liabilties,
        # total_liabilities,
        # equity,
        # retained_earnings,
    ):
        self.report_id = report_id
        self.cash = cash
        self.marketable_securities = marketable_securities
        self.accounts_receivable = accounts_receivable
        self.inventories = inventories
        # self.property_plant_equipment = property_plant_equipment
        # self.goodwill = goodwill
        # self.intangibles = intangibles
        # self.total_assets = total_assets
        # self.current_assets = current_assets
        # self.short_term_debt = short_term_debt
        # self.long_term_debt = long_term_debt
        # self.accounts_payable = accounts_payable
        # self.accrued_expenses = accrued_expenses
        # self.deferred_revenue = deferred_revenue
        # self.current_liabilties = current_liabilties
        # self.total_liabilities = total_liabilities
        # self.equity = equity
        # self.retained_earnings = retained_earnings

    def to_json(self):
        return {
            "report_id": self.report_id,
            "cash": self.cash,
            "marketable_securities": self.marketable_securities,
            "accounts_receivable": self.accounts_receivable,
            "inventories": self.inventories,
            # "property_plant_equipment": self.property_plant_equipment,
            # "goodwill": self.goodwill,
            # "intangibles": self.intangibles,
            # "total_assets": self.total_assets,
            # "current_assets": self.current_assets,
            # "short_term_debt": self.short_term_debt,
            # "long_term_debt": self.long_term_debt,
            # "accounts_payable": self.accounts_payable,
            # "accrued_expenses": self.accrued_expenses,
            # "deferred_revenue": self.deferred_revenue,
            # "current_liabilties": self.current_liabilties,
            # "total_liabilities": self.total_liabilities,
            # "equity": self.equity,
            # "retained_earnings": self.retained_earnings,
        }

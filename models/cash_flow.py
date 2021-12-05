from app import db


class CashFlowModel(db.Model):
    __tablename__ = "cash_flow"
    report_id = db.Column(
        db.Integer, db.ForeignKey("reports.report_id"), primary_key=True
    )
    depr_and_amort = db.Column(db.Integer)
    stock_based_comp = db.Column(db.Integer)
    cash_from_operating_activities = db.Column(db.Integer)
    cash_from_investing_activities = db.Column(db.Integer)
    cash_from_financing_activities = db.Column(db.Integer)
    # inventories = db.Column(db.Integer)  # operating activities
    # accounts_receivable = db.Column(db.Integer)
    # accounts_payable = db.Column(db.Integer)
    # deferred_revenue = db.Column(db.Integer)
    # capex = db.Column(db.Integer)  # investing activies
    # purchases_of_marketable_securities = db.Column(db.Integer)
    # sales_of_marketable_securities = db.Column(db.Integer)
    # cost_of_acquisition = db.Column(db.Integer)
    # issuance_of_debt = db.Column(db.Integer)  # financing activities
    # payments_of_debt = db.Column(db.Integer)
    # dividends = db.Column(db.Integer)
    # shares_repurchased = db.Column(db.Integer)
    # stock_issued = db.Column(db.Integer)
    # net_increase_of_cash = db.Column(db.Integer)  # misc
    # cash_at_beginning = db.Column(db.Integer)
    # cash_at_end = db.Column(db.Integer)

    def __init__(
        self,
        report_id,
        depr_and_amort,
        stock_based_comp,
        cash_from_operating_activities,
        cash_from_investing_activities,
        cash_from_financing_activities,
        # inventories,
        # accounts_receivable,
        # accounts_payable,
        # deferred_revenue,
        # capex,
        # purchases_of_marketable_securities,
        # sales_of_marketable_securities,
        # cost_of_acquisition,
        # issuance_of_debt,
        # payments_of_debt,
        # dividends,
        # shares_repurchased,
        # stock_issued,
        # net_increase_of_cash,
        # cash_at_beginning,
        # cash_at_end,
    ):

        self.report_id = (report_id,)
        self.depr_and_amort = (depr_and_amort,)
        self.stock_based_comp = (stock_based_comp,)
        self.cash_from_operating_activities = (cash_from_operating_activities,)
        self.cash_from_investing_activities = (cash_from_investing_activities,)
        self.cash_from_financing_activities = (cash_from_financing_activities,)
        # self.inventories = (inventories,)
        # self.accounts_receivable = (accounts_receivable,)
        # self.accounts_payable = (accounts_payable,)
        # self.deferred_revenue = (deferred_revenue,)
        # self.capex = (capex,)
        # self.purchases_of_marketable_securities = (purchases_of_marketable_securities,)
        # self.sales_of_marketable_securities = (sales_of_marketable_securities,)
        # self.cost_of_acquisition = (cost_of_acquisition,)
        # self.issuance_of_debt = (issuance_of_debt,)
        # self.payments_of_debt = (payments_of_debt,)
        # self.dividends = (dividends,)
        # self.shares_repurchased = (shares_repurchased,)
        # self.stock_issued = (stock_issued,)
        # self.net_increase_of_cash = (net_increase_of_cash,)
        # self.cash_at_beginning = (cash_at_beginning,)
        # self.cash_at_end = (cash_at_end,)

    def to_json(self):
        return {
            "report_id": self.report_id,
            "depr_and_amort": self.depr_and_amort,
            "stock_based_comp": self.stock_based_comp,
            "cash_from_operating_activities": self.cash_from_operating_activities,
            "cash_from_investing_activities": self.cash_from_investing_activities,
            "cash_from_financing_activities": self.cash_from_financing_activities,
            # "inventories": self.inventories,
            # "accounts_receivable": self.accounts_receivable,
            # "accounts_payable": self.accounts_payable,
            # "deferred_revenue": self.deferred_revenue,
            # "capex": self.capex,
            # "purchases_of_marketable_securities": self.purchases_of_marketable_securities,
            # "sales_of_marketable_securities": self.sales_of_marketable_securities,
            # "cost_of_acquisition": self.cost_of_acquisition,
            # "issuance_of_debt": self.issuance_of_debt,
            # "payments_of_debt": self.payments_of_debt,
            # "dividends": self.dividends,
            # "shares_repurchased": self.shares_repurchased,
            # "stock_issued": self.stock_issued,
            # "net_increase_of_cash": self.net_increase_of_cash,
            # "cash_at_beginning": self.cash_at_beginning,
            # "cash_at_end": self.cash_at_end,
        }

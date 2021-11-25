from app import db
from sqlalchemy.dialects.postgresql import JSON


class BalanceSheetModel(db.Model):
    __tablename__ = "balance_sheet"
    symbol = db.Column(db.String, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date)
    cash_and_cash_equivalents_current = db.Column(db.Integer)
    marketable_securities_current = db.Column(db.Integer)
    accounts_receivable_current = db.Column(db.Integer)
    inventories_current = db.Column(db.Integer)
    vendor_non_trade_receivables_current = db.Column(db.Integer)
    other_assets_current = db.Column(db.Integer)
    marketable_securities_non_current = db.Column(db.Integer)
    property_plant_equipment_non_current = db.Column(db.Integer)
    other_assets_non_current = db.Column(db.Integer)
    total_assets = db.Column(db.Integer)
    total_assets_current = db.Column(db.Integer)
    accounts_payable = db.Column(db.Integer)
    other_liabilities_current = db.Column(db.Integer)
    deferred_revenue = db.Column(db.Integer)
    debt_current = db.Column(db.Integer)
    debt_non_current = db.Column(db.Integer)
    other_liabilities_non_current = db.Column(db.Integer)
    total_liabilities = db.Column(db.Integer)
    total_liabilities_current = db.Column(db.Integer)
    retained_earnings = db.Column(db.Integer)
    equity = db.Column(db.Integer)
    additional_paid_in_capital = db.Column(db.Integer)

    def __init__(
        self,
        symbol,
        start_date,
        end_date,
        cash_and_cash_equivalents_current,
        marketable_securities_current,
        accounts_receivable_current,
        inventories_current,
        vendor_non_trade_receivables_current,
        other_assets_current,
        marketable_securities_non_current,
        property_plant_equipment_non_current,
        other_assets_non_current,
        total_assets,
        total_assets_current,
        accounts_payable,
        other_liabilities_current,
        deferred_revenue,
        debt_current,
        debt_non_current,
        other_liabilities_non_current,
        total_liabilities,
        total_liabilities_current,
        retained_earnings,
        equity,
        additional_paid_in_capital,
    ):
        self.symbol = (symbol,)
        self.start_date = (start_date,)
        self.end_date = (end_date,)
        self.cash_and_cash_equivalents_current = (cash_and_cash_equivalents_current,)
        self.marketable_securities_current = (marketable_securities_current,)
        self.accounts_receivable_current = (accounts_receivable_current,)
        self.inventories_current = (inventories_current,)
        self.vendor_non_trade_receivables_current = (
            vendor_non_trade_receivables_current,
        )
        self.other_assets_current = (other_assets_current,)
        self.marketable_securities_non_current = (marketable_securities_non_current,)
        self.property_plant_equipment_non_current = (
            property_plant_equipment_non_current,
        )
        self.other_assets_non_current = (other_assets_non_current,)
        self.total_assets = (total_assets,)
        self.total_assets_current = (total_assets_current,)
        self.accounts_payable = (accounts_payable,)
        self.other_liabilities_current = (other_liabilities_current,)
        self.deferred_revenue = (deferred_revenue,)
        self.debt_current = (debt_current,)
        self.debt_non_current = (debt_non_current,)
        self.other_liabilities_non_current = (other_liabilities_non_current,)
        self.total_liabilities = (total_liabilities,)
        self.total_liabilities_current = (total_liabilities_current,)
        self.retained_earnings = (retained_earnings,)
        self.equity = (equity,)
        self.additional_paid_in_capita = additional_paid_in_capital

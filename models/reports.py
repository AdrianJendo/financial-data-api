from app import db


class ReportModel(db.Model):
    __tablename__ = "reports"
    report_id = db.Column(
        db.Integer,
    )
    symbol = db.Column(db.String, primary_key=True)
    start_date = db.Column(db.Date)
    end_date = db.Column(db.Date, primary_key=True)
    # report_date = db.Column(db.Date)

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
        }

from flask import Flask, request
from flask_restful import Resource, Api
import os
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
import pdb
import requests
from datetime import datetime

finnhub_url = os.environ.get("finnhub_url")
api_key = os.environ.get("finnhub_key")
polygon_url = os.environ.get(
    "polygon_url"
)  # ?ticker=MSFT&filing_date.gte=2015-01-01&filing_date.lte=2021-01-01&limit=100&apiKey=***
polygon_key = os.environ.get("polygon_key")

# dotenv
load_dotenv(find_dotenv())

# App config && DB
app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://{}:{}@postgresdb/{}".format(
    os.environ.get("DB_USERNAME"),
    os.environ.get("DB_PASSWORD"),
    os.environ.get("DB_NAME"),
)
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)
api = Api(app)

from models.income_statement import IncomeStatementModel
from models.balance_sheet import BalanceSheetModel
from models.cash_flow import CashFlowModel
from models.reports import ReportModel


def filterQuery(query, start_date=None, end_date=None):
    limit = 5  # By default return 5 reports

    if start_date != None:
        # start_date = datetime.strptime(start_date, "%Y-%M-%d")
        query = query.filter(ReportModel.end_date >= start_date)
        limit = 20  # If querying from start date, allow up to 20 years of data
    if end_date != None:
        # end_date = datetime.strptime(end_date, "%Y-%M-%d")
        query = query.filter(ReportModel.end_date <= end_date)

    query = query.order_by(ReportModel.end_date.desc()).limit(limit).all()

    if query == None:
        return {"Error": "Not Found"}

    return query


def jsonifyStatement(resp):
    json_resp = []
    for entry in resp:
        temp = entry.to_json()
        temp["start_date"] = entry.reports.start_date.strftime("%Y-%m-%d")
        temp["end_date"] = entry.reports.end_date.strftime("%Y-%m-%d")
        json_resp.append(temp)

    return json_resp


class DefaultView(Resource):
    def get(self):
        return {"Hello": "World"}


class BalanceSheet(Resource):
    def get(self, ticker):
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        if end_date != None and start_date != None and end_date < start_date:
            return {"Error": "Start date less than end date"}

        resp = BalanceSheetModel.query.join(
            ReportModel, ReportModel.report_id == BalanceSheetModel.report_id
        ).filter(ReportModel.symbol == ticker)

        resp = filterQuery(resp, start_date, end_date)

        return jsonifyStatement(resp)


class CashFlow(Resource):
    def get(self, ticker):
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        if end_date != None and start_date != None and end_date < start_date:
            return {"Error": "Start date less than end date"}

        resp = CashFlowModel.query.join(
            ReportModel, ReportModel.report_id == CashFlowModel.report_id
        ).filter(ReportModel.symbol == ticker)

        resp = filterQuery(resp, start_date, end_date)

        return jsonifyStatement(resp)


class IncomeStatement(Resource):
    def get(self, ticker):
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        if end_date != None and start_date != None and end_date < start_date:
            return {"Error": "Start date less than end date"}

        resp = IncomeStatementModel.query.join(
            ReportModel, ReportModel.report_id == IncomeStatementModel.report_id
        ).filter(ReportModel.symbol == ticker)

        resp = filterQuery(resp, start_date, end_date)

        return jsonifyStatement(resp)


# Get all financial statements
class Report(Resource):
    def get(self, ticker):
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        if end_date != None and start_date != None and end_date < start_date:
            return {"Error": "Start date less than end date"}

        resp = ReportModel.query.filter(ReportModel.symbol == ticker.upper())

        resp = filterQuery(resp, start_date, end_date)

        return [entry.to_json() for entry in resp]


class Test(Resource):
    def get(self, ticker):
        # Test boys : LRCX, AAPL, DE, CRWD
        resp = requests.get(
            finnhub_url, params={"symbol": ticker, "token": api_key}
        ).json()

        new_income = IncomeStatementModel(report_id=12, revenue=100, cost_of_sales=10)
        db.session.add(new_income)

        try:
            db.session.commit()
        except:
            return {"Error": "Entry could not be added"}

        # pdb.set_trace()
        # db.session.delete()

        return new_income.to_json()


# Register Routes
api.add_resource(DefaultView, "/")
api.add_resource(BalanceSheet, "/balancesheet/<string:ticker>")
api.add_resource(CashFlow, "/cashflow/<string:ticker>")
api.add_resource(IncomeStatement, "/incomestatement/<string:ticker>")
api.add_resource(Report, "/report/<string:ticker>")
api.add_resource(Test, "/test/<string:ticker>")

if __name__ == "__main__":
    app.run(debug=True)

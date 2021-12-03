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

from models.balance_sheet import BalanceSheetModel
from models.reports import ReportModel


class DefaultView(Resource):
    def get(self):
        return {"Hello": "Godbye"}


class BalanceSheet(Resource):
    def get(self, ticker):
        resp = (
            db.session.query(BalanceSheetModel)
            .filter(BalanceSheetModel.symbol == ticker.upper())
            .first()
        )

        if resp == None:
            return {"Error": "Not Found"}

        return resp.to_json()


class Report(Resource):
    def get(self, ticker):
        start_date = request.args.get("start_date")
        end_date = request.args.get("end_date")

        if end_date != None and start_date != None and end_date < start_date:
            return {"Error": "Start date less than end date"}

        limit = 5  # By return 5 reports

        resp = db.session.query(ReportModel).filter(
            ReportModel.symbol == ticker.upper()
        )

        if start_date != None:
            # start_date = datetime.strptime(start_date, "%Y-%M-%d")
            resp = resp.filter(ReportModel.end_date >= start_date)
            limit = 20  # If querying from start date, allow up to 20 years of data
        if end_date != None:
            # end_date = datetime.strptime(end_date, "%Y-%M-%d")
            resp = resp.filter(ReportModel.end_date <= end_date)

        resp = resp.order_by(ReportModel.end_date.desc()).limit(limit).all()

        if resp == None:
            return {"Error": "Not Found"}

        resp = [entry.to_json() for entry in resp]

        return resp


class Test(Resource):
    def get(self):
        # Test boys : LRCX, AAPL, DE, CRWD
        # resp = requests.get(
        #     polygon_url,
        #     params={
        #         "apiKey": polygon_key,
        #         "ticker": "AAPL",
        #         # "filing_date.gte": "2010-01-01",
        #         "filing_date.lte": "2021-01-01",
        #         "limit": 100,
        #         "timeframe": "annual",
        #     },
        # )
        resp = requests.get(finnhub_url, params={"symbol": "CRWD", "token": api_key})
        return resp.json()


# Register Routes
api.add_resource(DefaultView, "/")
api.add_resource(BalanceSheet, "/<string:ticker>")
api.add_resource(Report, "/report/<string:ticker>")
api.add_resource(Test, "/test")

if __name__ == "__main__":
    app.run(debug=True)

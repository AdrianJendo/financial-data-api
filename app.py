from flask import Flask
from flask_restful import Resource, Api
import os
from dotenv import load_dotenv, find_dotenv
from flask_sqlalchemy import SQLAlchemy
import pdb

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


class DefaultView(Resource):
    def get(self):
        resp = (
            db.session.query(BalanceSheetModel)
            .filter(BalanceSheetModel.symbol == "AAPL")
            .first()
        )
        pdb.set_trace()
        return {"Hello": "Godbye"}


class BalanceSheet(Resource):
    def get(self, ticker):
        return {"ticker": ticker}


# Register Routes
api.add_resource(DefaultView, "/")
api.add_resource(BalanceSheet, "/<string:ticker>")

if __name__ == "__main__":
    app.run(debug=True)

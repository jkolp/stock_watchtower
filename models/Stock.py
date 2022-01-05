# use db.Model to connect with sqllite

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# class Stock(db.Model):
#     id = db.Column(db.Integer, primary_key = True)
#     stock_name = db.Column(db.String(10), nullable = False)

#     def __repr__(self):
#         return '%s has been added to the list' % self.stock_name

class Stock: 
    
    def __init__(self, stock_ticker):
        self.ticker = stock_ticker
        self.company_name = None
        self.prices_history = []
        # self.stock_profile = None    # may not need this property



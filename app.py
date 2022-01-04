import requests
from controllers.watchlist_controller import display_current_watchlist
from flask import Flask, render_template, url_for, request, redirect
from flask_sqlalchemy import SQLAlchemy
from models.Stock import Stock
from controllers.watchlist_controller import fetch_stock_profile, fetch_stock_history

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///watchList.db'

db = SQLAlchemy()
db.init_app(app)

# create watchList.db file to store data
with app.app_context():
    db.create_all() 


@app.route('/', methods=['GET'])
def index():
    if request.args.get('stock_ticker') == None :
        watchlist = [Stock(stock_name="apple"), Stock(stock_name="facebook")] # testing code
        return render_template('index.html', watchlist=watchlist) 
    else :
        stock_info= request.args.get('stock_ticker')
        print("*********" + stock_info)
        return stock_info 



#TODO
# API that returns JSON response of the stock_ticker info
# Create model objects then pass as response object
# Need to figure out how to use callbacks in python
@app.route('/get_stock_info/<string:stock_ticker>', methods=['GET'])
def get_stockInfo(stock_ticker):

    fetch_stock_profile(stock_ticker)

    
    fetch_stock_history(stock_ticker)

    return fetch_stock_profile(stock_ticker)
    



if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)



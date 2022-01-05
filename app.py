from controllers.watchlist_controller import display_current_watchlist, get_stock_obj
from flask import Flask, render_template, url_for, request, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.Stock import Stock
from controllers.watchlist_controller import fetch_stock_profile, fetch_stock_history
import requests

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
        watchlist = [Stock(stock_ticker="AAPL"), Stock(stock_ticker="FB")] # testing code
        return render_template('index.html', watchlist=watchlist) 
    else :
        stock_info= request.args.get('stock_ticker')
        print("*********" + stock_info)
        return stock_info 


# API that returns JSON response of the stock info
# Create model objects then pass create jsonify response
@app.route('/get_stock_info/<string:stock_ticker>', methods=['GET'])
def get_stockInfo(stock_ticker):
    stock = get_stock_obj(stock_ticker)
    
    #jsonify() makes it return JSON response
    return jsonify({
        'stock_name': stock.company_name,
        'prices_history': stock.prices_history
    })
    



if __name__ == "__main__":
    app.run(host="localhost", port=8000, debug=True)



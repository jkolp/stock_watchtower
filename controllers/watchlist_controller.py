from flask import Flask, render_template, url_for, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from models.Stock import Stock, db
import requests, json


def get_stock_obj(ticker):
    stock = Stock(ticker)
    stock.company_name = fetch_stock_profile(ticker)['quoteType']['shortName']
    date_and_close_arr = fetch_stock_history(ticker)['prices']

    # Picking out 'date' and 'close' price only and save into prices_history
    for price_dict in date_and_close_arr:
        stock.prices_history.append([price_dict['date'], round(price_dict['close'], 2)])

    return stock
    
    

def fetch_stock_profile(ticker):
    url = "https://yh-finance.p.rapidapi.com/stock/v2/get-profile"
    querystring = {"symbol":ticker,"region":"US"}
    headers = {
        'x-rapidapi-host': "yh-finance.p.rapidapi.com",
        'x-rapidapi-key': "2ac894d627mshd49f02a7d46c4fdp1aed5fjsnc810b6d13354"
        }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        # json.loads(response.text) turns json to python dictionary
        return json.loads(response.text)
    except requests.exceptions.Timeout as err:
        return err
    except requests.exceptions.TooManyRedirects as err:
        return err
    except requests.exceptions.RequestException as err:
        # catastrophic error. bail.
        raise SystemExit(err)

def fetch_stock_history(ticker):
    url = "https://yh-finance.p.rapidapi.com/stock/v3/get-historical-data"
    querystring = {"symbol":ticker,"region":"US"}
    headers = {
    'x-rapidapi-host': "yh-finance.p.rapidapi.com",
    'x-rapidapi-key': "2ac894d627mshd49f02a7d46c4fdp1aed5fjsnc810b6d13354"
    }

    try:
        response = requests.request("GET", url, headers=headers, params=querystring)
        # json.loads(response.text) turns json to python dictionary 
        return json.loads(response.text)
    except requests.exceptions.Timeout as err:
        return err
    except requests.exceptions.TooManyRedirects as err:
        return err
    except requests.exceptions.RequestException as err:
        # catastrophic error. bail.
        raise SystemExit(err)

def display_current_watchlist():
    
    watchlist = Stock.query.order_by(id).all()
    print(watchlist)
    return watchlist


def display_stock_info(id, template):
    stock = Stock.query.get_or_404(id)
    return stock

def store(stock_name):
    new_stock = Stock(stock_name=stock_name)
    try:
        db.session.add(new_stock)
        db.session.commit()
        return True
    except:
        return False

def delete_task(id):
    task_to_delete = Stock.query.get_or_404(id)
    try:
        db.session.delete(task_to_delete)
        db.session.commit()
        return True
    except:
        return False

def update_task(id, new_content):
    task = Stock.query.get_or_404(id)
    try:
        task.content = new_content
        db.session.commit()
        return True
    except:
        return False
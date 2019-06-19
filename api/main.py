# -*- coding: utf-8 -*-
import json
from bson import json_util
import pymongo
from flask import Flask, jsonify, request, render_template

def get_db_connection(uri):
    client = pymongo.MongoClient(uri)
    return  client.crypto

app = Flask(__name__)
db_connection = get_db_connection('mongodb://mongo-crypto:27017')

@app.route('/tickers', methods=['GET'])
def get_documents():
    res = []

    for ticker in db_connection.tickers.find().limit(100):

        ticker.pop('_id')

        res.append(ticker)

    return render_template('/tickers.html', monedas = res)

@app.route("/top-rank-20", methods=['GET'])
def get_rank_top20():
    res = []

    for ticker in db_connection.tickers.find({'rank': {'$lte': 20}}).limit(20):

        ticker.pop('_id')

        res.append(ticker)

    return render_template('/rank-top-20.html', monedas = res)
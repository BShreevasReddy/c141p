from flask import Flask, jsonify,request
import csv

all_articles = []

with open('data.csv','r',encoding='UTF8') as f:
    reader=csv.reader(f)
    data = list(reader)
    all_articles=data[1:]

liked_articles=[]
unliked_articles=[]
did_not_read_articles=[]

app=Flask(__name__)

@app.route("/get-articles")
def get_articles():
    return jsonify({
        "data":all_articles[0],
        "status":"success"
    })

@app.route("/liked-articles",methods=["POST"])
def liked_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    liked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/unliked-articles",methods=["POST"])
def unliked_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    unliked_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

@app.route("/did_not_read-articles",methods=["POST"])
def did_not_read_articles():
    article=all_articles[0]
    all_articles=all_articles[1:]
    did_not_read_articles.append(article)
    return jsonify({
        "status":"success"
    }),201

if __name__=="__main__":
    app.run()
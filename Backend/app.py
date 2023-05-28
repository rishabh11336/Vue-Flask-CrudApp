from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os
import datetime

current_dir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///" + os.path.join(current_dir, "database.sqlite3")

db = SQLAlchemy()
db.init_app(app)
app.app_context().push()

ma = Marshmallow(app)

class Article(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    body = db.Column(db.Text())
    date = db.Column(db.DateTime, default = datetime.datetime.now)

    def __init__(self, title, body):
        self.title = title
        self.body = body


class ArticleSchema(ma.Schema):
    class meta:
        fields = ('id', 'title', 'body', 'date')

article_schema = ArticleSchema()
articles_schema = ArticleSchema(many=True)


@app.route("/get", methods = ["GET"])
def get_article():
    all_articles = Article.query.all()
    result = []
    for article in all_articles:
        article_data = {
            'id': article.id,
            'title': article.title,
            'body': article.body,
            'date': article.date
        }
        result.append(article_data)
    return jsonify(result)

@app.route("/get/<int:id>", methods = ["GET"])
def get_article_id(id):
    all_articles = Article.query.filter_by(id=id).first()
    return jsonify({
        'id': all_articles.id,
        'title': all_articles.title,
        'body': all_articles.body,
        'date': all_articles.date
    })

@app.route('/add', methods = ['POST'])
def add_article():
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    article = Article(title, body)
    db.session.add(article)
    db.session.commit()
    articles = Article.query.filter_by(title=title, body=body).first()
    return jsonify({'id':articles.id, 'title':articles.title, 'body':articles.body, 'date':articles.date})

@app.route('/update/<int:id>', methods = ['PUT'])
def update_article(id):
    article = Article.query.filter_by(id=id).first()
    data = request.get_json()
    title = data.get('title')
    body = data.get('body')
    article.title = title
    article.body = body
    db.session.commit()
    articles = Article.query.filter_by(id=id).first()
    return jsonify({'id':articles.id, 'title':articles.title, 'body':articles.body, 'date':articles.date})

@app.route('/delete/<int:id>', methods = ['DELETE'])
def delete_article(id):
    article = Article.query.filter_by(id=id).first()
    db.session.delete(article)
    db.session.commit()

    return jsonify({'id':article.id, 'title':article.title, 'body':article.body, 'date':article.date})

if __name__ == "__main__":
    app.run(debug=True)
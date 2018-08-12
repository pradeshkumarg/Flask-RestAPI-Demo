from flask import Flask, jsonify
from flask_mysqldb import MySQL
import json

app = Flask(__name__)

# setting secret key
app.secret_key = 'lol'
app.config['SESSION_TYPE'] = 'filesystem'

# config mysql
app.config["MYSQL_HOST"]='localhost'
app.config["MYSQL_USER"]='root'
app.config["MYSQL_PASSWORD"]=''
app.config["MYSQL_DB"]='myapp'
app.config["MYSQL_CURSORCLASS"]='DictCursor' # for Dictionary

# init mysql
mysql = MySQL(app)

# root route
@app.route("/")
def hello():
    return jsonify({
        "about":"Rest API with Flask"
    });


# get all users
@app.route("/users")
def users():
        # create cursor
        cur = mysql.connection.cursor()

        # Get users
        result = cur.execute('SELECT * FROM users')

        if(result>0):
            users = []
            for row in cur.fetchall():
                users.append(row)
            return jsonify(users)
        else:
            return jsonify({
            "code":"404",
            "result":"No users found"
            });

# get all articles:
@app.route("/articles")
def articles():
        # create cursor
        cur = mysql.connection.cursor()

        # Get users
        result = cur.execute('SELECT * FROM articles')

        if(result>0):
            articles = []
            for row in cur.fetchall():
                articles.append(row)
            return jsonify(articles)
        else:
            return jsonify({
            "code":"404",
            "result":"No articles found"
            });

# get article by id
@app.route("/article/<string:id>")
def article(id):
        # create cursor
        cur = mysql.connection.cursor()

        # Get users
        result = cur.execute('SELECT * FROM articles where id = %s ',[id])

        if(result>0):
            return jsonify(cur.fetchone())
        else:
            return jsonify({
            "code":"404",
            "result":"No articles found"
            });



if __name__ == '__main__':
        app.run(debug=True)

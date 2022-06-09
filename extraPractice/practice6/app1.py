from flask import Flask, render_template, request
import sqlite3
app = Flask(__name__)

@app.route('/get_all_members')
def cmember():
	connect = sqlite3.connect('members.db')
	member = connect.execute('select * from students')


@app.route('/get_all_female_members')
def cfmember():
	connect = sqlite3.connect('members.db')
	member = connect.execute('select * from students where gender is f')


if __name__ == '__main__':
   app.run(debug = True)
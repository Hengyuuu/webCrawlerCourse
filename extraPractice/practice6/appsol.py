from flask import Flask
import sqlite3
import json

app = Flask(__name__)

# route() decorator in Flask is used to bind URL to a function
# url: 127.0.0.1/hello

@app.route('/get_all_members')
def get_all_members():
    conn = sqlite3.connect("members.db")     # 資料庫連線
    results = conn.execute("SELECT * from students")
    all_members = results.fetchall()    

    json_data = json.dumps(all_members)
    conn.close()
    return json_data
    
@app.route('/get_all_female_members')
def get_all_female_members():
    conn = sqlite3.connect("members.db")     # 資料庫連線
        
    sql = '''SELECT name, gender
        from students
        where gender = "f"'''
    results = conn.execute(sql)
    

    all_female_members = results.fetchall()    

    json_data = json.dumps(all_female_members)
    conn.close()
    return json_data


if __name__ == '__main__':
   app.run()
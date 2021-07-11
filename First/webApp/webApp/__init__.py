import mysql.connector
from mysql.connector import Error


from flask import Flask, render_template,request




def read(data):
    try:
        connection = mysql.connector.connect(host='localhost',
                                             database='first',
                                             user='root',
                                             password='admin')
        if connection.is_connected():
            db_Info = connection.get_server_info()
            print("Connected to MySQL Server version ", db_Info)
            cursor = connection.cursor()
            cursor.execute("select * from t1 where ts=%s;",[data])
            records = cursor.fetchall()
            for record in records:
                return record
               
                
    
    except Error as e:
        print("Error while connecting to MySQL", e)
        return e
    finally:
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
            


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/getData', methods=['POST','GET'])
def submit():
    if request.method == "POST":
       # getting input with name = fname in HTML form
       first_name = request.form.get("time")
       # getting input with name = lname in HTML fo
       a=read(first_name)
       #return first_name+a
    return render_template('submit.html',post=a)

if __name__ == "__main__":
    app.run(debug=True)




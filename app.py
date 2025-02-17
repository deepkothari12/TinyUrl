from flask import Flask, render_template , request  , url_for , redirect
import mysql.connector 
import dbHelper
import random 
import string

app = Flask(__name__)

url_mapping = {}
##Randome string and randomg number genrator Function
def RandomStrNum(len = 6):
    Random_string = ""
    for i in range(len):
        Random_string = Random_string + random.choice(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase)

    return Random_string

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/Data" , methods = ['POST' , 'GET'])
def get_data():
    if request.method == "POST":
        url = request.form.get("longUrl")
        # print(url , RandomStrNum())
        alias = request.form.get("alias")
        # RandomStrNums = RandomStrNum()
        if alias:
            url_mapping[alias] = url
            Short_url =  f"{request.host}/{alias}" 
            dbHelper.dataBase(long_url=url , alias=alias)#.DBConnect()
        else:
            #print(url , RandomStrNum())
            random_nu = RandomStrNum()
            url_mapping[random_nu] = url
            Short_url =  f"{request.host}/{random_nu}"

        # ##Call the Class
        
        # Short_url = Short_url
        #print(f"Short url -->  {request.host}/{alias}")
    
    return render_template('index.html'   , Short_url = Short_url)


@app.route("/<Short_url>")
def redirectTooriginal(Short_url):
    # print("D")
    try:
        or_u = url_mapping.get(Short_url)
        #print(or_u)
        if or_u:
            return redirect(or_u)
    except Exception as e:
        print(e)
    
    return render_template('index.html' )#, Short_url = Short_url)


if __name__ == "__main__":
    app.run(debug=True)
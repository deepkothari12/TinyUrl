from   flask import Flask, render_template , request  , url_for , redirect , session
import dbHelper
import Genrator ##fileee 
import random 
import string
import pyngrok

app = Flask(__name__)
app.secret_key = "200323"

#url = {}
##Randome string and randomg number genrator Function
def RandomStrNum(len = 6):
    Random_string = ""
    for i in range(len):
        Random_string = Random_string + random.choice(string.ascii_letters + string.ascii_lowercase + string.ascii_uppercase)

    return Random_string

@app.route("/")
def index():
    global ip
    ip = request.remote_addr
    #print(ip)
    # dbHelper.dataBase().IpaddressStore(ip) ##store the user ip address
    return render_template('index.html')

@app.route("/Data" , methods = ['POST' , 'GET'])
def get_data():
    if request.method == "POST":
        Short_url = ""
        url = request.form.get("longUrl")
        # print(url , RandomStrNum())
        alias = request.form.get("alias")
        # RandomStrNums = RandomStrNum()
        ##chek in DataBase
        dbObj = dbHelper.dataBase()
        DataFIndTrue = dbObj.FindData(aliass = alias)
        

        if  DataFIndTrue:
                #print("Data Availabel")

                return render_template('index.html' , DataFIndTrue = DataFIndTrue)

        elif alias:
                #url[alias] = url
                
                Short_url =  f"{request.host}/{alias}" 
                #dbHelper.dataBase.DBConnect(long_url=url , alias=alias)#.DBConnect()
                dbObj = dbHelper.dataBase()
                #dbObj.DBConnect(long_url = url , aliass = alias)
                dbObj.InsertData(long_url = url , aliass = alias , ip=ip)#ip from index
                #print(Short_url)
                #Short_url = Short_url
                session['alias'] = alias ##for another function herer we used seceret key 
                session['short_url'] = Short_url
                ## DONEEEEEEEEEEEEEEEEEEEEEEEEEE
        else:
                #print(url , RandomStrNum())
                random_nu = RandomStrNum()
                # url[random_nu] = url
                # Short_url =  f"{request.host}/{random_nu}"
                Short_url =  f"{request.host}/{random_nu}" 
                #dbHelper.dataBase.DBConnect(long_url=url , alias=alias)#.DBConnect()
                dbObj = dbHelper.dataBase()
                # dbObj.DBConnect(long_url = url , aliass = random_nu)
                dbObj.InsertData(long_url = url , aliass = alias , ip=ip)
                #print(Short_url)
                #Short_url = Sho
            

        #Call the Class
        
        #print(f"Short url -->  {request.host}/{alias}")
    
    return render_template('index.html', Short_url = Short_url) 



@app.route("/<Short_url>" ,  methods = ['POST' , 'GET'])
def redirectTooriginal(Short_url):
    # try:
    #or_u = url_mapping.get(Short_url)
    #print(or_u)
    #print(Short_url)
    if Short_url == "favicon.ico":
        #print("Favicon Wala hu")
        return "error - 404"
    else:
        #print("Startig Function" , Short_url)
        dbObj = dbHelper.dataBase()
        #print(dbObj)
        or_u = dbObj.FindData(aliass = Short_url)
        #print(or_u)
        if or_u:
            return redirect(or_u)
        else :
            pass

    # except Exception as e:
    #     print(e)
        
    return render_template('index.html') # Short_url = Short_url)

@app.route("/qrcode_genrator" , methods = ['GET' , 'POST'])
def QRcodeee():
    # qr_code = None
    #print("Dataaaa")
    #print(alias , short_url)
    # if  request.method == "POST":
    alias = session.get('alias')
    short_url = session.get('short_url')
    #print(short_url)
    if  short_url:
            QRobj = Genrator.QRGENRATOR() ##QR code Filee
            qr_codeee = QRobj.QRgenrator(Short_url=short_url)
            #print(qr_code)
            dbHelper.dataBase().QRStroe(qr_codeee , alias) ##DataBase Filee
            print("done")
    else :
        return render_template("index.html")
    # else:
    #     return render_template("index.html")

    #print("Doneeee")
    return render_template("index.html" , Done = qr_codeee)



if __name__ == "__main__":
    app.run(debug=True)
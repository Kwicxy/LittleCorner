from flask import Flask, render_template, request, redirect, send_file, flash
import datetime as dt
import json as js
import os
from urllib.parse import quote
import sys

IP = "0.0.0.0"
PORT = 114

#################### ���ߺ����ͳ�ʼ�� ####################
# ��ȡ����·��
def init_path():
    global PATH
    path = os.path.abspath(__file__)
    PATH = os.path.dirname(path)
    print(f"[INIT] PATH: {PATH}")
    
# ������־�ļ����û��ļ���ʼ��
def init_file():
    print("[INIT] READ DATA_FILE&USERS")
    global USER_LST, USERFILE
    init_path()
    bin_ = os.path.join(PATH,"bin")
    USERFILE = os.path.join(bin_,"users.json")
    USER_LST = read_file(USERFILE)
    


#################### Flask������ ####################
app = Flask("chat_room", static_url_path="/static", static_folder="./templates/static")
app.config['JSON_AS_ASCII'] = False
app.secret_key = "hard"

# ��ҳ
@app.route("/")
def index():
    addr = request.remote_addr
    if not addr in USER_LST:            # �û�δע�ᣬ�ض�����ע��ҳ��
        return redirect('/register')
    else:
        userid = USER_LST[addr]
        HOUR_NOW = dt.datetime.now().hour
        if HOUR_NOW in range(5,12):
            return render_template("index.html", greetings="Good Morning", userid=userid)
        elif HOUR_NOW in range(12,18):
            return render_template("index.html", greetings="Good Afternoon", userid=userid)
        elif HOUR_NOW in range(18,22):
            return render_template("index.html", greetings="Good Evening", userid=userid)
        else:
            return render_template("index.html", greetings="Good Night", userid=userid)


########################################
if __name__ =="__main__":
    app.run(host=IP, port=PORT, debug=True)
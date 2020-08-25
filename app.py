from flask import Flask, render_template, url_for, request
import requests
import random
app = Flask(__name__)

@app.route('/')
def hello_world():
    top=['cristiano','kyliejenner','leomessi','selenagomez','beyonce','nickiminaj','neymarjr','justinbieber','therock','badgalriri','arianagrande','kimkardashian','taylorswift','khloekardashian','mileycyrus','katyperry','kourtneykardash','kevinhart4real','theellenshow','zendaya','iamcardib','champagnepapi','chrisbrownofficial','kingjames','shakira','billieeilish','vindiesel','davidbeckham','justintimberlake','emmawatson','priyankachopra','gigihadid','shawnmendes','deepikapadukone','ronaldinho']
    cho=random.sample(top,2)
    
    user1 = cho[0]
    user2 = cho[1]
    # return val
    return render_template('index.html',p1=user1, p2=user2)

@app.route('/', methods=['POST','GET'])
def getvalue():
    val=request.form['name1']
    name=val.split(" ")

    url1 = 'https://www.instagram.com/' + name[0]
    r1 = requests.get(url1).text
    start1 = '"edge_followed_by":{"count":'
    end1 = '},"followed_by_viewer"'
    followers1=r1[r1.find(start1)+len(start1):r1.rfind(end1)]

    url2 = 'https://www.instagram.com/' + name[1]
    r2 = requests.get(url2).text
    start2 = '"edge_followed_by":{"count":'
    end2 = '},"followed_by_viewer"'
    followers2=r2[r2.find(start2)+len(start2):r2.rfind(end2)]

    if followers1>followers2:
        statu="Correct! "
    else:
        statu="Incorrect! "

    
    return render_template('result.html',status=statu, name11=name[0],name22=name[1], f1=followers1, f2=followers2)


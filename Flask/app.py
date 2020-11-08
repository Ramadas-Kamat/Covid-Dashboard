from flask import Flask
from flask import render_template, request

import json

app = Flask(__name__)
@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route('/about')
def about():
    return render_template("about.html")

@app.route('/sym')
def sym():
    return render_template("sym.html")

@app.route('/country')
def country():
    return render_template("country.html")

@app.route('/c')
def contributors():
    name1 = 'Sharath'
    name2 = 'Anup'
    name3 = 'Ramadas'
    name4 = 'Shravan'
    name5 = 'Deeksha'
    name6 = 'Karthik'
    name7 = 'Disha'
    names = [name1,name2,name3,name4,name5,name6,name7]
    return render_template('contributors.html',ans = names)
    return render_template("contributors.html")





@app.route('/covid19info', methods=['GET', 'POST'])
def covid19info():
    state = request.form['state']
    my = open('templates/json/ex.json')
    js = my.read()

    obj = json.loads(js)

    lst = obj["data"]["regional"]
    for i in range(0,len(lst)):
        if lst[i].get('loc').lower() == state.lower():
            totalcases = lst[i].get("confirmedCasesIndian")
            discharged = lst[i].get("discharged")
            deaths = lst[i].get("deaths")
            break
        if i>=len(lst)-1:
            return render_template("invalid.html")
    return render_template("covid1.html", totalcases= totalcases, discharged=discharged, deaths=deaths )
# @app.route('/about')

# def about():
#     return render_template("about.html", name1 = 'Shravan')





if __name__ == '__main__':
    app.run(host='localhost', port=6222, debug= True)

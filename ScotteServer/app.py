from flask import Flask, render_template
import datetime, json

app = Flask(__name__)

@app.route('/')
@app.route('/index.html')
def index():
    now = datetime.datetime.now()
    timeString = now.strftime("%Y-%m-%d %H:%M")
    metadata = {
      'title' : 'Online Pillefyr',
      'time': timeString
      }

    myweatherdata = {}
    with open('static/weatherdata.json') as infile:
        myweatherdata = json.load(infile)

    myscottedata = {}
    with open('static/scottedata.json') as infile:
        myscottedata = json.load(infile)

    mysystemdata = {}
    with open('static/systemdata.json') as infile:
        mysystemdata = json.load(infile)

    templatedata = {}
    templatedata['meta'] = metadata
    templatedata['weather'] = myweatherdata
    templatedata['scotte'] = myscottedata
    templatedata['system'] = mysystemdata
    return render_template('index.html', **templatedata)

@app.route('/<path:path>')
def static_file(path):
    return app.send_static_file(path)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=8080)
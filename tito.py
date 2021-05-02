# tito: a simple web ui to display current host stats

import os
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def tito():
    posts = {}

    # get system name
    returned_output = os.uname()
    posts['hostname'] = returned_output[1]

    # get system uptime
    posts['uptime'] = os.popen('uptime -p').read()[:-1]

    # get system temperature
    # cmd = "sudo vcgencmd measure_temp"
    # posts['temp'] = subprocess.check_output(cmd)


    return render_template('index.html', posts=posts)
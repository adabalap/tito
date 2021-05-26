# tito: a simple web ui to display current host stats

import os
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def tito():
    posts = {}

    # Get environment variables
    # get node/host name set from the container environment variables

    # Using ternary operator
    # [on_true] if [expression] else [on_false]

    posts['node_name'] = os.getenv('HOSTNAME') if os.getenv('HOSTNAME') else  os.getenv('MY_NODE_NAME')

    # get pod name
    returned_output = os.uname()
    posts['pod_name'] = returned_output[1]

    # get system uptime
    #posts['uptime'] = os.popen('uptime -p').read()[:-1]

    with open('/proc/uptime', 'r') as f:
        posts['uptime'] = float(f.readline().split()[0])

    # get system temperature
    #cmd = "sudo vcgencmd measure_temp"
    #posts['temp'] = subprocess.check_output(cmd)

    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

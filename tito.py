# tito.py: a simple web UI to display current host stats

import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def tito():
    posts = {}

    # Get environment variables
    #posts['node_name'] = os.getenv('HOSTNAME') or os.getenv('MY_NODE_NAME')
    posts['node_name'] =  os.getenv('MY_NODE_NAME')

    # Get pod name
    returned_output = os.uname()
    posts['pod_name'] = returned_output[1]

    # Get system uptime and format it
    with open('/proc/uptime', 'r') as f:
        total_seconds = float(f.readline().split()[0])
        days, remainder = divmod(int(total_seconds), 86400)
        hours, remainder = divmod(remainder, 3600)
        minutes, seconds = divmod(remainder, 60)
        posts['formatted_uptime'] = f"{days} Days {hours:02d}:{minutes:02d}:{seconds:02d}"

    # Get system memory information
    with open('/proc/meminfo', 'r') as f:
        mem_info = f.readlines()
        mem_total = int(mem_info[0].split()[1])
        mem_free = int(mem_info[1].split()[1])
        posts['mem_usage'] = f"{(mem_total - mem_free) / 1024} MB"

    # Get system CPU information
    with open('/proc/loadavg', 'r') as f:
        load_avg = f.read().split()[:3]
        posts['cpu_load'] = " ".join(load_avg)

    # Get the number of running processes
    posts['num_processes'] = len(os.listdir('/proc')) - 4  # Subtract system processes

    return render_template('index.html', posts=posts)

if __name__ == "__main__":
    app.run(host="0.0.0.0")

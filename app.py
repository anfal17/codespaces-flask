from flask import Flask
import os
import time
import subprocess

app = Flask(__name__)

@app.route('/htop')
def htop():
    name = "Moahmmed Anfal Sharief"
    try:
        username = pwd.getpwuid(os.getuid())[0]
    except:
        username = os.getenv('USER', 'unknown')
    server_time = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
    ist_time = time.strftime('%Y-%m-%d %H:%M:%S', time.gmtime(time.time() + 19800))  # IST is GMT+5:30

    # Run 'top' command and capture output
    top_output = subprocess.check_output(['top', '-b', '-n', '1']).decode('utf-8')

    return f"""
    <html>
      <body>
        <h1>System Info</h1>
        <p><strong>Name:</strong> {name}</p>
        <p><strong>Username:</strong> {username}</p>
        <p><strong>Server Time (IST):</strong> {ist_time}</p>
        <pre>{top_output}</pre>
      </body>
    </html>
    """

if __name__ == '_main_':
    app.run(host='0.0.0.0', port=8000)
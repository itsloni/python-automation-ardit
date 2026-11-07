from flask import Flask

app = Flask(__name__) # THIS '__name__' IS A VERY SPECIAL VARIABLE THAT HOLDS THE STRING OF THE SCRIPT __main__

@app.route('/')
def home():
    

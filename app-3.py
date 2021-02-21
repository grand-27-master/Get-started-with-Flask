from flask import Flask,redirect

app=Flask(__name__)

@app.route('/')
def main():
    return 'home page'

@app.route('/home')
def home():
    return redirect('/')

if __name__=='__main__':
        app.run(debug=True)

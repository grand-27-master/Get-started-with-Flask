from flask import Flask

# creating an object
app=Flask(__name__)

# creating a route
@app.route('/')
def main():
    return 'hello'

if __name__ == '__main__':
    app.run(debug=True)

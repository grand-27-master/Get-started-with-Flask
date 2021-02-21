from flask import Flask,render_template,request

# creating an object
app=Flask(__name__)

fruits=['apple','orange','banana']

# creating a route
@app.route('/')
def main():
    return render_template('fruits.html',my_fruits=fruits)

@app.route('/submit',methods=['POST'])
def submit():
    #return 'you are on submit page'
    if request.method=='POST':
        name=request.form['username']

        f=request.files['userfile']
        #print(f)
        f.save(f.filename)

    return '<h2>Hello {}'.format(name)

if __name__ == '__main__':
    app.run(debug=True)

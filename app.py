from flask import Flask, render_template

app = Flask(__name__)


# 1
@app.route('/')
def PAGE1():
    return render_template('PAGE1.html')


# 2
@app.route('/PAGE2/')
def PAGE2():
    return render_template('PAGE2.html')


# 3
@app.route('/PAGE3/')
def PAGE3():
    return render_template('PAGE3.html')



# 4
@app.route('/PAGE4')
def PAGE4():
    return render_template('PAGE4.html')



app.run(debug=True)





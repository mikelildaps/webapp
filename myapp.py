#----------------0. imports-----------------

from flask import Flask,render_template
#----------------1.Init app-----------------
app = Flask(__name__)
#----------------2. Routers-----------------

@app.route('/')
def foo():
    return render_template('boot.html')


@app.route('/bar')
def bar():
    return render_template('bar.html')

@app.route('/whereami')
def whereami():
    return 'Ghana!'

#@app.route('/foo/<name>')
#def foo(name):
  #  return render_template('foo.html', to=name)
#----------------3. Start Server------------
if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1')
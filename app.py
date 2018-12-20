from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/plot/basic')
def basic(name=None):
    from plot_basic import basic
    basic_obj = basic()
    data = basic_obj.plot_basic()
    return render_template('plot/basic.html', name=data)

if __name__ == "__main__":
    app.run(debug=True)
    app.debug = True
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
    return render_template('plot/basic.html', name=data, title='Basic Plot')

@app.route('/bar/chart/one')
def barChartOne(name=None):
    from bar_chart import barChart

    movies = ["Avenger3", "The Thor", "Spider Man", "Super Man", "Hulk"]
    awards = [5, 11, 3, 8, 10]

    basic_obj = barChart()
    data = basic_obj.basic(movies, awards)
    return render_template('plot/basic.html', name=data, title='Simple Bar Chart')

@app.route('/bar/chart/two')
def barChartTwo(name=None):
    from bar_chart import barChart
    # Display the increment in the chart
    mentions = [500, 505]
    years = [2013, 2014]

    basic_obj = barChart()
    data = basic_obj.increaseChart(mentions, years)
    return render_template('plot/basic.html', name=data, title='Increase Bar Chart ')

@app.route('/bar/chart/line')
def barChartLine(name=None):
    from bar_chart import barChart
    # Display the increment in the chart
    variance = [1, 2, 4, 8, 16, 32, 64, 126, 256]
    bias_squared = [256, 128, 64, 32, 16, 8, 4, 2, 1]

    basic_obj = barChart()
    data = basic_obj.ChartLine(variance, bias_squared)
    return render_template('plot/basic.html', name=data, title='Line Bar Chart ')

if __name__ == "__main__":
    app.run(debug=True)
    app.debug = True
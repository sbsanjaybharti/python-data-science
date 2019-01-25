from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')

@app.route('/plot/basic')
def basic(name=None):
    from plot_basic import basic

    years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
    gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3, 15900.8, 20122.7]
    basic_obj = basic()
    data = basic_obj.plot_basic(years, gdp)
    return render_template('plot/basic.html', name=data, title='Basic Plot')

@app.route('/plot/scattered')
def scatteredPlot(name=None):
    from plot_basic import basic

    friends = [70, 65, 72, 63, 71, 64, 60, 64, 67]
    minutes = [176, 170, 205, 120, 220, 130, 105, 145, 190]
    labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

    basic_obj = basic()
    data = basic_obj.scatter(friends, minutes, labels)
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
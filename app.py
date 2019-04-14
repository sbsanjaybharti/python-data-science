from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')

def index():
    return render_template('index.html')


# noinspection PyInterpreter
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
    return render_template('plot/basic.html', name=data, title='Scattered Plot')

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

@app.route('/plot/vector')
def vector(name=None):
    from Linear_Algebra.vector import vector

    hight_weight_age = [70, 170, 40]
    grade = [95, 80, 75, 62]
    linear_algebra = vector()
    vector_add = linear_algebra.add(hight_weight_age, grade)
    vector_dot = linear_algebra.dot(hight_weight_age, grade)
    return render_template('linear_algebra/vector.html', add_value=vector_add, dot_value=vector_dot, title='Vector Spaces in linear algebra')

@app.route('/plot/matrices')
def matrices(name=None):
    from Linear_Algebra.matrix import matrix

    a = [[1,2,3],[4,5,6]]
    b = [[1,2], [3,4], [5,6]]
    matrix = matrix()
    shape = matrix.shape(a)
    identity_matrix = matrix.make_matrix(5, 5, matrix.is_diagonal)
    #shape = matrix.shape(a)
    # matrix = matrix.dot(hight_weight_age, grade)
    value_dict = {}
    value_dict['shape'] = shape
    value_dict['row'] = matrix.get_row(a, 0)
    value_dict['column'] = matrix.get_column(b, 0)
    value_dict['identity_matrix'] = identity_matrix
    value_dict['shape_identity_matrix'] = matrix.shape(identity_matrix)
    return render_template('linear_algebra/matrix.html', value = value_dict, title='Matrices in linear algebra')

if __name__ == "__main__":
    app.run(debug=True)
    app.debug = True
from matplotlib import pyplot
import io
import base64

class barChart:
    def __init__(self):
        self.x_axis =[]
        self.y_axis =[]
    def basic(self, movies, awards):
        img = io.BytesIO()
        self.x_axis = movies
        self.y_axis = awards
        xs = [i + 0.1 for i, _ in enumerate(self.x_axis)]
        pyplot.bar(xs, self.y_axis)
        pyplot.ylabel("# of Academy Awards")
        pyplot.title("My favorite movies")
        pyplot.xticks([i + 0.5 for i, _ in enumerate(self.x_axis)], self.x_axis)
        pyplot.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        pyplot.close()
        return 'data:image/png;base64,{}'.format(graph_url)

    def increaseChart(self, mentions, years):
        self.x_axis = mentions
        self.y_axis = years
        img = io.BytesIO()

        pyplot.bar([2012.6, 2013.6], self.x_axis, 0.8)
        pyplot.xticks(self.y_axis)
        pyplot.ylabel("# of times 'Python'")
        pyplot.ticklabel_format(useOffset=False)
        pyplot.axis([2012.5, 2014.5, 499, 506])
        pyplot.title("Look at the 'Huge' Increase!")

        pyplot.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        pyplot.close()
        return 'data:image/png;base64,{}'.format(graph_url)
    def ChartLine(self, variance, bias_squared):
        self.x_axis = variance
        self.y_axis = bias_squared
        img = io.BytesIO()

        total_error = [x+y for x,y in zip(self.x_axis, self.y_axis)]
        xs = [i for i, _ in enumerate(self.x_axis)]
        pyplot.plot(xs, self.x_axis, 'g-', label='variance')
        pyplot.plot(xs, self.y_axis, 'r-', label='bias^2')
        pyplot.plot(xs, total_error, 'b:', label='total error')

        pyplot.legend(loc=9)
        pyplot.xlabel('model complexity')
        pyplot.title("The Bias-Variance Tradeoff!")
        pyplot.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        pyplot.close()
        return 'data:image/png;base64,{}'.format(graph_url)

# pyplot.show()

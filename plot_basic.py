from matplotlib import pyplot
import io
import base64

class basic:
    def __init__(self):
        self.x_axis =[]
        self.y_axis =[]
    def plot_basic(self, year, gdp):
        img = io.BytesIO()
        self.x_axis = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        self.y_axis = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3, 15900.8, 20122.7]
        # create a line chart, yearson x-axis and gdp on y-axis
        pyplot.plot(self.x_axis, self.y_axis, color='green', marker='o', linestyle='solid')
        pyplot.ylabel("Bilions of $")
        pyplot.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        pyplot.close()
        return 'data:image/png;base64,{}'.format(graph_url)
    def scatter(self, friends, minutes, labels):
        self.x_axis = friends
        self.y_axis = minutes
        img = io.BytesIO()
        pyplot.scatter(self.x_axis, self.y_axis)
        for label, friend_count, minute_count in zip(labels, self.x_axis, self.y_axis):
            pyplot.annotate(label, xy=(friend_count, minute_count), xytext=(5, -5), textcoords='offset points')
        pyplot.title('Daily Minutes vs Number of friends')
        pyplot.xlabel("# of friends")
        pyplot.ylabel("Daily minutes spend on site")
        pyplot.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        pyplot.close()
        return 'data:image/png;base64,{}'.format(graph_url)

# pyplot.show()

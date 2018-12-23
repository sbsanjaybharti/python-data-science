from matplotlib import pyplot
import io
import base64

class basic:
    def __init__(self):
        self.years =[]
        self.gdp =[]
    def plot_basic(self):
        img = io.BytesIO()
        self.years = [2010, 2011, 2012, 2013, 2014, 2015, 2016, 2017, 2018]
        self.gdp = [300.2, 543.3, 1075.9, 2862.5, 5979.6, 10289.7, 14958.3, 15900.8, 20122.7]
        # create a line chart, yearson x-axis and gdp on y-axis
        pyplot.plot(self.years, self.gdp, color='green', marker='o', linestyle='solid')
        pyplot.ylabel("Bilions of $")
        pyplot.savefig(img, format='png')
        img.seek(0)
        graph_url = base64.b64encode(img.getvalue()).decode()
        pyplot.close()
        return 'data:image/png;base64,{}'.format(graph_url)

# pyplot.show()

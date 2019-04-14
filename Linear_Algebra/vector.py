from matplotlib import pyplot
import io
import base64

class vector:
    def add(self, v, w):
        return [v_i+w_i for v_i, w_i in zip(v,w)]
    def dot(self, v, w):
        return [v_i*w_i for v_i, w_i in zip(v,w)]

# pyplot.show()

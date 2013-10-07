import matplotlib.pyplot as plt
from copy import deepcopy
from geom import geom

class geom_line(geom):
    VALID_AES = ['x', 'y', 'color', 'alpha']
    def plot_layer(self, layer):
        layer = {k: v for k, v in layer.iteritems() if k in self.VALID_AES}
        layer.update(self.manual_aes)
        if 'x' in layer:
            x = layer.pop('x')
        if 'y' in layer:
            y = layer.pop('y')
        pl.plot(x, y, **layer)
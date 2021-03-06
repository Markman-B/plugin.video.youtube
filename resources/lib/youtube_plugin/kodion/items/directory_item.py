from builtins import str
from .base_item import BaseItem


class DirectoryItem(BaseItem):
    def __init__(self, name, uri, image=u'', fanart=u''):
        BaseItem.__init__(self, name, uri, image, fanart)
        self._plot = str(name)

    def set_name(self, name):
        self._name = str(name)

    def set_plot(self, plot):
        self._plot = str(plot)

    def get_plot(self):
        return self._plot

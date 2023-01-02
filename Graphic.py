import matplotlib.pyplot as plt

class Graphic:
    def __init__(self):
        self.xData = [1, 2]
        self.yData = [1, 2]
        self.countryName = "none"

    def setX(self, data):
        self.xData = data

    def setY(self, data):
        self.yData = data

    def setCountry(self,name):
        self.countryName = name

    def plot(self):
        plt.plot(self.xData, self.yData)
        plt.ylabel('Value')
        plt.xlabel('Year')
        title = self.countryName + " data"
        plt.title(title)
        plt.show()
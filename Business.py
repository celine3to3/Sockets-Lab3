import json

class Business:
    def __init__(self, country):
        self.userCountry = country
        self.userJson = ""

    def buildYearQuery(self):
        return "SELECT years FROM country_data WHERE countries = " + "\'" + self.userCountry + "\'" + "ORDER BY years"

    def buildValueQuery(self):
        return "SELECT yearvalues FROM country_data WHERE countries = " + "\'" + self.userCountry + "\'" + \
               "ORDER BY years"

    def setJson(self, jsonString):
        self.userJson = jsonString

    def unpackJson(self):
        datadict = json.loads(self.userJson)
        xAxis = list(datadict.keys())
        yAxis = list(datadict.values())
        [float(i) for i in yAxis]
        parsedX = []
        for x in xAxis:
            parsedX.append(int(x))
        # print(parsedX)
        # print(yAxis)
        return parsedX, yAxis
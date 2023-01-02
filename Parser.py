# Celine Phan
# Lab 3 Sockets
import lxml as lxml
from bs4 import BeautifulSoup


class Parser:
    def __init__(self, file):
        self.file = file
        self.soup = "none"

    def loadList(self):
        infile = open(self.file, "r")
        contents = infile.read()
        self.soup = BeautifulSoup(contents, 'xml')
        countries = self.soup.find_all('Country')
        years = self.soup.find_all('Year')
        values = self.soup.find_all('Value')

        countryList = []
        yearList = []
        valuesList = []

        for country in countries:
            countryList.append(country.get_text())

        for year in years:
            yearList.append(year.get_text())

        for value in values:
            valuesList.append(value.get_text())

        return countryList, yearList, valuesList
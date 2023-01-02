# Celine Phan
# Lab 3 Sockets
import threading
import socket
import time
import Parser
import Database
import User
import Business
import Graphic

port = 5000


def server():
    print("INIT SERVER")
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Get local machine name
    s.bind((host, port))  # Bind to the port
    s.listen(5)  # Now wait for client connection.

    print('Server listening....')

    queryReceived = ""

    conn, addr = s.accept()  # Establish connection with client.
    print('Got connection from ', addr)

    while True:
        data = conn.recv(1024)

        dataDecoded = data.decode('utf-8')
        # print(dataDecoded)
        # if not data:
        #    print("All data received")
        #    break
        queryReceived += dataDecoded
        if data:
            print("All data received")
            break

    # print("query received: ", queryReceived)
    jsonString = db.retrieveJson(queryReceived)
    # jsonString = retrieve_data(queryReceived)

    data = jsonString.encode("utf-8")
    conn.send(data)
    # print('Sent ', repr(jsonString))

    print('Done sending\n')
    conn.close()


def client():
    print("INIT CLIENT")
    s = socket.socket()  # Create a socket object
    host = socket.gethostname()  # Ip address that the TCPServer  is there

    s.connect((host, port))

    b = Business.Business(selectedCountry)  # pass user's selection
    # build queries for database with user country
    valueQuery = b.buildValueQuery()
    # print(valueQuery)
    query = valueQuery.encode("utf-8")
    s.send(query)

    jsonString = ""
    while True:
        print('receiving data...')
        data = s.recv(1024)
        # print('data=%s', (data))
        dataDecoded = data.decode('utf-8')
        jsonString += dataDecoded
        if dataDecoded:
            break
    # print(jsonString)

    b.setJson(jsonString)
    plotData = b.unpackJson()

    xPlot = plotData[0]
    yPlot = plotData[1]


    tempplot.setX(xPlot)
    tempplot.setY(yPlot)
    tempplot.setCountry(selectedCountry)

    print('Successfully received data and plotted\n')
    s.close()
    print('connection closed')


if __name__ == "__main__":
    portnumber = 5000
    p = Parser.Parser("UNData.xml")
    p.loadList()
    lists = p.loadList()
    countries = lists[0]
    uniqueCountries = sorted(set(countries))
    # print(uniqueCountries)
    years = lists[1]
    values = lists[2]

    # create drop down menu
    u = User.User(uniqueCountries)
    u.create_UI()
    selectedCountry = u.getSelection()  # user's selection
    # create database
    db = Database.Database()
    db.createTable()
    # load data with lists
    db.insertData(countries, years, values)
    tempplot = Graphic.Graphic()
    t1 = threading.Thread(target=server)
    t1.start()
    time.sleep(1)
    t2 = threading.Thread(target=client)
    t2.start()
    t1.join()
    t2.join()
    tempplot.plot()


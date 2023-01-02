# Sockets-Lab3

**Process:** 
The user (client) requests data from the (server) database.  The database sends back the data to the user.  At acquisition of the data an XYPlot is drawn.

**DataFile:**
UNData.xml

**User Layer:**
The user selects a country, and passes the country name to the Business Layer.  Uses TKinter to produce a pull-down for the user to select a country. Sends the selected country to the Business Layer.

**Business Layer:**
Receives the information from the User Layer and constructs a SQL query to send to the Data Layer.  The query extracts the yearly data (1990,2017) for the requested country.  The data may be queried either country year-by-year or in one query for year range.  After receiving the JSON string back from the Data Layer, data is sent to the Graphic Layer for plotting.

**Data Layer:**
Constructs a SQL Database based on the data from the DataFile.  Processes the queries from the Business Layer.   Sends back a JSON string for the requested query.  

**Graphic Layer:**
Uses Graphic Class to draw a MatPlotLib XYPlot.

**Server Layer:**
The database access is controlled by the Server Socket.  The client sends a query, and the server sends a JSON string.

**Client Socket:**
Requests data from the server.  After receiving the data from the server, the client displays the data.

# Program Output

Country select pop up

![lab3 1](https://user-images.githubusercontent.com/121079918/210211828-4effba79-6221-438b-a322-7fa51897918b.png)

Country select drop down


![lab3 2](https://user-images.githubusercontent.com/121079918/210211835-f53fbb6b-befe-4a4a-b353-a26370b8c94f.png)


Send and exit


![lab3 4](https://user-images.githubusercontent.com/121079918/210211832-74a2855f-4e2c-4511-848f-954c221e8a28.png)

Creating database, listening and receiving

![lab3 5](https://user-images.githubusercontent.com/121079918/210211830-66caf12c-ab19-47aa-86ee-96e7f567a373.png)

Graphing data 

![lab3 6](https://user-images.githubusercontent.com/121079918/210211831-7ceb923e-94bf-40c2-be7a-1faab9280c4b.png)

# Database preview

![lab3 database preview](https://user-images.githubusercontent.com/121079918/210212894-723e5820-fa3e-494f-888e-f1f3b0338ae6.png)


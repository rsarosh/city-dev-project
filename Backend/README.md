## INSTALL DEPENDENCIES
 * cd to the Backend folder
 * 'npm install -g express'
 * 'npm install -g documentdb'
 * 'npm install -g nodemon' (not required, nodemon allows the server to restart when file changes are detected)
 
## RUN WEBSITE
 * cd to Client and run 'npm start'
 * leave running, and open a new command prompt:
 * cd to Backend and run 'nodemon start'
 
## CHANGING DATABASE
 * go to Backend/CosmosDB/config.js
 * config.host: The URI found in the 'Keys' section in the CosmosDB on the Azure Dashboard (Read-write Keys)
 * config.authKey: The primary key found under the URI
 * config.databaseID: The name of the database
 * config.collectionID: The name of the collection
 
## IMPORTING CSV FILES
 * download from https://cosmosdbportalstorage.blob.core.windows.net/datamigrationtool/2018.02.28-1.8.1/dt-1.8.1.zip
 * extract and run the 'dtui' executable
 * in source information, add the folder containing all the CSV files
 * in target information, add the connection string of the form "AccountEndpoint=<URI>;AccountKey=<PrimaryKey>;Database=<DatabaseID>"
   - refer to 'changing database' on how to get that info
 * put in the name of the collection under 'Collection'
 * finish uploading process
 
## PORTS
 * By default, the react server is hosted on localhost:3000 and the backend on localhost:3001
 * To change the backend port, 2 steps are required:
   1) Go into Client/package.json and change the proxy to the new port
   2) Go into Backend/bin/www and change the port in the 'normalizePort()' function called
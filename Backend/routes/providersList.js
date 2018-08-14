/*
 Sends a list of all the different course providers in the database, using the SQL 'SELECT DISTINCT' command
*/
var express = require('express');
var router = express.Router();
var path = require("path");

// Setup the documentdb client
var DocumentDBClient = require('documentdb').DocumentClient;
var config = require(path.join(__dirname, '..', 'CosmosDB/config'));
var DBManager = require(path.join(__dirname, '..', 'CosmosDB/dbmanager'))

const client = new DocumentDBClient(config.host, {masterKey: config.authKey});

var handler = new DBManager(client); 

//Initialize the handler
handler.init(function(err) {
	throw err;
}); 

/* GET all providers */
router.get('/', function(req, res, next) {
	
	// This querySpec will find all unique providers
	let querySpec = {
		query: 'SELECT DISTINCT r.Provider FROM root r',
    };	

	handler.find(querySpec, function(err, items){
		if( err ) {
			throw err;
		}
		else {
			// return all of the items found
			res.json( items );
		}
	});

});

module.exports = router;

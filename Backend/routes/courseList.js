/*
 Sends a list of all the courses from a given provider.

 The provider is given through the URL argument 'name', e.g localhost:3000/course-list?name=Seattle_Public_Library
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

/* GET course listing */
router.get('/', function(req, res, next) {
	
	// Returns the title of each course from the given provider
	let querySpec = {
		query: 'SELECT r.Title FROM root r WHERE r.Provider=@provider',
		parameters: [{
			name: '@provider',
			value: req.query.name
		}]
    };
	

	handler.find(querySpec, function(err, items){
		if( err ) {
			throw err;
		}
		else {
			res.json( items );
		}
	});

});

module.exports = router;

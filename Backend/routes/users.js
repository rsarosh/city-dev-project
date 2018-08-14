var express = require('express');
var router = express.Router();
var path = require("path");

var DocumentDBClient = require('documentdb').DocumentClient;
var config = require(path.join(__dirname, '..', 'CosmosDB/config'));
var DBManager = require(path.join(__dirname, '..', 'CosmosDB/dbmanager'))

const client = new DocumentDBClient(config.host, {masterKey: config.authKey});
	
var handler = new DBManager(client); // Create a new manager using the client
handler.init(function(err) { // initialize the handler and connect it to database / collection
	throw err;
}); 

/* GET users listing. */
router.get('/', function(req, res, next) {
	let querySpec = {
		query: 'SELECT r.Title FROM root r WHERE r.Provider=@provider',
		parameters: [{
			name: '@provider',
			value: 'Seattle Public Library'
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

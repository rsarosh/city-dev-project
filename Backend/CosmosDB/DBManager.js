/*
 Creates an object that can handle connections to CosmosDB
 
 Most of the methods are self explanatory.
 Callback functions are usually in the form of function(err, results) where err is null if no errors
*/

let DocumentDBClient = require('documentdb').DocumentClient;
let docdbUtils = require('./handle');

let config = require('./config');

function DBManager(documentDBClient) {
  this.client = documentDBClient;
  this.databaseID = config.databaseID;
  this.collectionID = config.collectionID;

  this.database = null;
  this.collection = null;
}

DBManager.prototype = {
	/*
	 Required to initialize the database manager before using any other methods
	*/
	init: function(callback) {
		let self = this;
		
		// Open the database (if database doesn't exist, it creates it)
		docdbUtils.getDatabase(self.client, self.databaseID, function(err, db) {
		if (err) {
			callback(err);
		} else {
			self.database = db;
			// Open the collection within the database (also creates new collection if not found)
			docdbUtils.getCollection(self.client, self.database._self, self.collectionID, function(err, coll) {
				if (err) {
					callback(err);
				} else {
					console.log('test');
					self.collection = coll;
				}
			});
		}
		});
	},
	
	/*
	 Runs an SQL command to return elements
	*/
	find: function(querySpec, callback) {
		let self = this;

		self.client.queryDocuments(self.collection._self, querySpec).toArray(function(err, results) {
			if (err) {
				callback(err);
			} else {
				callback(null, results);
			}
		});
	},

	addItem: function(item, callback) {
		let self = this;

		item.date = Date.now();
		item.completed = false;

		self.client.createDocument(self.collection._self, item, function(err, doc) {
			if (err) {
				callback(err);
			} else {
				callback(null, doc);
			}
		});
	},
	
	updateItem: function(itemId, callback) {
		let self = this;

		self.getItem(itemId, function(err, doc) {
		if (err) {
			callback(err);
		} else {
			doc.completed = true;

			self.client.replaceDocument(doc._self, doc, function(err, replaced) {
			if (err) {
				callback(err);
			} else {
				callback(null, replaced);
			}
			});
		}
		});
	},

	getItem: function(itemId, callback) {
		let self = this;
		let querySpec = {
			query: 'SELECT * FROM root r WHERE r.id = @id',
			parameters: [{ name: '@id', value: itemId }]
		};

		self.client.queryDocuments(self.collection._self, querySpec).toArray(function(err, results) {
			if (err) {
				callback(err);
			} else {
				callback(null, results[0]);
			}
		});
	}
};

module.exports = DBManager;
var config = {}

/*
If changing accounts, change config.host and config.authKey

config.host: URI found in Settings/Keys within Azure Portal
config.authKey: Primary Key found in Settings/Keys within Azure Portal
config.databaseID: Name of db being accessed
config.collectionID: Name of collection being accessed

*/

config.host = process.env.HOST || "https://9c7f15ff-0ee0-4-231-b9ee.documents.azure.com:443/";
config.authKey = process.env.AUTH_KEY || "jMr1NvGyUJDLdkIT7O13U84BaUfO39olaFwrOjaJ7pXTVYEs2C0VG0o5aLMxBYYDgtqp5HOeR1PBGsosXgTQ7g";
config.databaseID = "ComputingKidsFree";
config.collectionID = "Courses";

module.exports = config;

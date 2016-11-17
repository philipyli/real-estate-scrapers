var Zillow  = require('node-zillow');
var inspect  = require('eyes').inspector({maxLength: 50000});
var request = require('request');
var fs = require('fs');
var parse = require('csv-parse');
var async = require('async');
//var transform = require('stream-transform');
var propertyList;

//////////////////
// old school loop to turn csv into json
var properties = [];
var readFileContents = fs.readFileSync(__dirname+'/0109Run.csv');
var lines = readFileContents.toString().split('\015');

for (var i = 0; i < lines.length; i++) {
    properties.push(lines[i].toString().split(','));
}

//for (var i = 0; i < lines.length; i++) {
//    for (var j = 0; j < 3; j++) {
//        console.log(properties[i][j]);
//    }
//    console.log('\n');
//}

//inspect(properties);

var valuations = [];
//var lines = readFileContents.toString().split('\015');

//steve got this
var zillow = new Zillow('X1-ZWz1a27o8dkbnv_a1050');
// dave got this
//var zillow = new Zillow('X1-ZWz1bf8dhi70nf_2avji');



//////////////
// grabs zestimate for one property and time
var getValuation = function (element, doneCallback) {

	var addressParam = {
		address: element[0],
		citystatezip: element[1]
	//  address: '355 1st St #2102',
	//	citystatezip: '94105'
	};

	//var date = '1150441200000';
	var date = element[2];

	var output = {
	// zpid, street, city, hood, hoodId, zip, histZest, histZestDate
	};

	zillow.callApi('GetSearchResults', addressParam)
	  .then(function(searchResultsResponse) {
	 	fs.appendFileSync(__dirname+'/output.csv', '\015'+addressParam.address+',');
	    var searchResult = searchResultsResponse.response[0].results[0].result[0]
//	 	output.zpid = searchResult.zpid[0];
		fs.appendFileSync(__dirname+'/output.csv', searchResult.zpid[0]+',');
//		output.street = searchResult.address[0].street[0];
		fs.appendFileSync(__dirname+'/output.csv', searchResult.address[0].street[0]+'\015');

	//	output.hood = searchResult.localRealEstate[0].region[0].$.name;
	//	output.hoodId = searchResult.localRealEstate[0].region[0].$.id;
	//	output.city = searchResult.address[0].city[0];

//		output.zipcode = searchResult.address[0].zipcode[0];	
//		fs.appendFileSync(__dirname+'/50LansingOutput.csv', searchResult.address[0].zipcode[0]+',');
	// 	output.currentZestLow = parseInt(searchResult.zestimate[0].valuationRange[0].low[0]._);
	// 	output.currentZest = parseInt(searchResult.zestimate[0].amount[0]._);
	// 	output.currentZestHigh = parseInt(searchResult.zestimate[0].valuationRange[0].high[0]._);
	// 	output.currentZestDate = searchResult.zestimate[0]["last-updated"][0];
	// 	inspect(output);

		var rootUrl = 'http://www.zillow.com/ajax/homedetail/HomeValueChartData.htm?mt=1&format=json&zpid=';

		var req = request(rootUrl+searchResult.zpid[0], function (error, response, body) {
		  	if (!error && response.statusCode == 200) {
			    var result = JSON.parse(body.trim());
//			    inspect(result);
			    var zestFullHistory = result[0].points;
				for	(index = 0; index < zestFullHistory.length; index++) {
					// if within one month before
				    if((date - zestFullHistory[index].x) < (30 * 24 * 60 * 60 * 1000) &&
				       (date - zestFullHistory[index].x) > 0 )
				    {
				    	output.histZest = zestFullHistory[index].y;
				    	fs.appendFileSync(__dirname+'/output.csv', '\015'+searchResult.zpid[0]+','+zestFullHistory[index].y+',');
				    	var zestDate = new Date(zestFullHistory[index].x);
				    	output.histDate = zestDate.getMonth() +"/"+zestDate.getDate()+"/"+zestDate.getFullYear();
				    	fs.appendFileSync(__dirname+'/output.csv', output.histDate+'\015');

						valuations.push(output);

//						inspect(output);
						console.log(searchResult.zpid[0]+' = '+zestFullHistory[index].y);	
//						return doneCallback(null);
					}
				}
		  	}
		})
		req.end();
	  });
}

async.each(properties, getValuation, function (err) {
	inspect(valuations);
	console.log("Finished ALL!");
});

//function writeToCSV() {
//	inspect(valuations);
//	console.log('here');
//}

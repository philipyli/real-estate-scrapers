var Zillow  = require('node-zillow');
//var helpers = require('./helpers');
var inspect  = require('eyes').inspector({maxLength: 50000});
var request = require('request');
var fs = require('fs');
//var jsonQ = require("jsonq");

//var zwsid = process.env.ZWSID
var zillow = new Zillow('X1-ZWz1a27o8dkbnv_a1050')

var addressParam = {
  address: '333 1st St #1104',
	citystatezip: '94105'
};

var output = {
// zpid, street, city, hood, hoodId, zip, histZest, histZestDate
};


zillow.callApi('GetSearchResults', addressParam)
  .then(function(searchResultsResponse) {
 
    var result = searchResultsResponse.response[0].results[0].result[0]
// 	inspect(result);
 	output.zpid = result.zpid[0];
	output.street = result.address[0].street[0];
	output.hood = result.localRealEstate[0].region[0].$.name;
	output.hoodId = result.localRealEstate[0].region[0].$.id;
	output.city = result.address[0].city[0];
	output.zipcode = result.address[0].zipcode[0];	
 	output.currentZestLow = result.zestimate[0].valuationRange[0].low[0]._;
 	output.currentZest = result.zestimate[0].amount[0]._;
 	output.currentZestHigh = result.zestimate[0].valuationRange[0].high[0]._;

 	fs.writeFile("histZest.csv", output.zpid+","+output.street,","+output.hood, function(err) {
 		if(err) {
 			return console.log(err);
 		}
 		console.log("The file was saved!");
 	})


// 	inspect(result.zestimate[0].["last-updated"][0]);
// 	output.currentZestDate = result.zestimate[0].last-updated; 	

//	console.log('blah');
	var histZest = getHistoricalZestimate(output.zpid, '1149158800000')
//		.then(function() {
//			inspect(output);
//			console.log('blah');
//		});

  	inspect(histZest);
//	var zpidParam = {
//	  zpid: output.zpid
//	};

//	zillow.callApi('GetZestimate', zpidParam)
 // 	  .then(function(zestimateResponse) {
  //  	var result2 = zestimateResponse.response[0]	  	
//  	 	inspect(result2);
	//    var result = data.response[0].results[0]
	//    inspect(result);

	// 	console.log('zestimateresults=' + result);
//	    return;
  });

//});


// not part of official API
// doc: http://www.zillow.com/advice-thread/Can-I-get-historical-zestimate-values-from-the-API/471215/
// url: http://www.zillow.com/ajax/homedetail/HomeValueChartData.htm?mt=1&zpid=#&format=json
function getHistoricalZestimate(zpid, date) {

	var rootUrl = 'http://www.zillow.com/ajax/homedetail/HomeValueChartData.htm?mt=1&format=json&zpid=';
	var histZest; 
//	return helpers.httprequest(rootUrl+zpid)
//	    .then(helpers.toJson)
//	    .then(function(results) {
//	      var result = results[0];
//	        return result;
//			inspect(result);
//			inspect(results);
//		});
//}
	request(rootUrl+zpid, function (error, response, body) {
	  	if (!error && response.statusCode == 200) {
		    var result = JSON.parse(body.trim());
		    var zestFullHistory = result[0].points;
//			var zestHistory = jsonQ(result[0].points).jsonQ_root;
//		    inspect(zestHistory);
			for	(index = 0; index < zestFullHistory.length; index++) {
//				inspect(zestHistory[index]);
				// if within one month before
			    if((date - zestFullHistory[index].x) < (30 * 24 * 60 * 60 * 1000) &&
			       (date - zestFullHistory[index].x) > 0 )
			    {
			    	output.histZest = zestFullHistory[index].y;
			    	output.histDateUNIXMilliSec = zestFullHistory[index].x;
//			    	inspect(output);    	
			    	inspect(zestFullHistory[index]);
			    	histZest = zestFullHistory[index];
			    	break;
				}
			}
//			zestHistory.find('x', function() {
//				inspect((this.x - date) < (30 * 24 * 60 * 60 * 1000))
//	=		});
//			inspect(zestHistory.find())
	  	}
	})
	return histZest;
}


//	var requestUrl = rootUrl + params + zpid;



//  return helpers.httprequest(requestUrl)
//    .then(helpers.toJson)
//    .then(function(results) {
//    	inspect(results);
//      var result = results['SearchResults:searchresults'];
//      return result;
//    });
//}
//};
# MapSearch
craw the geographic location information from google map according to information of input.

Input:
>```
JoJo@ dist$ ./MapSearch 
Input Address, City, Country, Type, Radius.
Example:
Address: Zhejiang University
City: 	 Hangzhou
Country: China
Type:	 restaurant
Radius:	 1000
------------------------
Address:ucb
City:los angel
Country:usa
Type:restaurant
Radius:400
```

Output:
>
```
Address: ucb,  City: los angel,  Country: usa, lat and lng:  	 34.0984638 -118.3079614
https://maps.googleapis.com/maps/api/place/radarsearch/json?location=34.0984638,-118.3079614&radius=400&type=restaurant&key=AIzaSyDfa5iUU0doB1TzEbBcVx6xJLjdhQbW67E
Jitlada Restaurant , 5233 Sunset Blvd, Los Angeles, CA 90027, USA , 34.0985757 , -118.3040366
SUBWAY®Restaurants , 5537 Sunset Blvd #109, Los Angeles, CA 90028, USA , 34.0983781 , -118.3106331
Pollo Campero - Sunset Blvd. , 5547 Sunset Blvd, Los Angeles, CA 90028, USA , 34.098266 , -118.311214
Pa Ord Noodle , 5301 Sunset Blvd #8, Los Angeles, CA 90027, USA , 34.0985826 , -118.3061549
El Pollo Loco , 5319 Sunset Blvd, Los Angeles, CA 90027, USA , 34.0983781 , -118.3067404
Ono Hawaiian BBQ , 5539 Sunset Blvd, Los Angeles, CA 90028, USA , 34.0982831 , -118.3107223
.....
```

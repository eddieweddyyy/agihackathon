This app was created for The Good Acre during the Analytics for Good Hackathon in February 2023. The creators were 
Eddie Jang, Richie Kwok, Henri Nguyen, Wyatt Lindquist, and Audrey Stumpf.


Calculations used for each widget:
# To calculate the producer success rate, we found the number of planned deliveries for each producer and compared it to the
# number of actual deliveries. The ratio used is the actual count over the planned count. Similarly, for the product 
# success rate, we found the number of planned and actual deliveries for a product to determine the same ratio. The overall
# success rate is a combination of the two metrics. The number of planned deliveries of a product by a producer is compared 
# to the actuals. 

# The weekly success rate was found from the same ratio of ordered deliveries over planned deliveries of a product, looking
# at a single week (1-52). The price estimate is derived from the delivery success rate and contract details. The contract
# details needed for this are the contract price, sales price, and order quantity.


Backlog:
* Connect to external Database, opportunity to connect with Google Sheets
* Expand functionality through analyzing new variables
* Combine all variables to create a planning factor
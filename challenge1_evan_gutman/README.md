## Description:
	Basic microservice that allows for messages to be hashed and stored for retrieval.
	The two endpoints are:
		-POST /messages -- returns a SHA256 hash digest
		-GET /messages/<hash> -- returns the original message, or a 404 "NOT FOUND", if the message exists
	
	The microservice is published to https://msg-hash.herokuapp.com/


## Dependencies:
	Node v9.11.1
	Redis v5.0.3


## Instructions to Run Locally:
	In one terminal window
		1. redis-server

	In another terminal window
		1. npm install
		2. npm start


## Examples:
	$ curl -X POST -H "Content-Type: application/json" -d '{"message": "evan"}' https://msg-hash.herokuapp.com/messages
	{"digest":"ae74f72d212fb9871302a2459aeaf7b20bc2f792e4852be648a7d4e63967d9b1"}

	$ curl https://msg-hash.herokuapp.com/messages/ae74f72d212fb9871302a2459aeaf7b20bc2f792e4852be648a7d4e63967d9b1
	{"message":"evan"}


## Notes:
	As the number of users increases, the bottleneck would be having only one instance of the server running which would cause 
	the microservice to have a longer response time. In order to scale the microservice, I would use a load balancer with several 
	instances of the microservice running. Regarding the database, I would use a Redis cluster to achieve horizontal scaling 
	through sharding.

	I deployed my application with Heroku because it offers Platform as a Service so I can easily deploy my prototype with minimal 
	configuratin settings. If I was going to maintain the microservice long term, I would improve the deployment by setting up an 
	autoscaler to efficiently use resources while maintaining performance as usage increases. I would also set up continuous 
	integration and automated unit testing to reduce the number of manual unit tests I would have to perform.

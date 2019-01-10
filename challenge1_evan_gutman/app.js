var express = require('express');
var bodyParser = require('body-parser');
var crypto = require('crypto');
var redis = require('redis');
var bluebird = require('bluebird');
var url = require('url');

var hostAddress = process.env.REDISCLOUD_URL ? url.parse(process.env.REDISCLOUD_URL) : {port: 6379, hostname: 'localhost'};
var client = redis.createClient(hostAddress.port, hostAddress.hostname, {no_ready_check: true});
if(hostAddress.auth) {
  client.auth(hostAddress.auth.split(":")[1]);
}

bluebird.promisifyAll(redis.RedisClient.prototype);

var app = express();
app.set('port', process.env.PORT || 3000);
app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json());


app.post('/messages', function(req, res) {
  var digest = crypto.createHash('sha256').update(req.body.message).digest('hex');

  client.setAsync(digest.toString(), req.body.message).then(result => {
    if(result != 'OK'){
      res.send({'err_msg': result});
    } else {
      res.send({'digest': digest});
    }
  }).catch(error => res.send({'err_msg': error}));

});

app.get('/messages/:digest', function(req, res) {
  var digest = req.params.digest;

  client.getAsync(digest).then(result => {
    if(result) {
      res.send({'message': result});
    } else {
      res.status(404).send({'err_msg': 'Message not found'});
    }
  }).catch(error => res.send({'err_msg': error}));

});


app.listen(app.get('port'), function() {
  console.log("Server listening on :", app.get('port'));
});

client.on('connect', function() {
  console.log('Redis client connected');
});

client.on('error', function(err) {
  console.log('Redis client error' + err);
});

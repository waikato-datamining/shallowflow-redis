# RedisConnection

## Name
shallowflow.redis.standalones.RedisConnection

## Synopsis
Manages the connection to the Redis server.

## Flow input/output
-standalone-

## Options
* debug (bool)

  * If enabled, outputs some debugging information
  * default: False

* skip (bool)

  * Whether to skip this actor during execution
  * default: False

* annotation (str)

  * For adding documentation to the actor
  * default: ''

* name (str)

  * The name to use for this actor, leave empty for class name
  * default: ''

* stop_flow_on_error (bool)

  * Whether to stop the flow in case of an error
  * default: True

* host (str)

  * The Redis host to connect to
  * default: 'localhost'

* port (int)

  * The port the Redis instance is listening on
  * default: 6379

* db (int)

  * The database to use.
  * default: 0


# RedisSource

## Name
shallowflow.redis.sources.RedisSource

## Synopsis
Applies the specified action to retrieve data.

## Flow input/output
output: -unknown-

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

* action (AbstractAction)

  * The Redis action to perform
  * default: shallowflow.redis.sources.action.Null


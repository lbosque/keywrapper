# keywrapper


Extremely simple key-value storage wrapper


## Motivation

I usually use [Redis](http://redis.io/) for small projects with a dynamic storage component.
Most of the times I just need a very simple key-value storage and Redis does a terrific job with that. However not all the applications need a high performance storage but just being very easy to start using them.

The idea of this wrapper is to start using JSON based storage at the beginning and in the future, if necessary, move the storate of an application to Redis or any other supported driver without changing a single line of code.

## Installation

```
sudo pip install keywrapper
```

## Basic usage

JSON store:

```
import keywrapper

store = keywrapper.new_store('json')

store.set_value('foo', 'bar', '42')

store.get_value('foo', 'bar')
```

Redis store:

```
import keywrapper

store = keywrapper.new_store('redis')

store.set_value('foo', 'bar', '42')

store.get_value('foo', 'bar')
```

Migrate from JSON store to Redis store:

```
import keywrapper

json_store = keywrapper.new_store('json')
redis_store = keywrapper.new_store('redis')

redis_store.restore(json_store.dump())
```

## Current status

These are the current implemented features:

  * JSON and Redis drivers
  * Hash style data type (key, attribute, value)
  * set_value and get_value functions
  * dump function implemented only in JSON driver
  * restore function implemented in both JSON and Redis drivers

## Tests

```
python tests/unit/test_keywrapper.py
```

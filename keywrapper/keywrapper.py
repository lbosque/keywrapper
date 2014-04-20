import redis
import json
import os

class KeyStore:
  
  def get_value(key, attribute):
    return NotImplemented

  def set_value(key, attribute, value):
    return NotImplemented

  def dump():
    return NotImplemented

  def restore(data):
    return NotImplemented


class RedisStore(KeyStore):

  def __init__(self, options={}):
    redis_host = options['host'] if 'host' in options else 'localhost'
    redis_port = options['port'] if 'port' in options else 6379
    redis_db = options['db'] if 'db' in options else 0
    self.connection = redis.Redis(host=redis_host, port=redis_port, db=redis_db)

  def get_value(self, key, attribute):
    return self.connection.hget(key, attribute)

  def set_value(self, key, attribute, value):
    self.connection.hset(key, attribute, value)

  def restore(self, data):
    for key in data:
      self.connection.hmset(key, data[key])


class JSONStore(KeyStore):

  def __init__(self, options={}):
    self.store_filename = options['store_filename'] if 'store_filename' in options else 'store.json'
    if not os.path.exists(self.store_filename):
      f = open(self.store_filename, 'w')
      f.write('{}')
      f.close()

  def __read_store(self):
    raw_data = open(self.store_filename, 'r')
    data = json.load(raw_data)
    raw_data.close()
    return data

  def __write_store(self, data):
    json_file = open(self.store_filename, 'w')
    json_file.write(json.dumps(data))
    json_file.close()

  def dump(self):
    return self.__read_store()

  def restore(self, data):
    self.__write_store(data)

  def get_value(self, key, attribute):
    try:
      value = self.__read_store()[key][attribute]
    except KeyError:
      value = None
    return value

  def set_value(self, key, attribute, value):
    print key
    print attribute
    print value
    json_data = self.__read_store()
    if not key in json_data:
      json_data[key] = {attribute: value}
    else:
      json_data[key][attribute] = value
    self.__write_store(json_data)


def new_store(driver, options={}):
  if driver == 'redis':
    return RedisStore(options)
  elif driver == 'json':
    return JSONStore(options)
  else:
    raise Exception("Driver %s not supported" % driver)

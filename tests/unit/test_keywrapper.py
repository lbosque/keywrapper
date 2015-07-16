import unittest
import random
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..', '..'))
import keywrapper

class JSONStoreTestCase(unittest.TestCase):

  def test_instance(self):
    store = keywrapper.new_store('json')
    self.assertIsInstance(store, keywrapper.JSONStore)

  def test_written_value(self):
    store = keywrapper.new_store('json')
    store.set_value('a', 'b', 'c')
    self.assertEqual(store.get_value('a', 'b'), 'c')

  def test_restore(self):
    json_file = "/tmp/json-%d" % random.randint(1, 10000000000)
    store = keywrapper.new_store('json', {'store_filename': json_file})
    data = {'a': {'b': 'c'}}
    store.restore(data)
    f = open(json_file, 'r')
    file_raw = f.read()
    f.close()
    self.assertEqual(file_raw, "{\"a\": {\"b\": \"c\"}}")


class RedistoreTestCase(unittest.TestCase):

  def test_instance(self):
    store = keywrapper.new_store('redis')
    self.assertIsInstance(store, keywrapper.RedisStore)
  
  def test_written_value(self):
    store = keywrapper.new_store('redis')
    store.set_value('a', 'b', 'c')
    self.assertEqual(store.get_value('a', 'b'), 'c')

  def test_restore(self):
    hkey = random.randint(1, 10000000000)
    hattr = random.randint(1, 10000000000)
    hval = random.randint(1, 10000000000)
    store = keywrapper.new_store('redis', {'db': 2})
    data = {"testing-%d" % hkey: {"testing-%d" % hattr: hval}}
    store.restore(data)
    new_store = keywrapper.new_store('redis', {'db': 2})
    self.assertEqual(new_store.get_value("testing-%d" % hkey, "testing-%d" % hattr), str(hval))

if __name__ == '__main__':
      unittest.main()

import unittest,settings
from models.base_models import NamedEntity
from models.tag import Tag
from models.venue import Venue
from google.appengine.ext.db import *


class NamedEntityTests(unittest.TestCase):
  def test_named_entity_validations(self):
    self.assertRaises(BadValueError,NamedEntity,None)
    entity = NamedEntity(name="name")
    self.assertEqual("name",entity.name)
  
  def test_inherits(self):
    self.assertRaises(BadValueError,Tag,None)
    self.assertRaises(BadValueError,Venue,None)
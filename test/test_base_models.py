from google.appengine.ext import db
from models import city, company, performance, show, tag, venue
from models.base import NamedEntity, UrlBasedEntity
import extendedtestcase


class NamedEntityTests(extendedtestcase.ExtendedTestCase):
  def test_named_entity_validations(self):
    self.assertRaises(db.BadValueError, NamedEntity, None)
    entity = NamedEntity(name="name1")
    self.assertEqual("name1", entity.name)
  
  def test_inherits(self):
    self.assertRaises(db.BadValueError, show.Show, None)
    self.assertRaises(db.BadValueError, venue.Venue, None)
    self.assertRaises(db.BadValueError, tag.Tag, None)
    self.assertRaises(db.BadValueError, performance.Performance, None)
    self.assertRaises(db.BadValueError, company.Company, None)
    self.assertRaises(db.BadValueError, city.City, None)
    

class UrlBasedEntityTests(extendedtestcase.ExtendedTestCase):
  def test_url_validations(self):
    UrlBasedEntity(name='Chennai', url='chennai-city')
    self.assertRaises(ValueError, UrlBasedEntity, name="name1", url="chennai city")
    self.assertRaises(ValueError, UrlBasedEntity, name="name1", url="chennai.city")
    self.assertRaises(db.BadValueError, UrlBasedEntity, name="name1", url="")
    self.assertRaises(ValueError, UrlBasedEntity, name="name1", url=" ")
    self.assertRaises(ValueError, UrlBasedEntity, name="name1", url="che'nnai#$%@city")
  

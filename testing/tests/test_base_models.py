import extendedtestcase,settings
from models.basemodels import NamedEntity
from google.appengine.ext import db 
from models import tag
from models import show
from models import venue
from models import performance
from models import company
from models import city


class NamedEntityTests(extendedtestcase.ExtendedTestCase):
  def test_named_entity_validations(self):
    self.assertRaises(db.BadValueError,NamedEntity,None)
    entity = NamedEntity(name="name1")
    self.assertEqual("name1",entity.name)
  
  def test_inherits(self):
    self.assertRaises(db.BadValueError,show.Show,None)
    self.assertRaises(db.BadValueError,venue.Venue,None)
    self.assertRaises(db.BadValueError,tag.Tag,None)
    self.assertRaises(db.BadValueError,performance.Performance,None)
    self.assertRaises(db.BadValueError,company.Company,None)
    self.assertRaises(db.BadValueError,city.City,None)
from google.appengine.ext import db
from company import Company
import base

class Show(base.NamedEntity):
  company = db.ReferenceProperty(Company,collection_name='shows')
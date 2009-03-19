from google.appengine.ext import db
from company import Company
import base_models

class Show(base_models.NamedEntity):
  company = db.ReferenceProperty(Company,collection_name='shows')
  
  

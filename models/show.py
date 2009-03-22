from google.appengine.ext import db
from company import Company
import basemodels

class Show(basemodels.NamedEntity):
  company = db.ReferenceProperty(Company,collection_name='shows')
  
  

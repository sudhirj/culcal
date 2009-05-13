from google.appengine.ext import db
from company import Company
import base, validators

class Show(base.NamedEntity):
    company = db.ReferenceProperty(Company,collection_name='shows', required = True)
    url = db.StringProperty(required = True, validator = validators.validate_url)
    
    def put(self):
        if (not self.is_saved()) and self.company.get_show_by_url(self.url):
            raise ValueError("This URL is being used for another show by "+self.company.name)
        super(base.NamedEntity, self).put()
        
  
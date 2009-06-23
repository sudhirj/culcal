from google.appengine.ext import db
from company import Company
import base, validators
from models.mixins import HasPerformances

class Show(base.NamedEntity, HasPerformances):
    company = db.ReferenceProperty(Company,collection_name='shows', required = True)
    url = db.StringProperty(required = True, validator = validators.validate_url)
    
    def put(self):
        if (not self.is_saved()) and self.company.get_show_by_url(self.url):
            raise ValueError("This URL is being used for another show by "+self.company.name)
        super(Show, self).put()
        
    def get_route(self):
        return '/'+self.company.url+'/shows/'+self.url
  
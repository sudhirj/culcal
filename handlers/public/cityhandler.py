import wsgiref.handlers, settings, datetime
from handlers import base
from models.city import City
from models.performance import Performance

class CityHandler(base.CrudHandler):
    def get(self, city_url):
        city = City.get_by_url(city_url)
        
        if not city: 
            self.redirect('/', False)
            return
        
        performances = city.cached_performances.filter('utc_date_time >', datetime.datetime.now()).fetch(10)
        self.render("public/city.html", dict(city=city, performances=performances))
  
 

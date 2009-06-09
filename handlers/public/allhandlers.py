import wsgiref.handlers, settings, datetime
from handlers import base
from models.city import City
from models.performance import Performance
from models.company import Company

class CityHandler(base.CrudHandler):
    def get(self, city_url):
        city = City.get_by_url(city_url)
        if not city: 
            self.redirect('/', False)
            return
        performances = city.get_new_performances().fetch(50)
        self.render('public/city.html', dict(city=city, performances=performances))
  
class CompanyHandler(base.CrudHandler):
    def get(self, path_url, company_url):
        company = Company.get_by_url(company_url)
        if not company:
            self.redirect('/', False)
            return 
        performances = company.get_new_performances().fetch(50)
        self.render('public/company.html', dict(company=company, performances=performances))

class VenueHandler(base.CrudHandler):
    def get(self, city_url, venue_url):
        city = City.get_by_url(city_url) 
        if city: venue = city.get_venue_by_url(venue_url)
        else:
            self.redirect('/', False)
            return
        if not venue:
            self.redirect('/' + city_url, False)
            return
        performances = venue.get_new_performances().fetch(50)
        self.render('public/venue.html', dict(venue=venue, performances=performances))
        
class ShowHandler(base.CrudHandler):
    def get(self, path_url, company_url, show_url):
        company = Company.get_by_url(company_url)
        if company: show = company.get_show_by_url(show_url)
        else:
            self.redirect('/', False)
            return
        if not show:
            self.redirect('/' + company_url, False)
            return
        performances = show.get_new_performances().fetch(50)
        self.render('public/show.html', dict(show=show, performances=performances))

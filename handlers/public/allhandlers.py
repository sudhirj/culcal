from handlers import base
from models.city import City
from models.company import Company
from models.performance import Performance
import datetime
import settings
import wsgiref.handlers

class CommonHandler(base.CrudHandler):
    def get(self, url):
        city = City.get_by_url(url)
        if city: 
            performances = city.get_new_performances().fetch(50)
            self.render('public/city.html', dict(city=city, performances=performances))
            return
        
        company = Company.get_by_url(url)
        if company:
            performances = company.get_new_performances().fetch(50)
            self.render('public/company.html', dict(company=company, performances=performances))
            return
        
        if not city and not company:
            self.redirect('/', False)
        

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
    def get(self, company_url, show_url):
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

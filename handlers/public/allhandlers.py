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
        if not city: company = Company.get_by_url(url)
        
        if not city and not company:
            self.redirect('/', False)
            return
        
        data_type = 'city' if city else 'company'
        data = city or company
        performances = data.get_performances().fetch(50)
        render_data = dict(performances=performances)
        render_data[data_type] = data 
        
        self.render('public/' + data_type + '.html', render_data)
        
class VenueHandler(base.CrudHandler):
    def get(self, city_url, venue_url):
        redirect_url = None
        city = City.get_by_url(city_url) 
        if city: venue = city.get_venue_by_url(venue_url)
        else: redirect_url = '/'
        if not venue: redirect_url = '/' + city_url
        if not redirect_url:
            performances = venue.get_performances().fetch(50)
            self.render('public/venue.html', dict(venue=venue, performances=performances))
        else:
            self.redirect(redirect_url,False)
        
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
        performances = show.get_performances().fetch(50)
        self.render('public/show.html', dict(show=show, performances=performances))
        
class HomepageHandler(base.CrudHandler):
    def get(self):
        self.render('public/home.html', dict(cities = City.all()))
        

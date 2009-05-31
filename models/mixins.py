import datetime
class HasPerformances:
    def get_new_performances(self):
        return self.get_performances_from_time(datetime.datetime.now())
    
    def get_performances_from_time(self, dt):
        performance_query = self.cached_performances if hasattr(self, 'cached_performances') else  self.performances
        return performance_query.filter('utc_date_time >', dt).order('utc_date_time') 

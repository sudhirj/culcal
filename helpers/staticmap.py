import settings

class StaticMapBuilder:
    def __init__(self, size = dict(x = 256, y = 256)):
        self.url = settings.MAP_ENDPOINT+'&key='+settings.MAP_KEY
        self.marker = None
        self.size = size
        self.zoom = settings.MAP_ZOOM
    
    def addMarker(self, lat, lon):
        self.marker = dict(lat = lat, lon = lon)
        return self
    
    def build(self):
        self.url+='&zoom='+str(self.zoom)
        self.url+='&size='+str(self.size['x'])+'x'+str(self.size['y'])
        if (self.marker): self.url += '&markers='+str(self.marker['lat'])+','+str(self.marker['lon'])
        return self.url
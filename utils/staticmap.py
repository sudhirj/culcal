key = 'ABQIAAAAdOCIY5iMV76jbHcybACMhxQi34lAQvM27VfTNvVaic9PtTFTExQT6O_D3Qz8PAwmNygHnmR1lYm7qQ'
endpoint = "http://maps.google.com/staticmap?sensor=false"

class StaticMapBuilder:
    url = endpoint+'&key='+key
    marker = None
    size = dict(x = 300, y = 300)
    
    def addMarker(self, lat, lon):
        self.marker = dict(lat = lat, lon = lon)
        
    def setSize(self, x, y):
        self.size['x'], self.size['y'] = x, y
    
    def build(self):
        self.url+='&size='+str(self.size['x'])+'x'+str(self.size['y'])
        if (self.marker): self.url += '&markers='+str(self.marker['lat'])+','+str(self.marker['lon'])
        return self.url
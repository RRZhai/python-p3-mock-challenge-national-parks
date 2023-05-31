class Visitor:
    all = []
    def __init__(self, name = ''):
        self.name = name
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 15 and not hasattr(self, '_name'):
            self._name = name
        else:
            raise Exception

    def trips(self, new_trip=None):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self, new_national_park=None):
        from classes.national_park import NationalPark
        parks = []
        for trip in self.trips():
            if trip.national_park not in parks:
                parks.append(trip.national_park)
        return parks

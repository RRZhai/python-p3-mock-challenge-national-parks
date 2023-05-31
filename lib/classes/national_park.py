class NationalPark:
    all = []
    def __init__(self, name=''):
        if type(name) == str:
            self._name = name
        else:
            raise Exception
        self._trips = []
        self._visitors = []
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        # if type(name) == str and not hasattr(self, '_name'):
        #     self._name = name
        # else:
        raise AttributeError

    def trips(self, new_trip=None):
        from classes.trip import Trip
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self, new_visitor=None):
        from classes.visitor import Visitor
        visitors = []
        for trip in self.trips():
            if trip.visitor not in visitors:
                visitors.append(trip.visitor)
        return visitors
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        result = ''
        best = 0
        for visitor in self.visitors():
            best_count = visitors.count(visitor)
            if best_count > best:
                best = best_count
                result = visitor
        return result
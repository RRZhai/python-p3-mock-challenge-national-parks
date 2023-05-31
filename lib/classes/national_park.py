class NationalPark:
    all = []
    def __init__(self, name=''):
        self.name = name
        self._trips = []
        self._visitors = []
        type(self).all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str:
            self._name = name
        else:
            raise Exception

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
        

        # best = ''
        # for visitor in self.visitors():
        #     best_count = self.trips().visitor.count(best)
        #     current_count = self.trips().visitor.count(visitor)
        #     if current_count > best_count:
        #         best = visitor
        # return best
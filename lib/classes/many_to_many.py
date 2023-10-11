class NationalPark:

    all = []

    def __init__(self, name):
        self.name = name
        NationalPark.all.append(self)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and len(name) >= 3 and not hasattr(self, "name"):
            self._name = name
        # else:
        #     raise Exception
        
    def trips(self):
        return [trip for trip in Trip.all if trip.national_park == self]
    
    def visitors(self):
        return list({trip.visitor for trip in self.trips()})
    
    def total_visits(self):
        return len(self.trips())
    
    def best_visitor(self):
        visitors = [trip.visitor for trip in self.trips()]
        return max(set(visitors), key=visitors.count)


class Trip:

    all = []
    
    def __init__(self, visitor, national_park, start_date, end_date):
        self.visitor = visitor
        self.national_park = national_park
        self.start_date = start_date
        self.end_date = end_date
        Trip.all.append(self)
        # self.visitor.trips.append(visitor.trips)
        # self.visitor.national_parks.append(visitor.national_parks)
        # self.national_park.visitors.append(national_park.visitors)
        # self.national_park.trips.append(national_park.trips)

    @property
    def start_date(self):
        return self._start_date
    
    @start_date.setter
    def start_date(self, start_date):
        if type(start_date) == str and len(start_date) >= 7:
            self._start_date = start_date
        
    @property
    def end_date(self):
        return self._end_date
    
    @end_date.setter
    def end_date(self, end_date):
        if type(end_date) == str and len(end_date) >= 7:
            self._end_date = end_date
        
    @property
    def visitor(self):
        return self._visitor
    
    @visitor.setter
    def visitor(self, visitor):
        # from Visitor import Visitor
        if isinstance(visitor, Visitor):
            self._visitor = visitor
        else:
            raise Exception("Visitor must be an instance of Visitor class.")
        
    @property
    def national_park(self):
        return self._national_park
    
    @national_park.setter
    def national_park(self, national_park):
        # from NationalPark import NationalPark
        if isinstance(national_park, NationalPark):
            self._national_park = national_park
        else:
            raise Exception("National Park must be an instance of NationalPark class.")
        



class Visitor:

    def __init__(self, name):
        self.name = name

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        if type(name) == str and 1 <= len(name) <= 15:
            self._name = name
        
    def trips(self):
        return [trip for trip in Trip.all if trip.visitor == self]
    
    def national_parks(self):
        return list({trip.national_park for trip in self.trips()})
    
    def total_visits_at_park(self, park):
        # from NationalPark import NationalPark
        # if isinstance(park, NationalPark):
        return len([trip for trip in self.trips() if trip.national_park == park])

        # else:
        #     return 0
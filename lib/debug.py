#!/usr/bin/env python3
import ipdb

from classes.national_park import NationalPark
from classes.visitor import Visitor
from classes.trip import Trip

if __name__ == '__main__':
    print("HELLO! :) let's debug :vibing_potato:")

    # create parks
    yose = NationalPark("Yosemite")
    rock = NationalPark("Rocky Mountain")

    # create visitors
    steve = Visitor('Steve')
    matteo = Visitor('Matteo')
    mark = Visitor('Mark')

    # create trips
    t_1 = Trip(matteo, yose, "May 5th", "May 9th")
    t_2 = Trip(mark, rock, "May 20th","May 27th")
    t_3 = Trip(steve, rock, "January 5th","January 20th")
    t_4 = Trip(matteo, yose, "January 15th","January 20th")
    t_5 = Trip(steve, yose, "February 15th","March 20th")
    t_6 = Trip(mark, yose, "July 15th","September 20th")
    ipdb.set_trace()


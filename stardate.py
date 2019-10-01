from pelican import signals
from pelican.contents import Article
from pelican.utils import get_date

import math
from dateutil.parser import parse
from datetime import datetime
import sys

class StarDate():
    verbose = False
    date = None
    stardate = None
    
    def __init__(self, date = None, verbose = False):
        if(self.verbose):
            print("---Initializing---")

        self.date = date
        self.verbose = verbose

    def setDate(self, date):
        self.date = date

    def getStardate(self):
        if(self.date != None):
            stardateRequested = parse(self.date)
        else:
            stardateRequested = datetime.now()

        stardateOrigin = parse("1987-07-15T00:00:00-00:00")
        
        if(self.verbose):
        	print("Start Date : " + stardateRequested.strftime('%Y-%m-%d %H:%M:%S'))
        	print("Origin Date : " + stardateOrigin.strftime('%Y-%m-%d %H:%M:%S'))
        	print("---------------------")
        	
        if(self.verbose):
        	year = stardateRequested.strftime('%Y')
        	month = stardateRequested.strftime('%m')
        	day = stardateRequested.strftime('%d')
        	hour = stardateRequested.strftime('%H')
        	minutes = stardateRequested.strftime('%M')
        	seconds = stardateRequested.strftime('%S')
        	print("Year : " + year)
        	print("Month : " + month)
        	print("Day : " + day)
        	print("Hour : " + hour)
        	print("Minutes : " + minutes)
        	print("Seconds : " + seconds)
        	print("---------------------")
        	
        self.stardate = stardateRequested.timestamp() - stardateOrigin.timestamp()
        self.stardate = self.stardate / (60.0 * 60.0 * 24.0 * 0.036525)
        self.stardate = math.floor(self.stardate + 410000.0)
        self.stardate = self.stardate / 10.0
        
        if(self.verbose):
        	print("Selection Date - Origin Date = " + str(self.stardate))
        	print("---------------------")
        	
        	print("Previous Value / (60.0 * 60.0 * 24.0 * 0.036525) = " + str(self.stardate))
        	print("---------------------")
        	
        	print("Floor(Previous Value + 410000.0) = " + str(self.stardate))
        	print("---------------------")
        	
        	print("Previous Value / 10.0 = " + str(self.stardate))
        	print("---------------------")

        if(self.verbose):
            print()
            print("Stardate Final : " + str(self.stardate))
        
        return self.stardate

def get_stardate(generator):    
    for article in generator.articles:
        article.stardate = StarDate(str(article.date.strftime('%Y-%m-%d %H:%M:%S')), False).getStardate()

def register():
    signals.article_generator_finalized.connect(get_stardate)

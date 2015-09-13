import csv

"""
This is an helper class that read a CSV file in a pre-defined format.
The main pourpuse of this class is provide an easy way to access information.

Example of expected content:

SEZ2011,SEZ_period

152060000002,<=1945

152060000003,1961-1980

"""

class ISTATCSV:

    def __init__(self):
        self.filename = None
        self.valid = False
        self.table = None

    def load(self, filename):
        try:
            with open(filename, 'rb') as csvfile:
                result = csv.reader(csvfile, delimiter=',', quotechar='\\')
                self.table = { row[0]: row[1] for row in result }
                self.valid = True
        except:
            self.valid = False

    def get(self, istat):
        if not self.valid: 
            return 'NOT_VALID'
        try:
            #return 'TRY_FIND' + str(istat)
            return self.table[istat]
        except:
            return 'NOT_FOUND'

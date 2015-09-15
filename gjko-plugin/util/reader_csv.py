import csv
import sys

"""
This is an helper class that read a CSV file in a pre-defined format.
The main pourpuse of this class is provide an easy way to access information.

Example of expected content:

SEZ2011,SEZ_period

152060000002,<=1945

152060000003,1961-1980

"""

class ISTAT:

    def __init__(self):
        self.filename = None
        self.valid = False
        self.table = {}

    def load(self, filename):
        try:
            with open(filename, 'rU') as csvfile:
                result = csv.reader(csvfile, csv.excel) #delimiter=',', quotechar='\\')
                for row in result:
                    print("Adding row: " + str(row))
                    if len(row) >= 2:
                        self.table[str(row[0])] = str(row[1])
                self.valid = True
        except csv.Error as e:
            print('file %s, %s' % (filename, e))
        except:
            print('Exception: ' + str(sys.exc_info()[0]))
            self.valid = False

    def get(self, istat):
        if not self.valid: 
            return None
        try:
            #return 'TRY_FIND' + str(istat)
            return self.table[istat]
        except:
            return None


class EPCs:

    def __init__(self):
        self.filename = None
        self.valid = False
        self.table = None

    def load(self, filename):
        try:
            with open(filename, 'rb') as csvfile:
                result = csv.reader(csvfile, delimiter=',', quotechar='\\')
                self.table = { row[0]: row[1:] for row in result }
                self.valid = True
        except:
            self.valid = False

    def get(self, cadastre):
        if not self.valid: 
            return None
        try:
            #return 'TRY_FIND' + str(istat)
            return self.table[istat]
        except:
            return None

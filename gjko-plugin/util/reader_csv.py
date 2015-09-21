import csv
import sys

class BaseReader:
    """
    Base reader for CSV.
    """

    filename = None
    valid = False
    header = []
    table = {}

    def load(self, filename):
        try:
            first = True
            with open(filename, 'rU') as csvfile:
                result = csv.reader(csvfile, csv.excel) #delimiter=',', quotechar='\\')
                for row in result:
                    if first:
                        self.handle_header(row)
                    else:
                        self.handle_row(row)
                    first = False
                self.filename = filename
                self.valid = True
        except AttributeError as e:
            print('file %s, %s' % (filename, e))
        except csv.Error as e:
            print('file %s, %s' % (filename, e))
        except:
            print('Exception: ' + str(sys.exc_info()[0]))
            self.valid = False

    def get(self, code):
        if not self.valid: 
            return None
        try:
            return self.table[code]
        except:
            return None

    def get_element(self, code, header):
        idx = self.header.index(header)
        return self.table[code][idx]

    def handle_header(self, row):
        return False

    def handle_row(self, row):
        return False


class ISTAT(BaseReader):
    def __init__(self, filename):
        #super(ISTAT, self).__init__()
        self.load(filename)

    def handle_header(self, row):
        self.header.extend(row[:2])
        return True

    def handle_row(self, row):
        if len(row) >= 2:
            self.table[str(row[0])] = str(row[1])
            return True
        else:
            return False

def codcat_to_epcs(type_usage, cadastre):
    tokens = cadastre.split('|')
    if len(tokens) >= 3:
        ret = type_usage + '-' + '-'.join(tokens[2:])
        return ret
    else:
        return ''

class EPCs(BaseReader):
    def __init__(self, filename):
        #super(EPCs, self).__init__()
        self.load(filename)

    def handle_header(self, row):
        self.header.extend(row)
        return True

    def handle_row(self, row):
        if len(row) >= 2:
            self.table[str(row[0])] = row[1:]
            return True
        else:
            return False

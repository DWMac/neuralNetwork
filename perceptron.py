import csv

class Perceptron(object):
    """docstring for Perceptron."""
    def __init__(self, ):
        super(Perceptron, self).__init__()
        self.arg = arg
    def learn(self, arg):
        return weights
    def execute(self, weights):
        return desired


def convertCSVtoDict(csvPath):
    dictionary = {}
    print "Converting CSV to Dictionary"
    with open(csvPath) as csvFile:
        reader = csv.reader(csvFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            arr.append(row)
    print dictionary
    return dictionary
def convertCSVtoArr(csvPath):
    arr = []
    print "Converting CSV to Array"
    with open(csvPath) as csvFile:
        reader = csv.reader(csvFile, quoting=csv.QUOTE_NONNUMERIC)
        for row in reader:
            arr.append(row)
    print "Converted CSV"
    print arr
    return arr
if __name__ == '__main__':
    path = 'testCSV.csv'
    #convertCSVtoArr(path)
    perc = new Perceptron(path)

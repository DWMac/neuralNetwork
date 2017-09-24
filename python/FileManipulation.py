class FileManipulation(object):
    """docstring for FileManipulation."""
    def __init__(self, filePath):
        super(FileManipulation, self).__init__()
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

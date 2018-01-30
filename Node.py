class Node:

    def __init__(self, data, nextNode=None):
        self.data = data
        self.nextNode = nextNode

    def getData(self):
        return self.data

    def setData(self, val):
        self.data = val

    def getNext(self):
        return self.nextNode

    def setNext(self, val):
        self.nextNode = val

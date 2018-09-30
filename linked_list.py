#!/usr/bin/env python3

class Node:
    def __init__(self, val=None):
        self.val = val
        self.nextval = None


class LinkedList:
    def __init__(self):
        self.headval = None

    def addEnd(self, endData):
        newNode = Node(endData)
        if self.headval is None:
            self.headval = newNode
            return
        last = self.headval
        while(last.nextval):
            last = last.nextval
        last.nextval = newNode

    def removeNode(self, key):
        headVal = self.headval
        if headVal != None:
            if headVal.val == key:
                self.head = headVal.nextval
                headVal = None
                return
        while headVal != None:
            if headVal.val == key:
                break
            prev = headVal
            headVal = headVal.nextval
        if headVal == None:
            return
        prev.nextval = headVal.nextval
        headVal = None

    def printlist(self):
        printval = self.headval
        while printval != None:
            print(printval.val)
            printval = printval.nextval


def nodeGen(list):
        """pass in a list to generate nodes from the list items
        any list can be passed in.  I used the days of the week
        Usage: nodeGen(list)
        
        Args:
        list = [] any list"""
    
        try:
            for i in range(2, len(list)+1):
                print("d"+str(i) +" = Node('"+list[i-1]+"')")
        except(TypeError, ValueError):
            print("""pass in a list to generate nodes from the list items
        any list can be passed in.  I used the days of the week
        Usage: nodeGen(list)
        
        Args:
        list = [] any list""")


def nextGen(list):
    """used to generate the code for adding Node.nextval in the range of the list
    Usage: nextGen(list)

    Args:
    list = [] any list"""
    
    dlist = []
    try:
        for i in range(2,len(list)+1):
            dlist.append("d"+str(i))

        for d in range(len(dlist)-1):
            print(dlist[d]+".nextval = " + dlist[d+1]) 
    except(TypeError, ValueError):
        print("""used to generate the code for adding Node.nextval in the range of the list
    Usage: nextGen(list)

    Args:
    list = [] any list""")
    

list = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

dayList = LinkedList()
dayList.headval = Node("Monday")
#define the rest of the days as nodes with Node.nodeGen(list)

d2 = Node('Tuesday')
d3 = Node('Wednesday')
d4 = Node('Thursday')
d5 = Node('Friday')
d6 = Node('Saturday')
d7 = Node('Sunday')

# define the nextvals with Node.nextGen(list)
dayList.headval.nextval = d2
d2.nextval = d3
d3.nextval = d4
d4.nextval = d5
d5.nextval = d6
d6.nextval = d7

# nodeGen(list)
# nextGen(list)
dayList.printlist()
print("*"*40)
dayList.addEnd("frargsday")
dayList.printlist()
print("*"*40)
dayList.removeNode("frargsday")
dayList.printlist()

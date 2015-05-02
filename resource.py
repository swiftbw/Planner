import ast
from location import Location

class Resource(dict):
      uid = "UID"
      firstName = "First Name"
      lastName = "Last Name"
      location = "Location"
      status = "Status"
      dictKeys = uid, firstName, lastName, location, status
      elementKeys = firstName, lastName, location

      def __init__(self, instr):
            if instr == None:
                  return

            if type(instr) is dict:
                  idict = instr
            else:
                  idict = ast.literal_eval(instr)
                  
            if Resource.uid not in idict.keys():
                  idict[Resource.uid] = '0'

            if Resource.status not in idict.keys():
                  idict[Resource.status] = '1'

            for i in Resource.dictKeys:
                  self[i] = idict[i]

            self[Resource.location] = Location(idict[Resource.location])

      def updateFromDict(self, cdict):
            self[Resource.firstName] = cdict[Resource.firstName]
            self[Resource.lastName] = cdict[Resource.lastName]
            self[Resource.location] = cdict[Resource.location]

      def printOutStr(self):
            print str(self)

      def isValid(self):
            if self[Resource.uid] == 0 or self[Resource.firstName] == "" or self[Resource.lastName] == "" or self[Resource.location] == "UNK":
                  return False
            else:
                  return True
             
      def write(self, filehandle):
            outstr = str(self)
            print outstr
            filehandle.write(outstr+"\n")
            return

      def match(self, res):
            for i in Resource.dictKeys:
                  if self[i] != res[i]:
                        return False
            return true

      def getFullName(self):
            return self[Resource.lastName] + ", " + self[Resource.firstName]
        
        
def main():

      print "Testing Resource.py methods:  __init__, updateFromDict, PrintOutStr, isValid, write, match, and getFullName."
      print "Testing Init"
      
      per = Resource("{'UID': '0', 'First Name': 'Brian', 'Last Name': 'Swift', 'Location': 'CHI'}")
      x = str(per)
      print x
      print "Testing ability to construct a dict from a string?"
      
      y = ast.literal_eval(x)
      print y

      print "Testing ability to 'update from dict'"

      x={'First Name': 'Tony', 'Last Name' : 'Romo', 'Location' : 'CHI'}
      per.updateFromDict(x)
      print per
      
      print 'Testing ability to printOutStr'
      print per.printOutStr()

      print 'Testing isValid'
      print per.isValid()

      print 'Testing write -- not yet...'

      print 'Testing Match'
      print 'does x = y?'
      print 'per = '
      per.printOutStr()

      per2 = Resource(y)

      print 'per2 = '
      per2.printOutStr()

      print 'does per match per2? '
      print per.match(per2)

      print 'testing getFullName'
      print per.getFullName()
      
if __name__ == '__main__':
      main()
      

import ast
from location import Location

class Resource(dict):
      uid = "UID"
      firstName = "First Name"
      lastName = "Last Name"
      location = "Location"
      dictKeys = uid, firstName, lastName, location
      elementKeys = firstName, lastName, location
      def __init__(self, instr):
            if instr == None:
                  return

            idict = ast.literal_eval(instr)
            for i in Resource.dictKeys:
                self[i] = idict[i]

            self[Resource.location] = Location(idict[Resource.location])

      def getOutStr(self):
            return "%s,%s,%s,%s" % (self[Resource.uid], self[Resource.firstName], self[Resource.lastName], self[Resource.location])

      def updateFromDict(self, cdict):
            self[Resource.firstName] = cdict[Resource.firstName]
            self[Resource.lastName] = cdict[Resource.lastName]
            self[Resource.location] = cdict[Resource.location]
            
      def printOutStr(self):
            print self.getOutStr()

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

      def getFullName(self):
            return self[Resource.lastName] + ", " + self[Resource.firstName]
        
      @staticmethod
      def BuildInstrFromDict(idict):
            retstr = "0," + idict[Resource.firstName] + "," + idict[Resource.lastName] + "," + idict[Resource.location]
            return retstr
        
def main():
      per = Resource("{'UID': '0', 'First Name': 'Brian', 'Last Name': 'Swift', 'Location': 'CHI'}")
      x = str(per)
      print x
      y = ast.literal_eval(x)
      print y
      
if __name__ == '__main__':
      main()
      

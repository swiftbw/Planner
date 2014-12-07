from location import Location

class Resource:
      elementKeys = "First Name", "Last Name", "Location"
      def __init__(self, instr):
            if instr == None:
                  return

            resourceStrs = instr.split(",")
            
            self._uid = int(resourceStrs[0].strip())
            self._firstName = resourceStrs[1].strip()
            self._lastName = resourceStrs[2].strip()
            self._location = Location(resourceStrs[3].strip())

      def getOutStr(self):
            return "%d,%s,%s,%s" % (self._uid, self._firstName, self._lastName, self._location.get())

      def updateFromDict(self, cdict):
            self._firstName = cdict["First Name"]
            self._lastName = cdict["Last Name"]
            self._location = cdict["Location"]
            
      def getObjectAsDict(self):
            res = {}
            res["First Name"] = self._firstName
            res["Last Name"] = self._lastName
            res["Locaiton"] = self._location
            return res
      
      def printOutStr(self):
            print self.getOutStr()

      def isValid(self):
            if self._uid == 0 or self._firstName == "" or self._lastName == "" or self._location.get() == "UNK":
                  return False
            else:
                  return True
             
      def write(self, filehandle):
            outstr = self.getOutStr()
            print outstr
            filehandle.write(outstr+"\n")
            return

      def getFullName(self):
            return self._lastName + ", " + self._firstName
        
      @staticmethod
      def BuildInstrFromDict(idict):
            retstr = "0," + idict["First Name"] + "," + idict["Last Name"] + "," + idict["Location"]
            return retstr
        
def main():
      per = Resource("0, Brian, Swift, CHI")
      per.printOutStr()
            
if __name__ == '__main__':
      main()
      

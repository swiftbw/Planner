from location import Location

class Person:

      def __init__(self, instr):
            if instr == None:
                  return

            personStrs = instr.split(",")
            
            self._uid = int(personStrs[0].strip())
            self._firstName = personStrs[1].strip()
            self._lastName = personStrs[2].strip()
            self._location = Location(personStrs[3].strip())

      def getOutStr(self):
            return "%d,%s,%s,%s" % (self._uid, self._firstName, self._lastName, self._location.get())

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

def main():
      per = Person("0, Brian, Swift, CHI")
      per.printOutStr()
            
if __name__ == '__main__':
      main()
      

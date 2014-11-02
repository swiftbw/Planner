from location import Location

class Person:

      _uid = 0
      _firstName = ""
      _lastName = ""
      _location = Location()

      def __init__(self, instr):
            if instr == None:
                  return
            personStrs = instr.split(",")
            
            self._uid = personStrs[0]
            self._firstName = personStrs[1]
            self._lastName = personStrs[2]
            self._location = Location(personStrs[3])

      def getOutStr(self):
            print "UID = %d", self._uid
            print "First Name = %s" % self._firstName
            print "Last Name = %s" % self._lastName
            print "Location = %s" % self._location.get()
            return "%d,%s,%s,%s" % (self._uid, self._firstName, self._lastName, self._location.get())
      def printOutStr(self):
            print getOutStr()

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


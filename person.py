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
            print "First Name = %s", self._firstName
            print "Last Name = %s", self._lastName
            print "Location = %s", self._location.get()
            return str.format("%d,%s,%s,%s", self._uid, self._firstName, self._lastName, self._location.get())

      def isValid(self):
            if self._uid == 0 or self._firstName == "" or self._lastName == "" or self._location.get() == "UNK":
                  return False
            else:
                  return True
             
      def write(self, filehandle):
            outstr = self.getOutStr()
            filehandle.write(outstr+"\n")
            return

      def getFullName(self):
            return self._lastName + ", " + self._firstName

class Resources:
      def __init__(self, filestr = ""):
            self._filename = filestr
            self._resources = []
            try:
                  filehandle = open(self._filename, "r")
                  resources = filehandle.readlines()
                  filehandle.close()

                  for i in resources:
                        person = Person(i)
                        self._resources.add(person)
            except IOError as e:
                  print "I/O error({0}): {1}".format(e.errno, e.strerror)
                  print "Unable to open %s for reading.", filestr
                  

      def write(self):
            try:
                  filehandle = open(self._filename, "w")
                  for i in self._resources:
                        i.write(filehandle)
                  filehandle.close()
            except IOError as e:
                  print "I/O error({0}): {1}".format(e.errno, e.strerror)
                  print "Unable to open %s for writing.", filestr
                  
      def add(self, resource):
            if self.checkNameExists(resource) == True:
                  print "Person already exists!"
                  return
            else:
                  resource._uid = len(self._resources)+1
                  self._resources.append(resource)
            
      def checkNameExists(self, resource):
            for i in self._resources:
                  if i.getFullName() == resource.getFullName():
                        return True

            return False

      def getResources(self):
            ress = []
            for i in self._resources:
                  ress.append(i.getName(), i)

            return ress

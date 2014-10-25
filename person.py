from location import Location

class Person:

      _uid = 0
      _firstName = ""
      _lastName = ""
      _location = Location()

      def __init__(self, instr):
            if instr == None:
                  return
            personStrs = split(instr,",")
            
            _uid = personStrs[0]
            _firstName = personStrs[1]
            _lastName = personStrs[2]
            _role = Location(personStrs[3])

      def getOutStr(self):
            return str.format("%d,%s,%s,%s", _uid, _firstName, _lastName, _role.get())

      def isValid(self):
            if _uid == 0 or _firstName == "" or _lastName == "" or _role.get() == "UNK":
                  return False
            else:
                  return True
             
      def write(self, filehandle):
            outstr = getOutStr()
            filehandle.write(outstr+"\n")
            return

      def getName():
            return _lastName + ", " + _firstName

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
            self.checkNameExists(resource)
            for i in self._resources:
                  if resource._firstName == i._firstName and resource._lastName == i._lastName:
                        return
            resource._uid = len(self._resources+1)
            
            self._resources.append(resource)
          
      def getResources(self):
            ress = []
            for i in self._resources:
                  ress.append(i.getName(), i)

            return ress

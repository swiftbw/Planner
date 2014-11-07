from person import Person

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
                        self.add(person)
                        
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

      def getResourcesAsDict(self):
            ress = {}
            for i in self._resources:
                  ress[i.getOutStr()] = i #Used to be getfullname but think we want a unique key in the listbox
            return ress

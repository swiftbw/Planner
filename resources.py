from resource import Resource

class Resources:
      def __init__(self, filestr = ""):
            self._filename = filestr
            self._resources = []
            try:
                  filehandle = open(self._filename, "r")
                  resources = filehandle.readlines()
                  filehandle.close()

                  for i in resources:
                        resource = Resource(i)
                        self.add(resource)
                        
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
                  print "Resource already exists!"
                  return
            else:
                  resource._uid = len(self._resources)+1
                  self._resources.append(resource)
            
      def checkNameExists(self, resource):
            for i in self._resources:
                  if i.getFullName() == resource.getFullName():
                        return True

            return False

      def getKeys(self):
            schlussels = []
            for i in self._resources:
                  schlussels.append(i.getOutStr())
            return schlussels

      def getResourcesAsDict(self):
            ress = {}
            for i in self._resources:
                  ress[i.getOutStr()] = i #Used to be getfullname but think we want a unique key in the listbox
            return ress

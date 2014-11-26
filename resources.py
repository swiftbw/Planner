from resource import Resource

class Resources:
      def __init__(self, filestr = ""):
            self._filename = filestr
            self._resources = {}
            try:
                  filehandle = open(self._filename, "r")
                  resources = filehandle.readlines()
                  filehandle.close()

                  for i in resources:
                        resource = Resource(i)
                        self._resources[resource.getOutStr()] = resource
                        
            except IOError as e:
                  print "I/O error({0}): {1}".format(e.errno, e.strerror)
                  print "Unable to open %s for reading.", filestr

      def write(self):
            try:
                  filehandle = open(self._filename, "w")
                  print "TEST: "
                  print self.getKeysInOrder()
                  print "ENDTEST:"
                  for i in self.getKeysInOrder():
                        self._resources[i].write(filehandle)
                  filehandle.close()
            except IOError as e:
                  print "I/O error({0}): {1}".format(e.errno, e.strerror)
                  print "Unable to open %s for writing.", filestr
                  
      def add(self, resource):
            if self.checkNameExists(resource) == True:
                  print "Resource already exists!"
                  return
            else:
                  resource._uid = len(self.getKeysInOrder())+1
                  self._resources[resource.getOutStr()] = resource
            
      def addFromDict(self, resdict):
            resstr = Resource.BuildInstrFromDict(resdict)
            self.add(Resource(resstr))

      def checkNameExists(self, resource):
            for i in self.getKeysInOrder():
                  if self._resources[i].getFullName() == resource.getFullName():
                        return True

            return False

      def getKeysInOrder(self):
            schlussels = []
            keys = self._resources.keys()
            print "GK: Keys - "
            print keys
            print "end GK"
            l = len(keys)-1
            print "l = " + str(l)
            if l < 1:
                  schlussels = keys
            else:
                  i = 0
                  schlussels = keys
                  while i < l:
                        print "while: " + str(i)
                        el1 = schlussels[i]
                        el2 = schlussels[i+1]
                        idx1 = int(el1.split(",")[0])
                        idx2 = int(el2.split(",")[0])
                        if idx2 < idx1:
                              schlussels[i] = el2
                              schlussels[i+1] = el1
                              i = 0
                        else:
                              i+=1

            return schlussels
      def getElementKeys(self):
            return Resource.elementKeys

      def getAsDict(self):
            ress = {}
            for i in self._resources:
                  ress[i.getOutStr()] = i
            return ress

      def deleteElement(self, key):
            d = dict(self._resources)
            del d[key]
            self._resources = d

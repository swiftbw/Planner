'''
Might be good to make this inherit from dict at some point...
'''
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
                        self._resources.append(resource)
                        
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
            if self.checkNameExists(resource.uid) == True:
                  print "Resource already exists!"
                  return None
            else:
                  resource[Resource.uid] = str(len(self._resources)+1)
                  self._resources.append(resource)
                  return resource
            
      def addFromDict(self, resdict):
            print resdict
            res = Resource(resdict)
            retstr = self.add(res)
            return retstr

      def checkNameExists(self, resource):
            for i in self._resources:
                  if i[Resource.uid] == resource[Resource.uid]:
                        return True

            return False

      def getElementKeys(self):
            return Resource.elementKeys
      
      def getDictKeys(self):
            return Resource.dictKeys

      def getElementAsDict(self, key):
            return self._resources[key]

      def modifyElement(self, cdict, key):
            self._resources[key].updateFromDict(cdict)

      def deleteElement(self, key):
            d = dict(self._resources)
            del d[key]
            self._resources = d

def main():
      sl = Resources("/users/swiftb/dev/Planner/data/testresources.txt")
      for i in sl._resources:
            print str(i)
if __name__ == "__main__":
      main()

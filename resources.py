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
            if self.checkNameExists(resource) == True:
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

      def getElementAsDict(self, idx):
            return self._resources[idx]

      def modifyElement(self, cdict, idx):
            self._resources[idx].updateFromDict(cdict)

      def deleteElement(self, idx):
            d = list(self._resources)
            del d[idx]
            self._resources = d

def main():
      sl = Resources("/users/swiftb/dev/Planner/data/testresources.txt")
      for i in sl._resources:
            print str(i)

      per = Resource("{'UID': '0', 'First Name': 'Brian', 'Last Name': 'Swift', 'Location': 'CHI'}")
      per2 = Resource("{'UID': '0', 'First Name': 'Archy', 'Last Name': 'Swift', 'Location': 'CHI'}")

      print "Checking 'checkNameExists'"
      print 'does name exist? '
      print sl.checkNameExists(per)

      print 'Testing modifyElement'
      print sl._resources
      print per2
      print sl.modifyElement(per2, 1)
      
      print "Testing deleteElement"
      print sl._resources
      print "Deleting first element"
      sl.deleteElement(0)
      print sl._resources
      
if __name__ == "__main__":
      main()

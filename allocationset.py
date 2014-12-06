from allocation import Allocation
              
class AllocationSet():
      def __init__(self, filestr = ""):
            self._filename = filestr
            self._allocations = {}
            try:
                  filehandle = open(self._filename, "r")
                  allocations = filehandle.readlines()
                  filehandle.close()

                  for i in allocations:
                        allocation = Allocation(i)
                        self._allocations[allocation._uid][allocation._pid][allocation._date] = resource
                        
            except IOError as e:
                  print "I/O error({0}): {1}".format(e.errno, e.strerror)
                  print "Unable to open %s for reading.", filestr

      def write(self):
            try:
                  filehandle = open(self._filename, "w")
                  for i in self._allocations.keys():
                        for j in allocations[i].keys():
                              for k in allocations[i][j].keys():
                                    self._allocations[i][j][k].write(filehandle)
                  filehandle.close()
            except IOError as e:
                  print "I/O error({0}): {1}".format(e.errno, e.strerror)
                  print "Unable to open %s for writing.", filestr
                  


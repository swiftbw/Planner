from fundingsource import FundingSource

class FundingSources():
      def __init__(self, filestr=""):
            self._filename = filestr
            self._fundingSources = []
            try:
                  filehandle = open(self._filename, "r")
                  fundingsources = filehandle.readlines()
                  filehandle.close()

                  for i in fundingsources:
                        fundingSource = FundingSource(i)
                        self.add(fundingSource)
                        
            except IOError as e:
                  print "I/O error({0}): {1}".format(e.errno, e.strerror)
                  print "Unable to open %s for reading.", filestr
            
      def write(self):
            try:
                  filehandle = open(self._filename, "w")
                  for i in self._fundingSources:
                        i.write(filehandle)
                  filehandle.close()
            except IOError as e:
                  print "I/O error({0}): {1}".format(e.errno, e.strerror)
                  print "Unable to open %s for writing.", filestr
                  
      def add(self, fundingsource):
            if self.checkNameExists(fundingsource) == True:
                  print "FundingSource already exists!"
                  return
            else:
                  fundingsource._fid = len(self._fundingSources)+1
                  self._fundingSources.append(fundingsource)
            
      def checkNameExists(self, fundingsource):
            for i in self._fundingSources:
                  if i.getFundingSource() == fundingSource.getFundingSource():
                        return True

            return False

      def getFundingSourcesAsDict(self):
            fss = {}
            for i in self._fundingSources:
                  fss[i.getOutStr()] = i #Used to be getfullname but think we want a unique key in the listbox
            return fss

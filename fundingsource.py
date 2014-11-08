
class FundingSource():
      def __init__(self, instr):
            fundingElems = instr.split(",")

            self._fid = int(fundingElems[0])
            self._name = fundingElems[1].strip()
            self._type = fundingElems[2].strip()
            self._desc = fundingElems[3].strip(" \t,")

      def printOutStr(self):
            print self.getOutStr()

      def isValid(self):
            if self._uid == 0 or self._name == "" or (self._type != "AIT" and self._type != "INIT"):
                  return False
            else:
                  return True
             
      def write(self, filehandle):
            outstr = self.getOutStr()
            filehandle.write(outstr+"\n")
            return

      def getOutStr(self):
            return "%d,%s,%s,%s" % (self._fid, self._name, self._type, self._desc)

      def getFundingSource(self):
            return "%s,%s,%s" % (self._name, self._type, self._desc)

def main():
      src = FundingSource("0, CTC, INIT, A great project")
      src.printOutStr()
            
if __name__ == '__main__':
      main()
      
      def getOutStr(self):
            return "%d,%s,%s,%s" % (self._fid, self._name, self._type, self._desc)

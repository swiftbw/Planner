class Allocation:
      def __init__(self, instr):
            if instr == None:
                  return

            resourceStrs = instr.split(",")
            
            self._uid = int(resourceStrs[0].strip())
            self._pid = int(resourceStrs[1].strip())
            self._allocation = float(resourceStrs[2].strip())
            self._date = resourceStrs[3].strip()

      def write(self, filehandle):
            outstr = "%d,%d,%f,%s" % (self._uid, self._pid, self._allocation, self._date)
            print outstr
            filehandle.write(outstr+"\n")
            return

class Location:
      _validLocations = ["UNK", "CHI", "NY", "LDN", "CHE", "HKG", "TKY"]

      def __init__(self, locstr = "UNK"):
            self._location = "UNK"
            if self.isValid(locstr) == True:
                  self._location = locstr

      def isValid(self, instr):
            print instr
            for i in Location._validLocations:
                  if i == instr:
                        return True
            else:
                  return False
                
      def set(self, instr):
            if self.isValid(instr) == True:
                  self._location = instr

      def get(self):
            return self._location

    
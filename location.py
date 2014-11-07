class Location:
      _validLocations = ["UNK", "CHI", "NYC", "LDN", "CHE", "HKG", "TKY"]

      def __init__(self, locstr = "UNK"):
            self._location = "UNK"
            if self.isValid(locstr) == True:
                  self._location = locstr

      def isValid(self, instr):
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

def main():
      loc = Location("NYC")
      print loc.get()

      loc2 = Location("QWE")

      print loc2.get()
      loc2.set("NYC")
      print loc2.get()

            
if __name__ == '__main__':
      main()
      

    

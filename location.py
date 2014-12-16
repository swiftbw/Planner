class Location(str):
      _validLocations = ["UNK", "CHI", "NYC", "LDN", "CHE", "HKG", "TKY"]

      def __init__(self, locstr = "UNK"):
            
            if self.isValid(locstr) == True:
                  super(Location, self).__init__(locstr)
            else:
                  super(Location, self).__init__("UNK")

      def isValid(self, instr):
            for i in Location._validLocations:
                  if i == instr:
                        return True
            else:
                  return False

'''                              
      def set(self, instr):
            if self.isValid(instr) == True:
                  print "setting instr " + instr
                  self = Location(instr)
            else:
                  self = Location("")

      def get(self):
            return self
'''
              
def main():
      loc = Location("NYC")
      print loc

      loc2 = Location("QWE")

      print loc2
      loc2 = Location("NYC")
      print loc2

            
if __name__ == '__main__':
      main()
      

    

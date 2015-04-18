'''
The Planner class is the main class for the Planner application.  planner.py extends Frame.  Upon initialization a reference to the parent window is stored in the object, and _resources, _fundingSources, and _allocations objects are created.

initUI is then called.  When initUI is called the file menu and view menus are set up.

From the file menu, exit and save options are available.

From the view menu, the resources and funding sources set-up screens can be chosen.


'''
from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END
from resources import Resources
from fundingsources import FundingSources
from allocationset import AllocationSet
#from inputpanel import InputPanel
from selectionlistbox import SelectionListbox

_plannerDataDir = "/users/swiftb/dev/Planner/data/"
_ResourcesFileName = "PlannerResources.txt"
_FundingSourcesFileName = "PlannerFundingSources.txt"
_Allocations = "PlannerAllocations.txt"

class Planner(Frame):
      def __init__(self, parent):
            Frame.__init__(self, parent)   
            self._parent = parent
            self._resourcesWindow = None
            self._resources = Resources(_plannerDataDir+_ResourcesFileName)
            self._fundingSources = FundingSources(_plannerDataDir+_FundingSourcesFileName)
            self._allocations = AllocationSet(_plannerDataDir+_Allocations)
            self.initUI()
            
      def initUI(self):
            self._parent.title("Planner")
            menubar = Menu(self._parent)
            self._parent.config(menu=menubar)
            fileMenu = Menu(menubar)
            fileMenu.add_command(label="Save", command=self.onSave)
            fileMenu.add_command(label="Exit", command=self.onExit)
            menubar.add_cascade(label="File", menu=fileMenu)

            viewMenu = Menu(menubar)
            viewMenu.add_command(label="Resources", command=self.onResources)
            viewMenu.add_command(label="Funding Sources", command=self.onFundingSources)
            menubar.add_cascade(label="View", menu=viewMenu)
                        
      def onExit(self):
            self.quit()

      def onSave(self):
            self._resources.write()
            print "Resources Saved"
            self._fundingSources.write()
            print "Funding Sources Saved"
            
      def onResources(self):
            self._resourcesWindow = SelectionListbox(self._parent, self._resources)

      def onFundingSources(self):
            self._fundingSourcesWindow = SelectionListbox(self._parent, self._fundingSources)
        
            
def main():
      root = Tk()
      root.geometry("250x150+300+300")
      app = Planner(root)
      root.mainloop()

if __name__ == '__main__':
      main()
      

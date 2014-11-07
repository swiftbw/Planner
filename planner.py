from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END
from person import Person
from resources import Resources
from location import Location
from inputpanel import InputPanel
from selectionlistbox import SelectionListbox

_plannerDataDir = "/users/swiftb/data/Planner/"
_ResourcesFileName = "PlannerResources.txt"
_Allocations = "PlannerAllocations.txt"
_AITS = "PlannerAITs.txt"
_Inits = "PlannerInits.txt"

class Planner(Frame):
      def __init__(self, parent):
            Frame.__init__(self, parent)   
            self._parent = parent
            self._resourcesWindow = None
            self.loadResources()
            #self.loadAllocations()
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
            menubar.add_cascade(label="View", menu=viewMenu)
                        
      def loadResources(self):
            self._resources = Resources(_plannerDataDir+_ResourcesFileName)
            
      def onExit(self):
            self.quit()

      def onSave(self):
            self._resources.write()
            print "Resources Saved"
            
      def onResources(self):
            print self._resources
            self._resourcesWindow = SelectionListbox(self._parent, self._resources.getResourcesAsDict().keys(), self.onCreateResource, self.onModifyResource, self.onDeleteResource)
                  
      def destroyResourcesWindow(self):
            self._resourcesWindow.destroy()
            self._resourcesWindow = None
              
      def onCreateResource(self):
            print "Creating new Resource"
            self._newResourcePanel = InputPanel(self._parent, {"First Name":"","Last Name":"","Location":""}, self.processNewResources)
            self._resourcesWindow.destroy()
            self._resourcesWindow = SelectionListbox(self._parent, self._resources.getResourcesAsDict().keys(), self.onCreateResource, self.onModifyResource, self.onDeleteResource)

      def onModifyResource(self, key):
            print "Modify " + key

      def onDeleteResource(self, key):
            print "Deleting Resource " + key + " from Resources"
            self._resourcesWindow.destroy()
            self._resourcesWindow = SelectionListbox(self._parent, self._resources.getResourcesAsDict().keys(), self.onCreateResource, self.onModifyResource, self.onDeleteResource)

      def processNewResources(self, panel, tdict):
            res = Person("0, " + tdict["First Name"] + ", " + tdict["Last Name"] + ", " + Location(tdict["Location"]).get())
            self._resources.add(res)
            panel.destroy()
            self.onResources()             
            return
                  
def main():
      root = Tk()
      root.geometry("250x150+300+300")
      app = Planner(root)
      root.mainloop()

if __name__ == '__main__':
      main()
      

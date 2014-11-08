from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END
from resource import Resource
from resources import Resources
from fundingsource import FundingSource
from fundingsources import FundingSources
from location import Location
from inputpanel import InputPanel
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
            self.loadResources()
            self.loadFundingSources()
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
            viewMenu.add_command(label="Funding Sources", command=self.onFundingSources)
            menubar.add_cascade(label="View", menu=viewMenu)
                        
      def loadResources(self):
            self._resources = Resources(_plannerDataDir+_ResourcesFileName)
            
      def loadFundingSources(self):
            self._fundingSources = FundingSources(_plannerDataDir+_FundingSourcesFileName)
            
      def onExit(self):
            self.quit()

      def onSave(self):
            self._resources.write()
            print "Resources Saved"
            
      def onResources(self):
            self._resourcesWindow = SelectionListbox(self._parent, self._resources.getKeys(), self.onCreateResource, self.onModifyResource, self.onDeleteResource)

      def destroyResourcesWindow(self):
            self._resourcesWindow.destroy()
            self._resourcesWindow = None
              
      def onCreateResource(self):
            print "Creating new Resource"
            self._newResourcePanel = InputPanel(self._parent, [("First Name",""),("Last Name",""),("Location","")], self.processNewResources)
            self._resourcesWindow.destroy()
            self._resourcesWindow = SelectionListbox(self._parent, self._resources.getKeys(), self.onCreateResource, self.onModifyResource, self.onDeleteResource)

      def onModifyResource(self, key):
            print "Modify " + key

      def onDeleteResource(self, key):
            print "Deleting Resource " + key + " from Resources"
            self._resourcesWindow.destroy()
            self._resourcesWindow = SelectionListbox(self._parent, self._resources.getKeys(), self.onCreateResource, self.onModifyResource, self.onDeleteResource)

      def processNewResources(self, panel, tdict):
            res = Resource("0, " + tdict["First Name"] + ", " + tdict["Last Name"] + ", " + Location(tdict["Location"]).get())
            self._resources.add(res)
            panel.destroy()
            self.onResources()             
            return
                  
      def onFundingSources(self):
            self._fundingSourcesWindow = SelectionListbox(self._parent, self._fundingSources.getKeys(), self.onCreateFundingSource, self.onModifyFundingSource, self.onDeleteFundingSource)
                  
      def destroyFundingSourcesWindow(self):
            self._fundingSourcesWindow.destroy()
            self._fundingSourcesWindow = None
              
      def onCreateFundingSource(self):
            print "Creating new Funding Source"
            self._newFundingSourcePanel = InputPanel(self._parent, {"Source Name":"","Type":"","Description":""}, self.processNewFundingSources)
            self._fundingSourcesWindow.destroy()
            self._fundingSourcesWindow = SelectionListbox(self._parent, self._fundingSources.getKeys(), self.onCreateFundingSource, self.onModifyFundingSource, self.onDeleteFundingSource)

      def onModifyFundingSource(self, key):
            print "Modify " + key

      def onDeleteFundingSource(self, key):
            print "Deleting Funding Source " + key + " from Funding Sources"
            self._fundingSourcesWindow.destroy()
            self._fundingSourcesWindow = SelectionListbox(self._parent, self._fundingSources.getKeys(), self.onCreateFundingSource, self.onModifyFundingSource, self.onDeleteFundingSource)

      def processNewFundingSources(self, panel, tdict):
            res = FundingSource("0, " + tdict["Source Name"] + ", " + tdict["Type"] + ", " + Location(tdict["Description"]).get())
            self._fundingSources.add(res)
            panel.destroy()
            self.onFundingSources()             
            return
def main():
      root = Tk()
      root.geometry("250x150+300+300")
      app = Planner(root)
      root.mainloop()

if __name__ == '__main__':
      main()
      

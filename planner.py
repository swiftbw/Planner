from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END
from person import Person
from resources import Resources
from location import Location
from inputpanel import InputPanel

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
            if self._resourcesWindow == None:
                  self._resourcesWindow = Toplevel(self._parent)
                  self._resourcesWindow.protocol('WM_DELETE_WINDOW', self.destroyResourcesWindow)

                  lb = Listbox(self._resourcesWindow)
                  lb.pack()
                  resources = self._resources.getResourcesAsDict()
                  for i in resources:
                        lb.insert(END, i[0])
                  bt = Button(self._resourcesWindow, text="New Resource", command=self.newResource)
                  bt.pack()
      def destroyResourcesWindow(self):
            self._resourcesWindow.destroy()
            self._resourcesWindow = None
              
      def newResource(self):
            print "Hello World!"
            self._newResourcePanel = InputPanel(self._parent, {"First Name":"","Last Name":"","Location":""}, self.processNewResources)
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
      

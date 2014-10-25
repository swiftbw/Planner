from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel
from person import Resources, Person

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
            fileMenu.add_command(label="Exit", command=self.onExit)
            menubar.add_cascade(label="File", menu=fileMenu)

            viewMenu = Menu(menubar)
            viewMenu.add_command(label="Resources", command=self.onResources)
            menubar.add_cascade(label="View", menu=viewMenu)
                        
      def loadResources(self):
            self._resources = Resources(_plannerDataDir+_ResourcesFileName)
            
      def onExit(self):
            self.quit()
            
      def onResources(self):
            if self._resourcesWindow == None:
                  self._resourcesWindow = Toplevel(self._parent)
                  lb = Listbox(self._resourcesWindow)
                  lb.pack()
                  resources = self._resources.getResources()
                  for i in resources:
                        lb.insert(END, i[0])
                  bt = Button(self._resourcesWindow, text="New Resource", command=self.newResource)
                  bt.pack()
      def newResource(self):
            print "Hello World!"
                  
def main():
      root = Tk()
      root.geometry("250x150+300+300")
      app = Planner(root)
      root.mainloop()

if __name__ == '__main__':
      main()
      

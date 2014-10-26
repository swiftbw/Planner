from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END
from person import Resources, Person
from location import Location

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
            self._newResourceWindow = None
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
                  lb = Listbox(self._resourcesWindow)
                  lb.pack()
                  resources = self._resources.getResources()
                  for i in resources:
                        lb.insert(END, i[0])
                  bt = Button(self._resourcesWindow, text="New Resource", command=self.newResource)
                  bt.pack()
      def newResource(self):
            print "Hello World!"
            if self._newResourceWindow == None:
                  self._newResourceWindow = Toplevel(self._resourcesWindow)
                  self._fnPanel = PanedWindow(self._newResourceWindow)
                  self._lnPanel = PanedWindow(self._newResourceWindow)
                  self._locPanel = PanedWindow(self._newResourceWindow)
                  fnLabel = Label(self._fnPanel, text="First Name")
                  fnLabel.pack(side=LEFT)
                  self._fnEntry = Entry(self._fnPanel)
                  self._fnEntry.pack(side=RIGHT)
                  self._fnPanel.pack(side=TOP)
                  lnLabel = Label(self._lnPanel, text="Last Name")
                  lnLabel.pack(side=LEFT)
                  self._lnEntry = Entry(self._lnPanel)
                  self._lnEntry.pack(side=RIGHT)
                  self._lnPanel.pack(side=TOP)
                  locLabel = Label(self._locPanel, text="Location")
                  locLabel.pack(side=LEFT)
                  self._locEntry = Entry(self._locPanel)
                  self._locEntry.pack(side=RIGHT)
                  self._locPanel.pack(side=TOP)
                  subBt = Button(self._newResourceWindow, text="Submit", command=self.onNewResourceSubmit)
                  subBt.pack(side=TOP)
      def onNewResourceSubmit(self):
            res = Person("0, " + self._fnEntry.get() + ", " + self._lnEntry.get() + ", " + Location(self._locEntry.get()).get())
            self._resources.add(res)
                         
            return
                  
def main():
      root = Tk()
      root.geometry("250x150+300+300")
      app = Planner(root)
      root.mainloop()

if __name__ == '__main__':
      main()
      

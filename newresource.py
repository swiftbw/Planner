from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END
from person import Resources, Person
from location import Location

class NewResource(Toplevel):
      def __init__(self, parent):
            Toplevel.__init__(self, parent)   
            self.protocol('WM_DELETE_WINDOW', self.destroyNewResourceWindow)
            self._fnPanel = PanedWindow(self)
            self._lnPanel = PanedWindow(self)
            self._locPanel = PanedWindow(self)
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
            subBt = Button(self, text="Submit", command=self.onNewResourceSubmit)
            subBt.pack(side=TOP)
      def destroy(self):
            Toplevel.destroy()

      def onNewResourceSubmit(self):
            res = Person("0, " + self._fnEntry.get() + ", " + self._lnEntry.get() + ", " + Location(self._locEntry.get()).get())
            return(res)
#
#           
#                        self._resources.add(res)
#
#            self._newResourceWindow.destroy()
#            self._newResourceWindow = None
#            self._resourcesWindow.destroy()
#            self._resourcesWindow = None
#            self.onResources()             
#            return

def main():
      root = Tk()
      root.geometry("250x150+300+300")
      app = NewResource(root)
      root.mainloop()

if __name__ == '__main__':
      main()

from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END, SINGLE

class SelectionListbox(Toplevel):
      def __init__(self, parent, selections, createCallback, modifyCallback, deleteCallback):
            Toplevel.__init__(self, parent)
            self.protocol('WM_DELETE_WINDOW', self.destroy)

            self._createCallback = createCallback
            self._modifyCallback = modifyCallback
            self._deleteCallback = deleteCallback
            self._selections = selections
            
            self._lb = Listbox(self, selectmode = SINGLE)
            self._lb.pack()

            for i in selections:
                  self._lb.insert(END, i)

            createButton = Button(self, text="Create", command=self.onCreate)
            createButton.pack()

            modifyButton = Button(self, text="Modify", command=self.onModify)
            modifyButton.pack()
            
            deleteButton = Button(self, text="Delete", command=self.onDelete)
            deleteButton.pack()

      def onCreate(self):
            self._createCallback()

      def onModify(self):
            self._modifyCallback(self._lb.get(self._lb.curselection()))
            
      def onDelete(self):
            self._deleteCallback(self._lb.get(self._lb.curselection()))

      def destroy(self):
            Toplevel.destroy(self)
              
def main():
      root = Tk()
      root.geometry("250x150+300+300")

      l = ["asdf", "qwer", "zxcv"]
      
      app = SelectionListbox(root, l, CreateCallback, ModifyCallback, DeleteCallback)
      root.mainloop()

def CreateCallback():
      print "Create"

def ModifyCallback(key):
      print "Modify"

def DeleteCallback(key):
      print "Delete"

if __name__ == '__main__':
      main()

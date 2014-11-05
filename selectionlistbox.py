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
            self._buttons = PanedWindow(self)

            for i in selections:
                  self._lb.insert(END, i)

            createButton = Button(self._buttons, text="Create", command=self.onCreate)
            createButton.pack(side=LEFT)

            modifyButton = Button(self._buttons, text="Modify", command=self.onModify)
            modifyButton.pack(side=LEFT)
            
            deleteButton = Button(self._buttons, text="Delete", command=self.onDelete)
            deleteButton.pack(side=RIGHT)
            self._buttons.pack(side=BOTTOM)

      def onCreate(self):
            self._createCallback()

      def onModify(self):
            self._modifyCallback(self._lb.get(self._lb.curselection()))
            
      def onDelete(self):
            self._deleteCallback(self._lb.get(self._lb.curselection()))

      def destroy(self):
            Toplevel.destroy(self)
              
class mainclass():
      def __init__(self, root):
            self.l = ["asdf", "qwer", "zxcv"]
            self.root = root
            self.app = SelectionListbox(self.root, self.l, self.CreateCallback, self.ModifyCallback, self.DeleteCallback)

      def CreateCallback(self):
            print "Create"
            self.l.append("uiop")
            self.app.destroy()
            self.app = SelectionListbox(self.root, self.l, self.CreateCallback, self.ModifyCallback, self.DeleteCallback)

      def ModifyCallback(self, key):
            print "Modify " + key

      def DeleteCallback(self, key):
            print "Delete"
            self.l.remove(key)
            self.app.destroy()
            self.app = SelectionListbox(self.root, self.l, self.CreateCallback, self.ModifyCallback, self.DeleteCallback)

def main():
      
      root = Tk()
      root.geometry("250x150+300+300")
      mc = mainclass(root)
      root.mainloop()

if __name__ == '__main__':
      main()

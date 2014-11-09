'''
The SelectionListbox class is intended provide a list management window to users.  The listbox provides the ability to add, modify, and remove elements from the list.  The list takes as input an object which contains the list being managed.  Currently, this will either be a Resources list or a fundingSources list.

The Selectionlistbox contains three buttons -- Add, Modify, and Delete.  

The SelectionListbox contains the following methods:
__init__ -- Takes the parent ui and the objectList to be displayed.
onAdd
onModify
onDelete
destroy
inputCallback
'''
from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END, SINGLE

class SelectionListbox(Toplevel):
      def __init__(self, parent, objectList):
            Toplevel.__init__(self, parent)
            self.protocol('WM_DELETE_WINDOW', self.destroy)

            self._objectList = objectList
            
            self._lb = Listbox(self, selectmode = SINGLE)
            self._lb.pack()
            self._buttons = PanedWindow(self)

            for i in objectList.getLBNames():
                  self._lb.insert(END, i)

            addButton = Button(self._buttons, text="Add", command=self.onAdd)
            addButton.pack(side=LEFT)

            modifyButton = Button(self._buttons, text="Modify", command=self.onModify)
            modifyButton.pack(side=LEFT)
            
            deleteButton = Button(self._buttons, text="Delete", command=self.onDelete)
            deleteButton.pack(side=RIGHT)
            self._buttons.pack(side=BOTTOM)

      def onAdd(self):
            self._inputPanel = InputPanel(self, self._objectList.getKeys(), self.inputCallBack)

      def onModify(self):
            key = self._lb.curselection()
            obj = self._objectsList(key)
            mdict = obj.getValuesAsDict()
            self._inputPanel = InputPanel(self, self._objectList.getKeys(), self.inputCallBack, self._objectList.getAsDict()[self._lb.curselection())])
            
      def onDelete(self):
            self._deleteCallback(self._lb.get(self._lb.curselection()))

      def destroy(self):
            Toplevel.destroy(self)
              
      def inputCallback(self, cdict, key):
            print "Add/Change input"
            if self._objectList.
            self._objectList.newFromDict(cdict)
            self._lb.insert(END, key)
            self._lb.update()
            self._inputPanel.destroy()

      def DeleteCallback(self, key):
            print "Delete"
            self._objectList.remove(key)
            self._lb.remove(key)
            self._lb.update()

def main():
      
      root = Tk()
      root.geometry("250x150+300+300")
      mc = mainclass(root)
      root.mainloop()

if __name__ == '__main__':
      main()

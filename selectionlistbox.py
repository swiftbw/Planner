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

from resource import Resource
from resources import Resources
from inputpanel import InputPanel

class SelectionListbox(Toplevel):
      def __init__(self, parent, objectList):
            Toplevel.__init__(self, parent)
            self.protocol('WM_DELETE_WINDOW', self.destroy)

            self._objectList = objectList
            
            self._lb = Listbox(self, selectmode = SINGLE)
            self._lb.pack()
            self._buttons = PanedWindow(self)

            for i in objectList.getKeysInOrder():
                  self._lb.insert(END, i)

            addButton = Button(self._buttons, text="Add", command=self.onAdd)
            addButton.pack(side=LEFT)

            modifyButton = Button(self._buttons, text="Modify", command=self.onModify)
            modifyButton.pack(side=LEFT)
            
            deleteButton = Button(self._buttons, text="Delete", command=self.onDelete)
            deleteButton.pack(side=LEFT)

            cancelButton = Button(self._buttons, text="Cancel", command=self.onCancel)
            cancelButton.pack(side=RIGHT)

            self._buttons.pack(side=BOTTOM)

      def onAdd(self):
            self._inputPanel = InputPanel(self, self._objectList.getElementKeys(), self.addCallBack)

      def onModify(self):
            ctr = self._lb.curselection()
            key = self._lb.get(ctr)
            self._inputPanel = InputPanel(self, self._objectList.getElementKeys(), self.modifyCallBack, key, self._objectList.getAsDict(key))
            
      def onDelete(self):
            idx = self._lb.curselection()
            self.deleteCallBack(idx)

      def onCancel(self):
            self.destroy()

      def destroy(self):
            Toplevel.destroy(self)
              
      def addCallBack(self, cdict):
            print "Add new element"

            key = self._objectList.addFromDict(cdict)
                  
            self._lb.insert(END, key)
            self._lb.update()
            # self._inputPanel.destroy()

      def modifyCallBack(self, cdict, key):
            print "Modify Existing Element"

            self._objectList.modifyElement(cdict, key)
                  
            self._lb.insert(END, key)
            self._lb.update()
            # self._inputPanel.destroy()

      def deleteCallBack(self, idx):
            print "Delete"
            print idx
            key = self._lb.get(idx)
            self._objectList.deleteElement(key)
            self._lb.delete(idx)
            self._lb.update()

def main():
      
      root = Tk()
      root.geometry("250x150+300+300")
      sl = Resources("/users/swiftb/tmp/resources.txt")
      res = Resource("0, Brian, Swift, CHI")
      sl.add(res)
      res = Resource("1, John, DeValk, CHI")
      sl.add(res)
      sl.write()
      
      mc = SelectionListbox(root, sl)
      root.mainloop()

if __name__ == '__main__':
      main()    

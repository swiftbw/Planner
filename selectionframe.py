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
#from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END, SINGLE
import wx
from resources import Resources
from resource import Resource

from inputpanel import InputPanel

class SelectionFrame(wx.Frame):
      def __init__(self, parent, ress, id=wx.ID_ANY, title="", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE, name = "SelectionFrame" ):
            super(SelectionFrame, self).__init__(parent, id, title, pos, size, style, name)

            self._mainpanel = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)

            mainsizer = wx.BoxSizer(wx.VERTICAL)
            listctrlsizer = wx.BoxSizer(wx.VERTICAL)
            buttonsizer = wx.BoxSizer(wx.HORIZONTAL)

            self._listctrl = wx.ListCtrl(self, -1, style=wx.LC_REPORT)

            for i in ress._resources:
                  print i[Resource.uid]
                  print i[Resource.firstName]
                  print i[Resource.lastName]
                  print i[Resource.location]
                  print i[Resource.status]
                  self._listctrl.Append(str(i[Resource.uid]))
                  self._listctrl.Append(i[Resource.firstName])
                  self._listctrl.Append(i[Resource.lastName])
                  self._listctrl.Append(i[Resource.location])
                  self._listctrl.Append(i[Resource.status])

            i = 0
            for key in reversed(ress.getDictKeys()):
                  self._listctrl.InsertColumn(i, key)

            listctrlsizer.Add(self._listctrl)

            ADD_BTN = wx.NewId()
            MODIFY_BTN = wx.NewId()
            DELETE_BTN = wx.NewId()
            CANCEL_BTN = wx.NewId()
            
            addbtn = wx.Button(self._mainpanel, ADD_BTN, "Add")
            modifybtn = wx.Button(self._mainpanel, MODIFY_BTN, "Modify")
            deletebtn = wx.Button(self._mainpanel, DELETE_BTN, "Delete")
            cancelbtn = wx.Button(self._mainpanel, CANCEL_BTN, "Cancel")
            buttonsizer.Add(addbtn)
            buttonsizer.Add(modifybtn)
            buttonsizer.Add(deletebtn)
            buttonsizer.Add(cancelbtn)
            
            self.Bind(wx.EVT_LIST_ITEM_SELECTED, self.onUpdateSelection)
            
            self.Bind(wx.EVT_BUTTON, self.onAdd, id=ADD_BTN)
            # self.Bind(wx.EVT_BUTTON, self.onModify, MODIFY_BTN)
            # self.Bind(wx.EVT_BUTTON, self.onDelete, id=DELETE_BTN)
            self.Bind(wx.EVT_BUTTON, self.onCancel, id=CANCEL_BTN)

            mainsizer.Add(listctrlsizer)
            mainsizer.AddSpacer(50)
            mainsizer.Add(buttonsizer)
            
            self._mainpanel.SetSizer(mainsizer)
            self._mainpanel.SetInitialSize()
            self.Show()

      def onUpdateSelection(self, event):
            self.row_idx = event.GetIndex()
            
      def onAdd(self, event):
            d = {}
            for i in Resource.dictKeys:
                  d[i] = ""

            res = Resource(d)
            self._inputPanel = InputPanel(self, res, self.addCallBack)

      """
      def onDelete(self):
            idx = self._lb.curselection()
            self.deleteCallBack(idx)

      def onModify(self):
            ctr = self._lb.curselection()
            key = self._lb.get(ctr)
            print key
            print self._objectList
            self._inputPanel = InputPanel(self, self._objectList.getElementKeys(), self.modifyCallBack, key, self._objectList._resources[key])
            
      """
      def onCancel(self, event):
            self.destroy()

      def destroy(self):
            self.Destroy()
              
      def addCallBack(self, cdict):
            print "Add new element"

            key = self._objectList.addFromDict(cdict)
                  
            print self.row_idx
            #self._lb.insert(END, key)
            #self._lb.update()
            # self._inputPanel.destroy()

      '''            


      def modifyCallBack(self, cdict, key):
            print "Modify Existing Element"
            print cdict
            print key
            self._objectList.modifyElement(cdict, key)
            print self._objectList._resources[key]
                  
            self._lb.update()
            # self._inputPanel.destroy()

      def deleteCallBack(self, idx):
            print "Delete"
            print idx
            key = self._lb.get(idx)
            self._objectList.deleteElement(key)
            self._lb.delete(idx)
            self._lb.update()
      '''


def main():
      
      app = wx.App()

      ress = Resources("/users/swiftb/dev/Planner/data/testresources.txt")
      res = Resource("{'UID': '1', 'First Name': 'Brian', 'Last Name': 'Swift', 'Location': 'CHI'}")
      ress.add(res)
      res = Resource("{'UID': '2', 'First Name': 'John', 'Last Name': 'DeValk', 'Location': 'CHI'}")
      ress.add(res)
      ress.write()
      print ress._resources
      
      mc = SelectionFrame(None, ress)
      app.MainLoop()

if __name__ == '__main__':
      main()    

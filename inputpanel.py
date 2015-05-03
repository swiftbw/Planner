'''
The InputPanel class is a UI component intended to capture basic key values.  It can accept default values.

Any changes identified upon submit will be sent back as a dictionary in the callback function.

Instance values include:
_fieldValues
kvpanel
_rdict

methods are:
__init__
destroy
onSubmit
returns a dictionary to the callback function of all fieldLabels that ahve changed.

onCancel
returns am empty dictionary to the callback function since by definition no values have changed

'''
#from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END, StringVar

import wx
from resource import Resource

class InputPanel(wx.Frame):
      def __init__(self, parent, res, fieldLabels, onSubmitCallback, listKey=None, fieldValuesDict={}, id=wx.ID_ANY, title="", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE, name = "InputPanel" ):

            super(InputPanel, self).__init__(parent, id, title, pos, size, style, name)

            self._fieldLabels = fieldLabels
            self._listKey = listKey

            self._mainpanel = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)

            mainsizer = wx.BoxSizer(wx.VERTICAL)
            keyvaluesizers = []
            for i in self._fieldLabels:
                  keyvaluesizers.Append(wx.BoxSizer(wx.HORIZONTAL))
                  keyvaluesizers[-1].Add(wx.StaticText(self, label = i), 0, wx.ALIGN_CENTER_VERTICAL)
                  if i in self._fieldValuesDict:
                        self._fieldValues[i] = wx.TextCtrl(self)
                  
                  self._fieldValues[i].SetValue(self._fieldValuesDict[i])
                  keyvaluesizers[-1].Add(self._fieldValues[i], 0, wx.EXPAND)

            
            self._kvpanel = {}
            self._rdict = {}
            for i in self._fieldLabels:
                  if i not in fieldValuesDict:
                        fieldValuesDict[i] = ""
                        
            self._fieldValuesDict = fieldValuesDict

            self.onSubmitCallback = onSubmitCallback

            for i in self._fieldLabels:
                  self._kvpanel[i] = PanedWindow(self)
                  label = Label(self._kvpanel[i], text=i)
                  label.pack(side=LEFT)
                  v = StringVar()
                  entry = Entry(self._kvpanel[i], textvariable = v)
                  v.set(self._fieldValuesDict[i])
                  self._rdict[i] = v
                  entry.pack(side=RIGHT)
                  self._kvpanel[i].pack(side=TOP)

            self._buttonsPanel = PanedWindow(self)
            
            subBt = Button(self._buttonsPanel, text="Submit", command=self.onSubmit)
            subBt.pack(side=LEFT)
            cxlBt = Button(self._buttonsPanel, text="Cancel", command=self.onCancel)
            cxlBt.pack(side=RIGHT)

            self._buttonsPanel.pack(side=TOP)
            
      def destroy(self):
            Toplevel.destroy(self)

      def onSubmit(self):
            keyvalues = {}
            for i in self._fieldLabels:
                  keyvalues[i] = self._rdict[i].get()

            self.onSubmitCallback(keyvalues, self._listKey)
            self.destroy()
            
      def onCancel(self):
            self.destroy()

def main():

          
      app = wx.App()

      res = Resource("{'UID': '1', 'First Name': 'Brian', 'Last Name': 'Swift', 'Location': 'CHI'}")
      mc = InputPanel(None, res)

      app.MainLoop()

      app = InputPanel(root, ("first", "last"), print_results)
      tdict = {"first" : "Brian", "last" : "Swift"}
      app = InputPanel(root, ("first", "last"), print_results, "Swift, Brian", tdict)
      root.mainloop()

def print_results(tdict, listkey):
      for i in tdict.keys():
            print i, tdict[i]




if __name__ == '__main__':
      main()

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
      def __init__(self, parent, res, onSubmitCallback, id=wx.ID_ANY, title="", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE, name = "InputPanel" ):

            super(InputPanel, self).__init__(parent, id, title, pos, size, style, name)

            self._inputDict = res
            self.onSubmitCallback = onSubmitCallback

            self._mainpanel = wx.Panel(self, -1, style=wx.SIMPLE_BORDER)

            mainsizer = wx.BoxSizer(wx.VERTICAL)

            kvaluesizer = wx.GridSizer(6,2,5,5)
            
            self._inputTextCtrl = {}
            
            for i in self._inputDict.dictKeys:
                  kvaluesizer.Add(wx.StaticText(self, label = i))
                  if i in self._inputDict:
                        self._inputTextCtrl[i] = wx.TextCtrl(self)
                        self._inputTextCtrl[i].SetValue(self._inputDict[i])
                  
                  kvaluesizer.Add(self._inputTextCtrl[i])

            mainsizer.Add(kvaluesizer, 1, wx.EXPAND)

            SUB_BTN = wx.NewId()
            CXL_BTN = wx.NewId()
            
            subbtn = wx.Button(self._mainpanel, SUB_BTN, "Submit")
            cxlbtn = wx.Button(self._mainpanel, CXL_BTN, "Cancel")

            buttonsizer = wx.BoxSizer(wx.HORIZONTAL)

            self.Bind ( wx.EVT_BUTTON, self.onSubmit, id=SUB_BTN )
            self.Bind ( wx.EVT_BUTTON, self.onCancel, id=CXL_BTN )
            
            buttonsizer.Add(subbtn)
            buttonsizer.Add(cxlbtn)

            mainsizer.Add(buttonsizer)

            self._mainpanel.SetSizer(mainsizer)
            self._mainpanel.SetInitialSize()
            self.Show()
            
      def destroy(self):
            self.Destroy()

      def onSubmit(self, event):
            keyvalues = {}
            for i in self._inputDict.dictKeys:
                  keyvalues[i] = self._inputTextCtrl[i].GetValue()

            self.onSubmitCallback(keyvalues)
            self.Destroy()
            
      def onCancel(self, event):
            self.destroy()

def main():
      app = wx.App()

      res = Resource("{'UID': '1', 'First Name': 'Brian', 'Last Name': 'Swift', 'Location': 'CHI'}")
      mc = InputPanel(None, res, print_results)

      app.MainLoop()

def print_results(tdict):
      for i in tdict.keys():
            print i, tdict[i]

if __name__ == '__main__':
      main()

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

class PanelTest(wx.Frame):
      def __init__(self, parent=None, id=wx.ID_ANY, title="", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE, name = "PanelTest" ):

            super(PanelTest, self).__init__(parent, id, title, pos, size, style, name)

            self._mainpanel = wx.Panel(self, 0, style=wx.SIMPLE_BORDER)

            mainsizer = wx.BoxSizer(wx.VERTICAL)

            subpanel = wx.Panel(self, 0, style=wx.SIMPLE_BORDER)
            subsizer = wx.BoxSizer(wx.VERTICAL)
            subpanel.SetSizer(subsizer)
            subsizer.Add(wx.StaticText(self, label = "testing"), 0, wx.ALIGN_RIGHT)
            
            mainsizer.Add(subpanel, 0, wx.EXPAND)
            self._mainpanel.SetSizer(mainsizer)
            self._mainpanel.SetInitialSize()
            self.Show()

def main():

          
      app = wx.App()
      mc = PanelTest()
      app.MainLoop()

if __name__ == '__main__':
      main()

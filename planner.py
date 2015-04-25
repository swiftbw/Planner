'''
The Planner class is the main class for the Planner application.  planner.py extends Frame.  Upon initialization a reference to the parent window is stored in the object, and _resources, _fundingSources, and _allocations objects are created.

initUI is then called.  When initUI is called the file menu and view menus are set up.

From the file menu, exit and save options are available.

From the view menu, the resources and funding sources set-up screens can be chosen.


'''
# from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END
import wx
import sys
from resources import Resources
from fundingsources import FundingSources
from allocationset import AllocationSet
#from inputpanel import InputPanel
from selectionlistbox import SelectionListbox

_plannerDataDir = "/users/swiftb/dev/Planner/data/"
_ResourcesFileName = "PlannerResources.txt"
_FundingSourcesFileName = "PlannerFundingSources.txt"
_Allocations = "PlannerAllocations.txt"

class PlannerApp(wx.App):
      def OnInit(self):
            self._frame = PlannerFrame(None, title = "Planner")
            self.SetTopWindow(self._frame)
            self._frame.Show()

            return True
      
class PlannerFrame(wx.Frame):
      def __init__(self, parent, id=wx.ID_ANY, title="", pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_FRAME_STYLE, name = "PlannerFrame"):
            super(PlannerFrame, self).__init__(parent, id, title, pos, size, style, name)
            self._parent = parent
            self._title = title
            self._resources = Resources(_plannerDataDir+_ResourcesFileName)
            self._fundingSources = FundingSources(_plannerDataDir+_FundingSourcesFileName)
            self._allocations = AllocationSet(_plannerDataDir+_Allocations)

# Create MenuBar
            menuBar = wx.MenuBar()

# Create File Menu
            fileMenu = wx.Menu()
            menuExit = fileMenu.Append(wx.ID_EXIT, "E&xit"," Terminate the program")
            menuSave = fileMenu.Append(wx.ID_SAVE, "&Save", "Save Resources and Funding Sources")
            fileMenu.AppendSeparator()


# Create View Menu
            viewMenu = wx.Menu()

            PLN_RESOURCES = wx.NewId()
            PLN_FUNDINGSOURCES = wx.NewId()
            
            menuResources = viewMenu.Append(PLN_RESOURCES, "&Resources", "Bring up Resources Panel")
            menuFundingSources = viewMenu.Append(PLN_FUNDINGSOURCES, "F&unding Sources", "Bring up Funding Sources Panel")

            menuBar.Append(fileMenu, "&File")
            menuBar.Append(viewMenu, "&View")
            
            self.SetMenuBar(menuBar)
            self.CreateStatusBar()

# File Menu Items
            self.Bind(wx.EVT_MENU, self.OnExit, menuExit)
            self.Bind(wx.EVT_MENU, self.OnSave, menuSave)

# View Menu Items            
            self.Bind(wx.EVT_MENU, self.OnResources, menuResources)
            self.Bind(wx.EVT_MENU, self.OnFundingSources, menuFundingSources)
            
            self.Show(True)

      def OnExit(self, e):
            sys.exit()

      def OnSave(self, e):
            self._resources.write()
            print "Resources Saved"
            self._fundingSources.write()
            print "Funding Sources Saved"
            
      def OnResources(self, e):
            self._resourcesWindow = SelectionListbox(self, self._resources)

      def OnFundingSources(self, e):
            self._fundingSourcesWindow = SelectionListbox(self, self._fundingSources)
        
            
def main():
      app = PlannerApp(False)
      app.MainLoop()

if __name__ == '__main__':
      main()
      

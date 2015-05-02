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

class InputPanel(Toplevel):
      def __init__(self, parent, fieldLabels, onSubmitCallback, listKey=None, fieldValuesDict={}):
            Toplevel.__init__(self, parent)   
            self.protocol('WM_DELETE_WINDOW', self.destroy)
            self._fieldLabels = fieldLabels
            self._listKey = listKey
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
      root = Tk()
      root.geometry("250x150+300+300")
      app = InputPanel(root, ("first", "last"), print_results)
      tdict = {"first" : "Brian", "last" : "Swift"}
      app = InputPanel(root, ("first", "last"), print_results, "Swift, Brian", tdict)
      root.mainloop()

def print_results(tdict, listkey):
      for i in tdict.keys():
            print i, tdict[i]




if __name__ == '__main__':
      main()

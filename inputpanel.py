from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END
#from person import Resources, Person
#from location import Location

class InputPanel(Toplevel):
      def __init__(self, parent, keyvalues, onSubmitcallback):
            Toplevel.__init__(self, parent)   
            self.protocol('WM_DELETE_WINDOW', self.destroy)
            self._kvpanel = {"":""}
            self.onsubmitcallback = onSubmitcallback

            for i in keyvalues.keys():
                  print i
                  self._kvpanel[i] = PanedWindow(self)
                  label = Label(self._kvpanel[i], text=i)
                  label.pack(side=LEFT)
                  entry = Entry(self._kvpanel[i], textvariable = keyvalues[i])
                  entry.pack(side=RIGHT)
                  self._kvpanel[i].pack(side=TOP)

            subBt = Button(self, text="Submit", command=self.onSubmit)
            subBt.pack(side=TOP)
      def destroy(self):
            Toplevel.destroy(self)
      def onSubmit(self):
            self.onsubmitcallback(self, {"asdf":"asdf","qwer":"qwer"})
            

def main():
      root = Tk()
      root.geometry("250x150+300+300")
      tdict = {"first" : "Brian", "last" : "swift"}
      app = InputPanel(root, tdict, print_results)
      root.mainloop()

def print_results(panel, tdict):
      for i in tdict.keys():
            print i, tdict[i]

      panel.destroy()



if __name__ == '__main__':
      main()

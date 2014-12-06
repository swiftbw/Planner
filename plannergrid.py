'''
The PlannerGrid control is intended to be a tabular data grid control for the planner application.  we want to reuse it to provide the following views on Resource and Project data:

1.  Resources vs Projects
2.  For a given Project, Resources vs. Months
3.  For a given Resource, Projects vs. Months

There should be a Title bar that indicates the view

Resources vs Projects
From the Resources vs Projects view, a user should be able to:
1.  click on a row label and get a Projects vs Months view for that Resource
2.  click on a column label and get a Resources vs. Months view for that Project
3.  there should be no action for clicking in data cells
4.  should be able to click on the x and destroy the table

Resources vs Months
From the Resources vs Months view, a user should be able to:
1.  click on a data cell and edit the value in that cell


'''

from Tkinter import Tk, Frame, Menu, PanedWindow, Listbox, Button, Toplevel, Label, Entry, LEFT, RIGHT, TOP, BOTTOM, END, SINGLE

class PlannerGrid(Toplevel):
      def __init__(self, parent, dataGrid):
            Toplevel.__init(self, parent)
        
    
def main():
      root = Tk()
      root.geometry("250x150+300+300")
      app = Planner(root)
      root.mainloop()

if __name__ == '__main__':
      main()
      

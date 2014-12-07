'''
SelectionList is a base class for any objects that want to be represented using selectionlistbox.  



It has the following methods:

getLBNames, which returns an ordered list of strings that will be used as labels in the inputpanel window.  This is needed in order to provide a different sequence to the inputpanel window than is retrieved by using "getKeys" from the dict.

getKeys
'''
class SelectionList:
      def __init__():
            return

'''
Returns a list of strings representing labels for the given object type.  These can be used for display in the InputPanel.
'''
      def getElementKeys():
            return

'''
This method takes in a dictionary of values, creates an object of the type presented in the selectionlistbox, and returns a string which is the key to the new object.
This method takes as input a dictionary containing all the fields required to create an instance of the class comprising the listbox.  This is passed in to the static method on the class and returns a string which can be passed into the constructor to create an actual object.  This is then added to the objects already represented in the listbox, and returns the appropriate key, which will be added to the listbox.
'''
      def addFromDict(<fieldsDict>):
            return <string>


'''
Returns an object of base type inputelement from list or None if none exists.
'''
      def modifyElement(<fieldsDict>, <key>):
            return 

'''
The remove method needs to remove the element from the list.  It is assumed that a warning was already affirmed.
'''
      def deleteElement(key):
            return




      
      

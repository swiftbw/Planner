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
Returns a list of strings in the order that they should be presented in the listbox.  This list needs to be a unique set of keys that can be used to look up an element in the list.
'''
      def getKeys():
            return

'''
Returns an object of base type inputelement from list or None if none exists.
'''
      def addElement(<fieldsDict>):
            return 


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

        '''
Returns an object of base type inputelement from list or None if none exists.
'''
      def getFieldsDict(key):
            return <fieldsDict>

      
      

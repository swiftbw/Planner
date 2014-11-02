class NameValueElement(PanedWindow):
      def __init__(self, name):
            PanedWindow.__init__(self)
            self._label = Label(self, text=name)
            self._label.pack(side=LEFT)
            self._value = Entry(self)
            self._value.pack(side=RIGHT)

      def getLabel(self):
          return _label

      def getValue(self):
          return _value

      

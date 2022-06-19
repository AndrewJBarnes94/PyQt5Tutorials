import PyQt5.QtWidgets as qtw
import PyQt5.QtGui as qtg

class MainWindow(qtw.QWidget):
    def __init__(self):
        super().__init__()
        # Add a title
        self.setWindowTitle("hello world")
        # Set a vertical box layout
        self.setLayout(qtw.QVBoxLayout())
        # Create a label
        my_label = qtw.QLabel("Pick a pizza topping")
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        # Place label to the screen
        self.layout().addWidget(my_label)
        # Create a combo box
        my_combo = qtw.QComboBox(self,
            editable=True,
            insertPolicy=qtw.QComboBox.InsertAtTop)
        # Add items to the Combo Box
        my_combo.addItem("Pepperoni")
        my_combo.addItem("Cheese")
        my_combo.addItem("Mushroom")
        my_combo.addItem("Peppers")
        my_combo.addItems(["One", "Two", "Three"])
        my_combo.insertItem(2, "Third Topping")
        my_combo.insertItems(1, ["A", "B", "C"])
        # Put combo box on the screen
        self.layout().addWidget(my_combo)
        # Create a button that will call the function "press_it"
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        # Place button to the screen
        self.layout().addWidget(my_button)
        # Show the widget
        self.show()
        # Create the press_it function for the button click
        def press_it():
            my_label.setText(f"You picked {my_combo.currentText()}") #.currentData will return a second item of the tuple addItem() and .currentIndex will return the index number of all the elements in your combo box.
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
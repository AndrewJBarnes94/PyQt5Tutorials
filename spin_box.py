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
        my_label.setFont(qtg.QFont('Helvetica', 24))
        # Place label to the screen
        self.layout().addWidget(my_label)
        # Create a spin box
        my_spin = qtw.QSpinBox( # Use qtw.QDoubleSpingBox for float values
            self,
            value=0,
            maximum=100,
            minimum=0,
            singleStep=5,
            prefix="#",
            suffix=" Order"
        )
        my_spin.setFont(qtg.QFont('Helvetica', 18))
        # Place spin box on the screen
        self.layout().addWidget(my_spin)
        # Create a button that will call the function "press_it"
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        # Place button on the screen
        self.layout().addWidget(my_button)
        # Show the widget
        self.show()
        # Create the press_it function for the button click
        def press_it():
            my_label.setText(f"You picked {my_spin.value()}") #.currentData will return a second item of the tuple addItem() and .currentIndex will return the index number of all the elements in your combo box.
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
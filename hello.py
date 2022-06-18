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
        my_label = qtw.QLabel("Hello World. What's your name?")
        # Change the font size of label
        my_label.setFont(qtg.QFont('Helvetica', 18))
        # Place label to the screen
        self.layout().addWidget(my_label)
        # Create an entry box
        my_entry = qtw.QLineEdit()
        my_entry.setObjectName("name_field")
        my_entry.setText("")
        # Place entry box to the screen
        self.layout().addWidget(my_entry)
        # Create a button that will call the function "press_it"
        my_button = qtw.QPushButton("Press Me!",
            clicked = lambda: press_it())
        # Place button to the screen
        self.layout().addWidget(my_button)
        # Show the widget
        self.show()
        # Create the press_it function for the button click
        def press_it():
            my_label.setText(f"Hello {my_entry.text()}")
            my_entry.setText("")
app = qtw.QApplication([])
mw = MainWindow()
app.exec_()
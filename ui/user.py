class FORM_UI(QWidget):
    def __init__(self):
        super(FORM_UI, self).__init__()

        if os.path.exists("user.ui"):
            uic.loadUi("user.ui", self)
        else:
            print("File 'user.ui' tidak dapat ditemukan.")

app = QApplication(sys.argv)
window = FORM_UI()
window.show()
app.exec()
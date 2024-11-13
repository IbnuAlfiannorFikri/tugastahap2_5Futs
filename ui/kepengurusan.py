class FORM_UI(QWidget):
    def __init__(self):
        super(FORM_UI, self).__init__()

        if os.path.exists("kepengurusan.ui"):
            uic.loadUi("kepengurusan.ui", self)
        else:
            print("File 'kepengurusan.ui' tidak dapat ditemukan.")

app = QApplication(sys.argv)
window = FORM_UI()
window.show()
app.exec()
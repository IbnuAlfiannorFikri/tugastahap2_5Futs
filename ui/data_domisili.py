class FORM_UI(QWidget):
    def __init__(self):
        super(FORM_UI, self).__init__()

        if os.path.exists("data_domisili.ui"):
            uic.loadUi("data_domisili.ui", self)
        else:
            print("File 'data_domisili.ui' tidak dapat ditemukan.")

app = QApplication(sys.argv)
window = FORM_UI()
window.show()
app.exec()
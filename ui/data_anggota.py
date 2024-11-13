class FORM_UI(QWidget):
    def __init__(self):
        super(FORM_UI, self).__init__()

        if os.path.exists("data_anggota.ui"):
            uic.loadUi("data_anggota.ui", self)
        else:
            print("File 'data_anggota.ui' tidak dapat ditemukan.")

app = QApplication(sys.argv)
window = FORM_UI()
window.show()
app.exec()
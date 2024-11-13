class FORM_UI(QWidget):
    def __init__(self):
        super(FORM_UI, self).__init__()

        if os.path.exists("profil_partai.ui"):
            uic.loadUi("profil_partai.ui", self)
        else:
            print("File 'profil_partai.ui' tidak dapat ditemukan.")

app = QApplication(sys.argv)
window = FORM_UI()
window.show()
app.exec()
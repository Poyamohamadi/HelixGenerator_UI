import sys
from design import Ui_Root
from PyQt5.QtWidgets import QWidget, QApplication, QFileDialog, QMessageBox

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Root()
        self.ui.setupUi(self)
        self.uiSet()
        self.dxf_file = ''

    def uiSet(self):
        self.ui.btn_input.clicked.connect(self.openFile)
        self.ui.btn_export.setDisabled(1)
        self.ui.btn_export.clicked.connect(self.saveFile)
        self.ui.progressBar.setValue(0)

        self.ui.start_length_value.valueChanged.connect(self.evn)
        self.ui.end_length_value.valueChanged.connect(self.evn)
        self.ui.total_length_value.valueChanged.connect(self.evn)

        self.show()
    
    def evn(self):
        helix_lenght = self.ui.total_length_value.value() - (self.ui.start_length_value.value() + self.ui.end_length_value.value())
        self.ui.Helix_label.setText(f"{helix_lenght:.1f}mm")
    
    def openFile(self):
        Qf = QFileDialog().getOpenFileUrl(filter="*.dxf")[0].path()
        if len(Qf):
            self.dxf_file = Qf
        if len(self.dxf_file):
            self.ui.btn_export.setDisabled(0)
        
    def saveFile(self):
        import time
        time.sleep(1)
        self.ui.progressBar.setValue(10)
        time.sleep(1)
        self.ui.progressBar.setValue(30)
        time.sleep(1)
        self.ui.progressBar.setValue(50)
        time.sleep(2)
        self.ui.progressBar.setValue(100)

        Qf = QFileDialog()
        save = Qf.getSaveFileUrl(filter="*.tap")[0].path()[1:]
            
        # code = []
        # for str in gcode:
        #     code.append(str + "\n")
        # with open(os.path.abspath(save),"w") as tap:
        #     tap.writelines(code)
        
        self.ui.progressBar.setValue(0)

app = QApplication(sys.argv)
main = MyApp()
sys.exit(app.exec_())

# pyinstaller --noconsole --add-data="images;images" main.py

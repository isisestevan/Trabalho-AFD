import sys

from PyQt5.QtWidgets import QWidget, QMainWindow, QApplication
from Model.AFD import AFD
from Util.UtilAFD import UtilAFD
from View.ui.AfdUI import Ui_MainWindow


class MainWindow(QMainWindow, Ui_MainWindow):

    def __init__(self, parent=None):
        super().__init__(parent)
        super().setupUi(self)
        self.afd = AFD()

        self.testButton.clicked.connect(self.main)

    def set_attributes_afd(self):
        attributes = dict()
        attributes["qtdEstados"] = int(self.qtd_estados.text())
        attributes["qtdAlfabeto"] = int(self.qtd_alfabeto.text())
        attributes["qtdTransicoes"] = int(self.qtd_funcoes.text())
        attributes["qtdEstadosIniciais"] = int(self.qtd_estados_in.text())
        attributes["qtdEstadosFinais"] = int(self.qtd_estados_fin.text())
        attributes["estados"] = self.estados.text()
        attributes["alfabeto"] = self.alfabeto.text()
        attributes["estadosIniciais"] = self.estados_in.text()
        attributes["estadosFinais"] = self.estados_fin.text()
        attributes["transicoes"] = self.transicoes.toPlainText().strip()
        attributes["entrada"] = self.entrada.text().strip()
        self.afd.set_attributes(attributes)

    def main(self):
        self.set_attributes_afd()

        print()

        if UtilAFD.checar_valores(self.afd):

          transicoes: dict = UtilAFD.get_transicoes_dict(self.afd)


          if (transicoes):
            reconhece = UtilAFD.verifica_entrada(self.afd, transicoes)
            
            if reconhece: 
              self.resultado.setText("Reconhece!")
              self.resultado.setStyleSheet('color:green;')

            else:
              self.resultado.setText("Não reconhece")
              self.resultado.setStyleSheet('color:red;')


        


if __name__ == "__main__":
    app = QApplication(sys.argv)
    main = MainWindow()
    main.show()
    sys.exit(app.exec_())

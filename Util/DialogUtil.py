from PyQt5.QtWidgets import QMessageBox

class DialogUtil:

    @staticmethod
    def show_warning(message: str='Atenção'):
        QMessageBox.warning(None, "Atenção", message)

    @staticmethod
    def show_error(message: str='Ocorreu um erro'):
        QMessageBox.critical(None, "Erro", message)
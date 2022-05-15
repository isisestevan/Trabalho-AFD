class AFD:
    def __init__(self, attributes=None):
        self.qtdEstados = ''
        self.qtdAlfabeto = ''
        self.qtdTransicoes = ''
        self.qtdEstadosIniciais = ''
        self.qtdEstadosFinais = ''
        self.estados = ''
        self.alfabeto = ''
        self.estadosIniciais = ''
        self.estadosFinais = ''
        self.transicoes = ''
        self.entrada = ''
        self.set_attributes(attributes)

    def set_attributes(self, attributes):
        if attributes is None:
            return

        keys = dict(attributes).keys()
        for key in keys:
            self.__setattr__(str(key), attributes[key])

    def get_attributes(self):
        return self.__dict__


from Model.AFD import AFD
from Util.DialogUtil import DialogUtil


class UtilAFD:
    pass

    @staticmethod
    def checar_valores(afd: AFD, estadoAtual="", estadoTransicao="", caractereAtual=""):
        if (not (afd.qtdEstados
                 and afd.qtdAlfabeto
                 and afd.qtdTransicoes
                 and afd.qtdEstadosIniciais
                 and afd.qtdEstadosFinais
                 and afd.estados
                 and afd.alfabeto
                 and afd.estadosIniciais
                 and afd.estadosFinais
                 and afd.estadosFinais
                 and afd.transicoes
                 and afd.entrada
                 )):
            DialogUtil.show_error(
                "Todos campos são obrigatórios")
            return False

        if len(afd.transicoes.splitlines()) != afd.qtdTransicoes:
            DialogUtil.show_warning(
                "Transições incompativeis com a quantidade informada")
            return False

        if len(afd.alfabeto.strip().split(" ")) != afd.qtdAlfabeto:
            DialogUtil.show_warning(
                "Alfabeto incompativel com a quantidade informada")
            return False

        if len(afd.estados.strip().split(" ")) != afd.qtdEstados:
            DialogUtil.show_warning(
                "Estados incompativeis com a quantidade informada")
            return False

        if len(afd.estadosIniciais.strip().split(" ")) != afd.qtdEstadosIniciais:
            DialogUtil.show_warning(
                "Estados Iniciais incompativeis com a quantidade informada")
            return False

        if len(afd.estadosFinais.strip().split(" ")) != afd.qtdEstadosFinais:
            DialogUtil.show_warning(
                "Estados Finais incompativeis com a quantidade informada")
            return False

        if estadoAtual not in afd.estados:
            DialogUtil.show_warning(
                f"Estado: {estadoAtual} não existe nos estados: {afd.estados}")
            return False

        if estadoTransicao not in afd.estados:
            DialogUtil.show_warning(
                f"Estado: {estadoTransicao} não existe nos estados: {afd.estados}")
            return False

        if caractereAtual not in afd.alfabeto:
            DialogUtil.show_warning(
                f"Caractere: {caractereAtual} não existe no alfabeto: {afd.alfabeto}")
            return False

        return True

    @staticmethod
    def get_transicoes_dict(afd: AFD):
        transicoes = {}

        for i in range(afd.qtdTransicoes):
            listaQtds: list = afd.transicoes.splitlines()[i].split(" ")

            estadoAtual = listaQtds[0]
            estadoTransicao = listaQtds[1]
            caractere = listaQtds[2]

            if (UtilAFD.checar_valores(afd, estadoAtual, estadoTransicao, caractere)):
                if (transicoes.get(estadoAtual) is not None):
                    transicoes[estadoAtual].update(
                        {caractere: estadoTransicao})
                else:
                    aux = {
                        estadoAtual: {
                            caractere: estadoTransicao
                        }
                    }

                    transicoes.update(aux)
            else:
                return {}

        return transicoes

    def verifica_entrada(afd: AFD, transicoesDict: dict):
        estado = afd.estadosIniciais.split(" ")[0]

        i = 0
        while(i < len(afd.entrada)):
            letra = afd.entrada[i]
            if (transicoesDict.get(estado).get(letra) is not None):
                estado = transicoesDict.get(estado).get(letra)
                i += 1
            else:
                if (afd.entrada[i] not in afd.alfabeto):
                    estado = None
                i = len(afd.entrada)

        if (estado and estado in afd.estadosFinais):
            return True
        else:
            return False

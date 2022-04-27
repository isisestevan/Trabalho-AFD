import os

def getQuantidades(quantidade: int, frase: str):
  lista = []

  while len(lista) != quantidade:
    lista = input("Digite o " + frase + ": ").split(" ")

  return lista

quantidades = ""
while len(quantidades) != 5:
  quantidades = input("Digite respectivamente E Σ δ I F\n").replace(" ", "")

qtdEstados, qtdAlfabeto, qtdTransicoes, qtdEstadosIniciais, qtdEstadosFinais = [int(i) for i in list(quantidades)]

estados = getQuantidades(qtdEstados, "Estados")
alfabeto = getQuantidades(qtdAlfabeto, "Alfabeto")
estadosIniciais = getQuantidades(qtdEstadosIniciais, "Estados iniciais")
estadosFinais = getQuantidades(qtdEstadosFinais, "Estados finais")

def checarValores(estadoAtual, estadoTransicao, caractere):
    while estadoAtual not in estados:
      estadoAtual = input("Estado atual incorreto: ")
      
    while estadoTransicao not in estados:
      estadoTransicao = input("Estado transição incorreto: ")

    while caractere not in alfabeto:
      caractere = input("Caractere não existe no alfabeto: ")

def getTransicoes(qtdTransicoes: int):
  print("\nDigite Respectivamente: Estado atual - Estado de transicao - Caractere")

  transicoes = {}

  for i in range(qtdTransicoes):
    estadoAtual, estadoTransicao, caractere = input(str(i+1) + ": ").split(" ")

    checarValores(estadoAtual, estadoTransicao, caractere)

    if (transicoes.get(estadoAtual) is not None):
      transicoes[estadoAtual].update({caractere: estadoTransicao})
    else:
      aux = {
        estadoAtual: {
          caractere: estadoTransicao
        }
      }

      transicoes.update(aux)
  
  return transicoes

transicoes = getTransicoes(qtdTransicoes)

def verifica(entrada: str):
    estado = estadosIniciais[0]
    i = 0
    while(i<len(entrada)):
        letra = entrada[i]
        if (transicoes.get(estado).get(letra) is not None):
            estado  = transicoes.get(estado).get(letra)
            i += 1
        else:
            i = len(entrada)
            
    if (estado in estadosFinais):
        return True
    else:
        return False

def main():
  os.system("cls||clear")

  resp = -1
  while resp != 0:
    entrada = input("Entarada: ")
    result = verifica(entrada) 
    
    if result:
      printResult = "\033[92m RECONHECE \033[0m"
    else:
      printResult = "\033[91m NÃO RECONHECE \033[0m"

    print(f"{entrada} => {printResult}")

    resp = input("Digite 0 para sair")


main()
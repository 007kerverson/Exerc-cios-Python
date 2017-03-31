funcionarios = {}

def adicionarFuncionario(matricula, nome):
  funcionarios[matricula] = nome
  
  return
  
def buscarFuncionario(matricula):
  print(funcionarios.get(matricula))
  
  return
  
def exibirFuncionarios(funcionarios):
  print(funcionarios)
  
  return funcionarios
  
def main():
  while(True):
    print("A = Se deseja Adicionar um funcionario\n B = Se deseja Buscar um funcionario \n C = Se deseja Exibir um funcionario")
    opcao = str(input("Digite sua Opção:"))
    if opcao == "A" :
      matricula = int(input("Informe sua matrícula:"))
      nome = input("Informe seu nome:")
      adicionarFuncionario(matricula, nome)
    elif opcao == "B":
      matrícula = int(input("Informe sua matrícula:"))
      buscarFuncionario(matrícula)
    elif opcao == "C":
      exibirFuncionarios(funcionarios)
if __name__ =="builtins" : #Em uma plataforma diferente do "repl.it", seria --> __name__==__main__
  main()

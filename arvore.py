
#SISTEMA DE ARQUIVOS COM ÁRVORE.
class No:
    def __init__(self, nome, eh_diretorio=False):
        self.nome = nome
        self.eh_diretorio = eh_diretorio
        self.filhos = []  #Lista para subdiretórios ou arquivos.

    def adicionar_filho(self, filho):
        self.filhos.append(filho)

    def exibir(self, nivel=0):
        indentacao = " " * (nivel * 2)
        print(f"{indentacao}{self.nome}/" if self.eh_diretorio else f"{indentacao}{self.nome}")
        for filho in self.filhos:
            filho.exibir(nivel + 1)

#Cria o sistema de arquivos.
raiz = No("raiz", True)
casa = No("casa", True)
usuario = No("usuario", True)
documentos = No("documentos", True)
arquivo1 = No("arquivo1.txt")
arquivo2 = No("arquivo2.txt")
arquivo3 = No("relatorio.docx")

#Estrutura hierárquica (árvore).
raiz.adicionar_filho(casa)
casa.adicionar_filho(usuario)
usuario.adicionar_filho(documentos)
documentos.adicionar_filho(arquivo1)
documentos.adicionar_filho(arquivo2)
usuario.adicionar_filho(arquivo3)


#Exibindo o sistema de arquivos.
print("Estrutura do Sistema de Arquivos:")
raiz.exibir()

class No:
    def __init__(self, chave):
        self.chave = chave
        self.esquerda = None
        self.direita = None
        self.altura = 1

class ArvoreAVL:
    def __init__(self):
        self.raiz = None

    def altura(self, no):
        return no.altura if no else 0

    def balanceamento(self, no):
        return self.altura(no.esquerda) - self.altura(no.direita) if no else 0

    def atualiza_altura(self, no):
        if no:
            no.altura = 1 + max(self.altura(no.esquerda), self.altura(no.direita))

    def rotacao_direita(self, y):
        x = y.esquerda
        T2 = x.direita

        x.direita = y
        y.esquerda = T2

        self.atualiza_altura(y)
        self.atualiza_altura(x)

        return x

    def rotacao_esquerda(self, x):
        y = x.direita
        T2 = y.esquerda

        y.esquerda = x
        x.direita = T2

        self.atualiza_altura(x)
        self.atualiza_altura(y)

        return y

    def insere(self, raiz, chave):
        if raiz is None:
            return No(chave)

        if chave < raiz.chave:
            raiz.esquerda = self.insere(raiz.esquerda, chave)
        else:
            raiz.direita = self.insere(raiz.direita, chave)

        self.atualiza_altura(raiz)
        balanceamento = self.balanceamento(raiz)

        if balanceamento > 1:
            if chave < raiz.esquerda.chave:
                return self.rotacao_direita(raiz)
            else:
                raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
                return self.rotacao_direita(raiz)

        if balanceamento < -1:
            if chave > raiz.direita.chave:
                return self.rotacao_esquerda(raiz)
            else:
                raiz.direita = self.rotacao_direita(raiz.direita)
                return self.rotacao_esquerda(raiz)

        return raiz

    def insere_chave(self, chave):
        self.raiz = self.insere(self.raiz, chave)

    def busca(self, raiz, chave):
        if raiz is None:
            return False
        if chave == raiz.chave:
            return True
        elif chave < raiz.chave:
            return self.busca(raiz.esquerda, chave)
        else:
            return self.busca(raiz.direita, chave)

    def busca_chave(self, chave):
        return self.busca(self.raiz, chave)

    def minimo_valor(self, raiz):
        return self.minimo_valor(raiz.esquerda) if raiz and raiz.esquerda else raiz

    def remove(self, raiz, chave):
        if raiz is None:
            return raiz

        if chave < raiz.chave:
            raiz.esquerda = self.remove(raiz.esquerda, chave)
        elif chave > raiz.chave:
            raiz.direita = self.remove(raiz.direita, chave)
        else:
            if raiz.esquerda is None:
                return raiz.direita
            elif raiz.direita is None:
                return raiz.esquerda

            temp = self.minimo_valor(raiz.direita)
            raiz.chave = temp.chave
            raiz.direita = self.remove(raiz.direita, temp.chave)

        self.atualiza_altura(raiz)
        balanceamento = self.balanceamento(raiz)

        if balanceamento > 1:
            if self.balanceamento(raiz.esquerda) >= 0:
                return self.rotacao_direita(raiz)
            else:
                raiz.esquerda = self.rotacao_esquerda(raiz.esquerda)
                return self.rotacao_direita(raiz)

        if balanceamento < -1:
            if self.balanceamento(raiz.direita) <= 0:
                return self.rotacao_esquerda(raiz)
            else:
                raiz.direita = self.rotacao_direita(raiz.direita)
                return self.rotacao_esquerda(raiz)

        return raiz

    def remove_chave(self, chave):
        self.raiz = self.remove(self.raiz, chave)

    def imprime_arvore(self):
        self.inorder_traversal(self.raiz)

    def inorder_traversal(self, raiz):
        if raiz:
            self.inorder_traversal(raiz.esquerda)
            print(raiz.chave, end=' ')
            self.inorder_traversal(raiz.direita)

# Exemplo de uso:
avl_tree = ArvoreAVL()
avl_tree.insere_chave(10)
avl_tree.insere_chave(20)
avl_tree.insere_chave(30)
avl_tree.insere_chave(40)
avl_tree.insere_chave(50)

print("Árvore AVL após inserção:")
avl_tree.imprime_arvore()
print()

avl_tree.remove_chave(20)

print("Árvore AVL após exclusão:")
avl_tree.imprime_arvore()
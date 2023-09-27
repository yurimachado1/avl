# Árvore AVL em Python

Este é um exemplo de implementação de uma Árvore AVL em Python. A Árvore AVL é uma estrutura de dados de árvore binária balanceada que mantém um fator de equilíbrio em cada nó, garantindo que a altura da subárvore esquerda e direita de qualquer nó não difere mais do que 1.

## Funcionalidades

- Inserção de chaves na árvore.
- Exclusão de chaves na árvore.
- Busca de chaves na árvore.
- Impressão da árvore em ordem.

## Como usar

Você pode utilizar este código de exemplo para criar e manipular uma Árvore AVL em Python. Aqui está um exemplo de uso básico:

```python
# Importe a classe ArvoreAVL do arquivo avl.py

from avl import ArvoreAVL

# Crie uma instância da Árvore AVL

avl_tree = ArvoreAVL()

# Insira chaves na árvore

avl_tree.insere_chave(10)
avl_tree.insere_chave(20)
avl_tree.insere_chave(30)
avl_tree.insere_chave(40)
avl_tree.insere_chave(50)

# Imprima a árvore em ordem

print("Árvore AVL após inserção:")
avl_tree.imprime_arvore()
print()

# Remova uma chave da árvore

avl_tree.remove_chave(20)

# Imprima a árvore novamente após a remoção

print("Árvore AVL após exclusão:")
avl_tree.imprime_arvore()

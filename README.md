# Sistema de Biblioteca - PUCPR

Projeto final desenvolvido para a disciplina de Raciocínio Algorítmico do curso de Engenharia de Software da PUCPR. O sistema gerencia o acervo de livros, usuários, empréstimos e devoluções em Python.

## Pré-requisitos
- Python 3.x instalado na máquina.

## Como rodar
Execute o comando no terminal:
`python main.py`

## Funcionalidades
- Cadastro, listagem e pesquisa de livros do acervo.
- Cadastro e listagem de usuários.
- Sistema de empréstimos e devoluções com controle automático de multas.
- Geração de relatório: Ao encerrar o sistema, um relatório é salvo automaticamente em um arquivo `.txt`.

## Regras do Sistema
- Limite de 3 livros emprestados por usuário.
- Prazo de devolução: 14 dias.
- Multa por atraso: R$ 2,50 por dia.
- Teto de multa: R$ 50,00.

## Estrutura dos Arquivos
- `main.py`: Loop principal e menus.
- `livros.py`: Cadastro, listagem e pesquisa de livros.
- `usuarios.py`: Cadastro, listagem e pagamento de multas.
- `emprestimos.py`: Empréstimos, devoluções e listagens.
- `relatorios.py`: Geração e salvamento de relatórios.
- `dados.py`: Listas de estado do sistema em memória.
- `constantes.py`: Configurações de limites, prazos e valores.
- `auxiliares.py`: Funções utilitárias de formatação e limpeza.

## Desenvolvedores
- Anthony Gabriel Celli Marba
- Henrique Gnatkovski de Almeida
- Julia Moura Ruela
- Letícia Hellen Prata de Souza
- Sabrina Bernardi Ferreira
- Yasmin Luz de Araujo

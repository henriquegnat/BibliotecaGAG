# Sistema de Biblioteca - PUCPR

Projeto final desenvolvido para a disciplina de Raciocínio Algorítmico do curso de Engenharia de Software da PUCPR[cite: 10]. O sistema gerencia o acervo de livros, usuários, empréstimos e devoluções em Python[cite: 7].

## Pré-requisitos
- Python 3.x instalado na máquina[cite: 7].

## Como rodar
Execute o comando no terminal[cite: 7]:
`python main.py`

## Funcionalidades
- Cadastro, listagem e pesquisa de livros do acervo[cite: 7].
- Cadastro e listagem de usuários[cite: 7].
- Sistema de empréstimos e devoluções com controle automático de multas[cite: 7].
- Geração de relatório: Ao encerrar o sistema, um relatório é salvo automaticamente em um arquivo `.txt`[cite: 7, 10].

## Regras do Sistema
- Limite de 3 livros emprestados por usuário[cite: 7].
- Prazo de devolução: 14 dias[cite: 7].
- Multa por atraso: R$ 2,50 por dia[cite: 7].
- Teto de multa: R$ 50,00[cite: 7].

## Estrutura dos Arquivos
- `main.py`: Loop principal e menus[cite: 7].
- `livros.py`: Cadastro, listagem e pesquisa de livros[cite: 7].
- `usuarios.py`: Cadastro, listagem e pagamento de multas[cite: 7].
- `emprestimos.py`: Empréstimos, devoluções e listagens[cite: 7].
- `relatorios.py`: Geração e salvamento de relatórios[cite: 7].
- `dados.py`: Listas de estado do sistema em memória[cite: 7].
- `constantes.py`: Configurações de limites, prazos e valores[cite: 7].
- `auxiliares.py`: Funções utilitárias de formatação e limpeza[cite: 7].

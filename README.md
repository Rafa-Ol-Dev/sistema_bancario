
# Desafio de Projeto - Criando um sistema bancário com Python

Este projeto é parte do bootcamp da DIO **Potência Tech powered by iFood | Ciência de Dados** que me possibilitou aplicar os conhecimentos em programação Python e criar um sistema funcional que simule as operações bancárias.

O objetivo é simples, implementar três operações essenciais: depósito, saque e extrato.
O sistema foi desenvolvido para um banco que busca monetizar suas operações.

_Essa é a versão 1 do desafio._

## Regras usadas na implementação

### Depósito
- Deve ser possível depositar valores positivos para a conta bancária;
- A v1 do projeto trabalha apenas com 1 usuário, de modo que não foi preciso se preocupar em identificar o número da agência e conta bancária.
- Todos os depósitos devem ser armazenados em uma váriável e exibidos na operação de extrato.

### Saque
- O sistema deve permitir realizar três saques diários com limite máximo de R$500,00 por saque.
- Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo.
- Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

### Extrato
- Essa operação deve listar todos os depósitos e saques realizados na conta;
- No fim da listagem, deve ser exibido o saldo atual da conta;
- Os valores devem ser exibidos utilizando o formato R$ xxx.xx; exemplo:
    **1500.45 = R$1500.45**.

---

## Prints do programa em execução

### _Menu_

![Menu](./screenshots/menu.jpg)

### _Saque_

![Saque](./screenshots/saque_1.jpg)


![Saque](./screenshots/saque_2.jpg)


![Saque](./screenshots/saque_3.jpg)


![Saque](./screenshots/saque_4.jpg)

### _Depósito_

![Deposito](./screenshots/deposito_1.jpg)


![Deposito](./screenshots/deposito_2.jpg)

### _Extrato_

![Extrato](./screenshots/extrato.jpg)

### _Sair_

![Sair](./screenshots/sair.jpg)

---

💻 Feito por Rafael Oliveira, 2023.

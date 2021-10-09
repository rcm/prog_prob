---
author:
- Fichas
theme: Boadilla
title: Programação Probabilística
header-includes:
  - \hypersetup{colorlinks=true,urlcolor = blue, linkcolor=cyan,pdfborderstyle={/S/U/W 1}}
---


# Instruções
## Site
- Use o site [WebPPL](http://webppl.org) para resolver os seguintes problemas

## Ficha 1
- Experimente as várias distribuições possíveis e use a função *viz* para se familiarizar com o sistema.
- [Arrays](http://docs.webppl.org/en/master/functions/arrays.html)
- [viz](https://github.com/probmods/webppl-viz)
- [Distribuições](http://docs.webppl.org/en/master/distributions.html)

## Ficha 4
- [Inferência](http://docs.webppl.org/en/master/inference/index.html)

# Ficha 1
1. Crie uma lista com 10 valores aleatórios do tipo *verdadeiro* ou *falso*;
	1. Conte quantos dos valores são verdadeiros;
	1. Verifique se todos os valores são verdadeiros;
	1. Verifique se algum dos valores é verdadeiro;
1. Escreva uma função que lance 1000 vezes uma moeda ao ar, use a função **repeat**, e crie um histograma com as frequências;
1. Modifique a função anterior para receber a probabilidade de sair cara e experimente com vários casos possíveis;
1. Modifique a função anterior para lançar 5 moedas de cada vez e criar o histograma com o número de caras;
	1. Use a função **flip** para isso;
	1. Use outra distribuição que lhe pareça mais útil;
1. Crie um histograma correspondente ao lançamento de um dado;
1. Modifique o programa anterior para lançar mais do que um dado.

# RPGs e dados
## **X**d**Y**
X
 : número de dados rolado

Y
 : número de faces de cada dado

## Sistema Roll & Keep: **X**k**Y**
X
 : número de dados D10 *rolled*

Y
 : número de dados D10 *kept*

Exploding dice
 : cada 10 implica que esse dado é rolado novamente e se soma 10 ao total

## Sistema do *World of Darkness*
- Lançam-se **N** dados D10
- Contam-se os dados cujo valor é maior ou igual ao *target number* **TN**
- Cada **1** é um **fracasso** que subtrai ao número de **sucessos**
- O valor total pode ser negativo, neste caso, é um **Botch**

# Ficha 2
1. Escreva uma função que receba o número de dados e o número de faces de cada dado e imprima o histograma relativo a 10,000 lançamentos. Represente o histograma para os seguintes valores: 5d2; 2d5; 4d6; 2d100; 100d2;
1. Crie uma nova função onde os dados repetidos são removidos;
1. Crie uma função para o sistema *Roll & Keep*. Represente o histograma para 1k1; 3k1; 5k1; 7k2;
1. Crie uma função para o sistema *World of Darkness*. Represente o histograma do nº de sucessos para vários nºs de dados e *TN*;
1. Represente gráficamente o nº de sucessos para os vários **TN** usando um *heatmap* quando se lançam 10 dados;
1. Represente um *heatmap* com o nº de dados *vs* o  nº de sucessos para o **TN** de 9.

# Ficha 3
1. Assuma que 1% da população tem COVID. Dos que têm COVID, 70% tem um teste rápido positivo mas  10% das pessoas que não têm COVID tem um teste rápido positivo. Desenhe o modelo gráfico e imprima o histograma correspondente;
1. Assuma agora que existe o teste B (em oposição ao teste A referido acima) em que 90% das pessoas com COVID tem um teste positivo enquanto que só 1% das pessoas sem COVID tem um teste positivo. Assuma também que das pessoas que ligam para o Saúde24, 80% das pessoas fizeram o teste A e as restantes fizeram o teste B. Desenhe o modelo gráfico e imprima o histograma correspondente.

# Ficha 4
1. Calcule a probabilidade de ter COVID se tiver um teste positivo para a pergunta 1 da ficha anterior;
2. Se tiver um teste positivo para a pergunta 2 da ficha anterior, calcule:
	1. A probabilidade de ter COVID;
	1. A probabilidade de ter feito o teste A;
	1. A probabilidade de ter feito o teste A se tiver o teste positivo e tiver COVID;
3. Se tiver 3 moedas, uma normal com 50% de probabilidades de sair cara (N), uma com 70% de probabilidades de sair cara (H)  e outra com 70% de probabilidades de sair coroa (T), qual é a probabilidade de ter escolhido cada uma das moedas sabendo que:
	1. Lançou uma vez ao ar e saiu cara;
	1. Lançou a moeda duas vezes ao ar e saiu sempre cara;
	1. Lançou a moeda três vezes ao ar e saiu sempre cara;
	1. Lançou a moeda três vezes ao ar e saiu cara duas vezes;
	1. Como mudam as probabilidades das 3 alíneas anteriores caso a probabilidade de escolher a moeda N for de 60%?

# Ficha 5
4. Escreva uma função que sabendo que lançou X dados todos com o mesmo número de faces (2, 4, 6, 8, 10, 20 ou 100) e que a soma foi de S, qual é a probabilidade correspondente a cada tipo de dado?
1. Modifique a solução anterior para o caso de ter uma lista de lançamentos;
1. Escreva uma função que escolha aleatoriamente uma carta de um baralho;
1. Modifique o programa anterior para extrair várias cartas de um baralho sem reposição;
1. Crie um programa que permita calcular a probabilidade de cada uma das combinações do Blackjack.

# Ficha 6 --- Cenários
## Passaportes ilegais
- 1 em cada dez mil passageiros possuem um passaporte ilegal;
- São identificados corretamente 99 passaportes ilegais em cada 100;
- 1 em cada mil passaportes legais são identificados como ilegais.

## Loucura psicadélica
- São usadas drogas que colocam o paciente a dormir e provocam amnésia;
- O paciente é informado da experiência;
- Domingo, o paciente é posto a dormir com uma droga;
- É atirada uma moeda ao ar:
	- Se sair cara, ele é acordado e entrevistado só na segunda-feira
	- Se sair coroa, é acordado e entrevistado na segunda e terça-feira
- No final de cada entrevista, o paciente é drogado novamente
- Na quarta-feira, o paciente é acordado sem ser entrevistado

# Ficha 6
1. Apresente uma tabela com as probabilidades dos vários casos possíveis do cenário dos passaportes ilegais;
1. Sabendo que um passageiro foi preso, qual é a probabilidade de passaporte ser válido?
1. No cenário da loucura psicadélica, sabendo que o aluno conhece todo o procedimento e que é acordado num dado dia, se a pergunta que lhe fizerem for “qual é a probabilidade do lançamento da moeda ter dado coroa?” qual deverá ser a sua resposta?

# Ficha 7
## Craps
- Calcule a probabilidade de ganhar se for você a lançar os dados
- Calcule a probabilidade de ganhar dependendo do valor inicial que saiu nos dados

## Blackjack
- Faça um programa que seja capaz  de jogar Blackjack
- Deve ser decidir de decidir a ação mais conveniente em cada caso

## Badugi
- Faça uma função capaz de comparar duas mãos de [Badugi](https://en.wikipedia.org/wiki/Badugi)
- Faça uma função que receba as suas cartas e as cartas que sabe que já sairam e calcule a probabilidade de melhorar a sua mão dependendo do nº de cartas que trocar
- Faça uma função que, dadas as suas cartas e as cartas que já saíram, calcule a probabilidade da sua mão ser a melhor

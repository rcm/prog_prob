---
author:
- Fichas
theme: Boadilla
title: Programação Probabilística
header-includes:
  - \hypersetup{colorlinks=true,urlcolor = blue, linkcolor=cyan,pdfborderstyle={/S/U/W 1}}
  - \AtBeginDocument{\renewenvironment{Shaded} {\footnotesize} {}}
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
1. Escreva funções que lancem uma moeda ao ar *n* vezes e:
	1. Conte quantas vezes saiu cara;
	1. Verifique se todos os lançamentos foram coroa;
	1. Verifique se nem todos os lançamentos tiveram o mesmo resultado;
1. Escreva uma função que lance 1000 vezes uma moeda ao ar, use a função **repeat**, e crie um histograma com as frequências;
1. Modifique a função anterior para receber a probabilidade de sair cara e experimente com vários casos possíveis;
1. Modifique a função anterior para lançar 5 moedas de cada vez e criar o histograma com o número de caras;
	1. Use a função **flip** para isso;
	1. Use outra distribuição que lhe pareça mais útil;
1. Crie um histograma correspondente ao lançamento de um dado;
1. Modifique o programa anterior para lançar mais do que um dado;
1. Faça uma função para sortear uma carta;
1. Faça uma função que sorteie uma mão de *n* cartas.

# RPGs
## Sistema Roll & Keep
Trait
 : valor numérico que representa características

Skill
 : valor numérico que representa aptidões

## Sistema do *World of Darkness*
Atributos
 : valor numérico que representa características

Disciplines
 : valor numérico que representa aptidões

# RPGs e dados
## **X**d**Y**
X
 : número de dados rolado

Y
 : número de faces de cada dado

- Somam-se os valores dos dados

## Sistema Roll & Keep: **X**k**Y**
X
 : número de dados D10 *rolled*.
 Corresponde a **Trait+Skill**

Y
 : número de dados D10 *kept*.
 Corresponde a **Trait**

Exploding dice
 : cada 10 implica que esse dado é rolado novamente e se soma 10 ao total

- Somam-se os **Y** valores mais altos

## Sistema do *WoD*
- Lançam-se **Atributo+Discipline** dados D10
- Contam-se os dados cujo valor é maior ou igual ao *target number* **TN**
- Cada **1** é um **fracasso** que subtrai ao número de **sucessos**
- O valor total pode ser negativo, neste caso, é um **Botch**

# RPGs: Contested Rolls
## Roll & Keep
- Quem rolar o valor maior é vencedor

## WoD
- Cada oponente lança os dados *vs* um **TN**
- Quem tiver mais sucessos ganha
- O venceder pode ter que ganhar por uma certa margem

# Ficha 2
1. Escreva uma função que receba o número de dados e o número de faces de cada dado e imprima o histograma relativo a 10,000 lançamentos. Represente o histograma para os seguintes valores: 5d2; 2d5; 4d6; 2d100; 100d2;
1. Crie uma nova função onde os dados repetidos são removidos;
1. Crie uma função para o sistema *Roll & Keep*. Represente o histograma para 1k1; 3k1; 5k1; 7k2; 9k4
1. Crie uma função para o sistema *WoD*. Represente o histograma do nº de sucessos para vários nºs de dados e *TN*;
1. Represente gráficamente o nº de sucessos para os vários **TN** usando um *heatmap* quando se lançam 10 dados;
1. Represente um *heatmap* com o nº de dados *vs* o  nº de sucessos para o **TN** de 9;
1. Represente graficamente *contested rolls* de *Roll & Keep*; veja o impacto dos *Traits* e *Skills*;
1. Represente graficamente *contested rolls* de *WoD*; veja o impacto no nº de dados.

# Ficha 3
1. Assuma que 1% da população tem COVID. Dos que têm COVID, 70% tem um teste rápido positivo mas  10% das pessoas que não têm COVID tem um teste rápido positivo. Imprima o histograma  correspondente aos positivos;
2. Assuma agora que existe o teste B (em oposição ao teste A referido acima) em que 90% das pessoas com COVID tem um teste positivo enquanto que só 1% das pessoas sem COVID tem um teste positivo. Assuma também que das pessoas que ligam para o Saúde24, 80% das pessoas fizeram o teste A e as restantes fizeram o teste B. Imprima o histograma correspondente aos positivos.
3. Calcule p(COVID|positivo) para a pergunta 1 da ficha 3;
4. Se tiver um teste positivo para a pergunta 2 da ficha 3, calcule:
	1. A probabilidade de ter COVID;
	1. A probabilidade de ter feito o teste A;
	1. A probabilidade de ter feito o teste A com teste positivo e COVID;

# Ficha 4
1. Crie uma função ```sondagens(tamanho)``` que  gere sondagens baseada nas probabilidades dadas abaixo
~~~{.javascript}
var perc = {"ps":36.34,"psd":27.76,"cdu":6.33,"cds":4.22, "be":9.52,
  "pan":3.32,"chega":1.29,"il":1.29, "livre":1.09, "indecisos":8.84}
~~~
2. Utilizando os resultados da sondagem, crie um modelo para as probabilidades de um eleitor votar em cada partido
3. Use o ```viz.marginals``` para mostrar o resultado gráficamente
4. Use o estimador do High Density Interval para estimar o intervalo da probabilidade para cada partido

# Sugestões para a ficha 4
- Lembre-se que a distribuição multinomial recebe uma lista de probabilidades cuja soma é um
- Se quiser inspecionar quais são os métodos de um objeto use a função ```Object.getOwnPropertyNames(objeto)```
- O WebPPL parece utilizar a biblioteca ```Lodash``` que contém muitas funções úteis que pode consultar [aqui](https://lodash.com/docs)
- Eis algumas funções que podem ser úteis:
	- ```_.keys```
	- ```_.values```
	- ```_.toPairs```
	- ```_.fromPairs```
	- ```_.zip```
	- ```_.unzip```

# Exemplo
~~~{.javascript}
var prop = {"ps":36.34,"psd":27.76,"cdu":6.33,"cds":4.22, "be":9.52,
  "pan":3.32,"chega":1.29,"il":1.29, "livre":1.09, "indecisos":8.84}
var pares = _.toPairs(prop)
print(pares)
var tuplo = _.unzip(pares)
var partidos = tuplo[0]
var percentagens = tuplo[1]
print(partidos)
print(percentagens)
var dic = _.fromPairs(_.zip("partidos percentagens".split(" "), tuplo))
print(dic)
print(dic.partidos)
print(dic.percentagens)
~~~

# Ficha 5
1. Estime a probabilidade da moeda sair cara se tiver uma lista de observações;
1. E se tiver uma contagem **caras**/**lançamentos**?
1. Se tiver 3 moedas, uma normal com 50% de probabilidades de sair cara (N), uma com 70% de probabilidades de sair cara (H)  e outra com 70% de probabilidades de sair coroa (T), e sabendo à partida que pode ter escolhido qualquer dessas moedas, qual é a probabilidade de ter escolhido cada uma das moedas sabendo que:
	1. Lançou uma vez ao ar e saiu cara;
	1. Lançou a moeda três vezes ao ar e saiu sempre cara;
	1. Lançou a moeda três vezes ao ar e saiu cara duas vezes;
	1. Como mudam as probabilidades das 3 alíneas anteriores caso a probabilidade de escolher a moeda N for de 60%?
1. Escreva uma função que sabendo que lançou X dados todos com o mesmo número de faces (2, 4, 6, 8, 10, 20 ou 100) e que a soma foi de S, qual é a probabilidade correspondente a cada tipo de dado?
1. Modifique a solução anterior para o caso de ter uma lista de lançamentos;

# Ficha 6
- Construa um modelo que receba um texto e aprenda qual é a próxima palavra baseada nas *k* palavras anteriores

# Ficha 7 --- Cenários
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

# Ficha 8
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

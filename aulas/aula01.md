~~~~
var f = function() {
  return 2
}

var quad = function(x) {
  return prod(x , x)
}

var prod = function(x, y) {
  console.log("Quero multiolicar", x, "por", y)
  return x * y
}

var moeda = function() {
  return flip(0.6)
}

var make_coin = function(prob) {
  return function() {
    return flip(prob)
  }
}

var moeda1 = make_coin(0.7)
var moeda2 = make_coin(0.4)
var moeda3 = make_coin(0.3)

var make_crazy_toss = function(C1, C2) {
  if(flip()) {
    return C1()
  } else {
    return C2()
  }
}

var crazy_toss = function() {return make_crazy_toss(moeda1, moeda2)}

viz.table(Infer(crazy_toss))
~~~~

~~~~
// predicado que só devolve verdadeiro se o valor estiver entre 2 e 7
var pred = function(x) { return x >= 2 && x <= 7}
// Função identidade
var id = function(x) {return x}
filter(pred, mapN(id, 100))
~~~~

~~~~
// Função identidade
var id = function(x) {return x}
// Função sucessor
var succ = function(x) {return x + 1}

// Predicado que verifica se um número é par
var par = function(x) {
  return x % 2 == 0
}

// Dá todos os números pares até 100
filter(par, mapN(succ, 100))
~~~~

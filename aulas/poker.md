~~~
var values = "23456789TJQKA"
var suits = "SDCH"

var cards = map2(function(x, y) {x + y}, repeat(4, function(){values}).join(''), repeat(13, function() {suits}).join(''))
 
var valor = function(carta) {
   var valores = {2 : 2, 3 : 3, 4 : 4, 5 : 5, 6 : 6, 7 : 7, 8 : 8, 9 :
9, T : 10, J : 11, Q : 12, K : 13, A : 14}
   var val = valores[carta[0]]
   val
}

var naipe = function(carta) {
   return carta[1]
}

var agrupar_por = function(fun, cards) {
   var maior = function(x, y) {
     if(x.length == y.length)
       return valor(x[0]) > valor(y[0])
     return x.length > y.length
   }
   var length = function(x) {x.length}
   var gs = groupBy(function(x, y) { fun(x) == fun(y)}, cards)
   var gos = map(function(g) {sort(g, gt, valor)}, gs)
   sort(gos, maior)
}

var par = function(cartas) {
   var vs = agrupar_por(valor, cartas)
   return vs.length == 4
}

var dois_pares = function(cartas) {
   var vs = agrupar_por(valor, cartas)
   return vs.length == 3 && all(function(x) {x.length < 3}, vs)
}

var trio = function(cartas) {
   var vs = agrupar_por(valor, cartas)

   return vs.length == 3 && all(function(x) {x.length == 1 || x.length
== 3}, vs)
}

var seguidos = function(os) {
   _.isEqual(os, _.range(os[0], os[0] + os.length))
}

var sequencia = function(cartas) {
   var os = sort(cartas, lt, valor)
   var vs = map(valor, os)
   if(vs[0] == 2 && vs[4] == 14) {
     return seguidos(vs.slice(0,4))
   }
   return seguidos(vs)
}

var straight = function(cartas) {
   var vs = agrupar_por(naipe, cartas)
   return sequencia(cartas) && vs.length > 1
}

var flush = function(cartas) {
   var vs = agrupar_por(naipe, cartas)
   return vs.length == 1 && ! sequencia(cartas)
}

var straight_flush = function(cartas) {
   var vs = agrupar_por(naipe, cartas)
   return sequencia(cartas) && vs.length == 1
}

var full_house = function(cartas) {
   var vs = agrupar_por(valor, cartas)

   return vs.length == 2 && all(function(x) {x.length == 2 || x.length
== 3}, vs)
}

var four_of_a_kind = function(cartas) {
   var vs = agrupar_por(valor, cartas)

   return vs.length == 2 && all(function(x) {x.length == 1 || x.length
== 4}, vs)
}

var no_hand = function(cartas) {
   var vs = agrupar_por(valor, cartas)
   var ns = agrupar_por(naipe, cartas)
   return vs.length == 5 && ns.length > 1 && !sequencia(cartas)
}

var combinacao = function(cartas) {
   var combinacoes = [no_hand, par, dois_pares, trio, straight, flush,
full_house, four_of_a_kind, straight_flush]

   map(function(p) {p[0]}, filter(function(p) {p[1]},
mapIndexed(function(i, f) {
     [i, f(cartas)]
   }, combinacoes)))
}
//print(combinacao("KS JS 9H QS TS".split(/\s+/)))
var m1 = agrupar_por(valor, "QS KH JS AD 5D".split(/\s+/))
var m2 = agrupar_por(valor, "KS AS JD QD TS".split(/\s+/))

var dropWhile = function(pred, ls) {
  if(ls.length == 0) return []
  if(pred(_.first(ls)))
    return dropWhile(pred, ls.splice(1))
  return ls
}
var deitar_fora = function(l) {
  var A = l[0]
  var B = l[1]
  valor(A[0]) == valor(B[0])
}
dropWhile(deitar_fora, zip(m1, m2))
print(m1)
print(m2)
zip(m1, m2)
~~~

# Estimação do intervalo de maior densidade

~~~~
var prob = function(dist, low, up) {
  expectation(dist, function(x) { low < x && x < up })
}
var intervalo = function(dist, A, B, P, delta) {  
  if (prob(dist, A, B) < P) return [A,B]
  var PA = prob(dist, A + delta, B)
  var PB = prob(dist, A, B - delta)
  return PA > PB ? intervalo(dist, A + delta, B, P, delta) : intervalo(dist, A, B - delta, P, delta)
}

var dist = Infer(function(){gaussian(0,1)})
var I = intervalo(dist, -3, 3, 0.95, 0.01)
I
~~~~

# Geração de observações segundo um modelo

~~~~
var gerar_obs = function() {
  var modelo = function() {
    var covid = flip(0.01)
    var A = flip(0.8)
    var pA = covid ? flip(0.7) : flip(0.2)
    var pB = covid ? flip(0.9) : flip(0.05)
    var positivo = A ? pA : pB
    return {covid, teste : A ? "A" : "B", positivo}
  }
  var obs = repeat(5000, modelo)
  var same = function(o1, o2) {
    o1.covid == o2.covid && o1.teste == o2.teste && o1.positivo == o2.positivo
  }
  var agrupado = groupBy(same, obs)
  var tabela = map(function(l) {extend(l[0], {count : l.length})}, agrupado)
  tabela
}

var tabela = gerar_obs()

var count_filter = function(pred, tabela) {
  sum(map(function(o){o.count}, filter(pred, tabela)))
}

viz.table(tabela)

count_filter(function(o) {o.covid}, tabela)
~~~~

# Estimar os intervalos de maior densidade das margens

~~~
var estimate_margin = function(distribution, margin) {
  var dist = marginalize(distribution, margin)
  var prob = function(low, up) {
    expectation(dist, function(x) { low < x && x < up })
  }
  var intervalo = function(dist, A, B, P, delta) {  
    if (prob(A, B) < P) return [A,B]
    var PA = prob(A + delta, B)
    var PB = prob(A, B - delta)
    return PA > PB ? intervalo(dist, A + delta, B, P, delta) : intervalo(dist, A, B - delta, P, delta)
  }

  var interval = intervalo(dist, 0, 1, 0.95, 0.005)
  return {margin, interval}
}
~~~

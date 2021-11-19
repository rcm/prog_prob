~~~
var modeloInicial = function() {
  var covid = flip(0.01)
  var A = flip(0.8)
  var posA = covid ? flip(0.7) : flip(0.1)
  var posB = covid ? flip(0.9) : flip(0.01)
  var pos = A ? posA : posB
  var teste = A ? "A" : "B"
  return {covid, teste, pos}
}
var num_obs = 1000
var tabela = repeat(num_obs, modeloInicial)

var same = function(x, y) {
  x.covid == y.covid && x.teste == y.teste && x.pos == y.pos
}

var agrupados = groupBy(same, tabela)

var obs = map(function(x) {extend(x[0], {count: x.length})}, agrupados)

viz.table(obs)

//print(obs)

var modelo = function() {
  
}
~~~

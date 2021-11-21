~~~~
var modeloInicial = function() {
  var covid = flip(0.01)
  var A = flip(0.8)
  var posA = covid ? flip(0.7) : flip(0.1)
  var posB = covid ? flip(0.9) : flip(0.01)
  var pos = A ? posA : posB
  var teste = A ? "A" : "B"
  return {covid, teste, pos}
}
var num_obs = 25000
var tabela = repeat(num_obs, modeloInicial)

var same = function(x, y) {
  x.covid == y.covid && x.teste == y.teste && x.pos == y.pos
}

var agrupados = groupBy(same, tabela)

var obs = map(function(x) {extend(x[0], {count: x.length})}, agrupados)

viz.table(obs)

//print(obs)

var estimarProb = function(obs, todos, filtro) { 
  var linhas_todos = filter(todos, obs)
  var linhas_filtradas = filter(filtro, linhas_todos)
  var ctodos = sum(map(function(x) {x.count}, linhas_todos))
  var cfiltradas = sum(map(function(x) {x.count}, linhas_filtradas))
  var sucessos = cfiltradas
  var fracassos = ctodos - sucessos
  var prob = beta(sucessos + 1, fracassos + 1)
  
  observe(Binomial({p : prob, n: ctodos}), cfiltradas)
  
  return prob
}

var modelo = function() {
  var pCOVID = estimarProb(obs, function(x) {true}, function(x) {x.covid})
  var pA = estimarProb(obs, function(x) {true}, function(x) {x.teste == "A"})
  var pposAC = estimarProb(obs, function(x) {x.teste == "A" && x.covid}, function(x) {x.pos})
  var pposAnC = estimarProb(obs, function(x) {x.teste == "A" && !x.covid}, function(x) {x.pos})
  var pposCB = estimarProb(obs, function(x) {x.teste == "B" && x.covid}, function(x) {x.pos})
  var pposBnC = estimarProb(obs, function(x) {x.teste == "B" && !x.covid}, function(x) {x.pos})
  
  return {pCOVID, pA, pposAC, pposAnC, pposCB, pposBnC}
}

var estimar_intervalo = function(dist, margem, low, high) {
  expectation(marginalize(dist, margem), function(p) {low < p && p < high})
}

var HDI = function(dist, margem, low, high, delta) {
  var p = estimar_intervalo(dist, margem, low, high)
  if (p <= 0.95) return [low, high]
  var A  = estimar_intervalo(dist, margem, low + delta, high)
  var B  = estimar_intervalo(dist, margem, low, high - delta)
  return A > B ? HDI(dist, margem, low + delta, high, delta) : HDI(dist, margem, low, high - delta, delta)
}

var print_intervals = function(dist, margens) {
  map(function(m) {
    print(m + ": " + HDI(dist, m, 0, 1, 0.005))
  }, margens)
  
}
var dist = Infer(modelo)
viz.marginals(dist)

var dummy = print_intervals(dist, ["pCOVID", "pA", "pposAC", "pposAnC", "pposCB", "pposBnC"])
~~~~


var random_transition_state = function(transition) {
  return function(S) {
    var linha = transition[S]
    categorical({ps : _.values(linha), vs: _.keys(linha)})
  }
}
var random_state = function(line) {
  return function() {
    categorical({ps : _.values(line), vs: _.keys(line)})
  }
}

var hmm = function(num, inicial, transicao, emissao) {
  var prox_estado = random_transition_state(transicao)
  var prox_emissao = random_transition_state(emissao)
  var estado_inicial = random_state(inicial)
  var redux = function(i, acc) {
    var S = _.last(acc)
    var S1 = prox_estado(S)
    return acc.concat([S1])
  }

  var internos = reduce(redux, [estado_inicial()], _.range(num))
  var emitidos = map(prox_emissao, internos)
  return  {emitidos, internos}
}

var modelo = function(observados) {
  return function() {
    var transicao = {
      sol : {sol: 0.6, chuva: 0.1, nublado : 0.3},
      nublado: {sol: 0.6, chuva: 0.1, nublado : 0.3},
      chuva: {sol: 0.2, chuva: 0.5, nublado : 0.3},
    }

    var emissao = {
      sol : {ler: 0.2, passear: 0.6, cinema: 0.2},
      nublado: {ler: 0.2, passear: 0.3, cinema: 0.5},
      chuva: {ler: 0.4, passear: 0.2, cinema: 0.4},
    }

    var inicial = {sol: 0.5, chuva: 0.2, nublado : 0.3}
    var res = hmm(observados.length - 1, inicial, transicao, emissao)
    map2(function(o, e) {
      condition(o == e)
    }, observados, res.emitidos)
    res
  }
}


var opts = {method : "MCMC", samples : 100}
//viz.table(Infer(opts, modelo("ler ler cinema passear passear".split(/\s+/))))


var random_probs = function(estados) {
  _.fromPairs(
    map2(function(x, y) {[x,y]}, estados,
         _.values(dirichlet(ones([estados.length, 1])).data)))
}

var random_transmissions = function(internos, externos) {
  _.fromPairs(
    map2(function(x, y) {[x,y]}, internos,
                   repeat(internos.length, function(){random_probs(externos)})))
}

var deduzir = function() {
  var obs = ["ler", "passear", "passear"]
  var inicial = {sol : 0.7, chuva : 0.3}
  var trans = {sol: {sol: 0.7, chuva: 0.3}, chuva: {chuva : 0.6, sol: 0.4}}
  //var emis = {sol : {ler : 0.3, passear : 0.7}, chuva : {ler: 0.7, passear : 0.3}}
  var emis = random_transmissions("sol chuva".split(" "), "ler passear".split(" "))
  var res = hmm(2, inicial, trans, emis)
  map2(function(o, e) {
    condition(o == e)
  }, obs, res.emitidos)
  return emis
}

viz.table(Infer(deduzir))


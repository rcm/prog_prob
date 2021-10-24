# Exemplo da utilização de observe

~~~~
viz(Infer(function() {
   var prob = uniform(0, 1)
   observe(Binomial({p : prob, n : 10}), 4)
   prob
}))
~~~~

# Exemplos de utilização de factor

~~~~
var model =  function(fun) {
     return function() {
       var x = uniform(0, 10)
       factor(fun(x))
       return x
     }
}

var parabola = function(x) {25 - Math.pow(x - 5, 2)}
var doispicos = function(x) {
   -(Math.pow(x, 4) / 4 - 6*Math.pow(x, 3) + 99 * Math.pow(x, 2) / 2 -
162 * x)
}

var mostrar = function(funcao) {
   viz.line(mapN(function(x){x},11), mapN(funcao,11))
   viz(Infer({method: "MCMC", samples: 100000}, model(funcao)))
}

var nada = map(mostrar, [parabola, doispicos])
~~~~

# Exemplo de interpolação quadrática

~~~~
var modelo_quad = function(tab) {
   var distrib = function() {
     uniform(-1,1)
   }
   return function() {
     var a = distrib()
     var b = distrib()
     var c = distrib()

     var polinomio = function(x) {
         return a * x * x + b * x + c
     }

     map(function(par) {
       var x = par[0]
       var y = par[1]
       var erro = Math.abs(y - polinomio(x))
       factor(-erro)
     }, tab)
     return polinomio(10)
   }
}

var tab = [[1,3], [3, 8], [2,  4], [7, 52]]
var tab = [[1,3], [3, 7], [2,  5], [7, 15], [9,19]]
viz(Infer({method: "MCMC", samples: 100000}, modelo_quad(tab)))
~~~~

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 08:27:28 2019

@author: Labmirp
"""
sqn=('GGCACTGAA')
estados = ('H', 'L')
probInicio = {'H': 0.5, 'L': 0.5}
probTrans = {'H' : {'H': 0.5, 'L': 0.5}, 'L' : {'H': 0.4, 'L': 0.6}}
probEmision = {'H' : {'A': 0.2, 'C': 0.3, 'G': 0.3, 'T':0.2},   
             'L' : {'A': 0.3, 'C': 0.2, 'G': 0.2, 'T':0.3}}

if len(sqn)!=0:
    res = [{}]
    # Probabilidades de Inicio
    for e in estados:
       probabilidad=probInicio[e] * probEmision[e][sqn[0]] 
       estadoPrevio=None
       res[0][e] = {"prob":probabilidad , "prev": estadoPrevio}
    # Probabilidades Después del Inicio
    for i in range(1, len(sqn)):
       res.append({})
       for e in estados:
          
           ProbEstadoH=res[i-1][estados[0]]["prob"]*probTrans[estados[0]][e]
           ProbEstadoL=res[i-1][estados[1]]["prob"]*probTrans[estados[1]][e]
           
           if ProbEstadoH>ProbEstadoL:
               maxProbTrans=ProbEstadoH
               prev_e='H'
           else:
               maxProbTrans=ProbEstadoL
               prev_e='L'
               
           prob = maxProbTrans * probEmision[e][sqn[i]]
           res[i][e] = {"prob": prob, "prev": prev_e}
    # Encontrar Máxima Probabilidad
    maxProb=0
    for e in estados:
        current_p=res[-1][e]["prob"]
        if current_p>maxProb:
            prev_e=e
            maxProb=current_p;
    # Encontrar la Ruta        
    out=[]
    for i in range(len(res) - 2, -1, -1):
        out.insert(0, res[i + 1][prev_e]["prev"])
        previous = res[i + 1][prev_e]["prev"]

    print('La ruta más probable es: ')
    for o in out:
        print(o+" ",end="")
    print("")    
    print('Con una probabilidad de: '+str(maxProb))       
    
    

       
else:
    print('La secuencia eeá vacía')
                    

# -*- coding: utf-8 -*-
"""
Created on Mon Oct 21 14:20:09 2019

@author: Labmirp
"""

sqn=('GGCA')
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
       res[0][e] = {"prob":probabilidad}
    # Probabilidades Después del Inicio
    for i in range(1, len(sqn)):
       res.append({})
       for e in estados:
           ProbEstadoH=res[i-1][estados[0]]["prob"]*probTrans[estados[0]][e]
           ProbEstadoL=res[i-1][estados[1]]["prob"]*probTrans[estados[1]][e]
           prob=probEmision[e][sqn[i]]*(ProbEstadoH+ProbEstadoL)
           res[i][e] = {"prob": prob}
    # Encontrar la probabilidad de que la secuencia haya sido generada por los estados
    ProbSum=0
    for e in estados:
        ProbSum+= res[-1][e]['prob']
    
    print('La probabildidad que la secuencia "'+sqn+'" haya sido generada por el modelo HMM es de: '+str(ProbSum))    

else:
    print('La secuencia está vacía')
                    

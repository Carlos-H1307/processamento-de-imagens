# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 04:22:02 2023

@author: aluno
"""
import numpy
import math
import matplotlib.pyplot as plt


def equalizado():
    histograma1 = numpy.zeros( 256 )

    for i in range( 256 ):
        histograma1[i] = i/255
        
    soma = 0
    for i in range( 256):
        soma += histograma1[i] 
        
    for i in range(256):
        histograma1[i] /= soma
        
    return histograma1
  
    

    
def modulo():
    histogramaModulo = numpy.zeros( 256 )

    for i in range( 256 ):
        if i < 128:
            histogramaModulo[128 - i] =  (i % 128) / 128
        else:
            histogramaModulo[i] =  (i % 128) / 128
            
    soma = 0
    for i in range( 256):
        soma += histogramaModulo[i] 
        
    for i in range(256):
        histogramaModulo[i] /= soma   
        
    return histogramaModulo



def invertido():
    histograma = numpy.zeros( 256 )
    
    for i in range( 256 ):
        histograma[ 255 - i ] = i/256
        
    soma = 0
    for i in range( 256):
        soma += histograma[i] 
        
    #for i in range(256):
    #    histograma[i] /= soma    
    
    pixel = 256 * [0]
    for i in range( 256 ):
        pixel[i] = i
        
    plt.xlabel("Pixel")
    plt.ylabel("Quantidade")
    plt.title("histograma invertido")
    plt.bar( pixel, histograma, color="grey" )
    plt.show()
        
    return histograma
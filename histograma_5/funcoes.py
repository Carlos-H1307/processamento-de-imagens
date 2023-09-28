# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 03:53:55 2023

@author: aluno
"""
import cv2
import numpy
import matplotlib.pyplot as plt
import math

def mapear(imagem, histograma):
    pixel = 256 * [0]
    for i in range( 256 ):
        pixel[i] = i

    
    """ Acumular """
    acumulado = numpy.zeros( 256 )
    mapa = numpy.zeros( 256 )

    acumulado[0] = histograma[0]
    i = 1
    while i < 256 :
        aux = histograma[i] + acumulado[i - 1]
        if aux > 1:
            aux = 1
        acumulado[ i ] = aux
        i += 1
        
    plt.xlabel("Pixel")
    plt.ylabel("Quantidade")
    plt.title("histograma acumulado ")
    plt.bar( pixel, acumulado, color="#225500" )
    plt.show()
    
    
    """ Mapear """
    mapa = numpy.zeros( 256 )
    for i in range( 256 ):
        mapa[i] = round( acumulado[i] * 255 )
    
    saida = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
    
    for i in range( imagem.shape[0] ):
        for j in range( imagem.shape[1] ):
            saida[i][j] = mapa[ imagem[i][j] ]

    cv2.imshow("img Saida", saida)
    
def mapear2(imagem, histograma):
    pixel = 256 * [0]
    for i in range( 256 ):
        pixel[i] = i

    
    """ Acumular """
    acumulado = numpy.zeros( 256 )
    mapaAcumulado = numpy.zeros( 256 )

    acumulado[0] = histograma[0]
    i = 1
    while i < 256 :
        aux = histograma[i] + acumulado[i - 1]
        if aux > 1:
            aux = 1
        acumulado[ i ] = aux
        i += 1   
    
    
    """ Mapear """
    mapaAcumulado = numpy.zeros( 256 )
    for i in range( 256 ):
        mapaAcumulado[i] = round( acumulado[i] * 255 )
    
    saida = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
    
    for i in range( imagem.shape[0] ):
        for j in range( imagem.shape[1] ):
            saida[i][j] = mapaAcumulado[ imagem[i][j] ]
            
    """ histograma2 """
    histograma2 = numpy.zeros(256)
    
    for i in range( 256 ):
        menor = histograma[ i ] - mapaAcumulado[ 0 ]
        menorIndice = 0
        for j in range( 256 ):
            if abs( histograma[ i ] - mapaAcumulado[ j ] ) < menor:
                menor = mapaAcumulado[ j ]
                menorIndice = j
        histograma2[ i ] = menor
    
    plt.xlabel("Pixel")
    plt.ylabel("Quantidade")
    plt.title("histograma2")
    plt.bar( pixel, histograma2, color="#225500" )
    plt.show()
    
    cv2.imshow("img Saida", saida)

def mostrarHistograma(histograma, nomeHistograma, cor):
    pixel = 256 * [0]
    for i in range( 256 ):
        pixel[i] = i
    
    plt.xlabel("Pixel")
    plt.ylabel("Quantidade")
    plt.title( nomeHistograma )
    plt.bar( pixel, histograma, color=cor )
    plt.show()


def acumular(histograma):
    acumulado = numpy.zeros( 256 )
    mapaAcumulado = numpy.zeros( 256 )

    acumulado[0] = histograma[0]
    i = 1
    while i < 256 :
        aux = histograma[i] + acumulado[i - 1]
        if aux > 1:
            aux = 1
        acumulado[ i ] = aux
        i += 1   
        
    pixel = 256 * [0]
    for i in range( 256 ):
        pixel[i] = i
        

    
    return acumulado


def equalizar(histograma):
    for i in range(256):
        histograma[i] *= 255
    return histograma
    

def normalizarHistograma(histograma, totalPixels):
    for i in range(256):
        histograma[i] /= totalPixels
    return histograma

    
def mapear3(equalizado, acumulado):
    mapa2 = {}
    
    for valor in equalizado:
        menor = abs( valor - acumulado[0] )
        menorIndice = 0
        for j in range( len(acumulado) ):
            if abs(valor - acumulado[j]) < menor:
                menor = abs(valor - acumulado[j])
                menorIndice = j
        mapa2[valor] = menorIndice
    
    return mapa2

def remove_repetido(lista):
    l=[]
    for i in lista:
        if i not in l:
            l.append(i)
    return l
    
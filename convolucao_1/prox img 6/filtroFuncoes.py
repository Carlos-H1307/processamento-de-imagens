# -*- coding: utf-8 -*-
"""
Created on Tue Sep 26 18:09:07 2023
title: convoluçao
@author: carlos
"""

import cv2
import numpy
import math

LAPLACIANO = [
              [0,  1, 0],
              [1, -4, 1],
              [0,  1, 0]
             ]

def gerarOpOnes(dim):
    matriz = numpy.ones( (dim, dim) )
    return matriz

def gerarOpZeros(dim):
    matriz = numpy.zeros( (dim, dim) )
    return matriz

def mapOp(dimensao, num, funcMapeamento):
    
    matriz = numpy.zeros( (dimensao, dimensao) )
    
    for i in range(dimensao):
        for j in range(dimensao):
            matriz[i][j] = num
            
    return list( map(funcMapeamento, matriz) )


def filtrar(imagem, operador):
    imgRetorno = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
    
    #dimensao do operador quadrado
    dim = len( operador )
    
    #filtrar para dimensao impar
    if( dim%2 == 1 ):

        for i in range( imagem.shape[0]):
            for j in range( imagem.shape[1]):
                soma = 0
                for k in range( dim ):
                    for l in range( dim ):
                        
                        #verificar o limite horizontal da img
                        hor     = i - math.floor( dim/2 ) + k
                        
                        #verificar o limite vertical da img
                        vert    = j - math.floor( dim/2 ) + l
                        
                        #verifica os limites do eixo horizontal da img
                        if( hor < 0 or hor > imagem.shape[0] - 1 ):
                            soma += 0
                            
                        #verifica os limites do eixo vertical da img
                        elif( vert < 0 or vert > imagem.shape[1] - 1 ):
                            soma += 0
                            
                        #soma com os bits e multiplica pero operador
                        else:
                            soma += imagem[ hor ][ vert ] * operador[k][l]
                            
                #trata os bits com um maximo de 255 e minimo de 0 
                aux = 255 * dim * dim
                if soma > aux:
                    soma = aux
                elif soma < 0:
                    soma = 0
                imgRetorno[i][j] = soma / ( dim*dim )
                
        return imgRetorno
    
    #filtrar para dimensao par
    else:
        
        for i in range( imagem.shape[0]):
            for j in range( imagem.shape[1]):
                soma = 0
                for k in range( dim ):
                    for l in range( dim ):
                        
                        #verificar o limite horizontal da img
                        hor     = i + k
                        
                        #verificar o limite vertical da img
                        vert    = j + l
                        
                        #verifica os limites do eixo horizontal da img
                        if( hor > imagem.shape[0] - 1):
                            soma += 0
                            
                        #verifica os limites do eixo vertical da img
                        elif( vert > imagem.shape[1] - 1):
                            soma += 0
                            
                        #soma com os bits e multiplica pero operador
                        else:
                            soma += imagem[ hor ][ vert ] * operador[k][l]
                            
                #trata os bits com um maximo de 255 e minimo de 0 
                aux = 255 * dim * dim
                if soma > aux:
                    soma = aux
                elif soma < 0:
                    soma = 0
                imgRetorno[i][j] = soma / ( dim*dim )
                
        return imgRetorno
        


"""

for i in range( imagem.shape[0]):
    for j in range( imagem.shape[1]):
        soma = 0
        for k in range( 3 ):
            for l in range( 3 ):
                hor = i- math.floor(3/2) +k 
                vert = j- math.floor(3/2) +l 
                if( hor < 0 or hor > imagem.shape[0]-1 ):
                    soma += 0
                elif( vert < 0 or vert > imagem.shape[1]-1 ):
                    soma += 0
                else:
                    soma += cinza[ hor ][ vert ] * op[k][l]
                    
                    
        if soma > 255 * 3 * 3:
            soma = 255*3*3
        elif soma < 0:
            soma = 0
        imgConvoluida[i][j] = soma/(3*3)

"""
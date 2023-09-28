import cv2
import numpy
import matplotlib.pyplot as plt
import random
import math
import filtroFuncoes as f


#belgica.jpg
#piguin.jpg
#vermelho.jpg
#webb1.png
#webb2.png
#sem_contraste.jpg
#sem_contraste2.png

img     = "piguin.jpg"
imagem  = cv2.imread(img)


""" ----- ----- canais ----- ----- """
blue    = numpy.zeros( (imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8 )
green   = numpy.zeros( (imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8 )
red     = numpy.zeros( (imagem.shape[0], imagem.shape[1], imagem.shape[2]), dtype=numpy.uint8 )
cinza   = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )
teste   = numpy.zeros( (imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8 )

blue    [ : , : , 0 ] = imagem[ : , : , 0 ]
green   [ : , : , 1 ] = imagem[ : , : , 1 ]
red     [ : , : , 2 ] = imagem[ : , : , 2 ]

alturaImg = imagem.shape[0]
larguraImg = imagem.shape[1]
totalPixels = alturaImg * larguraImg


""" ----- ----- cinza ----- ----- """
for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        cinza[i][j] = imagem[i][j].sum() // 3
        


def fun(n):
    return n+n

result = f.mapOp(5, 5, fun)

print( list( result ))

#cv2.imshow("img", cinza)
cv2.imshow("img op3", f.filtrar( cinza, result ))
#cv2.imshow("img opPar", f.filtrar( cinza, opPar ))

cv2.waitKey(0)
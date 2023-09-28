import cv2
import numpy
import matplotlib.pyplot as plt
import random
import math
import funcoes
import histogramas

#belgica.jpg
#piguin.jpg
#vermelho.jpg
#webb1.png
#webb2.png
#sem_contraste.jpg
#sem_contraste2.png
img     = "sem_contraste2.png"
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


""" ----- ----- histograma cinza ----- ----- """

histogramaCinza = numpy.zeros( 256 )

for i in range( imagem.shape[0] ):
    for j in range( imagem.shape[1] ):
        histogramaCinza[ cinza[i][j] ] += 1

pixel = 256 * [0]
for i in range( 256 ):
    pixel[i] = i

#plt.xlabel("Pixel")
#plt.ylabel("Quantidade")
#plt.title("histograma da imagem em tons de cinza")
#plt.bar( pixel, histogramaCinza, color="grey" )
#plt.show()

eq = histogramas.equalizado()
acc = funcoes.acumular(eq)
mapear3 = funcoes.mapear3(eq, acc)

normalizado = funcoes.normalizarHistograma(histogramaCinza, totalPixels)
normAcc = funcoes.acumular(normalizado)
normEq = funcoes.equalizar(normAcc)

funcoes.mostrarHistograma(normEq, "histograma eq", "black")
funcoes.mostrarHistograma(normalizado, "histograma normalizado", "black")
funcoes.mostrarHistograma(normAcc, "histograma normalizado acc", "black")

#funcoes.mapear(cinza, histogramas.equalizado() )


#cv2.imshow("img",cinza)
cv2.waitKey(0)
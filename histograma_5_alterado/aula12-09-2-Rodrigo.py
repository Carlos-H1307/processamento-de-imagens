# -*- coding: utf-8 -*-
"""
Created on Tue Sep 12 14:25:43 2023

@author: rodri
"""

import cv2
import numpy 
import matplotlib.pyplot as plt

from funcao_remove import remove_repetido
from mapear import  mapeamento

pixel = 256*[0]
nTotal2 = 100
nTotal = 0
imagem = cv2.imread('imagem13.jpg')

pixel = 256*[0]
for i in range(256):
    pixel[i] = i

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da Imagem em Tons de Cinza')

hist = [0]*256
histnormalizado2 = [0]*256
histnormalizadoAcumulado2 = [0]*256
histSemRepetido = [0]*256
histMapeamento=[0]*256
histES=[0]*256
histnormalizado = [0]*256
histnormalizadoAcumulado = [0]*256
hist5=[0]*256
hist6=[0]*256
hist7=[0]*256
histMap3= [0]*256
mapa1_SemRepetido=[]
mapa2=[]

imagemCinza = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = (imagem[i][j].sum() // 3)
        hist[imagemCinza[i][j]] += 1
        nTotal +=1
        
cv2.imshow("imagem_cinza1.jpg", imagemCinza)    
cv2.imwrite("imagem_cinza2.jpg", imagemCinza)
        
plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da Imagem em Tons de Cinza')
plt.bar(pixel, hist, color='grey')
plt.show()



for i in range (256):
    if (i) == 0:
        histES[i]= 0
    elif (i)<= 125:
        histES[i]=1000/nTotal2
        histES[i]= histES[i]+ histES[i-1]
    elif (i) >= 251:
        histES[i]=(1000/nTotal2)*0
        ##hist7[i]= hist7[i]+ hist7[i]
    else:
        histES[i]=(1000/nTotal2)*(-1)
        histES[i]= histES[i]+ histES[i-1]

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma especificado') 
plt.bar(pixel, histES, color='grey')
plt.show()

soma = 0
for i in range (256):
    soma += histES[i]
    
for i in range (256):
    histnormalizado2[i] = histES[i]/soma
##print(nTotal)



plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da normalizado')    

plt.bar(pixel, histnormalizado2, color='grey')
plt.show()


for i in range (256):
    if (i) == 0:
        histnormalizadoAcumulado2 [i]= histES[i]/soma
    else:
        histnormalizadoAcumulado2 [i]= histES[i]/soma
        histnormalizadoAcumulado2 [i]= histnormalizadoAcumulado2[i]+histnormalizadoAcumulado2[i-1]
        ##print(histnormalizadoAcumulado[i])

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da normalizado acumulado') 
plt.bar(pixel, histnormalizadoAcumulado2, color='grey')
plt.show()


for i in range (256):
    histMapeamento[i]=round(histnormalizadoAcumulado2[i]*255)
    ##print(histMapeamento[i])
    




    
plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma ###') 
plt.bar(pixel, histMapeamento, color='grey')
plt.show()






for i in range (256):
    histnormalizado[i] = hist[i]/nTotal
print(nTotal)



plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da normalizado')    

plt.bar(pixel, histnormalizado, color='grey')
plt.show()

for i in range (256):
    if (i) == 0:
        histnormalizadoAcumulado [i]= hist[i]/nTotal
    else:
        histnormalizadoAcumulado [i]= hist[i]/nTotal
        histnormalizadoAcumulado [i]= histnormalizadoAcumulado[i]+histnormalizadoAcumulado[i-1]
        ##print(histnormalizadoAcumulado[i])

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da normalizado acumulado') 
plt.bar(pixel, histnormalizadoAcumulado, color='grey')
plt.show()




for i in range (256):
    hist5[i]=round(histnormalizadoAcumulado[i]*255)
    ##print(hist5[i])
    

    
imagemEqualizada = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
for i in range(imagem.shape[0]):
    for j in range(imagem.shape[1]):
        imagemCinza[i][j] = (imagem[i][j].sum() // 3)
        imagemEqualizada[i][j] = hist5[imagemCinza[i][j]]
        hist6[imagemEqualizada[i][j]]+=1

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da equalizado') 
plt.bar(pixel, hist6, color='grey')
plt.show()


cv2.imshow("imagem_eq.jpg", imagemEqualizada)    
cv2.imwrite("imagem_eq2.jpg", imagemEqualizada)


        
        




        

mapa1_SemRepetido = remove_repetido(hist5)

tamanho_mapa1 = len(mapa1_SemRepetido)
##tamanho_mapa2 = len(histMapeamento) 


print("O tamanho de mapa1 é:", tamanho_mapa1)
##print("O tamanho de mapa1 é:", tamanho_mapa2)



mapa2=mapeamento(mapa1_SemRepetido, histMapeamento)

tamanho_mapa2 = len(mapa2)
print("O tamanho de mapa2 é:", tamanho_mapa2)

imagemAlterada = numpy.zeros((imagem.shape[0], imagem.shape[1]), dtype=numpy.uint8())
for i in range (imagem.shape[0]):
    for j in range (imagem.shape[1]):
        imagemAlterada[i][j]= mapa2[hist5[imagemCinza[i][j]]]
        hist7[imagemAlterada[i][j]]+=1

plt.xlabel('Pixel')
plt.ylabel('Quantidade')
plt.title('Histograma da imagem encontrada') 
plt.bar(pixel, hist7, color='grey')
plt.show()

cv2.imshow("imagem_equalizada2.jpg", imagemAlterada)    
cv2.imwrite("imagem_equalizada2.jpg", imagemAlterada)

cv2.waitKey(0)
cv2.destroyAllWindows()

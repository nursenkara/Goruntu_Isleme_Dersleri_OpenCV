import cv2
## Resim Okuma
#resim = cv2.imread("ball.jpg")
#cv2.imshow("Futbol Topu", resim)

#cv2.waitKey(0)
#cv2.destroyAllWindows()
### Border özellikleri

cerceve_rengimiz = [144, 12, 63]
resim = cv2.imread("ball.jpg")

#cerceve = cv2.copyMakeBorder(resim, 10, 10, 10, 10, cv2.BORDER_CONSTANT, value=cerceve_rengimiz)
#cerceve = cv2.copyMakeBorder(resim, 50, 50, 50 , 50, cv2.BORDER_REFLECT)
#cerceve = cv2.copyMakeBorder(resim, 50, 50, 50, 50, cv2.BORDER_REPLICATE)
cerceve = cv2.copyMakeBorder(resim, 50, 50, 50, 50, cv2.BORDER_WRAP)
cv2.imshow("Futbol Topu", cerceve)

cv2.waitKey(0)
cv2.destroyAllWindows()

#import cv2
#resim = cv2.imread("everest.jpg", 0)
#cv2.imshow("everest", resim)
#cv2.waitKey(0)
#cv2.destroyAllWindows()
#cv2.imwrite("everestgri.png", resim)


# Mavi Renk İçin "0" Parametresi
# Yeşil Renk İçin "1" Parametresi
# Kırmızı Renk İçin "2" Parametresi
import cv2
resim = cv2.imread("everest.jpg")
cv2.imshow("everest", resim)
print(resim.shape)

print("200x200'lük Alan İçin Mavi Renk Değeri:" + str(resim.item(200, 200, 0)))
print("200x200'lük Alan İçin Yeşil Renk Değeri:" + str(resim.item(200, 200, 1)))
print("200x200'lük Alan İçin Kırmızı Renk Değeri:" + str(resim.item(200, 200, 2)))

cv2.waitKey(0)
cv2.destroyAllWindows()

yukseklik = resim.shape[0]
genislik = resim.shape[1]

print("Resim Yüksekliği: (px) ", yukseklik)
print("Resim Genişliği:  (px) ", genislik)

cv2.waitKey(0)
cv2.destroyAllWindows()

#resim Çerçeveleme





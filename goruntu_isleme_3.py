import cv2
resim = cv2.imread("manzara.jpg")
cozunurluk = [640, 480]
resim_genislik_olcegi = cozunurluk[0] /resim.shape[1]


from PIL import Image,ImageChops

im1 = Image.open("lemur.png")
im2 = Image.open("flag.png")

im3 = ImageChops.difference(im1,im2)

im3.show()
im3.save("final.png")

# flag: crypto{X0Rly_n0t!}

# alternative solution below

# import cv2
# im1 = cv2.imread("flag.png")
# im2 = cv2.imread("lemur.png")
# im3 = cv2.bitwise_xor(im1, im2, mask=None)
# cv2.imshow("Bitwise XOR", im3)
# if cv2.waitKey(0) & 0xff == 27:
#     cv2.destroyAllWindows()
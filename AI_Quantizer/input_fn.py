import os
import cv2

calib_image_list = "/workspace/train.txt"
calib_batch_size = 10

def calib_input(iter):
  images = []
  line = open(calib_image_list).readlines()
  for index in range(0,calib_batch_size):
    curline = line[iter*calib_batch_size+index]
    calib_image_name = curline.strip()
    
    img=cv2.imread(calib_image_name)
    img=cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
    img=cv2.resize(img,(260,260))
    img=img/255.0

    images.append(img.tolist())
  return {"image_in": images}

import cv2
import torch
import numpy as np


resim = np.array(cv2.imread("image.jpg",3))
yeniResim = cv2.resize(resim,(255,255))
print(yeniResim)

keditorch = torch.from_numpy(yeniResim)
print(keditorch.size())


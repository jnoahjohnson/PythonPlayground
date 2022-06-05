import cv2
import numpy as np

# read image as grayscale
img = cv2.imread('testimage.png')

# convert to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

# Blur
blur = cv2.GaussianBlur(gray, (15,15), 1)

# threshold
thresh = cv2.threshold(blur, 190, 255, cv2.THRESH_BINARY)[1]\

# apply morphology
kernel = np.ones((7,7), np.uint8)
morph = cv2.morphologyEx(thresh, cv2.MORPH_CLOSE, kernel)
kernel = np.ones((9,9), np.uint8)
morph = cv2.morphologyEx(morph, cv2.MORPH_ERODE, kernel)

# get largest contour
contours = cv2.findContours(morph, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_NONE)
contours = contours[0] if len(contours) == 2 else contours[1]
area_thresh = 0
for c in contours:
    area = cv2.contourArea(c)
    if area > area_thresh:
        area_thresh = area
        big_contour = c


# get bounding box
x,y,w,h = cv2.boundingRect(big_contour)

# draw filled contour on black background
mask = np.zeros_like(gray)
mask = cv2.merge([mask,mask,mask])
cv2.drawContours(mask, [big_contour], -1, (255,255,255), cv2.FILLED)

# apply mask to input
result1 = img.copy()
result1 = cv2.bitwise_and(result1, mask)

# crop result
result2 = result1[y:y+h, x:x+w]

# # view result
# cv2.imshow("threshold", thresh)
# cv2.imshow("morph", morph)
# cv2.imshow("mask", mask)
# cv2.imshow("result1", result1)
# cv2.imshow("result2", result2)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

# # save result
# cv2.imwrite("paper_thresh.jpg", thresh)
# cv2.imwrite("paper_morph.jpg", morph)
# cv2.imwrite("paper_mask.jpg", mask)

# def hisEqulColor(img):
#     ycrcb=cv2.cvtColor(img,cv2.COLOR_BGR2YCR_CB)
#     channels=cv2.split(ycrcb)
#     cv2.equalizeHist(channels[0],channels[0])
#     cv2.merge(channels,ycrcb)
#     cv2.cvtColor(ycrcb,cv2.COLOR_YCR_CB2BGR,img)
#     return img

def histogram_equalization(img_in):
# segregate color streams
    b,g,r = cv2.split(img_in)
    h_b, bin_b = np.histogram(b.flatten(), 256, [0, 256])
    h_g, bin_g = np.histogram(g.flatten(), 256, [0, 256])
    h_r, bin_r = np.histogram(r.flatten(), 256, [0, 256])
# calculate cdf    
    cdf_b = np.cumsum(h_b)  
    cdf_g = np.cumsum(h_g)
    cdf_r = np.cumsum(h_r)
    
# mask all pixels with value=0 and replace it with mean of the pixel values 
    cdf_m_b = np.ma.masked_equal(cdf_b,0)
    cdf_m_b = (cdf_m_b - cdf_m_b.min())*255/(cdf_m_b.max()-cdf_m_b.min())
    cdf_final_b = np.ma.filled(cdf_m_b,0).astype('uint8')
  
    cdf_m_g = np.ma.masked_equal(cdf_g,0)
    cdf_m_g = (cdf_m_g - cdf_m_g.min())*255/(cdf_m_g.max()-cdf_m_g.min())
    cdf_final_g = np.ma.filled(cdf_m_g,0).astype('uint8')
    cdf_m_r = np.ma.masked_equal(cdf_r,0)
    cdf_m_r = (cdf_m_r - cdf_m_r.min())*255/(cdf_m_r.max()-cdf_m_r.min())
    cdf_final_r = np.ma.filled(cdf_m_r,0).astype('uint8')
# merge the images in the three channels
    img_b = cdf_final_b[b]
    img_g = cdf_final_g[g]
    img_r = cdf_final_r[r]
  
    img_out = cv2.merge((img_b, img_g, img_r))
# validation
    equ_b = cv2.equalizeHist(b)
    equ_g = cv2.equalizeHist(g)
    equ_r = cv2.equalizeHist(r)
    equ = cv2.merge((equ_b, equ_g, equ_r))
    #print(equ)
    #cv2.imwrite('output_name.png', equ)
    return img_out

newImg = histogram_equalization(result1)
cv2.imshow('Image', newImg)
cv2.waitKey()
cv2.destroyAllWindows()

cv2.imwrite("paper_result1.jpg", result1)
cv2.imwrite("paper_result3.jpg", result2)
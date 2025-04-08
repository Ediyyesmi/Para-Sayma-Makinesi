# houghcircles değerleri değiştirilerek daha kesin sonuçlar oluşturulabilir


import cv2
import numpy as np

image = cv2.imread("paralar.jpg")
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
gray = cv2.equalizeHist(gray)
blurred = cv2.GaussianBlur(gray, (5, 5), 2)



circles = cv2.HoughCircles(
    blurred,            
    cv2.HOUGH_GRADIENT, 
    dp=1.2,             
    minDist=90,         #  Minimum iki daire merkezi arasındaki mesafe (pixel cinsinden)
    param1=100,         #  Canny edge detector için üst eşik
    param2=30,          #  Daire merkezini bulma hassasiyeti
    minRadius=25,       #  Min daire yarıçap (pixel)
    maxRadius=70        #  Max daire yarıçap (pixel)
)




coins = {
    "10kr":{"count":0, "value":0.1},
    "1tl": {"count":0, "value":1}
}


total_coins = 0
total_value = 0.0


if circles is not None:
    circles = np.round(circles[0,:]).astype("int")
    for (x,y,r) in circles:
        if r<50:
            coin_type = "10kr"
            color = (255,0,0)
        else:
            coin_type = "1tl"
            color = (0,0,255)

        coins[coin_type]["count"] +=1
        total_coins += 1
        total_value += coins[coin_type]["value"]


        #daireyi çizdik
        cv2.circle(image, (x, y), r, color, 2)
        cv2.putText(image, coin_type, (x-20, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, color, 2)



print("total money: ",total_coins)
print("total value: ",total_value)
for c in coins:
    print(f"{c}: {coins[c]['count']} adet")


cv2.imwrite("yeniresim.jpg",image)
cv2.imshow("tespit", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

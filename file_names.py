
#YOLOMODEL/objects/0001.jpg
## yolov4_sheep/sheep_images/001.jpg
f = open("deneme.txt", "a")
string = "yolov4_sheep/sheep_images/"
number = ""
for i in range(351,451):   
    
    f.write(string + str(i)+".jpg\n")

f.close()
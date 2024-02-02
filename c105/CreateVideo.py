import os
import cv2


path = "Images"

images = []


for file in os.listdir(path):
    name, ext = os.path.splitext(file)

    if ext in ['.gif', '.png', '.jpg', '.jpeg','.jfif']:
        file_name = path+"/"+file

        #print(file_name)
               
        images.append(file_name)
        
print(len(images))
frame = cv2.imread(images[0])
height,width,channels = frame.shape
size = (width,height)
print(size)

save = cv2.VideoWriter('sunset.mp4',cv2.VideoWriter_fourcc(*'DIVX'),2,size)

for i in range(0,91):
    frame = cv2.imread(images[i])
    save.write(frame)

save.release()
print('done')    
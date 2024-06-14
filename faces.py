import cv2
import os
import imutils

### Separar vídeo em frames
# vidcap = cv2.VideoCapture('la_cabra.mp4')
# success,image = vidcap.read()
# count = 0
# while success:
#   cv2.imwrite("frame_%d.jpg" % count, image)      
#   success,image = vidcap.read()
#   print('Read a new frame: ', success)
#   count += 1

el_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')
img_folder = 'og_frames'
output_folder = 'rec_frames'

for filename in os.listdir(img_folder):
    if filename.endswith('.jpg'):
        img_path = os.path.join(img_folder, filename)
        img = cv2.imread(img_path)
        img = imutils.resize(img, width=500)
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        emotions = el_cascade.detectMultiScale(gray, scaleFactor=1.05, minNeighbors=25, minSize=(30, 30))

        for (x, y, w, h) in emotions:
            cv2.rectangle(img, (x, y), (x+w, y+h), (255, 0, 0), 2)

        output_path = os.path.join(output_folder, filename)
        cv2.imwrite(output_path, img)

        cv2.imshow('img', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
### Convertendo frames em vídeo
# img_array = []
# for filename in os.listdir(output_folder):
#     if filename.endswith('.jpg'):
#         img_path = os.path.join(output_folder, filename)
#         img = cv2.imread(img_path)
#         height, width, layers = img.shape
#         size = (width, height)
#         img_array.append(img)

# out = cv2.VideoWriter('output.avi', cv2.VideoWriter_fourcc(*'DIVX'), 15, size)

# for i in range(len(img_array)):
#     out.write(img_array[i])
# out.release()

# cv2.waitKey(0)
# cv2.destroyAllWindows()

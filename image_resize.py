from PIL import Image
import os

folder =[]
i  = 0
for image_folder in os.listdir("image/"):
    print(image_folder)
    y = os.makedirs((image_folder))
    name,last = os.path.splitext(image_folder)
    folder.append(name)
    print(folder)
    for image in os.listdir("image"+"/"+ image_folder):
        #output = os.mkdir(image_folder+"/")
        f,e = os.path.splitext(image)
        im = Image.open("image"+"/"+ image_folder+"/"+image)
        #im_0 = im.resize((310,416), Image.ANTIALIAS)
        #im_1 = im.resize((620,832), Image.ANTIALIAS)
        im_2 = im.resize((930,1248), Image.ANTIALIAS)
        im_2.save(folder[i]+"/"+f+".png","PNG",quality = 100)        
    i += 1 

import os
images_folder="Train/" #to open folder with images
y = open("new.txt","w",newline="") # to create a new file
images=[] #list to store images
b=[]
c=[]
counter =0

""" code to store list of images"""

a=[]
for file in os.listdir(images_folder):
    for i,images in enumerate(os.listdir(images_folder+file)):
        x="/content/YOLOv3_TensorFlow/data/my_data/Train/ActaM_1970_37_63/"+str(i)+".png"+" "+"930 1248"
        a.append(x)

print(len(a)) #number of images
train_dict={} #dictionary to store images

for i in range(0,len(a)): # to store image names in the dictionary
    train_dict[i]=a[i]
    
for j in range(0,30): #print first 30 image names
    print(train_dict[j])
    
math_folder="GT_math_calculated/"
for file in os.listdir(math_folder):
    f =open(math_folder+file,"r")
    z = f.readlines()
    for j in range(0,len(b[0])):
        for i,line in enumerate(z):
            d = z[i]
            e=d.index(",")
            d=d[e+1:]
            g=int(d[:e])
            if g==j:
                y.write(str(counter)+" "+d+"\n")
            else:
                continue
                
y.close()         
        
    

import os.path
#from PIL import Image
import os
path = "new folder/"
image_path = 'C:/Users/j-one/Desktop/GAHAN AI/YOLO/Train/'
image_size = "930 1248"
counter =0
path_images = "Train/"
image_count=[]
image_list=[]
size = 28
#counter = 0
for folder in os.listdir(path_images):
    image_list.clear()
    for i,image in enumerate(os.listdir(path_images+folder)):
        #print(i)
        image_list.append(i)
    #print(image_list)
    image_count.append(len(image_list))
#for image_folder in os.listdir(image_path):
    #for image in os.listdir(image_path+image_folder):
no_of_folders = len(os.listdir(path))

#print(no_of_folders)

for file in os.listdir(path):
            #print(file)
            a,b = file.split(".") #to split file name
            f = open(path+file,"r") #open file to be split
            x = open(file,"w",newline="") #open or create file to save output
            z = f.readlines() # to read lines from the files
            counter = 0
            x.write(image_size)
            for i in range(0,len(z)):
                d  = z[i]
                for j in range(0,size):
                    
                    e = d.index(",")
                    d=d[e+1:]
                    image_index = d[:e]
                    comma = ","
                    d = d.replace(comma," ")
                    i_ = str(i)
                    d = i_+" "+d
                    print(d)
                    x.write(" "+d+"")               
                        
f.close()
x.close()


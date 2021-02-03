import glob
import os

# change this to the folder you wanna recursively upscale
my_path = "/home/uhh/Desktop/Projects/Minecraft/ai/doku/"

# oh my GLOB
files = glob.glob(my_path + '/**/*.png', recursive=True)

# just a counter, could do more with it (like % done and ETA)
current = 0
length = len(files)
# and now we upscale every file
for filename in files:
    head, tail = os.path.split(filename)
    print(str(current) + " " + "{:.2f}".format((current / length)*100) + "%"   ": " + tail)
    
    # this is just from the command line but filename shoved in there
    os.system("waifu2x-ncnn-vulkan -i " + filename + " -o " + filename +" -s 2")
    current += 1
              
              
print("DONE!!!!!!!!!!!!")

import os

# put the folder to the folder youve upscaled
path = r'C:\Users\$USER\AppData\Roaming\.minecraft\resourcepacks\progwammers_art\assets\minecraft\textures\entity\blah'
for filename in os.listdir(path):
    if filename[-8:] == "_00x.png":
        print(filename)
        os.remove(os.path.join(path, filename[:-25] + ".png"))
        os.rename(os.path.join(path, filename), os.path.join(path, filename[:-25] + ".png"))

print("done")
    

# scripts-mass-upscaling
This is two guides to using my python scripts in order to upscale a lot of game (minecraft) textures!
They are quite simple with little safe guarding, so make sure you understand what it's doing! 

There is a more manual GUI focused way and a simple one script to do every texture recursively.
Waifu2x is open source and upscales to a maximum of 2x but we can automate it completely!
Topaz Labs Gigapixel AI uses a GUI and I havent found a way to use it via the command line (despite their video product having it) but it does produce much more "realistic" results. 

# Using Waifu2x
This part uses Waifu2x (an upscaler mostly used for anime). I used https://github.com/nihui/waifu2x-ncnn-vulkan as it seemed fast enough (and it was the only one that installed for me) but I'm sure others would work, you'd just need to change a line. 

In the python script recursivewaifu.py change the file path to the file location with the pack.mcmeta , then run it with 
>python recursivewaifu.py
Simple!

# Using Topaz Labs Gigapixel AI
I used the generous free trial from here https://topazlabs.com/gigapixel-ai/ . This program is great fun. Load up a texture and fiddle with the settings on the right until you get something you like. Topaz renames the orignal file as name-settings-400x.png depending on your settings, his script simply deletes the original file and renames the new upscaled file to the regular one.
In gigapixel, pick a directory in the textures and select all images, and copy the directory path. Hit export on gigapixel and watch it go! After this is finished paste the location into the file path variable in the script and run! Repeat for all directories! 


# Getting the minecraft resourcepack


## Some problems in minecraft
### Ugly borders?
Using Waifu2x the transparancy remains but it is clipped so anything with transparancy will have an awful looking border. Yikes! Unfortunately this is more a limit of the model, Topaz Gigapixel does not have this issue as serverly.

### The grass isn't green on the other side?
Minecraft uses a greyscale image for the grass and just colours it based on the biome it is in. This has the nice effect of allowing biome-smoothing but makes Waifu2x pack look all grey! 

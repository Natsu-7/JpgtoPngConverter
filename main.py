import sys,os
from PIL import Image

parentDir = "D:/PyCharmProjects/ImageProcessing/"
# grabbing the arguments
sourceFolder = sys.argv[1]
targetFolder = sys.argv[2]

# check if new folders exists, if not create it

if not sourceFolder in os.listdir("./"):
    print(f"The {sourceFolder} does not exists")
    exit()
if not targetFolder in os.listdir("./") :
    path = os.path.join(parentDir,targetFolder)
    os.mkdir(path)
    print("Created Successfully")

# loop through the source folder and convert images into PNG

for i in os.listdir(sourceFolder):
    image = Image.open(f"{sourceFolder}/{i}")
    name = os.path.splitext(i)[0]
    # save to target folder
    image.save(f"{targetFolder}/{name}.png", "png")
print("Converted Successfully")
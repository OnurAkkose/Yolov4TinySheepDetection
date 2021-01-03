from pycocotools.coco import COCO
import requests

# instantiate COCO specifying the annotations json path
coco = COCO('annotations/instances_train2014.json')
# Specify a list of category names of interest
catIds = coco.getCatIds(catNms=['sheep'])
# Get the corresponding image ids and images using loadImgs
imgIds = coco.getImgIds(catIds=catIds)
images = coco.loadImgs(imgIds)

#######
# Save the images into a local folder
for im in images:
    img_data = requests.get(im['coco_url']).content
    with open('coco_sheep/' + im['file_name'], 'wb') as handler:
        handler.write(img_data)
        

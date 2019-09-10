from imageai.Detection import ObjectDetection
import os

execution_path = os.getcwd()

# Create Detection Object
detector = ObjectDetection()
detector.setModelTypeAsRetinaNet()
detector.setModelPath( os.path.join(execution_path , "resnet50_coco_best_v2.0.1.h5"))
detector.loadModel()

# Name of Target
image_name = 'cam_view.jpg'
image_target = 'processed_' + image_name

#Run Detection
detections = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , image_name), output_image_path=os.path.join(execution_path , image_target))

# Creates local images of objects found
# detections, extracted_images = detector.detectObjectsFromImage(input_image=os.path.join(execution_path , "image.jpg"), output_image_path=os.path.join(execution_path , "imagenew.jpg"), extract_detected_objects=True)

# Console output
for eachObject in detections:
    print(eachObject["name"] , " : " , eachObject["percentage_probability"] )
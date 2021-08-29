#image prediction: https://github.com/OlafenwaMoses/ImageAI
#https://github.com/OlafenwaMoses/ImageAI/blob/master/imageai/Classification/README.md
from imageai.Classification import ImageClassification
import os
execution_path = os.getcwd()

prediction = ImagePrediction()
prediction.setModelTypeAsMobileNetV2()
prediction.setModelPath(os.path.join(execution_path, "mobilenet_v2.h5"))
prediction.loadModel()

predictions, probabilities = prediction.classifyImage(os.path.join(execution_path, "giraffe.jpg"), result_count=5 )
for eachPrediction, eachProbability in zip(predictions, probabilities):
    print(eachPrediction , " : " , eachProbability)

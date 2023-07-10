""" Written by Benjamin Jack Cullen

    Note that experiments numer must be sufficient to reduce the loss else by here/before here
    the types in numpy arrays may result in type errors because the types are changing as the
    loss is reducing. Just train a model sufficiently to avoid different type errors.
"""

import os
from imageai.Classification import ImageClassification
from imageai.Classification.Custom import CustomImageClassification
from imageai.Detection.Custom import CustomObjectDetection
from imageai.Detection import ObjectDetection
import dt
import cv2

RETURNED_FRAME = ""


def process_image_classify(_image_input=None,  _result_count=5, _input_type='file',
                           _model_type=None, _model_json=None, _model_path=None, _classification_speed='normal',
                           PRIMARY_TARGET=None, SECONDARY_TARGET=None):

    if _model_json is not None:
        prediction = CustomImageClassification()
    else:
        prediction = ImageClassification()

    # fast
    if 'resnet50' in _model_type:
        prediction.setModelTypeAsResNet50()

    # higher accuracy
    elif 'densenet121' in _model_type:
        prediction.setModelTypeAsDenseNet121()

    # google higher accuracy+
    elif 'inceptionv3' in _model_type:
        prediction.setModelTypeAsInceptionV3()

    # improved performance for mobile architectures
    elif 'mobilenetv2' in _model_type:
        prediction.setModelTypeAsMobileNetV2()

    if _model_json is not None:
        prediction.setJsonPath(_model_json)

    prediction.setModelPath(_model_path)
    prediction.loadModel(classification_speed=_classification_speed)

    # predict
    predictions, probabilities = prediction.classifyImage(image_input=_image_input, result_count=_result_count,
                                                          input_type=_input_type)
    for eachPrediction, eachProbability in zip(predictions, probabilities):
        IN_PRIMARY = False
        for X in PRIMARY_TARGET:
            if eachPrediction == X.get("name"):
                print(f'{dt.dt()} [DETECTED] [PRIMARY_TARGET] [PRIORITY:{X.get("priority")}] [NAME:{eachPrediction}] [PROBABILITY:{eachProbability}]')
                IN_PRIMARY = True
                break
        IN_SECONDARY = False
        for X in SECONDARY_TARGET:
            if eachPrediction == X.get("name"):
                print(f'{dt.dt()} [DETECTED] [SECONDARY_TARGET] [PRIORITY:{X.get("priority")}] [NAME:{eachPrediction}] [PROBABILITY:{eachProbability}]')
                IN_SECONDARY = True
                break
        if IN_PRIMARY is False and IN_SECONDARY is False:
            print(
                f'{dt.dt()} [DETECTED] [NON_PRIORITY] [NAME:{eachPrediction}] [PROBABILITY:{eachProbability}]')
    print('')
    print('')


def process_image_detect(input_image="", output_directory_path="", input_type="file", output_type="file",
                         extract_detected_objects=False, minimum_percentage_probability=50, nms_treshold=0.4,
                         display_percentage_probability=True, display_object_name=True, thread_safe=False,
                         _model_path=None, _model_json=None,
                         _dump=False, PRIMARY_TARGET=None, SECONDARY_TARGET=None, save_in_class=False,
                         annotate=False):
    global RETURNED_FRAME
    if _model_json is not None:
        detector = CustomObjectDetection()
    else:
        detector = ObjectDetection()
    detector.setModelTypeAsYOLOv3()
    detector.setModelPath(_model_path)
    if _model_json is not None:
        detector.setJsonPath(_model_json)
    try:
        detector.loadModel()
    except Exception as e:
        print(e)

    # detect
    detected_copy, output_objects_array, detected_objects_image_array =\
        detector.detectObjectsFromImage(input_image=input_image, output_directory_path=output_directory_path,
                                        input_type=input_type, output_type=output_type,
                                        extract_detected_objects=extract_detected_objects,
                                        minimum_percentage_probability=minimum_percentage_probability,
                                        # nms_treshold=nms_treshold,
                                        display_percentage_probability=display_percentage_probability,
                                        display_object_name=display_object_name,
                                        thread_safe=thread_safe,
                                        save_in_class=save_in_class,
                                        _annotate=annotate)
    try:
        # print(f'-- {detected_copy, output_objects_array, detected_objects_image_array}')
        if output_objects_array:
            for d in output_objects_array:
                IN_PRIMARY = False
                for X in PRIMARY_TARGET:
                    if d.get("name") == X.get("name"):
                        print(f'{dt.dt()} [DETECTED] [PRIMARY_TARGET] [PRIORITY:{X.get("priority")}] [NAME:{d.get("name")}] [PROBABILITY:{d.get("percentage_probability")}]')
                        IN_PRIMARY = True
                        break
                IN_SECONDARY = False
                for X in SECONDARY_TARGET:
                    if d.get("name") == X.get("name"):
                        print(f'{dt.dt()} [DETECTED] [SECONDARY_TARGET] [PRIORITY:{X.get("priority")}] [NAME:{d.get("name")}] [PROBABILITY:{d.get("percentage_probability")}]')
                        IN_SECONDARY = True
                        break
                if IN_PRIMARY is False and IN_SECONDARY is False:
                    print(f'{dt.dt()} [DETECTED] [NON_PRIORITY] [NAME:{d.get("name")}] [PROBABILITY:{d.get("percentage_probability")}]')
        else:
            print(f'{dt.dt()} [DETECTION] Nothing detected.')

        RETURNED_FRAME = detected_copy
        cv2.imwrite(output_directory_path+'/detected.jpg', RETURNED_FRAME)
    except Exception as e:
        print(e)
    print('')
    print('')

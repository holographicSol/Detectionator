import time

import cv2
from imageai.Detection.keras_retinanet import models as retinanet_models
from imageai.Detection.keras_retinanet.utils.image import read_image_bgr, preprocess_image, resize_image
from imageai.Detection.keras_retinanet.utils.visualization import draw_box, draw_caption
# import matplotlib.pyplot as plt
# import matplotlib.image as pltimage
import numpy as np
# import tensorflow as tf
import os
# from tensorflow.keras import backend as K
from tensorflow.keras.layers import Input
# import warnings
from imageai.Detection.YOLO.yolov3 import tiny_yolov3_main, yolov3_main
from imageai.Detection.YOLO.utils import letterbox_image, yolo_eval, preprocess_input, retrieve_yolo_detections, draw_boxes
import annotator_video
from imageai import colors as color

# If calling Detection AND using these values then ensure these values are reset before making the call
PAUSE_FRAME = False
START_FRAME = 0
video_frames_count = 0
VIDEO_CLOSED = None
MINIMUM_PERCENTAGE_PROBABILITY = 50
KILL_LOOP = False
I_ANNOTATION = 0
I_IMAGES = 0
I_DETECTED_IMAGES = 0
FRAME_DETECTION_INTERVAL = 1


class ObjectDetection:

    def __init__(self):
        self.__modelType = ""
        self.modelPath = ""
        self.__modelPathAdded = False
        self.__modelLoaded = False
        self.__model_collection = []
        self.__input_image_min = 1333
        self.__input_image_max = 800
        self.numbers_to_names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus',
                                 6: 'train',
                                 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign',
                                 12: 'parking meter',
                                 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow',
                                 20: 'elephant',
                                 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag',
                                 27: 'tie',
                                 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball',
                                 33: 'kite',
                                 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard',
                                 38: 'tennis racket',
                                 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon',
                                 45: 'bowl',
                                 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot',
                                 52: 'hot dog',
                                 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant',
                                 59: 'bed',
                                 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote',
                                 66: 'keyboard',
                                 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink',
                                 72: 'refrigerator',
                                 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear',
                                 78: 'hair dryer',
                                 79: 'toothbrush'}
        self.__yolo_iou = 0.45
        self.__yolo_score = 0.1
        self.__nms_thresh = 0.45
        self.__yolo_anchors = [[116, 90,  156, 198,  373, 326],  [30, 61, 62, 45,  59, 119], [10, 13,  16, 30,  33, 23]]
        self.__yolo_model_image_size = (416, 416)
        self.__yolo_boxes, self.__yolo_scores, self.__yolo_classes = "", "", ""
        self.__tiny_yolo_anchors = [[81, 82, 135, 169, 344, 319], [10, 14, 23, 27, 37, 58]]
        self.__box_color = (112, 19, 24)

    def setModelTypeAsRetinaNet(self):
        self.__modelType = "retinanet"

    def setModelTypeAsYOLOv3(self):
        self.__modelType = "yolov3"

    def setModelTypeAsTinyYOLOv3(self):
        self.__modelType = "tinyyolov3"

    def setModelPath(self, model_path):
        if self.__modelPathAdded is False:
            self.modelPath = model_path
            self.__modelPathAdded = True

    def loadModel(self, detection_speed="normal"):
        if self.__modelType is "retinanet":
            if detection_speed is "normal":
                self.__input_image_min = 800
                self.__input_image_max = 1333
            elif detection_speed is "fast":
                self.__input_image_min = 400
                self.__input_image_max = 700
            elif detection_speed is "faster":
                self.__input_image_min = 300
                self.__input_image_max = 500
            elif detection_speed is "fastest":
                self.__input_image_min = 200
                self.__input_image_max = 350
            elif detection_speed is "flash":
                self.__input_image_min = 100
                self.__input_image_max = 250
        elif self.__modelType is "yolov3":
            if detection_speed is "normal":
                self.__yolo_model_image_size = (416, 416)
            elif detection_speed is "fast":
                self.__yolo_model_image_size = (320, 320)
            elif detection_speed is "faster":
                self.__yolo_model_image_size = (208, 208)
            elif detection_speed is "fastest":
                self.__yolo_model_image_size = (128, 128)
            elif detection_speed is "flash":
                self.__yolo_model_image_size = (96, 96)
        elif self.__modelType is "tinyyolov3":
            if detection_speed is "normal":
                self.__yolo_model_image_size = (832, 832)
            elif detection_speed is "fast":
                self.__yolo_model_image_size = (576, 576)
            elif detection_speed is "faster":
                self.__yolo_model_image_size = (416, 416)
            elif detection_speed is "fastest":
                self.__yolo_model_image_size = (320, 320)
            elif detection_speed is "flash":
                self.__yolo_model_image_size = (272, 272)
        if self.__modelLoaded is False:
            if self.__modelType is "":
                raise ValueError("You must set a valid model type before loading the model.")
            elif self.__modelType is "retinanet":
                model = retinanet_models.load_model(self.modelPath, backbone_name='resnet50')
                self.__model_collection.append(model)
                self.__modelLoaded = True
            elif self.__modelType is "yolov3" or self.__modelType is "tinyyolov3":
                input_image = Input(shape=(None, None, 3))
                if self.__modelType == "yolov3":
                    model = yolov3_main(input_image, len(self.__yolo_anchors), len(self.numbers_to_names.keys()))
                else:
                    model = tiny_yolov3_main(input_image, 3, len(self.numbers_to_names.keys()))
                model.load_weights(self.modelPath)
                self.__model_collection.append(model)
                self.__modelLoaded = True

    def detectObjectsFromImage(self, input_image="", input_type="file", output_type="file",
                               extract_detected_objects=False, minimum_percentage_probability=50,
                               display_percentage_probability=True, display_object_name=True,
                               display_box=True, thread_safe=False, custom_objects=None,
                               extract_during_video=False, save_in_class=False, _annotate=False,
                               video_frames_count=1, output_directory_path=""):
        # todo - upgrades in process
        print('-- plugged: Detection.detectObjectsFromImage')
        global I_ANNOTATION, I_IMAGES, I_DETECTED_IMAGES

        if self.__modelLoaded is False:
            raise ValueError("You must call the loadModel() function before making object detection.")
        elif self.__modelLoaded is True:
            # try:
                model_detections = list()
                detections = list()
                image_copy = None
                detected_objects_image_array = []
                min_probability = minimum_percentage_probability / 100

                if extract_during_video is True:
                    og_frame = input_image
                if input_type is "file":
                    input_image = cv2.imread(input_image)
                elif input_type is "array":
                    input_image = np.array(input_image)
                if extract_during_video is False:
                    og_frame = input_image
                untouched_original_frame = og_frame
                detected_copy = input_image
                image_copy = input_image
                if self.__modelType is "yolov3" or self.__modelType is "tinyyolov3":
                    image_h, image_w, _ = detected_copy.shape
                    detected_copy = preprocess_input(detected_copy, self.__yolo_model_image_size)
                    model = self.__model_collection[0]
                    yolo_result = model.predict(detected_copy)
                    model_detections = retrieve_yolo_detections(yolo_result,
                                                                self.__yolo_anchors,
                                                                min_probability,
                                                                self.__nms_thresh,
                                                                self.__yolo_model_image_size,
                                                                (image_w, image_h),
                                                                self.numbers_to_names)
                elif self.__modelType is "retinanet":
                    detected_copy = preprocess_image(detected_copy)
                    detected_copy, scale = resize_image(detected_copy)
                    model = self.__model_collection[0]
                    boxes, scores, labels = model.predict_on_batch(np.expand_dims(detected_copy, axis=0))
                    boxes /= scale
                    for box, score, label in zip(boxes[0], scores[0], labels[0]):
                        # scores are sorted so we can break
                        if score < min_probability:
                            break
                        detection_dict = dict()
                        detection_dict["name"] = self.numbers_to_names[label]
                        detection_dict["percentage_probability"] = score * 100
                        detection_dict["box_points"] = box.astype(int).tolist()
                        model_detections.append(detection_dict)
                counting = 0

                # set output paths
                output_image_path = output_directory_path + '/auto/images/' + 'frame_' + str(video_frames_count) + '.jpg'
                output_xml_path = output_directory_path + '/auto/annotations/' + 'frame_' + str(video_frames_count) + '.xml'
                if model_detections and _annotate is True:
                    annotator_video.annotation_tag_open(output_xml_path=output_xml_path,
                                                        output_directory_path=output_directory_path,
                                                        image_filename='frame_' + str(video_frames_count) + '.jpg',
                                                        output_image_path=output_image_path,
                                                        image_h=image_h, image_w=image_w)
                for detection in model_detections:

                    # print(f'[DETECTION] {detection}')
                    if _annotate is True:
                        annotator_video.annotate(output_directory=output_directory_path,
                                                 name=detection["name"], _verbose=True,
                                                 output_xml_path=output_xml_path,
                                                 box_points=detection["box_points"])

                    objects_dir = output_directory_path + '/objects'
                    # todo directory CLASS
                    if save_in_class is True:
                        objects_dir = os.path.join(objects_dir, detection["name"])

                    counting += 1
                    label = detection["name"]
                    percentage_probability = detection["percentage_probability"]
                    box_points = detection["box_points"]
                    if custom_objects is not None:
                        if custom_objects[label] != "valid":
                            continue
                    detections.append(detection)
                    if display_object_name is False:
                        label = None
                    if display_percentage_probability is False:
                        percentage_probability = None
                    image_copy = draw_boxes(image_copy,
                                            box_points,
                                            display_box,
                                            label,
                                            percentage_probability)
                    # image_copy inverted by here
                    if extract_detected_objects is True:
                        splitted_copy = og_frame.copy()[box_points[1]:box_points[3], box_points[0]:box_points[2]]
                        if extract_during_video is False:
                            if output_type is "file":
                                if os.path.exists(objects_dir) is False:
                                    os.makedirs(objects_dir, exist_ok=True)
                                splitted_image_path = os.path.join(objects_dir, detection["name"] + "-" + str(counting) + ".jpg")

                                # todo don't overwrite
                                if os.path.exists(splitted_image_path):
                                    sub_counting = counting
                                    while os.path.exists(splitted_image_path):
                                        sub_counting += 1
                                        splitted_image_path = os.path.join(objects_dir, detection["name"] + "-" + str(sub_counting) + ".jpg")

                                # todo IMAGE save from IMAGE
                                cv2.imwrite(splitted_image_path, splitted_copy)
                                detected_objects_image_array.append(splitted_image_path)
                            elif output_type is "array":
                                detected_objects_image_array.append(splitted_copy)
                        # todo IMAGE save from VIDEO
                        elif extract_during_video is True:
                            if os.path.exists(objects_dir) is False:
                                os.makedirs(objects_dir, exist_ok=True)
                            splitted_image_path = os.path.join(objects_dir, detection["name"] + "-" + str(counting) + ".jpg")

                            # todo don't overwrite
                            if os.path.exists(splitted_image_path):
                                sub_counting = counting
                                while os.path.exists(splitted_image_path):
                                    sub_counting += 1
                                    splitted_image_path = os.path.join(objects_dir, detection["name"] + "-" + str(sub_counting) + ".jpg")

                            cv2.imwrite(splitted_image_path, splitted_copy)
                            detected_objects_image_array.append(splitted_copy)

                if model_detections and _annotate is True:
                    annotator_video.annotation_tag_close(output_xml_path)
                    I_ANNOTATION += 1

                if extract_during_video is False or _annotate is True:
                    if output_type is "file":
                        if _annotate is False:
                            if not os.path.exists(output_directory_path + '/auto/detected_images/'):
                                os.makedirs(output_directory_path + '/auto/detected_images/', exist_ok=True)
                            output_image_path = output_directory_path + '/auto/detected_images/' + 'frame_' + str(video_frames_count) + '.jpg'
                            cv2.imwrite(output_image_path, image_copy)
                            I_DETECTED_IMAGES += 1
                        elif _annotate is True:
                            if model_detections:
                                if not os.path.exists(output_directory_path + '/auto/images/'):
                                    os.makedirs(output_directory_path + '/auto/images/')
                                output_image_path = output_directory_path + '/auto/images/' + 'frame_' + str(video_frames_count) + '.jpg'
                                cv2.imwrite(output_image_path, untouched_original_frame)
                                I_IMAGES += 1
                                if not os.path.exists(output_directory_path + '/auto/detected_images/'):
                                    os.makedirs(output_directory_path + '/auto/detected_images/')
                                output_image_path = output_directory_path + '/auto/detected_images/' + 'frame_' + str(video_frames_count) + '.jpg'
                                cv2.imwrite(output_image_path, image_copy)
                                I_DETECTED_IMAGES += 1

                return image_copy, detections, detected_objects_image_array

            # except Exception as e:
            #     print('Default.detectObjectsFromImage:', e)

    # def CustomObjects(self, person=False, bicycle=False, car=False, motorcycle=False, airplane=False,
    #                   bus=False, train=False, truck=False, boat=False, traffic_light=False, fire_hydrant=False,
    #                   stop_sign=False,
    #                   parking_meter=False, bench=False, bird=False, cat=False, dog=False, horse=False, sheep=False,
    #                   cow=False, elephant=False, bear=False, zebra=False,
    #                   giraffe=False, backpack=False, umbrella=False, handbag=False, tie=False, suitcase=False,
    #                   frisbee=False, skis=False, snowboard=False,
    #                   sports_ball=False, kite=False, baseball_bat=False, baseball_glove=False, skateboard=False,
    #                   surfboard=False, tennis_racket=False,
    #                   bottle=False, wine_glass=False, cup=False, fork=False, knife=False, spoon=False, bowl=False,
    #                   banana=False, apple=False, sandwich=False, orange=False,
    #                   broccoli=False, carrot=False, hot_dog=False, pizza=False, donut=False, cake=False, chair=False,
    #                   couch=False, potted_plant=False, bed=False,
    #                   dining_table=False, toilet=False, tv=False, laptop=False, mouse=False, remote=False,
    #                   keyboard=False, cell_phone=False, microwave=False,
    #                   oven=False, toaster=False, sink=False, refrigerator=False, book=False, clock=False, vase=False,
    #                   scissors=False, teddy_bear=False, hair_dryer=False,
    #                   toothbrush=False):
    #     custom_objects_dict = {}
    #     input_values = [person, bicycle, car, motorcycle, airplane,
    #                     bus, train, truck, boat, traffic_light, fire_hydrant, stop_sign,
    #                     parking_meter, bench, bird, cat, dog, horse, sheep, cow, elephant, bear, zebra,
    #                     giraffe, backpack, umbrella, handbag, tie, suitcase, frisbee, skis, snowboard,
    #                     sports_ball, kite, baseball_bat, baseball_glove, skateboard, surfboard, tennis_racket,
    #                     bottle, wine_glass, cup, fork, knife, spoon, bowl, banana, apple, sandwich, orange,
    #                     broccoli, carrot, hot_dog, pizza, donut, cake, chair, couch, potted_plant, bed,
    #                     dining_table, toilet, tv, laptop, mouse, remote, keyboard, cell_phone, microwave,
    #                     oven, toaster, sink, refrigerator, book, clock, vase, scissors, teddy_bear, hair_dryer,
    #                     toothbrush]
    #     actual_labels = ["person", "bicycle", "car", "motorcycle", "airplane",
    #                      "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign",
    #                      "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear",
    #                      "zebra",
    #                      "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis",
    #                      "snowboard",
    #                      "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
    #                      "tennis racket",
    #                      "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich",
    #                      "orange",
    #                      "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant",
    #                      "bed",
    #                      "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
    #                      "microwave",
    #                      "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
    #                      "hair dryer",
    #                      "toothbrush"]
    #     for input_value, actual_label in zip(input_values, actual_labels):
    #         if input_value is True:
    #             custom_objects_dict[actual_label] = "valid"
    #         else:
    #             custom_objects_dict[actual_label] = "invalid"
    #     return custom_objects_dict


class VideoObjectDetection:

    def __init__(self):
        self.__modelType = ""
        self.modelPath = ""
        self.__modelPathAdded = False
        self.__modelLoaded = False
        self.__detector = None
        self.__input_image_min = 1333
        self.__input_image_max = 800
        self.__detection_storage = None
        self.numbers_to_names = {0: 'person', 1: 'bicycle', 2: 'car', 3: 'motorcycle', 4: 'airplane', 5: 'bus',
                                 6: 'train',
                                 7: 'truck', 8: 'boat', 9: 'traffic light', 10: 'fire hydrant', 11: 'stop sign',
                                 12: 'parking meter',
                                 13: 'bench', 14: 'bird', 15: 'cat', 16: 'dog', 17: 'horse', 18: 'sheep', 19: 'cow',
                                 20: 'elephant',
                                 21: 'bear', 22: 'zebra', 23: 'giraffe', 24: 'backpack', 25: 'umbrella', 26: 'handbag',
                                 27: 'tie',
                                 28: 'suitcase', 29: 'frisbee', 30: 'skis', 31: 'snowboard', 32: 'sports ball',
                                 33: 'kite',
                                 34: 'baseball bat', 35: 'baseball glove', 36: 'skateboard', 37: 'surfboard',
                                 38: 'tennis racket',
                                 39: 'bottle', 40: 'wine glass', 41: 'cup', 42: 'fork', 43: 'knife', 44: 'spoon',
                                 45: 'bowl',
                                 46: 'banana', 47: 'apple', 48: 'sandwich', 49: 'orange', 50: 'broccoli', 51: 'carrot',
                                 52: 'hot dog',
                                 53: 'pizza', 54: 'donut', 55: 'cake', 56: 'chair', 57: 'couch', 58: 'potted plant',
                                 59: 'bed',
                                 60: 'dining table', 61: 'toilet', 62: 'tv', 63: 'laptop', 64: 'mouse', 65: 'remote',
                                 66: 'keyboard',
                                 67: 'cell phone', 68: 'microwave', 69: 'oven', 70: 'toaster', 71: 'sink',
                                 72: 'refrigerator',
                                 73: 'book', 74: 'clock', 75: 'vase', 76: 'scissors', 77: 'teddy bear',
                                 78: 'hair dryer',
                                 79: 'toothbrush'}

    def setModelTypeAsRetinaNet(self):
        self.__modelType = "retinanet"

    def setModelTypeAsYOLOv3(self):
        self.__modelType = "yolov3"

    def setModelTypeAsTinyYOLOv3(self):
        self.__modelType = "tinyyolov3"

    def setModelPath(self, model_path):
        if self.__modelPathAdded is False:
            self.modelPath = model_path
            self.__modelPathAdded = True

    def loadModel(self, detection_speed="normal"):
        if self.__modelLoaded is False:
            frame_detector = ObjectDetection()
            if self.__modelType is "retinanet":
                frame_detector.setModelTypeAsRetinaNet()
            elif self.__modelType is "yolov3":
                frame_detector.setModelTypeAsYOLOv3()
            elif self.__modelType is "tinyyolov3":
                frame_detector.setModelTypeAsTinyYOLOv3()
            frame_detector.setModelPath(self.modelPath)
            frame_detector.loadModel(detection_speed)
            self.__detector = frame_detector
            self.__modelLoaded = True

    def detectObjectsFromVideo(self, input_file_path="",
                               camera_input=None,
                               frames_per_second=20,
                               frame_detection_interval=1,
                               minimum_percentage_probability=50,
                               display_percentage_probability=True,
                               display_object_name=True, display_box=True,
                               save_detected_video=True,
                               per_frame_function=None,
                               video_complete_function=None,
                               extract_detected_objects=False,
                               custom_objects=None,
                               extract_during_video=False,
                               save_in_class=False,
                               output_directory_path="",
                               _annotate=False,
                               start_frame=0):
        ########################
        # DEFAULT VIDEO DETECTION
        ########################
        print('-- plugged: Detection.detectObjectsFromVideo')
        global PAUSE_FRAME, START_FRAME, video_frames_count, VIDEO_CLOSED, MINIMUM_PERCENTAGE_PROBABILITY
        global KILL_LOOP, FRAME_DETECTION_INTERVAL

        output_frames_dict = {}
        output_frames_count_dict = {}
        try:
            input_video = cv2.VideoCapture(input_file_path)
            input_video.set(cv2.CAP_PROP_POS_FRAMES, start_frame)
            if camera_input is not None:
                input_video = camera_input
            output_video_filepath = os.path.join(output_directory_path, 'capture.avi')
            frame_width = int(input_video.get(3))
            frame_height = int(input_video.get(4))
            output_video = cv2.VideoWriter(output_video_filepath, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'),
                                           frames_per_second,
                                           (frame_width, frame_height))
        except Exception as e:
            print(f'[E] {e}')
        counting = 0
        video_frames_count = start_frame
        MINIMUM_PERCENTAGE_PROBABILITY = minimum_percentage_probability
        FRAME_DETECTION_INTERVAL = frame_detection_interval
        #########################################
        # READ FRAMES
        #########################################
        while input_video.isOpened() and KILL_LOOP is False:
            VIDEO_CLOSED = False
            input_video.set(cv2.CAP_PROP_POS_FRAMES, video_frames_count)
            ret, frame = input_video.read()
            if ret is True:
                video_frames_count += 1
                output_objects_array = []
                counting += 1
                detected_copy = frame.copy()
                # todo swap out frame detection interval formula
                check_frame_interval = counting % FRAME_DETECTION_INTERVAL
                print('check_frame_interval:', check_frame_interval)
                if counting is 1 or check_frame_interval is 0:

                    if extract_detected_objects is False:
                        detected_copy, output_objects_array, detected_objects_image_array = self.__detector.detectObjectsFromImage(
                            input_image=frame, input_type="array", output_type="array",
                            minimum_percentage_probability=MINIMUM_PERCENTAGE_PROBABILITY,
                            display_percentage_probability=display_percentage_probability,
                            display_object_name=display_object_name,
                            display_box=display_box,
                            custom_objects=custom_objects,
                            extract_detected_objects=extract_detected_objects,
                            extract_during_video=extract_during_video,
                            save_in_class=save_in_class,
                            video_frames_count=video_frames_count,
                            output_directory_path=output_directory_path,
                            _annotate=_annotate)
                    elif extract_detected_objects is True:
                        detected_copy, output_objects_array, detected_objects_image_array = self.__detector.detectObjectsFromImage(
                            input_image=frame, input_type="array", output_type="file",
                            minimum_percentage_probability=MINIMUM_PERCENTAGE_PROBABILITY,
                            display_percentage_probability=display_percentage_probability,
                            display_object_name=display_object_name,
                            display_box=display_box,
                            custom_objects=custom_objects,
                            extract_detected_objects=extract_detected_objects,
                            extract_during_video=extract_during_video,
                            save_in_class=save_in_class,
                            video_frames_count=video_frames_count,
                            output_directory_path=output_directory_path,
                            _annotate=_annotate)
                # kill loop uncalled: proceed as usual
                if KILL_LOOP is False:
                    if PAUSE_FRAME is True:
                        while PAUSE_FRAME is True:
                            time.sleep(0.5)
                    output_frames_dict[counting] = output_objects_array
                    output_objects_count = {}
                    if save_detected_video is True:
                        output_video.write(detected_copy)
                    if counting is 1 or check_frame_interval is 0:
                        if per_frame_function is not None:
                            per_frame_function(video_frames_count, output_objects_array, output_objects_count,
                                               detected_copy)
            else:
                break
        # kill loop uncalled: proceed as usual
        if KILL_LOOP is False:
            VIDEO_CLOSED = True
            if video_complete_function is not None:
                this_video_output_object_array = []
                this_video_counting_array = []
                this_video_counting = {}
                for aa in range(counting):
                    this_video_output_object_array.append(output_frames_dict[aa + 1])
                    this_video_counting_array.append(output_frames_count_dict[aa + 1])
                for eachCountingDict in this_video_counting_array:
                    for eachItem in eachCountingDict:
                        try:
                            this_video_counting[eachItem] = this_video_counting[eachItem] + eachCountingDict[eachItem]
                        except:
                            this_video_counting[eachItem] = eachCountingDict[eachItem]
                for eachCountingItem in this_video_counting:
                    this_video_counting[eachCountingItem] = int(this_video_counting[eachCountingItem] / counting)
                video_complete_function(this_video_output_object_array, this_video_counting_array,
                                        this_video_counting)
            input_video.release()
            output_video.release()
            if save_detected_video is True:
                return output_video_filepath
        # kill loop called: skip things and leave
        else:
            print('-- self destructing...')
            KILL_LOOP = False

    # def CustomObjects(self, person=False, bicycle=False, car=False, motorcycle=False, airplane=False,
    #                   bus=False, train=False, truck=False, boat=False, traffic_light=False, fire_hydrant=False,
    #                   stop_sign=False,
    #                   parking_meter=False, bench=False, bird=False, cat=False, dog=False, horse=False, sheep=False,
    #                   cow=False, elephant=False, bear=False, zebra=False,
    #                   giraffe=False, backpack=False, umbrella=False, handbag=False, tie=False, suitcase=False,
    #                   frisbee=False, skis=False, snowboard=False,
    #                   sports_ball=False, kite=False, baseball_bat=False, baseball_glove=False, skateboard=False,
    #                   surfboard=False, tennis_racket=False,
    #                   bottle=False, wine_glass=False, cup=False, fork=False, knife=False, spoon=False, bowl=False,
    #                   banana=False, apple=False, sandwich=False, orange=False,
    #                   broccoli=False, carrot=False, hot_dog=False, pizza=False, donut=False, cake=False, chair=False,
    #                   couch=False, potted_plant=False, bed=False,
    #                   dining_table=False, toilet=False, tv=False, laptop=False, mouse=False, remote=False,
    #                   keyboard=False, cell_phone=False, microwave=False,
    #                   oven=False, toaster=False, sink=False, refrigerator=False, book=False, clock=False, vase=False,
    #                   scissors=False, teddy_bear=False, hair_dryer=False,
    #                   toothbrush=False):
    #     custom_objects_dict = {}
    #     input_values = [person, bicycle, car, motorcycle, airplane,
    #                     bus, train, truck, boat, traffic_light, fire_hydrant, stop_sign,
    #                     parking_meter, bench, bird, cat, dog, horse, sheep, cow, elephant, bear, zebra,
    #                     giraffe, backpack, umbrella, handbag, tie, suitcase, frisbee, skis, snowboard,
    #                     sports_ball, kite, baseball_bat, baseball_glove, skateboard, surfboard, tennis_racket,
    #                     bottle, wine_glass, cup, fork, knife, spoon, bowl, banana, apple, sandwich, orange,
    #                     broccoli, carrot, hot_dog, pizza, donut, cake, chair, couch, potted_plant, bed,
    #                     dining_table, toilet, tv, laptop, mouse, remote, keyboard, cell_phone, microwave,
    #                     oven, toaster, sink, refrigerator, book, clock, vase, scissors, teddy_bear, hair_dryer,
    #                     toothbrush]
    #     actual_labels = ["person", "bicycle", "car", "motorcycle", "airplane",
    #                      "bus", "train", "truck", "boat", "traffic light", "fire hydrant", "stop sign",
    #                      "parking meter", "bench", "bird", "cat", "dog", "horse", "sheep", "cow", "elephant", "bear",
    #                      "zebra",
    #                      "giraffe", "backpack", "umbrella", "handbag", "tie", "suitcase", "frisbee", "skis",
    #                      "snowboard",
    #                      "sports ball", "kite", "baseball bat", "baseball glove", "skateboard", "surfboard",
    #                      "tennis racket",
    #                      "bottle", "wine glass", "cup", "fork", "knife", "spoon", "bowl", "banana", "apple", "sandwich",
    #                      "orange",
    #                      "broccoli", "carrot", "hot dog", "pizza", "donut", "cake", "chair", "couch", "potted plant",
    #                      "bed",
    #                      "dining table", "toilet", "tv", "laptop", "mouse", "remote", "keyboard", "cell phone",
    #                      "microwave",
    #                      "oven", "toaster", "sink", "refrigerator", "book", "clock", "vase", "scissors", "teddy bear",
    #                      "hair dryer",
    #                      "toothbrush"]
    #     for input_value, actual_label in zip(input_values, actual_labels):
    #         if input_value is True:
    #             custom_objects_dict[actual_label] = "valid"
    #         else:
    #             custom_objects_dict[actual_label] = "invalid"
    #     return custom_objects_dict

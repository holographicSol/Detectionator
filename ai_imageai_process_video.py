""" Written by Benjamin Jack Cullen """

import time
import datetime
import dt
from matplotlib import pyplot as plt
from imageai.Detection import VideoObjectDetection
import os
from datetime import timedelta

color_index = {'bus': 'red', 'handbag': 'steelblue', 'giraffe': 'orange', 'spoon': 'gray', 'cup': 'yellow', 'chair': 'green', 'elephant': 'pink', 'truck': 'indigo', 'motorcycle': 'azure', 'refrigerator': 'gold', 'keyboard': 'violet', 'cow': 'magenta', 'mouse': 'crimson', 'sports ball': 'raspberry', 'horse': 'maroon', 'cat': 'orchid', 'boat': 'slateblue', 'hot dog': 'navy', 'apple': 'cobalt', 'parking meter': 'aliceblue', 'sandwich': 'skyblue', 'skis': 'deepskyblue', 'microwave': 'peacock', 'knife': 'cadetblue', 'baseball bat': 'cyan', 'oven': 'lightcyan', 'carrot': 'coldgrey', 'scissors': 'seagreen', 'sheep': 'deepgreen', 'toothbrush': 'cobaltgreen', 'fire hydrant': 'limegreen', 'remote': 'forestgreen', 'bicycle': 'olivedrab', 'toilet': 'ivory', 'tv': 'khaki', 'skateboard': 'palegoldenrod', 'train': 'cornsilk', 'zebra': 'wheat', 'tie': 'burlywood', 'orange': 'melon', 'bird': 'bisque', 'dining table': 'chocolate', 'hair drier': 'sandybrown', 'cell phone': 'sienna', 'sink': 'coral', 'bench': 'salmon', 'bottle': 'brown', 'car': 'silver', 'bowl': 'maroon', 'tennis racket': 'palevilotered', 'airplane': 'lavenderblush', 'pizza': 'hotpink', 'umbrella': 'deeppink', 'bear': 'plum', 'fork': 'purple', 'laptop': 'indigo', 'vase': 'mediumpurple', 'baseball glove': 'slateblue', 'traffic light': 'mediumblue', 'bed': 'navy', 'broccoli': 'royalblue', 'backpack': 'slategray', 'snowboard': 'skyblue', 'kite': 'cadetblue', 'teddy bear': 'peacock', 'clock': 'lightcyan', 'wine glass': 'teal', 'frisbee': 'aquamarine', 'donut': 'mincream', 'suitcase': 'seagreen', 'dog': 'springgreen', 'banana': 'emeraldgreen', 'person': 'honeydew', 'surfboard': 'palegreen', 'cake': 'sapgreen', 'book': 'lawngreen', 'potted plant': 'greenyellow', 'toaster': 'ivory', 'stop sign': 'beige', 'couch': 'khaki'}
resized = False
T_START_PERF = 0
T_START_DATETIME = 0
DUMP = False
PRIMARY_TARGET = None
SECONDARY_TARGET = None
TOTAL_FRAMES = 0
FRAME_NUM = 0
RETURNED_FRAME = ""
t_frame = time.perf_counter()
t_frame_elapsed = 0
fps = 0
OUTPUT_OBJECTS_ARRAY = []
UNIQUE_OBJECTS = []
total_time_elapsed = 0


def GetTime(_sec):
    sec = timedelta(seconds=_sec)
    d = datetime.datetime(1, 1, 1) + sec
    return "%d:%d:%d:%d" % (d.day - 1, d.hour, d.minute, d.second)


def process_video(frame_number, output_objects_array, output_objects_count, returned_frame):
    global resized, t_frame, RETURNED_FRAME, FRAME_NUM, fps, OUTPUT_OBJECTS_ARRAY_TOTAL, t_frame_elapsed
    global total_time_elapsed

    FRAME_NUM = frame_number
    # display frame information
    fps = (100 / (time.perf_counter() - t_frame)) / 100
    t_frame_elapsed = time.perf_counter() - t_frame
    t_frame = time.perf_counter()
    # total_time_elapsed = datetime.timedelta(seconds=(time.perf_counter()-T_START_PERF))
    total_time_elapsed = GetTime(_sec=(time.perf_counter()-T_START_PERF))
    print(f'{dt.dt()} [AI] OBJECT DETECTION')
    print(f'{dt.dt()} [TIME STARTED] {T_START_DATETIME}')
    print(f'{dt.dt()} [TIME ELAPSED] {str(total_time_elapsed)}')
    print(f'{dt.dt()} [AI] [FILE] {INPUT_FILE}')
    print(f'{dt.dt()} [FPS] {fps}')
    print(f'{dt.dt()} [FRAME] {frame_number} / {TOTAL_FRAMES}')

    # display detection information
    for d in output_objects_array:
        OUTPUT_OBJECTS_ARRAY.append(d)
        if d.get("name") not in UNIQUE_OBJECTS:
            UNIQUE_OBJECTS.append(d.get("name"))
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

    # display video
    if DUMP is False:
        plt.clf()
        if resized is False:
            plt.axis("off")
            plt.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=None)
            plt.margins(0, 0, tight=True)
            resized = True
        plt.imshow(returned_frame, interpolation="none")
        plt.pause(0.01)
    RETURNED_FRAME = returned_frame


def entry_point(input_file_path="",
                camera_input=None,
                frames_per_second=20,
                frame_detection_interval=1, minimum_percentage_probability=50,
                display_percentage_probability=True, display_object_name=True, display_box=True,
                save_detected_video=True,
                video_complete_function=None, extract_detected_objects=False,
                custom_objects=None, _ai_model=None, _ai_model_path=None, _ai_model_json=None,
                _detection_speed='normal', _dump=False, _PRIMARY_TARGET=None, _SECONDARY_TARGET=None,
                save_in_class=False, total_frames=0, t_start_perf=0, t_start_datetime=0,
                output_directory_path="", _annotate=False, start_frame=0):
    global DUMP
    global PRIMARY_TARGET
    global SECONDARY_TARGET
    global TOTAL_FRAMES
    global T_START_PERF
    global T_START_DATETIME
    global INPUT_FILE
    INPUT_FILE = input_file_path
    T_START_PERF = t_start_perf
    T_START_DATETIME = t_start_datetime
    DUMP = _dump
    PRIMARY_TARGET = _PRIMARY_TARGET
    SECONDARY_TARGET = _SECONDARY_TARGET
    TOTAL_FRAMES = total_frames
    video_detector = VideoObjectDetection()
    if _ai_model_json is not None:
        # use custom detection if a json is specified
        from imageai.Detection.Custom import CustomVideoObjectDetection
        video_detector = CustomVideoObjectDetection()
        video_detector.setModelTypeAsYOLOv3()
        video_detector.setJsonPath(_ai_model_json)

    elif _ai_model is 'yolov3':
        video_detector.setModelTypeAsYOLOv3()

    elif _ai_model is 'resnet50':
        video_detector.setModelTypeAsRetinaNet()

    video_detector.setModelPath(_ai_model_path)
    if _ai_model_json is None:
        video_detector.loadModel(detection_speed=_detection_speed)

    else:
        video_detector.loadModel()
    video_detector.detectObjectsFromVideo(input_file_path=input_file_path,
                                          camera_input=None,
                                          frames_per_second=frames_per_second,
                                          frame_detection_interval=frame_detection_interval,
                                          minimum_percentage_probability=minimum_percentage_probability,
                                          display_percentage_probability=display_percentage_probability,
                                          display_object_name=display_object_name,
                                          display_box=display_box,
                                          save_detected_video=save_detected_video,
                                          per_frame_function=process_video,
                                          video_complete_function=video_complete_function,
                                          extract_detected_objects=extract_detected_objects,
                                          custom_objects=custom_objects,
                                          extract_during_video=extract_detected_objects,
                                          save_in_class=save_in_class,
                                          output_directory_path=output_directory_path,
                                          _annotate=_annotate,
                                          start_frame=start_frame
                                          )

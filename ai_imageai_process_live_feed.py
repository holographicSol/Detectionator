""" Written by Benjamin Jack Cullen """

import time
import cv2
from imageai.Detection import VideoObjectDetection
from imageai.Detection.Custom import CustomVideoObjectDetection
from matplotlib import pyplot as plt
import dt
import datetime


color_index = {'bus': 'red', 'handbag': 'steelblue', 'giraffe': 'orange', 'spoon': 'gray', 'cup': 'yellow', 'chair': 'green', 'elephant': 'pink', 'truck': 'indigo', 'motorcycle': 'azure', 'refrigerator': 'gold', 'keyboard': 'violet', 'cow': 'magenta', 'mouse': 'crimson', 'sports ball': 'raspberry', 'horse': 'maroon', 'cat': 'orchid', 'boat': 'slateblue', 'hot dog': 'navy', 'apple': 'cobalt', 'parking meter': 'aliceblue', 'sandwich': 'skyblue', 'skis': 'deepskyblue', 'microwave': 'peacock', 'knife': 'cadetblue', 'baseball bat': 'cyan', 'oven': 'lightcyan', 'carrot': 'coldgrey', 'scissors': 'seagreen', 'sheep': 'deepgreen', 'toothbrush': 'cobaltgreen', 'fire hydrant': 'limegreen', 'remote': 'forestgreen', 'bicycle': 'olivedrab', 'toilet': 'ivory', 'tv': 'khaki', 'skateboard': 'palegoldenrod', 'train': 'cornsilk', 'zebra': 'wheat', 'tie': 'burlywood', 'orange': 'melon', 'bird': 'bisque', 'dining table': 'chocolate', 'hair drier': 'sandybrown', 'cell phone': 'sienna', 'sink': 'coral', 'bench': 'salmon', 'bottle': 'brown', 'car': 'silver', 'bowl': 'maroon', 'tennis racket': 'palevilotered', 'airplane': 'lavenderblush', 'pizza': 'hotpink', 'umbrella': 'deeppink', 'bear': 'plum', 'fork': 'purple', 'laptop': 'indigo', 'vase': 'mediumpurple', 'baseball glove': 'slateblue', 'traffic light': 'mediumblue', 'bed': 'navy', 'broccoli': 'royalblue', 'backpack': 'slategray', 'snowboard': 'skyblue', 'kite': 'cadetblue', 'teddy bear': 'peacock', 'clock': 'lightcyan', 'wine glass': 'teal', 'frisbee': 'aquamarine', 'donut': 'mincream', 'suitcase': 'seagreen', 'dog': 'springgreen', 'banana': 'emeraldgreen', 'person': 'honeydew', 'surfboard': 'palegreen', 'cake': 'sapgreen', 'book': 'lawngreen', 'potted plant': 'greenyellow', 'toaster': 'ivory', 'stop sign': 'beige', 'couch': 'khaki'}
resized = False
T_START_PERF = 0
T_START_DATETIME = 0
DUMP = False
PRIMARY_TARGET = None
SECONDARY_TARGET = None
TARGETS = []
ACQUIRED_TARGETS = []
RETURNED_FRAME = ""
t_frame = time.perf_counter()
FRAME_NUM = 0
fps = 0
total_time_elapsed = 0

OUTPUT_OBJECTS_ARRAY = []
UNIQUE_OBJECTS = []

CAMERA_WARNING = ''
CAMERA_INPUT = 0
CAMERA = []
KILL_LOOP = False
COMPLETED = False


def GetTime(_sec):
    sec = datetime.timedelta(seconds=_sec)
    d = datetime.datetime(1, 1, 1) + sec
    return "%d:%d:%d:%d" % (d.day - 1, d.hour, d.minute, d.second)


def process_live_feed(frame_number, output_objects_array, output_count, returned_frame):
    global resized, t_frame, RETURNED_FRAME, FRAME_NUM, fps, total_time_elapsed, OUTPUT_OBJECTS_ARRAY_TOTAL
    global TARGETS, ACQUIRED_TARGETS
    FRAME_NUM = frame_number
    # display frame information
    fps = (100 / (time.perf_counter() - t_frame)) / 100
    t_frame = time.perf_counter()
    total_time_elapsed = GetTime(_sec=(time.perf_counter() - T_START_PERF))
    print(f'{dt.dt()} [AI] OBJECT DETECTION')
    print(f'{dt.dt()} [TIME STARTED] {T_START_DATETIME}')
    print(f'{dt.dt()} [TIME ELAPSED] {str(total_time_elapsed)}')
    print(f'{dt.dt()} [FPS] {fps}')
    print(f'{dt.dt()} [FRAME] {frame_number}')

    # display detection information
    for d in output_objects_array:
        OUTPUT_OBJECTS_ARRAY.append(d)
        if d.get("name") not in UNIQUE_OBJECTS:
            UNIQUE_OBJECTS.append(d.get("name"))
        IN_TARGETS = False
        ACQUIRED_TARGETS = []
        for X in TARGETS:
            if d.get("name") == X.get("name"):
                print(f'{dt.dt()} [DETECTED] [TARGET] [NAME:{d.get("name")}] [PROBABILITY:{d.get("percentage_probability")}]')
                IN_TARGETS = True
                Y = X
                Y.update({'detection_percentage_probability': d.get('percentage_probability')})
                if Y not in ACQUIRED_TARGETS:
                    ACQUIRED_TARGETS.append(Y)
                    break
        if IN_TARGETS is False:
            print(f'{dt.dt()} [DETECTED] [OBJECT] [NAME:{d.get("name")}] [PROBABILITY:{d.get("percentage_probability")}]')

    # if DUMP is False:
    #     plt.clf()
    #     if resized is False:
    #         plt.axis("off")
    #         plt.tight_layout(pad=0.0, h_pad=0.0, w_pad=0.0, rect=None)
    #         plt.margins(0, 0, tight=True)
    #         resized = True
    #     plt.imshow(returned_frame, interpolation="none")
    #     plt.pause(0.01)

    RETURNED_FRAME = returned_frame
    # print('RETURNED_FRAME:', RETURNED_FRAME)


def entry_point_live_feed(input_file_path="", camera_input=None, frames_per_second=20,
                          frame_detection_interval=1, minimum_percentage_probability=50, log_progress=False,
                          display_percentage_probability=True, display_object_name=True, save_detected_video=True,
                          display_box=True,
                          per_frame_function=None,
                          video_complete_function=None, return_detected_frame=False, extract_detected_objects=False,
                          detection_timeout=None,
                          _model_path=None, _model=None, _ai_json_path=None,
                          _PRIMARY_TARGET=None, _SECONDARY_TARGET=None, save_in_class=False, t_start_datetime=0,
                          t_start_perf=0,
                          output_directory_path="", _annotate=False):
    global PRIMARY_TARGET
    global SECONDARY_TARGET
    global T_START_PERF
    global T_START_DATETIME
    global CAMERA_WARNING
    global CAMERA_INPUT
    global CAMERA
    global KILL_LOOP
    global COMPLETED
    COMPLETED = False
    try:
        T_START_PERF = t_start_perf
        T_START_DATETIME = t_start_datetime
        PRIMARY_TARGET = _PRIMARY_TARGET
        SECONDARY_TARGET = _SECONDARY_TARGET
        if _ai_json_path is not None:
            detector = CustomVideoObjectDetection()
            detector.setModelTypeAsYOLOv3()
            detector.setModelPath(_model_path)
            detector.setJsonPath(_ai_json_path)
        else:
            detector = VideoObjectDetection()
            detector.setModelTypeAsYOLOv3()
            detector.setModelPath(_model_path)
        detector.loadModel()
        CAMERA_INPUT = camera_input

        while KILL_LOOP is False:
            camera_input = CAMERA_INPUT
            CAMERA = cv2.VideoCapture(camera_input)

            print(f'{dt.dt()} [CAMERA]', CAMERA)
            if CAMERA is None or not CAMERA.isOpened():
                CAMERA_WARNING = f'Warning: unable to open video source: {CAMERA}'
            else:
                CAMERA_WARNING = ''
                detector.detectObjectsFromVideo(camera_input=CAMERA,
                                                frames_per_second=frames_per_second,
                                                frame_detection_interval=frame_detection_interval,
                                                minimum_percentage_probability=minimum_percentage_probability,
                                                display_percentage_probability=display_percentage_probability,
                                                display_object_name=display_object_name,
                                                display_box=display_box,
                                                save_detected_video=save_detected_video,
                                                per_frame_function=process_live_feed,
                                                video_complete_function=None,
                                                extract_detected_objects=extract_detected_objects,
                                                extract_during_video=True,
                                                save_in_class=save_in_class,
                                                output_directory_path=output_directory_path,
                                                _annotate=_annotate,
                                                start_frame=0)
            time.sleep(1)
        if KILL_LOOP is True:
            KILL_LOOP = False
            print('-- destroyed outer loop')
    except Exception as e:
        print(e)
    COMPLETED = True

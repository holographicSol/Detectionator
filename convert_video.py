""" Written by Benjamin Jack Cullen """

import os
import cv2
import time
import datetime
import dt

T_START_PERF = time.perf_counter()
T_START_DATETIME = datetime.datetime.now()


def convert(IN_DIR: str, OUT_DIR: str, FPS: int):
    file_list = os.listdir(IN_DIR)
    for _file in file_list:
        try:
            FILE_IN = os.path.join(IN_DIR, _file)
            cap = cv2.VideoCapture(FILE_IN)
            video_fps = round(cap.get(cv2.CAP_PROP_FPS))
            tf = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            hop = round(video_fps / FPS)
            FILE_OUT = os.path.join(OUT_DIR, _file+'_(FPS_'+str(FPS)+').avi')
            print('_'*50)
            print(f'{dt.dt()} [TIME STARTED] {T_START_DATETIME}')
            print(f'{dt.dt()} [TIME ELAPSED] {str(datetime.timedelta(seconds=(time.perf_counter() - T_START_PERF)))}')
            print(f'{dt.dt()} [FILE_IN] {FILE_IN}')
            print(f'{dt.dt()} [FILE_OUT] {FILE_OUT}')
            print(f'{dt.dt()} [FPS] {video_fps}')
            print(f'{dt.dt()} [TOTAL_FRAMES] {tf}')
            print(f'{dt.dt()} [HOP] {hop}')
            try:
                input_video = cv2.VideoCapture(FILE_IN)
                output_video_filepath = FILE_OUT
                frame_width = int(input_video.get(3))
                frame_height = int(input_video.get(4))
                output_video = cv2.VideoWriter(output_video_filepath, cv2.VideoWriter_fourcc('M', 'J', 'P', 'G'), fps=FPS, frameSize=(frame_width, frame_height))
                i_frame = 0
                curr_frame = 0
                while True:
                    i_frame += 1
                    curr_frame += 1
                    ret, frame = cap.read()
                    if not ret:
                        break
                    if curr_frame % hop == 0:
                        print(' ' * 100, end='\r', flush=True)
                        print('[FRAME] '+str(i_frame)+'/'+str(tf), end='\r', flush=True)
                        output_video.write(frame)
                cap.release()
            except Exception as e:
                print(f'{dt.dt()} [ERROR] {e}')
        except Exception as e:
            print(f'{dt.dt()} [ERROR] {e}')

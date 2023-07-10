"""
Written by Benjamin Jack Cullen aka Holographic_Sol

Mechanized application template. Creates a grid of objects, creates modules containing functions pertaining to the objects and plugs the objects
into the modules created.

No need to move objects around tweaking geometries etc. No need to plug them in. Better workflow.
Object workflow: show/hide/repurpose/etc.
Blow it up, then go inside and grill some food.

1. Dial in Configuration 1 & 2 values according to desired specs.
2. Run. (objects will be automatically created in a grid and automatically plugged into automatically created modules).
3. Turn off auto_setup to ensure any changes made to the automatically created modules will not be overwritten.
4. Click something, it's all plugged in and ready.
5. Go ahead and start writing code straight into the mechanically created modules:
    auto_gen_btnx_function.py
    auto_gen_btnx_double_function.py
    auto_gen_btnx_title_toolbar_functions.py
    auto_gen_qle_returnpressed_connect_function.py
    auto_gen_qle_double_returnpressed_connect_function.py
    auto_gen_tbx_update_function.py

"""
import os
import sys
import ast
import time
import datetime
import subprocess
from PIL import Image
import win32com.client
import win32com
import pathlib
import cv2
import numpy

from PyQt5 import QtCore
from PyQt5.QtGui import *
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtMultimedia import *
from PyQt5.QtGui import QIcon, QCursor, QFont, QPainter, QBrush, QColor
from PyQt5.QtWidgets import QPushButton, QLabel, QDesktopWidget, QSlider
from PyQt5.QtCore import Qt, QThread, QSize, QPoint, QCoreApplication, QTimer

from imageai import Detection
from imageai.Detection import Custom

import annotator_video
import ai_imageai_process_live_feed
import ai_imageai_process_video
import application_images
import ai_imageai_process_image
import ai_imageai_training_detection
import ai_imageai_training_prediction


# CONFIGURATION 1 - SETUP APPLICATION TEMPLATE BOOLEAN
auto_setup = False  # WARNING (SET FALSE IF AFTER SETUP IS COMPLETE OR MODULES WILL BE OVERWRITTEN).
auto_generate = True  # creates objects automatically using values below.
auto_generate_btn = True  # enables automatic button creation. plugged in automatically to automatically created module.
auto_generate_btn_double = True
auto_generate_lbl = True
auto_generate_qle = True
auto_generate_qle_double = True
auto_generate_tb = True
enable_title_bar_toolbar = True  # enables toolbar creation.
# debug_verbosity_bool = False  # enables verbose output
# debug_enable_bool = True
pin_to_taskbar = False
l_pin_to_taskbar = False
r_pin_to_taskbar = False
c_pin_to_taskbar = False
configuration_override_size = False  # enables app_width_static and app_height_static to be set manually.
reserve_btnx_bool = False
reserve_btnx_double_bool = True
bool_switch_run_at_startup = False

# CONFIGURATION 2 - SETUP APPLICATION TEMPLATE GEOMETRY
theme_color = (0, 255, 255)
object_color_0 = (240, 240, 240)
object_color_background_0 = (0, 0, 0)
object_color_border_0 = (0, 0, 0)

# dev style override (providing background is black then uncommenting 14,14,14 will show object spacing/consistencies)
theme_color = (255, 255, 255)
object_color_0 = (240, 240, 240)
object_color_background_0 = (14, 14, 14)
object_color_border_0 = (14, 14, 14)

app_width_static, app_height_static = 888, 440  # application window size
main_border_height = 1
titlebar_height = 28
btn_size_titlebar = 48
btnx_position_initialize_x, btnx_position_initialize_y = 0, 0  # offset button position
btnx_size = 56  # set button size
btnx_size_Y = btnx_size
btnx_sp_size = 4  # set button spacing
btnx_sp_size_Y = btnx_sp_size
turn_page_reserved = [83]
btnx_gen_max = 144  # maximum number of buttons to create (ensure btnx_gen_max is equally divisible by btnx_row_idx_max)
btnx_row_idx_max = 16  # maximum number of buttons in a row
reserve_btnx_double = [0, 2, 4, 6]
reserve_btnx = []
reserve_qlex = []
reserve_qlex_double = []
reserve_tbx = []

title_bar_toolbar_w = 56
title_bar_toolbar_h = 24
title_bar_toolbar_sp = 8

btnx_master = [[btnx_gen_max, btnx_row_idx_max, btnx_position_initialize_x, btnx_position_initialize_y, btnx_size,
                btnx_size_Y, btnx_sp_size, btnx_sp_size_Y]]

# initiation
event_filter_self = []
shell = win32com.client.Dispatch("WScript.Shell")
pid_main = os.getpid()
print(str('[' + str(datetime.datetime.now()) + '] [pid_main]' + str(pid_main)))
print(str('[' + str(datetime.datetime.now()) + '] initializing application'))
program_fname = os.path.basename(__file__)
program_fname_no_suffix = program_fname.replace('.py', '')
print(str('[' + str(datetime.datetime.now()) + '] [program_fname] ' + str(program_fname)))
cwd = os.getcwd() + '\\'

# subprocess arguments
info = subprocess.STARTUPINFO()  # Subprocess Control
info.dwFlags = 1
info.wShowWindow = 0

# use high dpi scaling and high dpi pixel maps if available
if hasattr(Qt, 'AA_EnableHighDpiScaling'):
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    print(str('[' + str(datetime.datetime.now()) + '] AA_EnableHighDpiScaling: True'))
elif not hasattr(Qt, 'AA_EnableHighDpiScaling'):
    print(str('[' + str(datetime.datetime.now()) + '] AA_EnableHighDpiScaling: False'))
if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    print(str('[' + str(datetime.datetime.now()) + '] AA_UseHighDpiPixmaps: True'))
elif not hasattr(Qt, 'AA_UseHighDpiPixmaps'):
    print(str('[' + str(datetime.datetime.now()) + '] AA_UseHighDpiPixmaps: False'))

# cursor tracking
win_pos_w, win_pos_h = 0, 0
cur_pos_x = 0
cur_pos_y = 0
self_pos_x = 0
self_pos_y = 0
app_w = 0
app_h = 0
app_x_range = False
app_y_range = False
app_range_xy = False
titlebar_range_xy = False
user_mouse_activity = False

# boolean
first_load = True
app_display_default_bool = True
app_display_stays_on_top_bool = False
app_display_stays_on_bottom_bool = False

# lists
ui_object_complete = []
obj_geo_item = []
obj_icon_geo = []
obj_icon = []
ui_object_font_list_s6b = []
ui_object_font_list_s7b = []
ui_object_font_list_s8b = []
ui_object_font_list_s9b = []
debug_messages = []
btnx_var = []
lblx_var = []
btnx_double_var = []
qlex_var = []
qlex_double_var = []
tbx_var = []
btnx_titlebar_toolbar_var = []
tbx_message = []
tbx_message_0 = []
tbx_timer = []
btnx_double_timer = []
btnx_double_timer_sub = []
btnx_timer = []
btnx_timer_sub = []

# integers
avail_w, avail_h = 2, 2
prev_multiplier_w, prev_multiplier_h = 1, 1
pos_w_prev, pos_h_prev = 2, 2

# APPLICATION
model_type = 'yolov3'
model_path = './models/yolov3.h5'
model_json_path = None

directory_input_video = ''
directory_input_image = ''
directory_input_annotation = ''
directory_input_training = ''
training_objects_array = []
input_files_images = []
input_files_annotations = []
input_files_videos = []
index_input_files_images = 0
index_input_files_videos = 0
index_annotation_object = 0
auto_iter_object = False

enable_target = False
camera_input = 0
frames_per_second = 1
frame_detection_interval = 1
minimum_percentage_probability = 50
display_percentage_probability = True
display_object_name = True
display_box = True
save_detected_video = True
video_complete_function = None
extract_detected_objects = True
custom_objects = None
_detection_speed = 'normal'
_dump = True
save_in_class = True
output_directory_path = os.path.join(os.getcwd(), 'capture')
_annotate = True
start_frame = 0
_PRIMARY_TARGET = []
_SECONDARY_TARGET = []
TARGETS = []

# make dirs
if not os.path.exists('./config'):
    os.makedirs('./config/', exist_ok=True)

# Create target events list of dictionaries. This list should never be appended to after here, instead update by index.
TE_MAX = 1000
target_exec = []
target_exec_logs = []
target_exec_logs_spent = []
for i in range(0, TE_MAX):
    target_exec.append({'event': i, 'name': '', 'percentage_probability': 50, 'program': '', 'file': '', 'exec_mode': 'run_once', 'enabled': False, 'allow_exec': True, 'proc': False, 'detection_percentage_probability': 0})
    target_exec_logs.append([])
    target_exec_logs_spent.append([])

# write new file / overwrite existing file
if not os.path.exists('./config/target_events.dat'):
    print('-- creating new configuration file: target_events.dat')
    open('./config/target_events.dat', 'w').close()
    with open('./config/target_events.dat', 'a+') as fo:
        for target_event in target_exec:
            fo.write(str(target_event) + '\n')

# Read configuration file. Target event number must pertain to line number of target event.
if os.path.exists('./config/target_events.dat'):
    with open('./config/target_events.dat', 'r') as fo:
        i_line = 0
        for line in fo:
            line = line.strip()
            if line:
                try:
                    # create dictionary from dictionary type string
                    TE = ast.literal_eval(line)

                    # initial get values enables checks to be performed before putting values in the master dictionary
                    # _prog = TE.get('program')
                    _file = TE.get('file')
                    _exec_mode = TE.get('exec_mode')
                    _enabled = TE.get('enabled')

                    # do checks here

                    # update some values
                    TE.update({'exec_mode': _exec_mode})
                    TE.update({'enabled': _enabled})
                    TE.update({'allow_exec': True})
                    TE.update({'detection_percentage_probability': 0})
                    TE.update({'proc': False})

                    # check, compile and update
                    # if os.path.exists(_file):
                    #     _code = open(_file).read()
                    #     _prog = compile(_code, 'program_x', 'exec')
                    #     TE.update({'program': _prog})

                    target_exec[i_line] = TE
                except:
                    print(f'[CONFIGURATION] {e}')
            i_line += 1

for target in target_exec:
    print(target)

TARGETS_CONTENTS_0 = []
TARGETS_CONTENTS_1 = []
RESULT_COUNT = 50
LOG_PROGRESS = False
DUMP = False
INPUT_TYPE = 'file'
OUTPUT_TYPE = 'file'
CUSTOM_OBJECTS = None
MODE_CAMERA = False
MODE_VIDEO = False
MODE_MANUAL_ANNOTATION = False
MODE_TRAINING = False
MODE_CONVERT_VFR = False
MODE_CONVERT_VTI = False

# TRAINING
_num_objects = None
_batch_size = 32
_num_experiments = 200
_enhance_data = False
_show_network_summary = False
_object_names_array = None
_data_directory = ''
_train_subdirectory = 'train'
_test_subdirectory = 'test'
_models_subdirectory = 'models'
_json_subdirectory = 'json'
_initial_learning_rate = 1e-3
_training_image_size = 224
_continue_from_model = None
_transfer_from_model = None
_transfer_with_full_training = True
_initial_num_objects = None
_save_full_model = False
_train_from_pretrained_model = False

prev_click_x, prev_click_y = 0, 0
bounding_box = [0, 0, 0, 0]
bounding_box2 = [0, 0, 0, 0]
annotations = []


class ObjEveFilter(QObject):
    def eventFilter(self, obj, event):

        global event_filter_self
        global app_range_xy
        global app_height_static
        global pos_w_prev, pos_h_prev
        global pin_to_taskbar, l_pin_to_taskbar, r_pin_to_taskbar, c_pin_to_taskbar
        global win_pos_w, win_pos_h
        global target_exec
        
        obj_eve = obj, event

        # uncomment to display all events
        # print('-- ObjEveFilter(QObject).eventFilter(self, obj, event):', obj_eve)

        # scaling geometry
        pos_w = (QDesktopWidget().availableGeometry().width())
        pos_h = (QDesktopWidget().availableGeometry().height())
        if str(obj_eve[1]).startswith('<PyQt5.QtGui.QResizeEvent') or str(obj_eve[1]).startswith(
                '<PyQt5.QtGui.QMoveEvent'):
            self.scaling_geometry_function()

        # taskbar tracking
        if pos_w != pos_w_prev or pos_h != pos_h_prev:
            print(str('[' + str(datetime.datetime.now()) + '] taskbar may have changed position/resized/other event'))
            pos_w_prev = pos_w
            pos_h_prev = pos_h
            
            # set application window geometry
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                if l_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(0, app_height_pos, app_width_static, app_height_static)
                elif r_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(QDesktopWidget().availableGeometry().width() - app_width_static,
                                                     app_height_pos, app_width_static, app_height_static)
                elif c_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(
                        int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2),
                        app_height_pos, app_width_static, app_height_static)

        return False

    def scaling_geometry_function(self):
        global event_filter_self
        global first_load
        global avail_w, avail_h
        global prev_multiplier_w, prev_multiplier_h
        global ui_object_complete, obj_geo_item, obj_icon_geo, obj_icon
        global ui_object_font_list_s6b, ui_object_font_list_s7b, ui_object_font_list_s8b, ui_object_font_list_s9b
        global app_width_static, app_height_static

        # runs once on startup: loads all geometries into separate lists
        if first_load is True:
            first_load = False
            for _ in ui_object_complete:
                obj_geo_width = _.geometry().width()
                obj_geo_height = _.geometry().height()
                obj_geo_pos_w = _.geometry().x()
                obj_geo_pos_h = _.geometry().y()
                var = obj_geo_width, obj_geo_height, obj_geo_pos_w, obj_geo_pos_h
                obj_geo_item.append(var)
                try:
                    obj_icon_geo.append(_.iconSize())
                    obj_icon.append(_)
                except:
                    pass

        # get available geometry
        new_avail_w = QDesktopWidget().availableGeometry().width()
        new_avail_h = QDesktopWidget().availableGeometry().height()

        # obtain a multiplier from the available geometry
        if new_avail_w >= 1000 and new_avail_h >= 1000:
            multiplier_h = int(str(new_avail_h)[0])
        elif new_avail_w < 1000 and new_avail_h < 1000:
            multiplier_h = 1
        else:
            multiplier_h = 1
        multiplier_w = multiplier_h

        # check if multiplier has changed
        if prev_multiplier_w != multiplier_w or prev_multiplier_h != multiplier_h or new_avail_w != avail_w or new_avail_h != avail_h:

            # set new available geometry
            avail_h = new_avail_h
            avail_w = new_avail_w

            # set new application geometry using multiplier
            app_width = app_width_static * multiplier_w
            app_height = app_height_static * multiplier_h

            # centre application on the screen
            pos_w = (QDesktopWidget().availableGeometry().width())
            pos_h = (QDesktopWidget().availableGeometry().height())

            # set application window geometry
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                if l_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(0, app_height_pos, app_width_static, app_height_static)
                elif r_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(QDesktopWidget().availableGeometry().width() - app_width_static,
                                                     app_height_pos, app_width_static, app_height_static)
                elif c_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(
                        int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2),
                        app_height_pos, app_width_static, app_height_static)
            elif pin_to_taskbar is False:
                app_height_pos = int(QDesktopWidget().availableGeometry().height() / 2) - int(app_height_static / 2)
                app_width_pos = int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2)
                event_filter_self[0].setGeometry(app_width_pos, app_height_pos, app_width_static, app_height_static)
            
            # set application object geometries
            i = 0
            for _ in ui_object_complete:

                # Default Width
                obj_w = obj_geo_item[i]
                obj_w = obj_w[0]

                # Default Height
                obj_h = obj_geo_item[i]
                obj_h = obj_h[1]

                # Default Position Width
                obj_pos_w = obj_geo_item[i]
                obj_pos_w = obj_pos_w[2]

                # Default Position Height
                obj_pos_h = obj_geo_item[i]
                obj_pos_h = obj_pos_h[3]
                
                # set new object geometries using multiplier
                new_obj_w = obj_w * multiplier_w
                new_obj_h = obj_h * multiplier_h
                new_obj_pos_w = obj_pos_w * multiplier_w
                new_obj_pos_h = obj_pos_h * multiplier_h

                # move and resize object geometries using new geometries
                _.move(new_obj_pos_w, new_obj_pos_h)
                _.resize(new_obj_w, new_obj_h)
                i += 1

            # set icon geometries
            i = 0
            for _ in obj_icon_geo:
                try:
                    # obtain last known geometries
                    geo_var = str(_)
                    geo_var = geo_var.replace('PyQt5.QtCore.QSize(', '')
                    geo_var = geo_var.replace(')', '')
                    geo_var = geo_var.replace(',', '')
                    geo_var_split = geo_var.split()
                    icon_sz_w = int(geo_var_split[0])
                    icon_sz_h = int(geo_var_split[1])

                    # set new geometries using multipliers
                    icon_size_w = icon_sz_w * multiplier_w
                    icon_size_h = icon_sz_h * multiplier_h
                    obj_icon[i].setIconSize(QSize(icon_size_w, icon_size_h))

                except:
                    pass
                i += 1

            # set font geometries using multipliers
            font_size_6b = int(6 * multiplier_h)
            font_size_7b = int(7 * multiplier_h)
            font_size_8b = int(8 * multiplier_h)
            font_size_9b = int(9 * multiplier_h)
            font_s6b = QFont("Segoe UI", (font_size_6b), QFont.Bold)
            font_s7b = QFont("Segoe UI", (font_size_7b), QFont.Bold)
            font_s8b = QFont("Segoe UI", (font_size_8b), QFont.Bold)
            font_s9b = QFont("Segoe UI", (font_size_9b), QFont.Bold)
            for _ in ui_object_font_list_s6b:
                _.setFont(font_s6b)
            for _ in ui_object_font_list_s7b:
                _.setFont(font_s7b)
            for _ in ui_object_font_list_s8b:
                _.setFont(font_s8b)
            for _ in ui_object_font_list_s9b:
                _.setFont(font_s9b)

            # finally change previously known multipliers to current multipliers
            prev_multiplier_w = multiplier_w
            prev_multiplier_h = multiplier_h

            event_filter_self[0].update()


class App(QMainWindow):
    cursorMove = pyqtSignal(object)

    def __init__(self):
        super(App, self).__init__()
        global btnx_var
        global event_filter_self, ui_object_complete
        global ui_object_font_list_s6b, ui_object_font_list_s7b, ui_object_font_list_s8b, ui_object_font_list_s9b
        global app_height_static, app_width_static
        global auto_generate, enable_title_bar_toolbar

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.save_menu_bar))
        self.save_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.enabled_menu_bar))
        self.enabled_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.exit_menu_bar))
        self.exit_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.open_menu_bar))
        self.open_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.theme_stone_menu_bar))
        self.theme_stone_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.theme_red_menu_bar))
        self.theme_red_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.theme_yellow_menu_bar))
        self.theme_yellow_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.theme_green_menu_bar))
        self.theme_green_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.theme_blue_menu_bar))
        self.theme_blue_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.theme_light_blue_menu_bar))
        self.theme_light_blue_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.theme_purple_menu_bar))
        self.theme_purple_menu_bar = QIcon(pixmap)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.theme_pink_menu_bar))
        self.theme_pink_menu_bar = QIcon(pixmap)

        self_style = """

                QMainWindow {background-color: rgb(0, 0, 0);
                color: rgb(200, 200, 200);
                border-top:""" + str(main_border_height) + """px solid rgb""" + str(theme_color) + """;
                border-bottom:""" + str(main_border_height + 0) + """px solid rgb""" + str(theme_color) + """;
                border-right:""" + str(main_border_height + 0) + """px solid rgb""" + str(theme_color) + """;
                border-left:""" + str(main_border_height + 0) + """px solid rgb""" + str(theme_color) + """;}
                }

                QToolTip {background-color: rgb(35, 35, 35);
                color: rgb(200, 200, 200);
                border-top:0px solid rgb(35, 35, 35);
                border-bottom:0px solid rgb(35, 35, 35);
                border-right:0px solid rgb(0, 0, 0);
                border-left:0px solid rgb(0, 0, 0);
                }

                QScrollBar:vertical {
                width: 20px;
                margin: 20px 0px 20px 0px;
                background-color: rgb(18, 18, 18);
                }
                QScrollBar:horizontal {
                height: 20px;
                margin: 0px 20px 0px 20px;
                background-color: rgb(18, 18, 18);
                }

                QScrollBar::handle:vertical {
                background-color: rgb""" + str(theme_color) + """;
                border-bottom:4px solid rgb(0, 0, 0);
                border-top:4px solid rgb(0, 0, 0);
                min-height: 8px;
                }
                QScrollBar::handle:horizontal {
                background-color: rgb""" + str(theme_color) + """;
                border-left:4px solid rgb(0, 0, 0);
                border-right:4px solid rgb(0, 0, 0);
                min-width: 8px;
                }

                QScrollBar::add-line:vertical {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                }
                QScrollBar::sub-line:vertical {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: top;
                subcontrol-origin: margin;
                }

                QScrollBar::add-line:horizontal {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: right;
                subcontrol-origin: margin;
                }
                QScrollBar::sub-line:horizontal {
                background-color: rgb(20, 20, 20);
                height: 20px;
                width: 20px;
                subcontrol-position: top left;
                subcontrol-origin: margin;
                }

                QScrollBar::up-arrow:vertical {
                background-color: rgb""" + str(theme_color) + """;
                height: 8px;
                width: 20px;
                }
                QScrollBar::down-arrow:vertical {
                background-color: rgb""" + str(theme_color) + """;
                height: 8px;
                width: 20px;
                }

                QScrollBar::left-arrow:horizontal {
                background-color: rgb""" + str(theme_color) + """;
                height: 20px;
                width: 8px;
                }
                QScrollBar::right-arrow:horizontal {
                background-color: rgb""" + str(theme_color) + """;
                height: 20px;
                width: 8px;
                }

                QScrollBar::add-page:vertical {
                background-color: rgb(0, 0, 0);
                width: 20px;
                height: 20px;
                }
                QScrollBar::sub-page:vertical {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }

                QScrollBar::add-page:horizontal {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }
                QScrollBar::sub-page:horizontal {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }

                QSlider::groove:horizontal {
                height: 6px;
                background: rgb(30, 30, 30);
                margin: 8px;
                border: 2px rgb""" + str(object_color_border_0) + """;
                }
                QSlider::handle:horizontal {
                background: rgb""" + str(theme_color) + """;
                border: 2px rgb""" + str(object_color_background_0) + """;
                width: 10px;
                height: 10px;
                margin: -15px 0px;
                }

                QMenuBar {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                }
                QMenuBar::item {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                }
                QMenuBar::item::selected {
                background-color: rgb(0, 0, 0);
                }
                QMenu {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                border-top:0px solid rgb(0, 0, 0);
                border-bottom:0px solid rgb""" + str(theme_color) + """;
                border-right:0px solid rgb""" + str(theme_color) + """;
                border-left:0px solid rgb""" + str(theme_color) + """;
                }
                QMenu::item::selected {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb""" + str(theme_color) + """;
                }

                QPushButton{background-color: rgb(0, 0, 0);
                color : rgb(255, 255, 255);
                background-color : rgb(14, 14, 14);
                border-top:10px solid rgb(14, 14, 14);
                border-bottom:10px solid rgb(14, 14, 14);
                border-right:20px solid rgb(14, 14, 14);
                border-left:20px solid rgb(14, 14, 14);}
                }
                QPushButton::hover {background-color : rgb(14, 14, 14);
                }
                QPushButton::pressed {
                color : rgb(255, 255, 255);
                background-color : rgb(14, 14, 14);
                border-top:14px solid rgb(14, 14, 14);
                border-bottom:14px solid rgb(14, 14, 14);
                border-right:24px solid rgb(14, 14, 14);
                border-left:24px solid rgb(14, 14, 14);}
                }

                QLabel{background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                border-top:4px solid rgb(0, 0, 0);
                border-bottom:4px solid rgb(0, 0, 0);
                border-right:4px solid rgb(0, 0, 0);
                border-left:4px solid rgb(0, 0, 0);}

                QLineEdit{background-color: rgb(16, 16, 16);
                color: rgb(255, 255, 255);
                border-top:4px solid rgb(14, 14, 14);
                border-bottom:4px solid rgb(14, 14, 14);
                border-right:4px solid rgb(14, 14, 14);
                border-left:4px solid rgb(14, 14, 14);}

                QTextBrowser {background-color: rgb(0, 0, 0);
                selection-color: black;
                selection-background-color: rgb(0, 180, 0);
                color: rgb(0, 255, 0);
                border-bottom:0px solid rgb(5, 5, 5);
                border-right:0px solid rgb(5, 5, 5);
                border-top:0px solid rgb(5, 5, 5);
                border-left:0px solid rgb(5, 5, 5);}

                QComboBox {background-color: rgb(0, 0, 0);
                selection-color: black;
                selection-background-color: rgb(255, 0, 0);
                color: rgb(0, 255, 0);
                border-bottom:0px solid rgb(5, 5, 5);
                border-right:0px solid rgb(5, 5, 5);
                border-top:0px solid rgb(5, 5, 5);
                border-left:0px solid rgb(5, 5, 5);}

                """
        self.setStyleSheet(self_style)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.logo_placeholder))
        icon = QIcon(pixmap)

        # initiate some basics
        self.setWindowIcon(QIcon(icon))
        self.title = 'Detectionator'
        self.setWindowTitle(self.title)

        # main window color & window frame style
        p = self.palette()
        p.setColor(self.backgroundRole(), Qt.black)
        self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
        self.setPalette(p)

        # initialize fonts
        self.font_s6b = QFont("Segoe UI", 6, QFont.Bold)
        self.font_s7b = QFont("Segoe UI", 7, QFont.Bold)
        self.font_s8b = QFont("Segoe UI", 8, QFont.Bold)
        self.font_s9b = QFont("Segoe UI", 9, QFont.Bold)

        # initiate object event filter
        event_filter_self.append(self)
        self.filter = ObjEveFilter()
        
        # cursor tracking
        self.cursorMove.connect(self.handle_cursor_move)
        self.timer = QTimer(self)
        self.timer.setInterval(50)
        self.timer.timeout.connect(self.poll_cursor)
        self.timer.start()
        self.cursor = None

        # Toolbar background label
        self.toolbar_label = QLabel(self)
        self.toolbar_label.move(main_border_height, main_border_height * 4)
        self.toolbar_label.resize(1900, (btn_size_titlebar * 1) + main_border_height * 3)
        self.toolbar_label.setStyleSheet("""
            QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-top:0px solid rgb""" + str(object_color_background_0) + """;
            border-bottom:1px solid rgb""" + str(object_color_background_0) + """;
            border-right:0px solid rgb""" + str(object_color_background_0) + """;
            border-left:0px solid rgb""" + str(object_color_background_0) + """;
            }""")
        self.toolbar_label.setText('')
        ui_object_complete.append(self.toolbar_label)

        # button: logo (use main_border_height)
        self.btn_title_logo = QPushButton(self)
        self.btn_title_logo.move(main_border_height * 2, main_border_height * 2)
        self.btn_title_logo.resize(btn_size_titlebar * 1, btn_size_titlebar * 1)
        # self.btn_title_logo.setIcon(QIcon(icon))
        # self.btn_title_logo.setIconSize(QSize(titlebar_height, titlebar_height))
        self.btn_title_logo.setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        self.btn_title_logo.installEventFilter(self)
        ui_object_complete.append(self.btn_title_logo)

        self.menu_bar_size_x = btnx_size * 4 + (btnx_sp_size * 3)
        self.menu_bar_size_y = int(btn_size_titlebar / 2)

        self.menu_bar_move_x = main_border_height + (btnx_sp_size * 2) + (btn_size_titlebar * 1)
        self.menu_bar_move_y = (main_border_height * 2) + (self.menu_bar_size_y / 2)

        self.file_menu = QMenu(self)
        self.model_menu = QMenu(self)
        self.detection_menu = QMenu(self)
        self.view_menu = QMenu(self)
        self.help_menu = QMenu(self)
        self.main_menu_bar = QMenuBar(self)
        self.main_menu_bar.resize(self.menu_bar_size_x, self.menu_bar_size_y)
        self.main_menu_bar.move(self.menu_bar_move_x, self.menu_bar_move_y)
        ui_object_complete.append(self.main_menu_bar)

        def app_display_stays_on_top():
            global app_display_default_bool, app_display_stays_on_top_bool, app_display_stays_on_bottom_bool
            print(str('[' + str(datetime.datetime.now()) + '] [app_display_stays_on_top] plugged in'))
            app_display_default_bool = False
            app_display_stays_on_top_bool = True
            app_display_stays_on_bottom_bool = False
            create_titlebar_menubar()
            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnTopHint)
            self.show()

        def about_function():
            print(str('[' + str(datetime.datetime.now()) + '] [about_function] plugged in'))

        def app_display_stays_on_bottom():
            global app_display_default_bool, app_display_stays_on_top_bool, app_display_stays_on_bottom_bool
            print(str('[' + str(datetime.datetime.now()) + '] [app_display_stays_on_bottom] plugged in'))
            app_display_default_bool = False
            app_display_stays_on_top_bool = False
            app_display_stays_on_bottom_bool = True
            create_titlebar_menubar()
            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint | Qt.WindowStaysOnBottomHint)
            self.show()

        def app_display_default():
            global app_display_default_bool, app_display_stays_on_top_bool, app_display_stays_on_bottom_bool
            print(str('[' + str(datetime.datetime.now()) + '] [app_display_default] plugged in'))
            app_display_default_bool = True
            app_display_stays_on_top_bool = False
            app_display_stays_on_bottom_bool = False
            create_titlebar_menubar()
            self.setWindowFlags(Qt.Window | Qt.FramelessWindowHint)
            self.show()

        def create_vbs():
            print(str('[' + str(datetime.datetime.now()) + '] [create_vbs] plugged in'))
            vbs_f = cwd + program_fname_no_suffix + '.vbs'
            exe_f = cwd + program_fname_no_suffix + '.exe'
            open(vbs_f, 'w').close()
            with open(vbs_f, 'a') as vbs_fo:
                vbs_fo.write('Set WshShell = CreateObject("WScript.Shell")' + '\n')
                vbs_fo.write('WshShell.Run chr(34) & "' + exe_f + '" & Chr(34), 0' + '\n')
                vbs_fo.write('Set WshShell = Nothing' + '\n')
            vbs_fo.close()

        def create_lnk():
            print(str('[' + str(datetime.datetime.now()) + '] [create_lnk] plugged in'))
            vbs_f = cwd + program_fname_no_suffix + '.vbs'
            lnk_f = cwd + program_fname_no_suffix + '.lnk'
            open(lnk_f, 'w').close()
            vbs_icon = cwd + 'icon.ico'
            shortcut = shell.CreateShortCut(lnk_f)
            shortcut.Targetpath = vbs_f
            shortcut.WorkingDirectory = cwd
            shortcut.IconLocation = vbs_icon
            shortcut.save()

        def run_at_startup_check():
            global bool_switch_run_at_startup
            print(str('[' + str(datetime.datetime.now()) + '] [run_at_startup_check] plugged in'))
            shortcut_out = os.path.join(os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/' + program_fname_no_suffix + '.lnk')
            if os.path.exists(shortcut_out):
                bool_switch_run_at_startup = True
            else:
                bool_switch_run_at_startup = False

        def run_at_startup():
            global bool_switch_run_at_startup
            print(str('[' + str(datetime.datetime.now()) + '] [run_at_startup] plugged in'))
            vbs_f = cwd + program_fname_no_suffix + '.vbs'
            shortcut_out = os.path.join(os.path.expanduser('~') + '/AppData/Roaming/Microsoft/Windows/Start Menu/Programs/Startup/' + program_fname_no_suffix + '.lnk')
            # remove shortcut from startup directory
            if bool_switch_run_at_startup is True:
                if os.path.exists(shortcut_out):
                    os.remove(shortcut_out)
                    bool_switch_run_at_startup = False
            # create shortcut in startup directory
            elif bool_switch_run_at_startup is False:
                _icon = cwd + './icon.ico'
                _shell = win32com.client.Dispatch("WScript.Shell")
                shortcut = _shell.CreateShortCut(shortcut_out)
                shortcut.Targetpath = vbs_f
                shortcut.WorkingDirectory = cwd
                shortcut.IconLocation = _icon
                shortcut.save()
                bool_switch_run_at_startup = True
            create_titlebar_menubar()

        create_vbs()
        create_lnk()
        run_at_startup_check()

        def l_attatch_to_taskbar():
            global pin_to_taskbar, pos_w_prev
            global l_pin_to_taskbar, r_pin_to_taskbar, c_pin_to_taskbar
            if l_pin_to_taskbar is False:
                r_pin_to_taskbar = False
                c_pin_to_taskbar = False
                l_pin_to_taskbar = True
                pin_to_taskbar = True
                pos_w_prev = int()
            elif l_pin_to_taskbar is True:
                pin_to_taskbar = False
                r_pin_to_taskbar = False
                c_pin_to_taskbar = False
                l_pin_to_taskbar = False
                pos_w_prev = int()
            create_titlebar_menubar()

        def r_attatch_to_taskbar():
            global pin_to_taskbar, pos_w_prev
            global l_pin_to_taskbar, r_pin_to_taskbar, c_pin_to_taskbar
            if r_pin_to_taskbar is False:
                l_pin_to_taskbar = False
                c_pin_to_taskbar = False
                r_pin_to_taskbar = True
                pin_to_taskbar = True
                pos_w_prev = int()
            elif r_pin_to_taskbar is True:
                pin_to_taskbar = False
                l_pin_to_taskbar = False
                c_pin_to_taskbar = False
                r_pin_to_taskbar = False
                pos_w_prev = int()
            create_titlebar_menubar()

        def c_attatch_to_taskbar():
            global pin_to_taskbar, pos_w_prev
            global l_pin_to_taskbar, r_pin_to_taskbar, c_pin_to_taskbar
            if c_pin_to_taskbar is False:
                l_pin_to_taskbar = False
                r_pin_to_taskbar = False
                c_pin_to_taskbar = True
                pin_to_taskbar = True
                pos_w_prev = int()
            elif c_pin_to_taskbar is True:
                pin_to_taskbar = False
                l_pin_to_taskbar = False
                r_pin_to_taskbar = False
                c_pin_to_taskbar = False
                pos_w_prev = int()
            create_titlebar_menubar()

        def model_type_select_yolov3():
            global model_type
            model_type = 'yolov3'
            create_titlebar_menubar()

        def model_type_select_resnet():
            global model_type
            model_type = 'resnet'
            create_titlebar_menubar()

        def model_type_select_resnet50():
            global model_type
            model_type = 'resnet50'
            create_titlebar_menubar()

        def model_type_select_densenet():
            global model_type
            model_type = 'densenet'
            create_titlebar_menubar()

        def model_type_select_densenet121():
            global model_type
            model_type = 'densenet121'
            create_titlebar_menubar()

        def model_type_select_inceptionv3():
            global model_type
            model_type = 'inceptionv3'
            create_titlebar_menubar()

        def model_type_select_mobilenetv2():
            global model_type
            model_type = 'mobilenetv2'
            create_titlebar_menubar()

        def model_path_select():
            global model_path
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Select model:", "", "All Files (*);;", options=options)
            if file_name:
                print(f'-- selecting model file: {file_name}')
                model_path = file_name

        def model_json_path_select():
            global model_json_path
            options = QFileDialog.Options()
            file_name, _ = QFileDialog.getOpenFileName(self, "Select model JSON:", "", "All Files (*);;", options=options)
            if file_name:
                print(f'-- selecting model JSON file: {file_name}')
                model_json_path = file_name

        # output_directory_path
        def select_output_directory():
            global output_directory_path
            _cwd = os.getcwd()
            dir_name = QFileDialog.getExistingDirectory(caption='Select output directory:', directory=_cwd)
            if dir_name:
                print(f'-- selecting output directory: {dir_name}')
                output_directory_path = dir_name
            create_titlebar_menubar()

        def set_detection_speed_normal():
            global _detection_speed
            _detection_speed = 'normal'
            create_titlebar_menubar()

        def set_detection_speed_fast():
            global _detection_speed
            _detection_speed = 'fast'
            create_titlebar_menubar()

        def set_detection_speed_faster():
            global _detection_speed
            _detection_speed = 'faster'
            create_titlebar_menubar()

        def set_detection_speed_fastest():
            global _detection_speed
            _detection_speed = 'fastest'
            create_titlebar_menubar()

        def set_detection_speed_flash():
            global _detection_speed
            _detection_speed = 'flash'
            create_titlebar_menubar()

        def set_display_object_name():
            global display_object_name
            if display_object_name is False:
                display_object_name = True
            elif display_object_name is True:
                display_object_name = False
            create_titlebar_menubar()

        def set_display_percentage_probability():
            global display_percentage_probability
            if display_percentage_probability is False:
                display_percentage_probability = True
            elif display_percentage_probability is True:
                display_percentage_probability = False
            create_titlebar_menubar()

        def set_display_box():
            global display_box
            if display_box is False:
                display_box = True
            elif display_box is True:
                display_box = False
            create_titlebar_menubar()

        def set_extract_detected_objects():
            global extract_detected_objects
            if extract_detected_objects is False:
                extract_detected_objects = True
            elif extract_detected_objects is True:
                extract_detected_objects = False
            create_titlebar_menubar()

        def set_save_in_class():
            global save_in_class
            if save_in_class is False:
                save_in_class = True
            elif save_in_class is True:
                save_in_class = False
            create_titlebar_menubar()

        def set_annotate():
            global _annotate
            if _annotate is False:
                _annotate = True
            elif _annotate is True:
                _annotate = False
            create_titlebar_menubar()

        def save_targets():
            global target_exec
            """ Writes targets to configuration file. Does not update targets lists, targets lists are updated
             automatically """

            # Save targets
            if not os.path.exists('./config'):
                os.makedirs('./config/', exist_ok=True)

            # Save target events
            if not os.path.exists('./config'):
                os.makedirs('./config/', exist_ok=True)
            open('./config/target_events.dat', 'w').close()

            with open('./config/target_events.dat', 'a') as te_fo:
                for te in target_exec:
                    print(f'target_event: {te}')
                    tmp_target_event = te
                    tmp_target_event.update({'program': ''})
                    tmp_target_event.update({'proc': False})
                    tmp_target_event.update({'detection_percentage_probability': 0})
                    te_fo.write(f'{tmp_target_event}\n')

        def app_theme_stone():
            global theme_color
            theme_color = (255, 255, 255)
            self.set_style()
            create_titlebar_menubar()

        def app_theme_red():
            global theme_color
            theme_color = (255, 0, 0)
            self.set_style()
            create_titlebar_menubar()

        def app_theme_yellow():
            global theme_color
            theme_color = (255, 255, 0)
            self.set_style()
            create_titlebar_menubar()

        def app_theme_green():
            global theme_color
            theme_color = (0, 255, 0)
            self.set_style()
            create_titlebar_menubar()

        def app_theme_blue():
            global theme_color
            theme_color = (0, 0, 255)
            self.set_style()
            create_titlebar_menubar()

        def app_theme_light_blue():
            global theme_color
            theme_color = (0, 255, 255)
            self.set_style()
            create_titlebar_menubar()

        def app_theme_purple():
            global theme_color
            theme_color = (255, 0, 255)
            self.set_style()
            create_titlebar_menubar()

        def app_theme_pink():
            global theme_color
            theme_color = (255, 115, 195)
            self.set_style()
            create_titlebar_menubar()

        # title_bar_toolbar
        def create_titlebar_menubar():
            global btnx_titlebar_toolbar_var, app_display_default_bool, app_display_stays_on_top_bool
            global app_display_stays_on_bottom_bool, pin_to_taskbar, l_pin_to_taskbar, r_pin_to_taskbar
            global c_pin_to_taskbar, output_directory_path, theme_color
            self.main_menu_bar.clear()
            self.file_menu.clear()
            self.model_menu.clear()
            self.detection_menu.clear()
            self.view_menu.clear()
            self.help_menu.clear()
            self.file_menu.setTitle('File')
            self.file_menu.addSeparator()

            # set save location
            if output_directory_path:
                self.file_menu.addAction(self.save_menu_bar, f' Save location:  (current: {output_directory_path})',
                                         select_output_directory)
            else:
                self.file_menu.addAction(self.save_menu_bar, ' Save location', select_output_directory)
            self.file_menu.addSeparator()

            # save configuration
            self.file_menu.addAction(self.save_menu_bar, f' Save configuration settings', save_targets)
            self.file_menu.addSeparator()

            # run at startup self.enabled_menu_bar
            if bool_switch_run_at_startup is True:
                self.file_menu.addAction(self.enabled_menu_bar, ' Run at startup', run_at_startup)
            else:
                self.file_menu.addAction(' Run at startup', run_at_startup)
            self.file_menu.addSeparator()

            # exit
            self.file_menu.addAction(self.exit_menu_bar, ' Exit', app.quit)
            self.file_menu.addSeparator()

            self.model_menu.addSeparator()
            self.model_menu.setTitle('Model')
            self.model_menu.addSeparator()
            self.detection_menu.addSeparator()
            self.detection_menu.setTitle('Detection')
            self.detection_menu.addSeparator()
            if model_type == 'yolov3':
                self.model_menu.addAction(self.enabled_menu_bar, ' Use Model Type (yolov3)', model_type_select_yolov3)
            else:
                self.model_menu.addAction(' Use Model Type (yolov3)', model_type_select_yolov3)
            self.model_menu.addSeparator()
            self.model_menu.addSeparator()
            if model_type == 'resnet':
                self.model_menu.addAction(self.enabled_menu_bar, ' Use Model Type (resnet)', model_type_select_resnet)
            else:
                self.model_menu.addAction(' Use Model Type (resnet)', model_type_select_resnet)

            if model_type == 'resnet50':
                self.model_menu.addAction(self.enabled_menu_bar, ' Use Model Type (resnet50)',
                                          model_type_select_resnet50)
            else:
                self.model_menu.addAction(' Use Model Type (resnet50)', model_type_select_resnet50)
            self.model_menu.addSeparator()
            self.model_menu.addSeparator()
            if model_type == 'densenet':
                self.model_menu.addAction(self.enabled_menu_bar, ' Use Model Type (densenet)',
                                          model_type_select_densenet)
            else:
                self.model_menu.addAction(' Use Model Type (densenet)', model_type_select_densenet)

            if model_type == 'densenet121':
                self.model_menu.addAction(self.enabled_menu_bar, ' Use Model Type (densenet121)',
                                          model_type_select_densenet121)
            else:
                self.model_menu.addAction(' Use Model Type (densenet121)', model_type_select_densenet121)
            self.model_menu.addSeparator()
            self.model_menu.addSeparator()
            if model_type == 'inceptionv3':
                self.model_menu.addAction(self.enabled_menu_bar, ' Use Model Type (inceptionv3)',
                                          model_type_select_inceptionv3)
            else:
                self.model_menu.addAction(' Use Model Type (inceptionv3)', model_type_select_inceptionv3)
            self.model_menu.addSeparator()
            self.model_menu.addSeparator()
            if model_type == 'mobilenetv2':
                self.model_menu.addAction(self.enabled_menu_bar, ' Use Model Type (mobilenetv2)',
                                          model_type_select_mobilenetv2)
            else:
                self.model_menu.addAction(' Use Model Type (mobilenetv2)', model_type_select_mobilenetv2)
            self.model_menu.addSeparator()
            self.model_menu.addSeparator()
            self.model_menu.addAction(self.open_menu_bar, ' Select Model Path', model_path_select)
            self.model_menu.addSeparator()
            self.model_menu.addAction(self.open_menu_bar, ' Select Model JSON Path', model_json_path_select)
            self.model_menu.addSeparator()
            self.detection_menu.setTitle('Detection')
            self.detection_menu.addSeparator()
            if _detection_speed == 'normal':
                self.detection_menu.addAction(self.enabled_menu_bar, ' Set detection speed (normal)',
                                              set_detection_speed_normal)
            else:
                self.detection_menu.addAction(' Set detection speed (normal)', set_detection_speed_normal)
            if _detection_speed == 'fast':
                self.detection_menu.addAction(self.enabled_menu_bar, ' Set detection speed (fast)',
                                              set_detection_speed_fast)
            else:
                self.detection_menu.addAction(' Set detection speed (fast)', set_detection_speed_fast)
            if _detection_speed == 'faster':
                self.detection_menu.addAction(self.enabled_menu_bar, ' Set detection speed (faster)',
                                              set_detection_speed_faster)
            else:
                self.detection_menu.addAction(' Set detection speed (faster)', set_detection_speed_faster)
            if _detection_speed == 'fastest':
                self.detection_menu.addAction(self.enabled_menu_bar, ' Set detection speed (fastest)',
                                              set_detection_speed_fastest)
            else:
                self.detection_menu.addAction(' Set detection speed (fastest)', set_detection_speed_fastest)
            if _detection_speed == 'flash':
                self.detection_menu.addAction(self.enabled_menu_bar, ' Set detection speed (flash)',
                                              set_detection_speed_flash)
            else:
                self.detection_menu.addAction(' Set detection speed (flash)', set_detection_speed_flash)
            self.detection_menu.addSeparator()
            self.detection_menu.addSeparator()
            if display_object_name is True:
                self.detection_menu.addAction(self.enabled_menu_bar, ' Display object name', set_display_object_name)
            else:
                self.detection_menu.addAction(' Display object name', set_display_object_name)
            if display_percentage_probability is True:
                self.detection_menu.addAction(self.enabled_menu_bar, ' Display percentage probability',
                                              set_display_percentage_probability)
            else:
                self.detection_menu.addAction(' Display percentage probability', set_display_percentage_probability)
            if display_box is True:
                self.detection_menu.addAction(self.enabled_menu_bar, ' Display bounding box', set_display_box)
            else:
                self.detection_menu.addAction(' Display bounding box', set_display_box)
            self.detection_menu.addSeparator()
            self.detection_menu.addSeparator()
            if extract_detected_objects is True:
                self.detection_menu.addAction(self.enabled_menu_bar, ' Extract detected objects',
                                              set_extract_detected_objects)
            else:
                self.detection_menu.addAction(' Extract detected objects', set_extract_detected_objects)
            if save_in_class is True:
                self.detection_menu.addAction(self.enabled_menu_bar, ' Save objects to class', set_save_in_class)
            else:
                self.detection_menu.addAction(' Save objects to class', set_save_in_class)
            if _annotate is True:
                self.detection_menu.addAction(self.enabled_menu_bar, ' Enable auto-annotation', set_annotate)
            else:
                self.detection_menu.addAction(' Enable auto-annotation', set_annotate)
            self.detection_menu.addSeparator()
            self.detection_menu.addSeparator()

            self.view_menu.setTitle('View')
            self.view_menu.addSeparator()
            if l_pin_to_taskbar is True:
                self.view_menu.addAction(self.enabled_menu_bar, ' Attach to taskbar (Left)',
                                         l_attatch_to_taskbar)
            else:
                self.view_menu.addAction(' Attach to taskbar (Left)', l_attatch_to_taskbar)

            if r_pin_to_taskbar is True:
                self.view_menu.addAction(self.enabled_menu_bar, ' Attach to taskbar (Right)',
                                         r_attatch_to_taskbar)
            else:
                self.view_menu.addAction(' Attach to taskbar (Right)', r_attatch_to_taskbar)

            if c_pin_to_taskbar is True:
                self.view_menu.addAction(self.enabled_menu_bar, ' Attach to taskbar (Centre)',
                                         c_attatch_to_taskbar)
            else:
                self.view_menu.addAction(' Attach to taskbar (Centre)', c_attatch_to_taskbar)

            self.view_menu.addSeparator()

            if app_display_default_bool is True:
                self.view_menu.addAction(self.enabled_menu_bar, ' Always display default', app_display_default)
            else:
                self.view_menu.addAction(' Always display default', app_display_default)

            if app_display_stays_on_top_bool is True:
                self.view_menu.addAction(self.enabled_menu_bar, ' Always display on top', app_display_stays_on_top)
            else:
                self.view_menu.addAction(' Always display on top', app_display_stays_on_top)

            if app_display_stays_on_bottom_bool is True:
                self.view_menu.addAction(self.enabled_menu_bar, ' Always display on bottom', app_display_stays_on_bottom)
            else:
                self.view_menu.addAction(' Always display on bottom', app_display_stays_on_bottom)
            self.view_menu.addSeparator()

            """
            theme_color = (255, 255, 255)
            theme_color = (255, 0, 0)
            theme_color = (255, 255, 0)
            theme_color = (0, 255, 0)
            theme_color = (0, 0, 255)
            theme_color = (0, 255, 255)
            theme_color = (255, 0, 255)
            theme_color = (255, 115, 195)
            """
            # uncomment to enable themes
            # if theme_color == (255, 0, 0):
            #     self.view_menu.addAction(self.enabled_menu_bar, ' Theme: Tartarus', app_theme_red)
            # else:
            #     self.view_menu.addAction(' Theme: Tartarus', app_theme_red)
            #
            # if theme_color == (255, 255, 0):
            #     self.view_menu.addAction(self.enabled_menu_bar, ' Theme: Helios', app_theme_yellow)
            # else:
            #     self.view_menu.addAction(' Theme: Helios', app_theme_yellow)
            #
            # if theme_color == (0, 255, 0):
            #     self.view_menu.addAction(self.enabled_menu_bar, ' Theme: Terminal', app_theme_green)
            # else:
            #     self.view_menu.addAction(' Theme: Terminal', app_theme_green)
            #
            # if theme_color == (0, 0, 255):
            #     self.view_menu.addAction(self.enabled_menu_bar, ' Theme: Dark Blue', app_theme_blue)
            # else:
            #     self.view_menu.addAction(' Theme: Dark Blue', app_theme_blue)
            #
            # if theme_color == (0, 255, 255):
            #     self.view_menu.addAction(self.enabled_menu_bar, ' Theme: Neon Sky', app_theme_light_blue)
            # else:
            #     self.view_menu.addAction(' Theme: Neon Sky', app_theme_light_blue)
            #
            # if theme_color == (255, 0, 255):
            #     self.view_menu.addAction(self.enabled_menu_bar, ' Theme: Asgard', app_theme_purple)
            # else:
            #     self.view_menu.addAction(' Theme: Asgard', app_theme_purple)
            #
            # if theme_color == (255, 115, 195):
            #     self.view_menu.addAction(self.enabled_menu_bar, ' Theme: Aura', app_theme_pink)
            # else:
            #     self.view_menu.addAction(' Theme: Aura', app_theme_pink)
            #
            # if theme_color == (255, 255, 255):
            #     self.view_menu.addAction(self.enabled_menu_bar, ' Theme: Ascendance', app_theme_stone)
            # else:
            #     self.view_menu.addAction(' Theme: Ascendance', app_theme_stone)
            self.view_menu.addSeparator()

            # Help menu todo -> help
            self.help_menu.setTitle('Help')

            self.help_menu.addSeparator()
            self.help_menu.addAction(' About', about_function)
            self.help_menu.addSeparator()
            self.help_menu.addAction(' Created and written by Benjamin Jack Cullen.', about_function)
            # About Page  todo -> about

            self.main_menu_bar.setStyleSheet("""
                QMenuBar {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                }
                QMenuBar::item {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                }
                QMenuBar::item::selected {
                background-color: rgb(0, 0, 0);
                }
                QMenu {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                border-top:0px solid rgb(0, 0, 0);
                border-bottom:0px solid rgb""" + str(theme_color) + """;
                border-right:0px solid rgb""" + str(theme_color) + """;
                border-left:0px solid rgb""" + str(theme_color) + """;
                }
                QMenu::item::selected {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb""" + str(theme_color) + """;
                }
                """)
            self.main_menu_bar.addMenu(self.file_menu)
            self.main_menu_bar.addMenu(self.model_menu)
            self.main_menu_bar.addMenu(self.detection_menu)
            self.main_menu_bar.addMenu(self.view_menu)
            self.main_menu_bar.addMenu(self.help_menu)
            self.main_menu_bar.resize(self.menu_bar_size_x, self.menu_bar_size_y)
            print('-- created/updated menu bar')

        # Create objects and modules automatically
        def automatic_object_generator():
            global btnx_var, ui_object_complete, app_width_static, app_height_static
            global auto_generate_lbl, auto_generate_btn, auto_generate_btn_double, auto_generate_qle, btnx_master
            global btnx_var, lblx_var, btnx_double_var, qlex_var, qlex_double_var, tbx_var, tbx_message, tbx_timer
            global reserve_btnx, btnx_double_timer_sub, btnx_timer, btnx_timer_sub, btnx_double_timer
            global pin_to_taskbar, l_pin_to_taskbar, r_pin_to_taskbar, c_pin_to_taskbar

            list_import_0 = ['os', 'PyQt5', 'PyQt5.QtCore', 'datetime', 'sol_style']
            list_import_1 = ['auto_gen_main_page', 'auto_gen_btnx_function',
                             'auto_gen_btnx_double_function',
                             'auto_gen_qle_returnpressed_connect_function',
                             'auto_gen_qle_double_returnpressed_connect_function',
                             'auto_gen_tbx_update_function',
                             'auto_gen_btnx_bool',
                             'auto_gen_btnx_double_bool',
                             'auto_gen_qle_bool',
                             'auto_gen_qle_double_bool']
            list_objects = ['var_btnx',
                            'var_btnx_double',
                            'var_lblx',
                            'var_qlex',
                            'var_qlex_double',
                            'var_tbx',
                            'var_tbx_timer',
                            'var_btnx_double_timer',
                            'var_btnx_double_timer_sub',
                            'var_btnx_timer',
                            'var_btnx_timer_sub',
                            'var_self']
            if auto_setup is True:
                # wipe modules
                for _ in list_import_1:
                    open(str('./' + _ + '.py'), 'w').close()
                # head clean module files
                for _ in list_import_1:
                    with open(str('./' + _ + '.py'), 'a') as fo:
                        for _ in list_import_0:
                            fo.write('import ' + _ + '\n')
                        for _ in list_import_1:
                            fo.write('import ' + _ + '\n')
                        fo.write('\n')
                        for _ in list_objects:
                            fo.write(_ + ' = []' + '\n')
                        fo.write('\n')
                    fo.close()
                with open('./auto_gen_main_page.py', 'a') as fo:
                    fo.write('main_page = 0\n')
                fo.close()

            # step through btnx_master
            layer_count = 0
            i_btnx_master = 0
            for _ in btnx_master:

                # bring in variables from btnx_master
                btnx_gen_max = btnx_master[i_btnx_master][0]
                btnx_row_idx_max = btnx_master[i_btnx_master][1]
                btnx_position_initialize_x, btnx_position_initialize_y = btnx_master[i_btnx_master][2], btnx_master[i_btnx_master][3]
                btnx_size = btnx_master[i_btnx_master][4]
                btnx_size_Y = btnx_master[i_btnx_master][5]
                btnx_sp_size = btnx_master[i_btnx_master][6]
                btnx_sp_size_Y = btnx_master[i_btnx_master][7]

                # automatically generate objects in a loop
                i = 0
                i_x = 0
                main_page = 0
                btnx_i_timer = 0
                btnx_i_sub_timer = 0
                btnx_double_i_timer = 0
                btnx_double_i_sub_timer = 0
                while i_x < btnx_gen_max:

                    # button intitiation using values from btnx_master
                    if auto_generate_btn is True:
                        btnx_name = 'btnx_' + str(i_x)
                        self.btnx = btnx_name
                        self.btnx = QPushButton(self)
                        self.btnx.resize(btnx_size, btnx_size)
                        self.btnx.setText(btnx_name)
                        btnx_var.append(self.btnx)
                        ui_object_complete.append(self.btnx)
                        self.btnx.installEventFilter(self.filter)
                        self.btnx.hide()

                        # automatically position
                        if i == 0:
                            self.btnx.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))
                        elif i >= 1:
                            self.btnx.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i) + (btnx_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))

                        if auto_setup is True:

                            # automatically write boolean file
                            with open('./auto_gen_btnx_bool.py', 'a') as fo:
                                fo.write(btnx_name + '_bool = False' + '\n')
                            fo.close()

                            # automatically create functions
                            with open('./auto_gen_btnx_function.py', 'a') as fo:
                                if i_x in turn_page_reserved:
                                    # start timer
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_start_timer_function():' + '\n')
                                    fo.write("    global var_btnx_timer\n")
                                    fo.write("    var_btnx_timer[" + str(btnx_i_timer) + "].start()" + '\n\n')
                                    # stop timer
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_stop_timer_function():' + '\n')
                                    fo.write("    global var_btnx_timer\n")
                                    fo.write("    var_btnx_timer[" + str(btnx_i_timer) + "].stop()" + '\n\n')
                                    # update tbx
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_timer_clicked_function():' + '\n')
                                    fo.write('    print(' + btnx_name + '_timer_clicked_function)\n\n')
                                    btnx_i_timer += 1
                                else:
                                    # automatically create page conditions
                                    inner_loop_i = 0
                                    while inner_loop_i < len(turn_page_reserved):
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_start_timer_function():' + '\n')
                                        fo.write("    global var_btnx_timer_sub\n")
                                        fo.write("    var_btnx_timer_sub[" + str(btnx_i_sub_timer) + "].start()" + '\n\n')
                                        # stop timer
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_stop_timer_function():' + '\n')
                                        fo.write("    global var_btnx_timer_sub\n")
                                        fo.write("    var_btnx_timer_sub[" + str(btnx_i_sub_timer) + "].stop()" + '\n\n')
                                        # update tbx
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_timer_clicked_function():' + '\n')
                                        fo.write('    print(' + btnx_name + '_' + str(inner_loop_i) + '_timer_clicked_function)\n\n')
                                        btnx_i_sub_timer += 1
                                        inner_loop_i += 1
                                fo.write('def ' + btnx_name + '_function():' + '\n')

                                # automatically create page functions
                                if i_x in turn_page_reserved:
                                    fo.write('    auto_gen_main_page.main_page = ' + str(main_page) + '\n')
                                    fo.write('    if auto_gen_btnx_bool.' + btnx_name + '_bool is True:' + '\n')
                                    fo.write('        auto_gen_btnx_bool.' + btnx_name + '_bool = False' + '\n')
                                    fo.write('        # ' + btnx_name + '_stop_timer_function()' + '\n')
                                    fo.write('    elif auto_gen_btnx_bool.' + btnx_name + '_bool is False:' + '\n')
                                    fo.write('        auto_gen_btnx_bool.' + btnx_name + '_bool = True' + '\n')
                                    fo.write('        # ' + btnx_name + '_start_timer_function()' + '\n')
                                    fo.write("    print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool." + btnx_name + "_bool) + ']')\n\n")
                                else:
                                    # automatically create page conditions
                                    inner_loop_i = 0
                                    while inner_loop_i < len(turn_page_reserved):
                                        if inner_loop_i == 0:
                                            fo.write('    if auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                        else:
                                            fo.write('    elif auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                        fo.write('        if auto_gen_btnx_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool is True:' + '\n')
                                        fo.write('            auto_gen_btnx_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                        fo.write("            print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool." + btnx_name + '_' + str(inner_loop_i) + "_bool) + ']')\n")
                                        fo.write('            # ' + btnx_name + '_' + str(inner_loop_i) + '_stop_timer_function()' + '\n\n')
                                        fo.write('        elif auto_gen_btnx_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool is False:' + '\n')
                                        fo.write('            auto_gen_btnx_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool = True' + '\n')
                                        fo.write("            print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool." + btnx_name + '_' + str(inner_loop_i) + "_bool) + ']')\n")
                                        fo.write('            # ' + btnx_name + '_' + str(inner_loop_i) + '_start_timer_function()' + '\n\n')
                                        # automatically write boolean file
                                        with open('./auto_gen_btnx_bool.py', 'a') as fo_bool:
                                            fo_bool.write(btnx_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                        fo_bool.close()
                                        inner_loop_i += 1
                            fo.close()
                        # automatically create timers
                        if i_x in turn_page_reserved:
                            # btnx_name_timer = btnx_name + '_timer'
                            btnx_name_timer = QTimer(self)
                            btnx_name_timer.setInterval(0)
                            btnx_timer.append(btnx_name_timer)
                        else:
                            inner_loop_i = 0
                            while inner_loop_i < len(turn_page_reserved):
                                # btnx_name_timer = btnx_name + '_' + str(inner_loop_i) + '_timer'
                                btnx_name_timer = QTimer(self)
                                btnx_name_timer.setInterval(0)
                                btnx_timer_sub.append(btnx_name_timer)
                                inner_loop_i += 1
                        # automatically size window per object created
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * btnx_size)
                            app_width_static = app_width_static + (btnx_row_idx_max * btnx_sp_size) + btnx_sp_size
                    # button double initiation using values from btnx_master
                    if auto_generate_btn_double is True:
                        btnx_name = 'btnx_double_' + str(i_x)
                        self.btnx = btnx_name
                        self.btnx = QPushButton(self)
                        self.btnx.resize((btnx_size * 2) + btnx_sp_size, btnx_size)
                        self.btnx.setText(btnx_name)
                        btnx_double_var.append(self.btnx)
                        ui_object_complete.append(self.btnx)
                        self.btnx.installEventFilter(self.filter)
                        self.btnx.hide()
                        # automatically position
                        if i == 0:
                            self.btnx.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))
                        elif i >= 1:
                            self.btnx.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i) + (btnx_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))
                        # automatically write boolean file
                        if auto_setup is True:
                            with open('./auto_gen_btnx_double_bool.py', 'a') as auto_fo:
                                auto_fo.write(btnx_name + '_bool = False' + '\n')
                            auto_fo.close()

                            # automatically create functions
                            with open('./auto_gen_btnx_double_function.py', 'a') as fo:

                                if i_x in turn_page_reserved:
                                    # start timer
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_start_timer_function():' + '\n')
                                    fo.write("    global var_btnx_double_timer\n")
                                    fo.write("    var_btnx_double_timer[" + str(btnx_double_i_timer) + "].start()" + '\n\n')
                                    # stop timer
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_stop_timer_function():' + '\n')
                                    fo.write("    global var_btnx_double_timer\n")
                                    fo.write("    var_btnx_double_timer[" + str(btnx_double_i_timer) + "].stop()" + '\n\n')
                                    # update tbx
                                    fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                    fo.write('def ' + btnx_name + '_timer_clicked_function():' + '\n')
                                    fo.write('    print(' + btnx_name + '_timer_clicked_function)\n\n')
                                    btnx_double_i_timer += 1
                                else:
                                    # automatically create page conditions
                                    inner_loop_i = 0
                                    while inner_loop_i < len(turn_page_reserved):
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_start_timer_function():' + '\n')
                                        fo.write("    global var_btnx_double_timer_sub\n")
                                        fo.write("    var_btnx_double_timer_sub[" + str(btnx_double_i_sub_timer) + "].start()" + '\n\n')
                                        # stop timer
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_stop_timer_function():' + '\n')
                                        fo.write("    global var_btnx_double_timer_sub\n")
                                        fo.write("    var_btnx_double_timer_sub[" + str(btnx_double_i_sub_timer) + "].stop()" + '\n\n')
                                        # update tbx
                                        fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                        fo.write('def ' + btnx_name + '_' + str(inner_loop_i) + '_timer_clicked_function():' + '\n')
                                        fo.write('    print(' + btnx_name + '_' + str(inner_loop_i) + '_timer_clicked_function)\n\n')
                                        btnx_double_i_sub_timer += 1
                                        inner_loop_i += 1

                                # automatically create page functions
                                if i_x in turn_page_reserved:
                                    fo.write('def ' + btnx_name + '_function():' + '\n')
                                    fo.write('    auto_gen_main_page.main_page = ' + str(main_page) + '\n')
                                    fo.write('    if auto_gen_btnx_double_bool.' + btnx_name + '_bool is True:' + '\n')
                                    fo.write('        auto_gen_btnx_double_bool.' + btnx_name + '_bool = False' + '\n')
                                    fo.write('        # ' + btnx_name + '_stop_timer_function()' + '\n')
                                    fo.write('    elif auto_gen_btnx_double_bool.' + btnx_name + '_bool is False:' + '\n')
                                    fo.write('        auto_gen_btnx_double_bool.' + btnx_name + '_bool = True' + '\n')
                                    fo.write('        # ' + btnx_name + '_start_timer_function()' + '\n')
                                    fo.write("    print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool." + btnx_name + "_bool) + ']')\n\n")
                                else:
                                    # automatically create page conditions
                                    fo.write('def ' + btnx_name + '_function():' + '\n')
                                    inner_loop_i = 0
                                    while inner_loop_i < len(turn_page_reserved):
                                        if inner_loop_i == 0:
                                            fo.write('    if auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                        else:
                                            fo.write('    elif auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                        fo.write('        if auto_gen_btnx_double_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool is True:' + '\n')
                                        fo.write('            auto_gen_btnx_double_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                        fo.write("            print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool." + btnx_name + '_' + str(inner_loop_i) + "_bool) + ']')\n")
                                        fo.write('            # ' + btnx_name + '_' + str(inner_loop_i) + '_stop_timer_function()' + '\n\n')
                                        fo.write('        elif auto_gen_btnx_double_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool is False:' + '\n')
                                        fo.write('            auto_gen_btnx_double_bool.' + btnx_name + '_' + str(inner_loop_i) + '_bool = True' + '\n')
                                        fo.write("            print('[" + btnx_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool." + btnx_name + '_' + str(inner_loop_i) + "_bool) + ']')\n")
                                        fo.write('            # ' + btnx_name + '_' + str(inner_loop_i) + '_start_timer_function()' + '\n\n')

                                        # automatically write boolean file
                                        with open('./auto_gen_btnx_double_bool.py', 'a') as fo_bool:
                                            fo_bool.write(btnx_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                        fo_bool.close()
                                        inner_loop_i += 1
                            fo.close()

                        # automatically create timers
                        if i_x in turn_page_reserved:
                            # btnx_double_name_timer = btnx_name + '_timer'
                            btnx_double_name_timer = QTimer(self)
                            btnx_double_name_timer.setInterval(0)
                            btnx_double_timer.append(btnx_double_name_timer)
                        else:
                            inner_loop_i = 0
                            while inner_loop_i < len(turn_page_reserved):
                                # btnx_double_name_timer = btnx_name + '_' + str(inner_loop_i) + '_timer'
                                btnx_double_name_timer = QTimer(self)
                                btnx_double_name_timer.setInterval(0)
                                btnx_double_timer_sub.append(btnx_double_name_timer)
                                inner_loop_i += 1

                        # automatically size window per object created
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * btnx_size)
                            app_width_static = app_width_static + (btnx_row_idx_max * btnx_sp_size) + btnx_sp_size
                    
                    # label initiation using values from btnx_master and multiplied
                    if auto_generate_lbl is True:
                        lblx_name = 'lblx_' + str(i_x)
                        self.lblx = lblx_name
                        self.lblx = QLabel(self)
                        self.lblx.resize((btnx_size * 2) + btnx_sp_size, btnx_size)
                        self.lblx.setText(lblx_name)
                        lblx_var.append(self.lblx)
                        ui_object_complete.append(self.lblx)
                        self.lblx.installEventFilter(self.filter)
                        self.lblx.hide()
                        # automatically position
                        if i == 0:
                            self.lblx.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))
                        elif i >= 1:
                            self.lblx.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + ((btnx_sp_size*1) * i) + ((btnx_size*1) * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * (btnx_size*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_size*1)) + btnx_sp_size

                    # qlineedit intitiation using values from btnx_master and multiplied  returnPressed.connect
                    if auto_generate_qle is True:
                        qlex_name = 'qlex_' + str(i_x)
                        self.qlex = qlex_name
                        self.qlex = QLineEdit(self)
                        self.qlex.resize(btnx_size, int(btnx_size / 2))
                        self.qlex.setText(qlex_name)
                        qlex_var.append(self.qlex)
                        ui_object_complete.append(self.qlex)
                        self.qlex.installEventFilter(self.filter)
                        self.qlex.hide()
                        # automatically position button
                        if i == 0:
                            self.qlex.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))
                        elif i >= 1:
                            self.qlex.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i) + (btnx_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))

                        # automatically create functions
                        if auto_setup is True:
                            with open('./auto_gen_qle_returnpressed_connect_function.py', 'a') as fo:
                                fo.write('def ' + qlex_name + '_returnPressed_connect_function():' + '\n')
                                fo.write("    print(str('[' + str(datetime.datetime.now()) + '] return pressed: " + qlex_name + "'))\n")

                                # automatically create page conditions
                                inner_loop_i = 0
                                while inner_loop_i < len(turn_page_reserved):
                                    if inner_loop_i == 0:
                                        fo.write('    if auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                    else:
                                        fo.write('    elif auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                    fo.write('        if auto_gen_qle_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool is True:' + '\n')
                                    fo.write('            auto_gen_qle_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                    fo.write("            print('[" + qlex_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool." + qlex_name + '_' + str(inner_loop_i) + "_bool) + ']')\n\n")
                                    fo.write('        elif auto_gen_qle_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool is False:' + '\n')
                                    fo.write('            auto_gen_qle_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool = True' + '\n')
                                    fo.write("            print('[" + qlex_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool." + qlex_name + '_' + str(inner_loop_i) + "_bool) + ']')\n\n")

                                    # automatically write boolean file
                                    with open('./auto_gen_qle_bool.py', 'a') as fo_bool:
                                        fo_bool.write(qlex_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                    fo_bool.close()
                                    inner_loop_i += 1
                            fo.close()

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * (btnx_size*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_size*1)) + btnx_sp_size

                    # qlineedit double intitiation using values from btnx_master and multiplied
                    if auto_generate_qle_double is True:
                        qlex_name = 'qlex_double_' + str(i_x)
                        self.qlex = qlex_name
                        self.qlex = QLineEdit(self)
                        self.qlex.resize((btnx_size * 2) + btnx_sp_size, int(btnx_size / 2))
                        self.qlex.setText(qlex_name)
                        qlex_double_var.append(self.qlex)
                        ui_object_complete.append(self.qlex)
                        self.qlex.installEventFilter(self.filter)
                        self.qlex.hide()

                        # automatically position
                        if i == 0:
                            self.qlex.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))
                        elif i >= 1:
                            self.qlex.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + ((btnx_sp_size*1) * i) + ((btnx_size*1) * i),
                                            btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))

                        # automatically create functions
                        if auto_setup is True:
                            with open('./auto_gen_qle_double_returnpressed_connect_function.py', 'a') as fo:
                                fo.write('def ' + qlex_name + '_returnPressed_connect_function():' + '\n')
                                fo.write("    print(str('[' + str(datetime.datetime.now()) + '] return pressed: " + qlex_name + "'))\n")

                                # automatically create page conditions
                                inner_loop_i = 0
                                while inner_loop_i < len(turn_page_reserved):
                                    if inner_loop_i == 0:
                                        fo.write('    if auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                    else:
                                        fo.write('    elif auto_gen_main_page.main_page == ' + str(inner_loop_i) + ':\n')
                                    fo.write('        if auto_gen_qle_double_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool is True:' + '\n')
                                    fo.write('            auto_gen_qle_double_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                    fo.write("            print('[" + qlex_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool." + qlex_name + '_' + str(inner_loop_i) + "_bool) + ']')\n\n")
                                    fo.write('        elif auto_gen_qle_double_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool is False:' + '\n')
                                    fo.write('            auto_gen_qle_double_bool.' + qlex_name + '_' + str(inner_loop_i) + '_bool = True' + '\n')
                                    fo.write("            print('[" + qlex_name + "] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool." + qlex_name + '_' + str(inner_loop_i) + "_bool) + ']')\n\n")

                                    # automatically write boolean file
                                    with open('./auto_gen_qle_double_bool.py', 'a') as fo_bool:
                                        fo_bool.write(qlex_name + '_' + str(inner_loop_i) + '_bool = False' + '\n')
                                    fo_bool.close()
                                    inner_loop_i += 1
                            fo.close()

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * (btnx_size*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_size*1)) + btnx_sp_size

                    # auto_generate_tb
                    if auto_generate_tb is True:
                        tbx_name = 'tbx_' + str(i_x)
                        self.tbx = tbx_name
                        self.tbx = QTextBrowser(self)
                        self.tbx.resize((btnx_size * 2) + btnx_sp_size, btnx_size)
                        self.tbx.setText(tbx_name)
                        # self.tbx.setLineWrapMode(QTextBrowser.NoWrap)  # optional nowrap
                        # self.tbx.horizontalScrollBar().setValue(0)  # optional keep horizontal scroll full left
                        tbx_var.append(self.tbx)
                        ui_object_complete.append(self.tbx)
                        self.tbx.installEventFilter(self.filter)
                        self.tbx.hide()

                        # automatically position
                        if i == 0:
                            self.tbx.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + (btnx_sp_size * i),
                                           btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))
                        elif i >= 1:
                            self.tbx.move(main_border_height + btnx_position_initialize_x + btnx_sp_size + ((btnx_sp_size*1) * i) + ((btnx_size*1) * i),
                                           btnx_position_initialize_y + btnx_size_Y + (btnx_sp_size_Y))

                        # automatically create functions
                        if auto_setup is True:
                            with open('./auto_gen_tbx_update_function.py', 'a') as fo:

                                # start timer
                                fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_start_timer_function():' + '\n')
                                fo.write("    global var_tbx_timer\n")
                                fo.write("    var_tbx_timer[" + str(i_x) + "].start()" + '\n\n')

                                # stop timer
                                fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_stop_timer_function():' + '\n')
                                fo.write("    global var_tbx_timer\n")
                                fo.write("    var_tbx_timer[" + str(i_x) + "].stop()" + '\n\n')

                                # update tbx
                                fo.write('message_'+str(i_x)+' = []\n')
                                fo.write('@PyQt5.QtCore.pyqtSlot()' + '\n')
                                fo.write('def ' + tbx_name + '_timer_append_function():' + '\n')
                                fo.write("    global message_" + str(i_x) + '\n')
                                fo.write("    global var_tbx\n")
                                fo.write("    if message_" + str(i_x) + ':' + '\n')
                                fo.write("        var_tbx[" + str(i_x) + "].append(" + "message_" + str(i_x) + '[0])' + '\n')
                                fo.write("        message_"+str(i_x)+".remove(message_" + str(i_x) + '[0])' + '\n\n')
                                
                            fo.close()

                        # automatically create timers
                        # tbx_name_timer = tbx_name + '_timer'
                        tbx_name_timer = QTimer(self)
                        tbx_name_timer.setInterval(0)
                        tbx_timer.append(tbx_name_timer)

                        # set application window geometry each iteration
                        if configuration_override_size is False:
                            app_height_static = ((layer_count+2) * btnx_size)
                            app_height_static = app_height_static + ((layer_count+2) * btnx_sp_size)
                            app_width_static = ((btnx_row_idx_max) * (btnx_size*1))
                            app_width_static = app_width_static + (btnx_row_idx_max * (btnx_sp_size*1)) + btnx_sp_size

                    # add one to row index
                    i += 1

                    # adjust height position for objects after reaching row index max
                    if i == btnx_row_idx_max:
                        i = 0
                        layer_count += 1
                        btnx_size_Y = btnx_size_Y + btnx_size
                        btnx_sp_size_Y = btnx_sp_size_Y + btnx_sp_size

                    # add one every time a button is created that exists in turn_page_reserved
                    if i_x in turn_page_reserved:
                        main_page += 1

                    # add one every time a button is created
                    i_x += 1

                i_btnx_master += 1

            # FINALLY - set application window geometry and position some extras
            app_height_static += (main_border_height)
            app_width_static += (main_border_height * 2)

            # attatch to taskbar
            if pin_to_taskbar is True:
                app_height_pos = int(QDesktopWidget().availableGeometry().height()) - int(app_height_static)
                if l_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(0, app_height_pos, app_width_static, app_height_static)
                elif r_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(QDesktopWidget().availableGeometry().width() - app_width_static,
                                                     app_height_pos, app_width_static, app_height_static)
                elif c_pin_to_taskbar is True:
                    event_filter_self[0].setGeometry(
                        int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2),
                        app_height_pos, app_width_static, app_height_static)

            # position application center screen
            elif pin_to_taskbar is False:
                app_height_pos = int(QDesktopWidget().availableGeometry().height() / 2) - int(app_height_static / 2)
                app_width_pos = int(QDesktopWidget().availableGeometry().width() / 2) - int(app_width_static / 2)
                self.setGeometry(app_width_pos, app_height_pos, app_width_static, app_height_static)

            # close, minimize
            # self.btn_minimize.move((app_width_static - (titlebar_height + main_border_height) * 2), main_border_height)
            # self.btn_quit.move((app_width_static - (titlebar_height + main_border_height)), main_border_height)

            # automatically plug everything in
            if auto_generate_btn is True:
                # import auto_gen_btnx_bool
                import auto_gen_btnx_function
                auto_gen_btnx_function.var_btnx = btnx_var
                auto_gen_btnx_function.var_btnx_double = btnx_double_var
                auto_gen_btnx_function.var_lblx = lblx_var
                auto_gen_btnx_function.var_qlex = qlex_var
                auto_gen_btnx_function.var_qlex_double = qlex_double_var
                auto_gen_btnx_function.var_tbx = tbx_var
                auto_gen_btnx_function.var_tbx_timer = tbx_timer
                auto_gen_btnx_function.var_btnx_timer = btnx_timer
                auto_gen_btnx_function.var_btnx_timer_sub = btnx_timer_sub
                auto_gen_btnx_function.var_self.append(self)

                i = 0
                for _ in btnx_var:
                    btnx_var[i].clicked.connect(getattr(auto_gen_btnx_function, 'btnx_' + str(i) + '_function'))
                    i += 1

                # timeout connect for btnx_double_var in turn_page_reserved
                i = 0
                i_2 = 0
                for _ in btnx_var:
                    if i in turn_page_reserved:
                        btnx_timer[i_2].timeout.connect(getattr(auto_gen_btnx_function, 'btnx_' + str(i) + '_timer_clicked_function'))
                        print('plugging in btn:', i)
                        i_2 += 1
                    i += 1

                # timeout connect for btnx_double_var not in turn_page_reserved
                i = 0
                i_timer_sub = 0
                for _ in btnx_var:
                    if i not in turn_page_reserved:
                        inner_i_timer_sub = 0
                        while inner_i_timer_sub < len(turn_page_reserved):
                            print(i, i_timer_sub, inner_i_timer_sub, _)
                            btnx_timer_sub[i_timer_sub].timeout.connect(getattr(auto_gen_btnx_function, 'btnx_' + str(i) + '_' + str(inner_i_timer_sub) + '_timer_clicked_function'))
                            inner_i_timer_sub += 1
                            i_timer_sub += 1
                    i += 1

            # automatically plug everything in
            if auto_generate_btn_double is True:
                # import auto_gen_btnx_double_bool
                import auto_gen_btnx_double_function
                auto_gen_btnx_double_function.var_btnx = btnx_var
                auto_gen_btnx_double_function.var_btnx_double = btnx_double_var
                auto_gen_btnx_double_function.var_lblx = lblx_var
                auto_gen_btnx_double_function.var_qlex = qlex_var
                auto_gen_btnx_double_function.var_qlex_double = qlex_double_var
                auto_gen_btnx_double_function.var_tbx = tbx_var
                auto_gen_btnx_double_function.var_tbx_timer = tbx_timer
                auto_gen_btnx_double_function.var_btnx_double_timer = btnx_double_timer
                auto_gen_btnx_double_function.var_btnx_double_timer_sub = btnx_double_timer_sub
                auto_gen_btnx_double_function.var_self.append(self)

                print('btnx_double_timer_sub:', btnx_double_timer_sub)
                print('btnx_double_timer_sub len:', len(btnx_double_timer_sub))

                i = 0
                for _ in btnx_double_var:
                    btnx_double_var[i].clicked.connect(getattr(auto_gen_btnx_double_function, 'btnx_double_' + str(i) + '_function'))
                    i += 1

                # timeout connect for btnx_double_var in turn_page_reserved
                i = 0
                i_2 = 0
                for _ in btnx_double_var:
                    if i in turn_page_reserved:
                        btnx_double_timer[i_2].timeout.connect(getattr(auto_gen_btnx_double_function, 'btnx_double_' + str(i) + '_timer_clicked_function'))
                        print('plugging in btn:', i)
                        i_2 += 1
                    i += 1

                # timeout connect for btnx_double_var not in turn_page_reserved
                i = 0
                i_timer_sub = 0
                for _ in btnx_double_var:
                    if i not in turn_page_reserved:
                        inner_i_timer_sub = 0
                        while inner_i_timer_sub < len(turn_page_reserved):
                            print(i, i_timer_sub, inner_i_timer_sub, _)
                            btnx_double_timer_sub[i_timer_sub].timeout.connect(getattr(auto_gen_btnx_double_function, 'btnx_double_' + str(i) + '_' + str(inner_i_timer_sub) + '_timer_clicked_function'))
                            inner_i_timer_sub += 1
                            i_timer_sub += 1
                    i += 1

            # automatically plug everything in
            if auto_generate_qle is True:
                # import auto_gen_qle_bool
                import auto_gen_qle_returnpressed_connect_function
                auto_gen_qle_returnpressed_connect_function.var_btnx = btnx_var
                auto_gen_qle_returnpressed_connect_function.var_btnx_double = btnx_double_var
                auto_gen_qle_returnpressed_connect_function.var_lblx = lblx_var
                auto_gen_qle_returnpressed_connect_function.var_qlex = qlex_var
                auto_gen_qle_returnpressed_connect_function.var_qlex_double = qlex_double_var
                auto_gen_qle_returnpressed_connect_function.var_tbx = tbx_var
                auto_gen_qle_returnpressed_connect_function.var_tbx_timer = tbx_timer
                i = 0
                for _ in qlex_var:
                    qlex_var[i].returnPressed.connect(getattr(auto_gen_qle_returnpressed_connect_function, 'qlex_' + str(i) + '_returnPressed_connect_function'))
                    i += 1

            # automatically plug everything in
            if auto_generate_qle_double is True:
                # import auto_gen_qle_double_bool
                import auto_gen_qle_double_returnpressed_connect_function
                auto_gen_qle_double_returnpressed_connect_function.var_btnx = btnx_var
                auto_gen_qle_double_returnpressed_connect_function.var_btnx_double = btnx_double_var
                auto_gen_qle_double_returnpressed_connect_function.var_lblx = lblx_var
                auto_gen_qle_double_returnpressed_connect_function.var_qlex = qlex_var
                auto_gen_qle_double_returnpressed_connect_function.var_qlex_double = qlex_double_var
                auto_gen_qle_double_returnpressed_connect_function.var_tbx = tbx_var
                auto_gen_qle_double_returnpressed_connect_function.var_tbx_timer = tbx_timer
                i = 0
                for _ in qlex_double_var:
                    qlex_double_var[i].returnPressed.connect(getattr(auto_gen_qle_double_returnpressed_connect_function, 'qlex_double_' + str(i) + '_returnPressed_connect_function'))
                    i += 1

            # automatically plug everything in
            if auto_generate_tb is True:
                import auto_gen_tbx_update_function
                auto_gen_tbx_update_function.var_btnx = btnx_var
                auto_gen_tbx_update_function.var_btnx_double = btnx_double_var
                auto_gen_tbx_update_function.var_lblx = lblx_var
                auto_gen_tbx_update_function.var_qlex = qlex_var
                auto_gen_tbx_update_function.var_qlex_double = qlex_double_var
                auto_gen_tbx_update_function.var_tbx = tbx_var
                auto_gen_tbx_update_function.var_tbx_timer = tbx_timer
                i = 0
                for _ in tbx_timer:
                    tbx_timer[i].timeout.connect(getattr(auto_gen_tbx_update_function, 'tbx_' + str(i) + '_timer_append_function'))
                    i += 1

        # automatic object generation
        if enable_title_bar_toolbar is True:
            create_titlebar_menubar()
        if auto_generate is True:
            automatic_object_generator()

        # show reserved
        def show_reserved_btnx():
            global reserve_btnx, btnx_var
            i_res = 0
            for _ in btnx_var:
                if i_res in reserve_btnx:
                    _.show()
                i_res += 1

        # show reserved
        def show_reserved_btnx_double():
            global reserve_btnx_double, btnx_double_var
            i_res = 0
            for _ in btnx_double_var:
                if i_res in reserve_btnx_double:
                    _.show()
                i_res += 1

        # button title bar logo
        def btn_title_logo_function_0():
            print('')

        print(f'self.width(): {self.width()}')
        print(f'self.height(): {self.height()}')
        self.toolbar_label.resize(self.width() - (main_border_height * 2), (btn_size_titlebar * 1) + main_border_height)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.title_bar_close))
        self.title_bar_close = QIcon(pixmap)

        # button: quit (use main_border_height)
        self.btn_quit = QPushButton(self)
        self.btn_quit.move(btnx_var[15].pos().x(), main_border_height)
        self.btn_quit.resize(btnx_size - 4, btnx_size - 4)
        self.btn_quit.setIcon(self.title_bar_close)
        self.btn_quit.setIconSize(QSize(48, 48))
        self.btn_quit.setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        self.btn_quit.installEventFilter(self.filter)
        ui_object_complete.append(self.btn_quit)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.title_bar_minimize))
        self.title_bar_minimize = QIcon(pixmap)

        # button: minimize (use main_border_height)
        self.btn_minimize = QPushButton(self)
        self.btn_minimize.move(btnx_var[14].pos().x(), main_border_height)
        self.btn_minimize.resize(btnx_size - 4, btnx_size - 4)
        self.btn_minimize.setIcon(self.title_bar_minimize)
        self.btn_minimize.setIconSize(QSize(48, 48))
        self.btn_minimize.setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        self.btn_minimize.installEventFilter(self.filter)
        ui_object_complete.append(self.btn_minimize)

        # plug in title bar quit, minimize and logo button
        self.btn_quit.clicked.connect(QCoreApplication.instance().quit)
        self.btn_minimize.clicked.connect(self.showMinimized)
        self.btn_title_logo.clicked.connect(btn_title_logo_function_0)

        # display reserved buttons (could be main menu button(s))
        if reserve_btnx_double_bool is True:
            show_reserved_btnx_double()

        # install an event filter to self
        self.installEventFilter(self.filter)

        # uncomment timer start function to enable view locals/globals sizes
        # self.timer_00 = QTimer(self)
        # self.timer_00.setInterval(3000)
        # self.timer_00.timeout.connect(self.timer_00_function)
        # self.timer_00_start_function()

        # set main image timer
        self.timer_0 = QTimer(self)
        self.timer_0.setInterval(1000)
        self.timer_0.timeout.connect(self.timer_0_function)

        # set main image timer
        self.timer_1 = QTimer(self)
        self.timer_1.setInterval(1000)
        self.timer_1.timeout.connect(self.timer_1_function)

        # set training output timer
        self.timer_2 = QTimer(self)
        self.timer_2.setInterval(250)  # 0
        self.timer_2.timeout.connect(self.timer_2_function)

        # set annotation output timer
        self.timer_3 = QTimer(self)
        self.timer_3.setInterval(250)  # 0
        self.timer_3.timeout.connect(self.timer_3_function)

        # set main image timer
        self.timer_4 = QTimer(self)
        self.timer_4.setInterval(1000)
        self.timer_4.timeout.connect(self.timer_4_function)

        # set main image timer
        self.timer_5 = QTimer(self)
        self.timer_5.setInterval(250)  # 0
        self.timer_5.timeout.connect(self.timer_gui_updates)
        self.timer_5_start_function()

        # threads
        self.thread_0 = Class0()
        self.thread_1 = Class1()
        self.thread_2 = Class2()

        self.frame = ""

        # main image label
        self.video_label = 16
        self.video_label_size_w = (btnx_size * 14) + (btnx_sp_size * 13)
        self.video_label_size_h = (btnx_size * 7) + (btnx_sp_size * 6)
        lblx_var[self.video_label].setText('')
        lblx_var[self.video_label].resize(self.video_label_size_w, self.video_label_size_h)
        self.image_size_w = 0
        self.image_size_h = 0
        self.splash_image = numpy.zeros((self.video_label_size_w, self.video_label_size_h, 3), dtype=numpy.uint8)
        self.splash_image = QImage(self.splash_image, self.splash_image.shape[1], self.splash_image.shape[0], QImage.Format_RGB888)
        self.set_main_label_1()

        # main output textbox
        tbx_var[16].setText('')
        tbx_var[16].resize((btnx_size * 14) + (btnx_sp_size * 13), (btnx_size * 7) + (btnx_sp_size * 6))
        tbx_var[16].hide()

        # Camera Det.
        btnx_double_var[0].setText('Camera')
        btnx_double_var[0].clicked.connect(self.mode_select_camera)

        # Video Det.
        btnx_double_var[2].setText('Video')
        btnx_double_var[2].clicked.connect(self.mode_select_video)

        # Manual Annotation.
        btnx_double_var[4].setText('Annotate')
        btnx_double_var[4].clicked.connect(self.mode_manual_annotation)

        # Training.
        btnx_double_var[6].setText('Training')
        btnx_double_var[6].clicked.connect(self.mode_training)

        # Frame slider
        self.slider_frame_track = QSlider(self)
        self.slider_frame_track.setGeometry(QtCore.QRect(btnx_double_var[132].pos().x(), btnx_double_var[132].pos().y(), (btnx_size * 4) + (btnx_sp_size * 2), btnx_size))
        self.slider_frame_track.setOrientation(QtCore.Qt.Horizontal)
        self.slider_frame_track.hide()

        # Probability slider
        self.slider_minimum_percentage_probability = QSlider(self)
        self.slider_minimum_percentage_probability.setGeometry(QtCore.QRect(btnx_double_var[47].pos().x(), btnx_double_var[47].pos().y(), (btnx_size * 1), btnx_size))
        self.slider_minimum_percentage_probability.setOrientation(QtCore.Qt.Horizontal)
        self.slider_minimum_percentage_probability.setMinimum(1)
        self.slider_minimum_percentage_probability.setMaximum(100)
        self.slider_minimum_percentage_probability.setSliderPosition(minimum_percentage_probability)
        self.slider_minimum_percentage_probability.hide()

        # Target Probability slider
        self.slider_target_minimum_percentage_probability = QSlider(self)
        self.slider_target_minimum_percentage_probability.setGeometry(QtCore.QRect(btnx_double_var[44].pos().x(), btnx_double_var[44].pos().y(), (btnx_size * 2) + btnx_sp_size, btnx_size))
        self.slider_target_minimum_percentage_probability.setOrientation(QtCore.Qt.Horizontal)
        self.slider_target_minimum_percentage_probability.setMinimum(1)
        self.slider_target_minimum_percentage_probability.setMaximum(100)
        self.slider_target_minimum_percentage_probability.setSliderPosition(50)
        self.slider_target_minimum_percentage_probability.hide()

        # Frame detection interval slider
        self.slider_frame_detection_interval = QSlider(self)
        self.slider_frame_detection_interval.setGeometry(QtCore.QRect(btnx_double_var[31].pos().x(), btnx_double_var[31].pos().y(), (btnx_size * 1), btnx_size))
        self.slider_frame_detection_interval.setOrientation(QtCore.Qt.Horizontal)
        self.slider_frame_detection_interval.setMinimum(1)
        self.slider_frame_detection_interval.setMaximum(1000)
        self.slider_frame_detection_interval.setSliderPosition(frame_detection_interval)
        self.slider_frame_detection_interval.hide()

        # Alpha slider
        self.slider_alpha = QSlider(self)
        self.slider_alpha.setGeometry(QtCore.QRect(btnx_var[143].pos().x(), btnx_var[143].pos().y(), (btnx_size * 1), btnx_size))
        self.slider_alpha.setOrientation(QtCore.Qt.Horizontal)
        self.slider_alpha.setMinimum(1)
        self.slider_alpha.setMaximum(230)
        self.slider_alpha.setSliderPosition(minimum_percentage_probability)
        self.slider_alpha.hide()

        # Select camera
        self.combo_box_camera = QComboBox(self)
        self.combo_box_camera.move(btnx_var[14].pos().x(), btnx_var[14].pos().y())
        self.combo_box_camera.resize((btnx_size * 2) + (btnx_sp_size * 1), btnx_size)
        self.combo_box_camera.setStyleSheet("""
            QComboBox {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            selection-color: rgb(14, 14, 14);
            selection-background-color: rgb(255, 0, 0);
            border-bottom:4px solid rgb""" + str(object_color_border_0) + """;
            border-right:4px solid rgb""" + str(object_color_border_0) + """;
            border-top:4px solid rgb""" + str(object_color_border_0) + """;
            border-left:4px solid rgb""" + str(object_color_border_0) + """;}
            }
            QComboBox QAbstractItemView {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border: 4px rgb(0, 0, 0);
            selection-background-color: rgb(0, 0, 0);
            outline: 0;}
            }
            """)
        for i_range in range(0, 1000):
            self.combo_box_camera.addItem(f'Camera: {i_range}')
        self.combo_box_camera.show()
        self.combo_box_camera.currentIndexChanged.connect(self.select_camera)
        self.combo_box_camera.hide()

        # Select exec event
        self.combo_box_exec = QComboBox(self)
        self.combo_box_exec.move(btnx_var[12].pos().x(), btnx_var[12].pos().y())
        self.combo_box_exec.resize((btnx_size * 2) + btnx_sp_size, btnx_size)
        self.combo_box_exec.setStyleSheet("""
            QComboBox {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            selection-color: rgb(14, 14, 14);
            selection-background-color: rgb(255, 0, 0);
            border-bottom:4px solid rgb""" + str(object_color_border_0) + """;
            border-right:4px solid rgb""" + str(object_color_border_0) + """;
            border-top:4px solid rgb""" + str(object_color_border_0) + """;
            border-left:4px solid rgb""" + str(object_color_border_0) + """;}
            }
            QComboBox QAbstractItemView {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border: 4px rgb(0, 0, 0);
            selection-background-color: rgb(0, 0, 0);
            outline: 0;}
            }
            """)
        self.combo_box_exec.addItem('Target Event')
        for i_range in range(0, TE_MAX):
            self.combo_box_exec.addItem(f'Event: {i_range}')
        self.combo_box_exec.setItemData(0, Qt.AlignCenter, Qt.TextAlignmentRole)
        self.combo_box_exec.currentIndexChanged.connect(self.add_remove_exec)
        self.combo_box_exec.hide()

        btnx_double_var[0].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;c
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:10px solid rgb""" + str(theme_color) + """;
            border-right:4px solid rgb""" + str(object_color_border_0) + """;
            border-top:4px solid rgb""" + str(object_color_border_0) + """;
            border-left:4px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color: rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:14px solid rgb(14, 14, 100);
            border-right:4px solid rgb""" + str(object_color_border_0) + """;
            border-top:4px solid rgb""" + str(object_color_border_0) + """;
            border-left:4px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)

        # Target event background label
        lblx_var[24].move(lblx_var[24].pos().x() - btnx_sp_size, lblx_var[24].pos().y() - btnx_sp_size)

        # Specify object name
        qlex_double_var[130].move(qlex_double_var[130].pos().x(), qlex_double_var[130].pos().y() + (btnx_size / 2))

        # tbx_var[88].verticalScrollBar().rangeChanged.connect(
        #     self.scrollToBottom_88,
        # )

        # Brush settings
        self.brush_color_a = 72
        self.brush_color_r, self.brush_color_g, self.brush_color_b = 0, 0, 0

        # Global position
        self.prev_pos = 0

        self.initUI()

    def initUI(self):
        # load camera tab
        self.mode_select_camera()
        # display application
        self.show()

    @QtCore.pyqtSlot()
    def GetTimeFromSeconds(self, _sec):
        sec = datetime.timedelta(seconds=_sec)
        d = datetime.datetime(1, 1, 1) + sec
        return "%d:%d:%d:%d" % (d.day - 1, d.hour, d.minute, d.second)

    @QtCore.pyqtSlot()
    def brush_alpha(self):
        if self.brush_color_a in range(0, 25):
            btnx_var[142].setText('25')
            self.brush_color_a = 25
        elif self.brush_color_a in range(25, 50):
            btnx_var[142].setText('50')
            self.brush_color_a = 50
        elif self.brush_color_a in range(50, 75):
            btnx_var[142].setText('75')
            self.brush_color_a = 75
        elif self.brush_color_a in range(75, 100):
            btnx_var[142].setText('100')
            self.brush_color_a = 100
        elif self.brush_color_a in range(100, 125):
            btnx_var[142].setText('125')
            self.brush_color_a = 125
        elif self.brush_color_a in range(125, 150):
            btnx_var[142].setText('150')
            self.brush_color_a = 150
        elif self.brush_color_a in range(150, 175):
            btnx_var[142].setText('175')
            self.brush_color_a = 175
        elif self.brush_color_a in range(175, 200):
            btnx_var[142].setText('200')
            self.brush_color_a = 200
        elif self.brush_color_a in range(200, 230):
            btnx_var[142].setText('230')
            self.brush_color_a = 230
        elif self.brush_color_a is 230:
            btnx_var[142].setText('1')
            self.brush_color_a = 1
        self.slider_alpha.setSliderPosition(self.brush_color_a)

    @QtCore.pyqtSlot()
    def set_style(self):
        # Stylesheet: self
        global theme_color, main_border_height, object_color_background_0, object_color_border_0
        self_style = """

                QMainWindow {background-color: rgb(0, 0, 0);
                color: rgb(200, 200, 200);
                border-top:""" + str(main_border_height) + """px solid rgb""" + str(theme_color) + """;
                border-bottom:""" + str(main_border_height) + """px solid rgb""" + str(theme_color) + """;
                border-right:""" + str(main_border_height) + """px solid rgb""" + str(theme_color) + """;
                border-left:""" + str(main_border_height) + """px solid rgb""" + str(theme_color) + """;}
                }

                QToolTip {background-color: rgb(35, 35, 35);
                color: rgb(200, 200, 200);
                border-top:0px solid rgb(35, 35, 35);
                border-bottom:0px solid rgb(35, 35, 35);
                border-right:0px solid rgb(0, 0, 0);
                border-left:0px solid rgb(0, 0, 0);
                }

                QScrollBar:vertical {
                width: 20px;
                margin: 20px 0px 20px 0px;
                background-color: rgb(18, 18, 18);
                }
                QScrollBar:horizontal {
                height: 20px;
                margin: 0px 20px 0px 20px;
                background-color: rgb(18, 18, 18);
                }

                QScrollBar::handle:vertical {
                background-color: rgb""" + str(theme_color) + """;
                border-bottom:4px solid rgb(0, 0, 0);
                border-top:4px solid rgb(0, 0, 0);
                min-height: 8px;
                }
                QScrollBar::handle:horizontal {
                background-color: rgb""" + str(theme_color) + """;
                border-left:4px solid rgb(0, 0, 0);
                border-right:4px solid rgb(0, 0, 0);
                min-width: 8px;
                }

                QScrollBar::add-line:vertical {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: bottom;
                subcontrol-origin: margin;
                }
                QScrollBar::sub-line:vertical {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: top;
                subcontrol-origin: margin;
                }

                QScrollBar::add-line:horizontal {
                background-color: rgb(18, 18, 18);
                height: 20px;
                width: 20px;
                subcontrol-position: right;
                subcontrol-origin: margin;
                }
                QScrollBar::sub-line:horizontal {
                background-color: rgb(20, 20, 20);
                height: 20px;
                width: 20px;
                subcontrol-position: top left;
                subcontrol-origin: margin;
                }

                QScrollBar::up-arrow:vertical {
                background-color: rgb""" + str(theme_color) + """;
                height: 8px;
                width: 20px;
                }
                QScrollBar::down-arrow:vertical {
                background-color: rgb""" + str(theme_color) + """;
                height: 8px;
                width: 20px;
                }

                QScrollBar::left-arrow:horizontal {
                background-color: rgb""" + str(theme_color) + """;
                height: 20px;
                width: 8px;
                }
                QScrollBar::right-arrow:horizontal {
                background-color: rgb""" + str(theme_color) + """;
                height: 20px;
                width: 8px;
                }

                QScrollBar::add-page:vertical {
                background-color: rgb(0, 0, 0);
                width: 20px;
                height: 20px;
                }
                QScrollBar::sub-page:vertical {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }

                QScrollBar::add-page:horizontal {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }
                QScrollBar::sub-page:horizontal {
                background-color: rgb(8, 8, 8);
                width: 20px;
                height: 20px;
                }

                QSlider::groove:horizontal {
                height: 6px;
                background: rgb(30, 30, 30);
                margin: 8px;
                border: 2px rgb""" + str(object_color_border_0) + """;
                }
                QSlider::handle:horizontal {
                background: rgb""" + str(theme_color) + """;
                border: 2px rgb""" + str(object_color_background_0) + """;
                width: 10px;
                height: 10px;
                margin: -15px 0px;
                }

                QMenuBar {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                }
                QMenuBar::item {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                }
                QMenuBar::item::selected {
                background-color: rgb(0, 0, 0);
                }
                QMenu {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb(224,224,224);
                border-top:0px solid rgb(0, 0, 0);
                border-bottom:0px solid rgb""" + str(theme_color) + """;
                border-right:0px solid rgb""" + str(theme_color) + """;
                border-left:0px solid rgb""" + str(theme_color) + """;
                }
                QMenu::item::selected {
                background-color: rgb""" + str(object_color_background_0) + """;
                color: rgb""" + str(theme_color) + """;
                }

                QPushButton{background-color: rgb(0, 0, 0);
                color : rgb(255, 255, 255);
                background-color : rgb(14, 14, 14);
                border-top:10px solid rgb(14, 14, 14);
                border-bottom:10px solid rgb(14, 14, 14);
                border-right:20px solid rgb(14, 14, 14);
                border-left:20px solid rgb(14, 14, 14);}
                }
                QPushButton::hover {background-color : rgb(14, 14, 14);
                }
                QPushButton::pressed {
                color : rgb(255, 255, 255);
                background-color : rgb(14, 14, 14);
                border-top:14px solid rgb(14, 14, 14);
                border-bottom:14px solid rgb(14, 14, 14);
                border-right:24px solid rgb(14, 14, 14);
                border-left:24px solid rgb(14, 14, 14);}
                }

                QLabel{background-color: rgb(0, 0, 0);
                color: rgb(255, 255, 255);
                border-top:4px solid rgb(0, 0, 0);
                border-bottom:4px solid rgb(0, 0, 0);
                border-right:4px solid rgb(0, 0, 0);
                border-left:4px solid rgb(0, 0, 0);}

                QLineEdit{background-color: rgb(16, 16, 16);
                color: rgb(255, 255, 255);
                border-top:4px solid rgb(14, 14, 14);
                border-bottom:4px solid rgb(14, 14, 14);
                border-right:4px solid rgb(14, 14, 14);
                border-left:4px solid rgb(14, 14, 14);}

                QTextBrowser {background-color: rgb(0, 0, 0);
                selection-color: black;
                selection-background-color: rgb(0, 180, 0);
                color: rgb(0, 255, 0);
                border-bottom:0px solid rgb(5, 5, 5);
                border-right:0px solid rgb(5, 5, 5);
                border-top:0px solid rgb(5, 5, 5);
                border-left:0px solid rgb(5, 5, 5);}

                QComboBox {background-color: rgb(0, 0, 0);
                selection-color: black;
                selection-background-color: rgb(255, 0, 0);
                color: rgb(0, 255, 0);
                border-bottom:0px solid rgb(5, 5, 5);
                border-right:0px solid rgb(5, 5, 5);
                border-top:0px solid rgb(5, 5, 5);
                border-left:0px solid rgb(5, 5, 5);}

                """
        self.setStyleSheet(self_style)
        self.update()
        print('-- updated style sheet')
        self.main_menu_bar.resize(self.menu_bar_size_x, self.menu_bar_size_y)
        print('-- updated main menu bar')

        global MODE_CAMERA, MODE_VIDEO, MODE_MANUAL_ANNOTATION, MODE_TRAINING
        if MODE_CAMERA is True:
            self.display_camera_mode()
        elif MODE_VIDEO is True:
            self.display_video_mode()
        elif MODE_MANUAL_ANNOTATION is True:
            self.display_annotation_mode()
        elif MODE_TRAINING is True:
            self.display_training_mode()

    @QtCore.pyqtSlot()
    def timer_gui_updates(self):
        global enable_target, btnx_double_var, target_exec_logs
        try:
            if MODE_CAMERA is True:

                # Cam status
                if self.thread_1.isRunning():
                    if ai_imageai_process_live_feed.CAMERA_WARNING:

                        # Main info label
                        lblx_var[17].resize((btnx_size * 14) + (btnx_sp_size * 13), int(btnx_size / 1))
                        lblx_var[17].move(lblx_var[16].pos().x(), lblx_var[16].pos().y())
                        lblx_var[17].setStyleSheet("""QLabel{
                            color: rgb(255,255,0);
                            background-color: rgba(0,0,0,230);
                            border-top:4px rgba(0,0,0,230);
                            border-bottom:4px rgba(0,0,0,230);
                            border-right:3px rgba(0,0,0,230);
                            border-left:3px rgba(0,0,0,230);
                            }""")
                        lblx_var[17].setAlignment(Qt.AlignCenter)
                        lblx_var[17].setText(ai_imageai_process_live_feed.CAMERA_WARNING)
                        lblx_var[17].show()

                        # Status
                        lblx_var[141].setStyleSheet("""QLabel{
                            background-color : rgb(255,255,0);
                            border: 26px solid rgb""" + str(object_color_background_0) + """;
                            }""")
                    else:
                        # Main info label
                        lblx_var[17].setText('')
                        lblx_var[17].hide()

                        # Status
                        lblx_var[141].setStyleSheet("""QLabel{
                            background-color : rgb(255,0,0);
                            border:26px solid rgb""" + str(object_color_border_0) + """;
                            }""")
                elif not self.thread_1.isRunning():

                    # Main info label
                    lblx_var[17].setText('')
                    lblx_var[17].hide()

                    # Status
                    lblx_var[141].setStyleSheet("""QLabel{
                        background-color : rgb(255,255,255);
                        border:26px solid rgb""" + str(object_color_border_0) + """;
                        }""")

                if enable_target is True:
                    btnx_double_var[10].setStyleSheet("""QPushButton{
                        color: rgb(255, 0, 0);
                        background-color: rgb""" + str(object_color_background_0) + """;
                        border-right:1px solid rgb(0, 0, 0);
                        border-bottom:1px solid rgb(0, 0, 0);
                        border-top:1px solid rgb(0, 0, 0);
                        border-left:1px solid rgb(0, 0, 0);
                         }""")
                elif enable_target is False:
                    btnx_double_var[10].setStyleSheet("""QPushButton{
                        color: rgb""" + str(object_color_0) + """;
                        background-color: rgb""" + str(object_color_background_0) + """;
                        border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
                        border-right:2px solid rgb""" + str(object_color_border_0) + """;
                        border-top:2px solid rgb""" + str(object_color_border_0) + """;
                        border-left:2px solid rgb""" + str(object_color_border_0) + """;}
                         }""")

                # target event execution status
                for TARGET in target_exec:
                    try:
                        if self.combo_box_exec.currentText().replace('Event: ', '').isdigit():
                            if int(self.combo_box_exec.currentText().replace('Event: ', '')) == TARGET.get('event'):

                                # turn target execution status red
                                if TARGET.get('proc') is False:
                                    self.target_exec_off()
                                    # btnx_double_var[74].hide()
                                    btnx_double_var[74].setStyleSheet("""QPushButton{
                                         color: rgb""" + str(object_color_0) + """;
                                         background-color: rgb""" + str(object_color_background_0) + """;
                                         border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-right:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-top:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-left:0px solid rgb""" + str(object_color_border_0) + """;}
                                         }""")
                                elif TARGET.get('proc').poll() is not None:
                                    self.target_exec_off()
                                    btnx_double_var[74].setStyleSheet("""QPushButton{
                                         color: rgb""" + str(object_color_0) + """;
                                         background-color: rgb""" + str(object_color_background_0) + """;
                                         border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-right:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-top:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-left:0px solid rgb""" + str(object_color_border_0) + """;}
                                         }""")

                                # turn target execution status green
                                elif TARGET.get('proc').poll() is None:
                                    self.target_exec_on()
                                    btnx_double_var[74].setStyleSheet("""QPushButton{
                                         color: rgb""" + str('(255, 0, 0)') + """;
                                         background-color: rgb""" + str(object_color_background_0) + """;
                                         border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-right:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-top:0px solid rgb""" + str(object_color_border_0) + """;
                                         border-left:0px solid rgb""" + str(object_color_border_0) + """;}
                                         }""")

                                # display log for current target event
                                p = tbx_var[88].verticalScrollBar().value()
                                if p == tbx_var[88].verticalScrollBar().maximum():
                                    tbx_var[88].setText('')
                                    for log in target_exec_logs[int(self.combo_box_exec.currentText().replace('Event: ', ''))]:
                                        tbx_var[88].append(log)

                    except:
                        pass
        except:
            pass

    @QtCore.pyqtSlot()
    def timer_5_start_function(self):
        self.timer_5.start()

    @QtCore.pyqtSlot()
    def timer_5_stop_function(self):
        self.timer_5.stop()

    @QtCore.pyqtSlot()
    def brush_white(self):
        self.brush_color_r, self.brush_color_g, self.brush_color_b,  = 255, 255, 255

    @QtCore.pyqtSlot()
    def brush_pink(self):
        self.brush_color_r, self.brush_color_g, self.brush_color_b = 255, 105, 180

    @QtCore.pyqtSlot()
    def brush_light_blue(self):
        self.brush_color_r, self.brush_color_g, self.brush_color_b = 163, 206, 255

    @QtCore.pyqtSlot()
    def brush_blue(self):
        self.brush_color_r, self.brush_color_g, self.brush_color_b = 0, 0, 255

    @QtCore.pyqtSlot()
    def brush_green(self):
        self.brush_color_r, self.brush_color_g, self.brush_color_b = 0, 255, 0

    @QtCore.pyqtSlot()
    def brush_yellow(self):
        self.brush_color_r, self.brush_color_g, self.brush_color_b = 255, 255, 0

    @QtCore.pyqtSlot()
    def brush_red(self):
        self.brush_color_r, self.brush_color_g, self.brush_color_b = 255, 0, 0

    @QtCore.pyqtSlot()
    def brush_black(self):
        self.brush_color_r, self.brush_color_g, self.brush_color_b = 0, 0, 0

    @QtCore.pyqtSlot()
    def adjust_alpha(self):
        try:
            print(f'self.slider_alpha.value(): {self.slider_alpha.value()}')
            btnx_var[142].setText(str(self.slider_alpha.value()))
            self.brush_color_a = self.slider_alpha.value()
        except:
            print(f'App.adjust_alpha: {e}')

    @QtCore.pyqtSlot()
    def timer_1_start_function(self):
        self.timer_1.start()

    @QtCore.pyqtSlot()
    def timer_1_stop_function(self):
        self.timer_1.stop()

    @QtCore.pyqtSlot()
    def target_exec_on(self):
        btnx_var[77].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(0,255,0);
            border-bottom:26px solid rgb""" + str(object_color_border_0) + """;
            border-right:26px solid rgb""" + str(object_color_border_0) + """;
            border-top:26px solid rgb""" + str(object_color_border_0) + """;
            border-left:26px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_var[77].setText('')

    @QtCore.pyqtSlot()
    def target_exec_off(self):
        global btnx_double_var
        btnx_var[77].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(170,170,170);
            border-bottom:26px solid rgb""" + str(object_color_border_0) + """;
            border-right:26px solid rgb""" + str(object_color_border_0) + """;
            border-top:26px solid rgb""" + str(object_color_border_0) + """;
            border-left:26px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_var[77].setText('')

    @QtCore.pyqtSlot()
    def timer_1_function(self):
        ######################
        #    CAMERA
        ######################
        global lblx_var, MODE_CAMERA, enable_target, target_exec, enable_target, target_exec_logs
        if enable_target is True:
            ai_imageai_process_live_feed.TARGETS = target_exec

            # get acquired targets
            ACQUIRED_TARGETS = ai_imageai_process_live_feed.ACQUIRED_TARGETS
            for ACQUIRED_TARGET in ACQUIRED_TARGETS:
                try:
                    # compare acquired targets to target list
                    for TARGET in target_exec:
                        if ACQUIRED_TARGET.get("name") == TARGET.get('name'):
                            if ACQUIRED_TARGET.get("detection_percentage_probability") >= TARGET.get("percentage_probability"):
                                if TARGET.get('enabled') is True:
                                    if TARGET.get('allow_exec') is True:

                                        # run once
                                        if TARGET.get('exec_mode') == 'run_once':
                                            print(f'-- executing program for target: {ACQUIRED_TARGET.get("name")} --> program: {TARGET.get("file")}')
                                            target_exec_logs[TARGET.get('event')].append(f'[{datetime.datetime.now()}] [{len(target_exec_logs[TARGET.get("event")])+1}]')

                                            p1 = subprocess.Popen(f'{TARGET.get("file")}', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                                            TARGET.update({'proc': p1})
                                            TARGET.update({'allow_exec': False})

                                        #  run every detection
                                        elif TARGET.get('exec_mode') == 'run_every':
                                            print(f'-- executing program for target: {ACQUIRED_TARGET.get("name")} --> program: {TARGET.get("file")}')
                                            target_exec_logs[TARGET.get('event')].append(f'[{datetime.datetime.now()}] [{len(target_exec_logs[TARGET.get("event")])+1}]')

                                            p1 = subprocess.Popen(f'{TARGET.get("file")}', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                                            TARGET.update({'proc': p1})

                                        # run every detection if not already running
                                        elif TARGET.get('exec_mode') == 'run_complete':
                                            if TARGET.get('proc') is False:
                                                print(f'-- executing program for target: {ACQUIRED_TARGET.get("name")} --> program: {TARGET.get("file")}')
                                                target_exec_logs[TARGET.get('event')].append(f'[{datetime.datetime.now()}] [{len(target_exec_logs[TARGET.get("event")])+1}]')

                                                p1 = subprocess.Popen(f'{TARGET.get("file")}', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                                                TARGET.update({'proc': p1})

                                            elif TARGET.get('proc').poll() is not None:
                                                print(f'-- executing program for target: {ACQUIRED_TARGET.get("name")} --> program: {TARGET.get("file")}')
                                                target_exec_logs[TARGET.get('event')].append(f'[{datetime.datetime.now()}] [{len(target_exec_logs[TARGET.get("event")])+1}]')

                                                p1 = subprocess.Popen(f'{TARGET.get("file")}', stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                                                TARGET.update({'proc': p1})
                                            else:
                                                print(f'-- target event already running: {TARGET}')
                except:
                    pass
                ACQUIRED_TARGETS.remove(ACQUIRED_TARGET)
        else:
            if ai_imageai_process_live_feed.TARGETS is not []:
                ai_imageai_process_live_feed.TARGETS = []
        try:
            if MODE_CAMERA is True:

                # Set stats todo -> set separate stats at module level for video & camera
                lblx_var[46].setText(f'P: {minimum_percentage_probability}')
                btnx_double_var[62].setText(f'AF: {Detection.I_ANNOTATION}')
                btnx_double_var[78].setText(f'IF: {Detection.I_IMAGES}')
                btnx_double_var[94].setText(f'DF: {Detection.I_DETECTED_IMAGES}')
                btnx_double_var[110].setText(f'OB: {len(ai_imageai_process_live_feed.OUTPUT_OBJECTS_ARRAY)}')
                btnx_double_var[126].setText(f'UOB: {len(ai_imageai_process_live_feed.UNIQUE_OBJECTS)}')
                lblx_var[142].setText(f'TE: {ai_imageai_process_live_feed.total_time_elapsed}')
                lblx_var[136].setText(f'{ai_imageai_process_live_feed.FRAME_NUM}/{ai_imageai_process_live_feed.FRAME_NUM}')
                lblx_var[139].setText(f'FPS: {"{:.2f}".format(ai_imageai_process_live_feed.fps)}')
                self.slider_frame_track.setMaximum(ai_imageai_process_live_feed.FRAME_NUM)
                self.slider_frame_track.setSliderPosition(ai_imageai_process_live_feed.FRAME_NUM)

                # Display camera frame
                frame = ai_imageai_process_live_feed.RETURNED_FRAME
                if isinstance(frame, numpy.ndarray):
                    qimage = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                    pixmap = QPixmap(qimage)
                    pixmap = pixmap.scaled(self.video_label_size_w, self.video_label_size_h, Qt.KeepAspectRatio)
                    lblx_var[self.video_label].setPixmap(pixmap)
        except:
            print(f'App.timer_1_function: {e}')

    def set_main_label_1(self):
        global lblx_var
        pixmap = QPixmap(self.splash_image)
        lblx_var[self.video_label].setPixmap(pixmap)
        lblx_var[self.video_label].setStyleSheet("""
            QLabel{
            color: rgb(200, 200, 200);
            background-color: rgb(0, 0, 0);
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
        """)
        lblx_var[self.video_label].show()

    @QtCore.pyqtSlot()
    def select_camera(self):
        global camera_input

        # set camera index
        camera_input = int(self.combo_box_camera.currentText().replace('Camera: ', ''))
        print(f'selected camera: {camera_input}')

        # stop the timer function while making changes to module arguments
        self.timer_1_stop_function()

        # break imageai.Detection loop
        Detection.KILL_LOOP = True

        # clear video label
        ai_imageai_process_live_feed.RETURNED_FRAME = ''
        self.set_main_label_1()

        try:
            ai_imageai_process_live_feed.CAMERA.release()
        except:
            pass

        # send out new camera index
        ai_imageai_process_live_feed.CAMERA_INPUT = camera_input

        # restart timer function
        self.timer_1_start_function()

    # select_training_directory, train_from_pre_trained_model
    @QtCore.pyqtSlot()
    def select_training_directory(self):
        global directory_input_training, training_objects_array
        _cwd = os.getcwd()
        dir_name = QFileDialog.getExistingDirectory(caption='Select dataset directory:', directory=_cwd)
        if dir_name:
            # display selected directory
            print(f'-- selecting input directory: {dir_name}')
            directory_input_training = dir_name

    @QtCore.pyqtSlot()
    def select_pre_trained_model_file(self):
        global model_path
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select pre-trained model:", "",
                                                  "All Files (*);;", options=options)
        if file_name:
            print(f'-- selecting model file: {file_name}')
            model_path = file_name

    @QtCore.pyqtSlot()
    def train_from_pre_trained_model(self):
        global _train_from_pretrained_model, theme_color
        if _train_from_pretrained_model is False:
            _train_from_pretrained_model = True
            btnx_double_var[46].setText('Pre-Trained (On)')
        else:
            _train_from_pretrained_model = False
            btnx_double_var[46].setText('Pre-Trained (Off)')
        print(f'_train_from_pretrained_model: {_train_from_pretrained_model}')

    @QtCore.pyqtSlot()
    def timer_2_start_function(self):
        self.timer_2.start()

    @QtCore.pyqtSlot()
    def timer_2_stop_function(self):
        self.timer_2.stop()

    @QtCore.pyqtSlot()
    def timer_2_function(self):
        global tbx_message_0
        if tbx_message_0:
            print(tbx_message_0[0])
            del tbx_message_0[0]

    @QtCore.pyqtSlot()
    def timer_3_start_function(self):
        self.timer_3.start()

    @QtCore.pyqtSlot()
    def timer_3_stop_function(self):
        self.timer_3.stop()

    @QtCore.pyqtSlot()
    def timer_3_function(self):
        global tbx_message_0, bounding_box, bounding_box2
        try:
            tbx_var[8].setText(f'0: x1:{str(bounding_box[0])} y1:{str(bounding_box[1])} x2:{str(bounding_box[2])} y2:{str(bounding_box[3])}')
            tbx_var[8].append(f'1: x1:{str(bounding_box2[0])} y1:{str(bounding_box2[1])} x2:{str(bounding_box2[2])} y2:{str(bounding_box2[3])}')
        except:
            pass

    @QtCore.pyqtSlot()
    def start_training(self):
        global btnx_double_var
        if self.thread_2.isRunning():
            self.thread_2.stop_thread()
            btnx_double_var[126].setText('Start')
        elif not self.thread_2.isRunning():
            btnx_double_var[126].setText('Stop')
            self.thread_2.start()

    @QtCore.pyqtSlot()
    def mode_select_camera(self):
        global lblx_var
        global MODE_CAMERA, MODE_VIDEO, MODE_MANUAL_ANNOTATION, MODE_TRAINING
        MODE_CAMERA = True
        MODE_VIDEO = False
        MODE_MANUAL_ANNOTATION = False
        MODE_TRAINING = False
        self.display_camera_mode()

    @QtCore.pyqtSlot()
    def mode_select_video(self):
        global lblx_var
        global MODE_CAMERA, MODE_VIDEO, MODE_MANUAL_ANNOTATION, MODE_TRAINING
        MODE_CAMERA = False
        MODE_VIDEO = True
        MODE_MANUAL_ANNOTATION = False
        MODE_TRAINING = False
        self.display_video_mode()

    @QtCore.pyqtSlot()
    def mode_manual_annotation(self):
        global lblx_var, qlex_double_var
        global MODE_CAMERA, MODE_VIDEO, MODE_MANUAL_ANNOTATION, MODE_TRAINING
        MODE_CAMERA = False
        MODE_VIDEO = False
        MODE_MANUAL_ANNOTATION = True
        MODE_TRAINING = False
        self.timer_3_stop_function()
        self.timer_3_start_function()
        self.display_annotation_mode()

    @QtCore.pyqtSlot()
    def mode_training(self):
        global MODE_CAMERA, MODE_VIDEO, MODE_MANUAL_ANNOTATION, MODE_TRAINING
        MODE_CAMERA = False
        MODE_VIDEO = False
        MODE_MANUAL_ANNOTATION = False
        MODE_TRAINING = True
        self.display_training_mode()

    @QtCore.pyqtSlot()
    def timer_0_start_function(self):
        self.timer_0.start()

    @QtCore.pyqtSlot()
    def timer_0_stop_function(self):
        self.timer_0.stop()

    @QtCore.pyqtSlot()
    def timer_0_function(self):
        ######################
        #    VIDEO FILE
        ######################
        global lblx_var, MODE_VIDEO

        if MODE_VIDEO is True:
            # Detect video closed by imageai.Detection
            allow_continue = True
            if Detection.VIDEO_CLOSED is True:
                # Stop reading data, clear displayed frame and values
                self.stop_video()
                allow_continue = False
            if allow_continue is True:
                try:
                    # Set stats
                    lblx_var[46].setText(f'P: {minimum_percentage_probability}')
                    btnx_double_var[62].setText(f'AF: {Detection.I_ANNOTATION}')
                    btnx_double_var[78].setText(f'IF: {Detection.I_IMAGES}')
                    btnx_double_var[94].setText(f'DF: {Detection.I_DETECTED_IMAGES}')
                    btnx_double_var[110].setText(f'OB: {len(ai_imageai_process_video.OUTPUT_OBJECTS_ARRAY)}')
                    btnx_double_var[126].setText(f'UOB: {len(ai_imageai_process_video.UNIQUE_OBJECTS)}')
                    lblx_var[136].setText(f'{ai_imageai_process_video.FRAME_NUM}/{ai_imageai_process_video.TOTAL_FRAMES}')
                    lblx_var[138].setText(f'FPS: {"{:.2f}".format(ai_imageai_process_video.fps)}')
                    lblx_var[140].setText(f'ETA: {self.GetTimeFromSeconds(_sec=ai_imageai_process_video.t_frame_elapsed * (ai_imageai_process_video.TOTAL_FRAMES - ai_imageai_process_video.FRAME_NUM))}')
                    lblx_var[142].setText(f'TE: {ai_imageai_process_video.total_time_elapsed}')
                    self.slider_frame_track.setMaximum(ai_imageai_process_video.TOTAL_FRAMES)
                    self.slider_frame_track.setSliderPosition(ai_imageai_process_video.FRAME_NUM)

                    # Display video frame
                    frame = ai_imageai_process_video.RETURNED_FRAME
                    if isinstance(frame, numpy.ndarray):
                        qimage = QImage(frame, frame.shape[1], frame.shape[0], QImage.Format_RGB888)
                        pixmap = QPixmap(qimage)
                        pixmap = pixmap.scaled(self.video_label_size_w, self.video_label_size_h, Qt.KeepAspectRatio)
                        lblx_var[self.video_label].setPixmap(pixmap)
                except:
                    print(f'App.timer_0_function: {e}')

    @QtCore.pyqtSlot()
    def frame_track(self):
        try:
            print(f'self.slider_frame_track.value(): {self.slider_frame_track.value()}')
            ai_imageai_process_video.FRAME_NUM = self.slider_frame_track.value()
            Detection.video_frames_count = ai_imageai_process_video.FRAME_NUM
        except:
            print(f'App.frame_track: {e}')

    @QtCore.pyqtSlot()
    def frame_camera_track(self):
        try:
            print(f'self.slider_frame_track.value(): {self.slider_frame_track.value()}')
            # todo track to camera frame
        except:
            print(f'App.frame_camera_track: {e}')

    @QtCore.pyqtSlot()
    def adjust_minimum_percentage_probability(self):
        global minimum_percentage_probability, lblx_var
        try:
            print(f'self.slider_minimum_percentage_probability.value(): {self.slider_minimum_percentage_probability.value()}')
            minimum_percentage_probability = self.slider_minimum_percentage_probability.value()
            Detection.MINIMUM_PERCENTAGE_PROBABILITY = minimum_percentage_probability
            lblx_var[46].setText(f'P: {minimum_percentage_probability}')
        except:
            print(f'App.adjust_minimum_percentage_probability: {e}')

    @QtCore.pyqtSlot()
    def adjust_minimum_percentage_probability_custom(self):
        global minimum_percentage_probability, lblx_var
        try:
            print(f'self.adjust_minimum_percentage_probability_custom.value(): {self.slider_minimum_percentage_probability.value()}')
            minimum_percentage_probability = self.slider_minimum_percentage_probability.value()
            Custom.MINIMUM_PERCENTAGE_PROBABILITY = minimum_percentage_probability
            lblx_var[46].setText(f'P: {minimum_percentage_probability}')
        except:
            print(f'App.adjust_minimum_percentage_probability_custom: {e}')

    @QtCore.pyqtSlot()
    def adjust_frame_detection_interval(self):
        global frame_detection_interval, lblx_var
        try:
            print(f'self.slider_frame_detection_interval.value(): {self.slider_frame_detection_interval.value()}')
            frame_detection_interval = self.slider_frame_detection_interval.value()
            Detection.FRAME_DETECTION_INTERVAL = frame_detection_interval
            lblx_var[30].setText(f'FD: {frame_detection_interval}')
        except:
            print(f'App.adjust_frame_detection_interval: {e}')

    @QtCore.pyqtSlot()
    def adjust_target_minimum_percentage_probability(self):
        global frame_detection_interval, lblx_var, target_exec
        try:
            print(f'self.slider_target_minimum_percentage_probability.value(): {self.slider_target_minimum_percentage_probability.value()}')
            target_minimum_percentage_probability = self.slider_target_minimum_percentage_probability.value()
            i_exec = int(self.combo_box_exec.currentText().replace('Event: ', ''))
            print(f'i_exec: {i_exec}')
            print(f'changing target_minimum_percentage_probability: {target_exec[int(i_exec)]}')
            target_exec[int(i_exec)].update({'percentage_probability': target_minimum_percentage_probability})
            print(f'new dictionary: {target_exec[int(i_exec)]}')
            lblx_var[40].setText(f'Target Minimum Probability: {str(target_exec[int(i_exec)].get("percentage_probability"))}')
        except:
            print(f'App.adjust_target_minimum_percentage_probability: {e}')

    @QtCore.pyqtSlot()
    def pause_frame(self):
        global btnx_double_var

        if not self.thread_0.isRunning():

            # If calling Detection AND using these values then ensure these values are reset to zero each call
            Detection.I_ANNOTATION = 0
            Detection.I_IMAGES = 0
            Detection.I_DETECTED_IMAGES = 0
            Detection.VIDEO_CLOSED = None

            # Start detection thread
            self.timer_0_start_function()
            self.thread_0.start()
            btnx_double_var[128].setText('Pause')
        else:
            # Pause
            if Detection.PAUSE_FRAME is False:
                Detection.PAUSE_FRAME = True
                btnx_double_var[128].setText('Start')
            # Continue
            else:
                Detection.PAUSE_FRAME = False
                btnx_double_var[128].setText('Pause')
            # Display modified module level value
            print(f'Detection.PAUSE_FRAME: {Detection.PAUSE_FRAME}')

    @QtCore.pyqtSlot()
    def start_live(self):
        global lblx_var, btnx_double_var

        if not self.thread_1.isRunning():

            # If calling Detection AND using these values then ensure these values are reset to zero each call
            Detection.I_ANNOTATION = 0
            Detection.I_IMAGES = 0
            Detection.I_DETECTED_IMAGES = 0

            ai_imageai_process_live_feed.RETURNED_FRAME = ""

            # Start detection thread
            self.timer_1_start_function()
            self.thread_1.start()
            btnx_double_var[128].setText('Pause')
        else:
            # Pause
            if Detection.PAUSE_FRAME is False:
                Detection.PAUSE_FRAME = True
                btnx_double_var[128].setText('Start')
            # Continue
            else:
                Detection.PAUSE_FRAME = False
                btnx_double_var[128].setText('Pause')
            print(f'Detection.PAUSE_FRAME: {Detection.PAUSE_FRAME}')

    @QtCore.pyqtSlot()
    def timer_4_function(self):
        print(f'self.thread_1.isRunning(): {self.thread_1.isRunning()}')
        if self.thread_1.isRunning() is True:
            if ai_imageai_process_live_feed.COMPLETED is True:
                print('-- terminating thread from timer')
                self.thread_1.stop_thread()
                print('-- terminating timer')
                self.timer_4_stop_function()
        else:
            print('-- terminating timer')
            self.timer_4_stop_function()

    @QtCore.pyqtSlot()
    def timer_4_start_function(self):
        self.timer_4.start()

    @QtCore.pyqtSlot()
    def timer_4_stop_function(self):
        self.timer_4.stop()

    @QtCore.pyqtSlot()
    def stop_live(self):
        global lblx_var, btnx_double_var

        self.timer_1_stop_function()

        self.timer_4_stop_function()
        self.timer_4_start_function()

        # initiate shutdown events before terminating
        Detection.KILL_LOOP = True
        ai_imageai_process_live_feed.KILL_LOOP = True

        self.set_main_label_1()

        try:
            # Ensure these values are reset each call
            ai_imageai_process_live_feed.resized = False
            ai_imageai_process_live_feed.T_START_PERF = 0
            ai_imageai_process_live_feed.T_START_DATETIME = 0
            ai_imageai_process_live_feed.DUMP = False
            ai_imageai_process_live_feed.PRIMARY_TARGET = None
            ai_imageai_process_live_feed.SECONDARY_TARGET = None
            ai_imageai_process_live_feed.RETURNED_FRAME = ""
            ai_imageai_process_live_feed.t_frame = time.perf_counter()
            ai_imageai_process_live_feed.FRAME_NUM = 0
            ai_imageai_process_live_feed.fps = 0
            ai_imageai_process_live_feed.total_time_elapsed = 0
            ai_imageai_process_live_feed.OUTPUT_OBJECTS_ARRAY_TOTAL = 0
            ai_imageai_process_live_feed.CAMERA_WARNING = ''

            try:
                ai_imageai_process_live_feed.CAMERA.release()
            except:
                pass

            # If calling Detection AND using these values then ensure these values are reset to zero each call
            Detection.I_ANNOTATION = 0
            Detection.I_IMAGES = 0
            Detection.I_DETECTED_IMAGES = 0

            # Clear stats
            self.slider_frame_track.setSliderPosition(0)
            btnx_double_var[62].setText('AF: 0')
            btnx_double_var[78].setText('IF: 0')
            btnx_double_var[94].setText('DF: 0')
            btnx_double_var[110].setText('OB: 0')
            btnx_double_var[126].setText('UOB: 0')
            lblx_var[142].setText('TE: 0')
            lblx_var[136].setText('0/0')
            lblx_var[139].setText('FPS: 0')
            btnx_double_var[128].setText('Start')

            # Main info label
            lblx_var[17].setText('')
            lblx_var[17].hide()
        except:
            pass

    @QtCore.pyqtSlot()
    def select_video_file(self):
        global input_files_videos
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select video:", "", "All Files (*);;", options=options)
        if file_name:
            print(f'-- selecting input file: {file_name}')
            input_files_videos = [file_name]

    @QtCore.pyqtSlot()
    def stop_video(self):
        global lblx_var, btnx_double_var

        if self.thread_0.isRunning():
            self.thread_0.stop_thread()
            self.timer_0_stop_function()

        self.set_main_label_1()

        self.slider_frame_track.setSliderPosition(0)

        # Clear stats
        btnx_double_var[62].setText('AF: 0')
        btnx_double_var[78].setText('IF: 0')
        btnx_double_var[94].setText('DF: 0')
        btnx_double_var[110].setText('OB: 0')
        btnx_double_var[126].setText('UOB: 0')
        lblx_var[140].setText('ETA: 0')
        lblx_var[142].setText('TE: 0')
        lblx_var[136].setText('0/0')
        lblx_var[138].setText('FPS: 0')
        btnx_double_var[128].setText('Start')

        # If calling Detection AND using these values then ensure these values are reset to zero each call
        Detection.I_ANNOTATION = 0
        Detection.I_IMAGES = 0
        Detection.I_DETECTED_IMAGES = 0

    @QtCore.pyqtSlot()
    def previous_manual_annotation(self):
        global input_files_images, index_input_files_images, annotations
        annotations = []
        if input_files_images:
            if index_input_files_images > 0:
                index_input_files_images -= 1
            else:
                index_input_files_images = len(input_files_images)-1
            print(f'index_input_files_images: {index_input_files_images}')
            self.iter_input_file()

    @QtCore.pyqtSlot()
    def next_manual_annotation(self):
        global input_files_images, index_input_files_images, annotations
        annotations = []
        if input_files_images:
            if index_input_files_images < len(input_files_images)-1:
                index_input_files_images += 1
            else:
                index_input_files_images = 0
            print(f'index_input_files_images: {index_input_files_images}')
            self.iter_input_file()

    @QtCore.pyqtSlot()
    def read_annotation_file(self):
        global annotations, bounding_box, bounding_box2
        object_names = []
        object_xmin = []
        object_ymin = []
        object_xmax = []
        object_ymax = []
        image_width = int()
        image_height = int()
        with open(input_files_annotations[index_input_files_images], 'r') as fo:
            for line in fo:
                line = line.strip()
                if '<width>' in line:
                    image_width = int(line.replace('<width>', '').replace('</width>', ''))
                if '<height>' in line:
                    image_height = int(line.replace('<height>', '').replace('</height>', ''))
                elif '<name>' in line:
                    object_names.append(line.replace('<name>', '').replace('</name>', ''))
                elif '<xmin>' in line:
                    object_xmin.append(int(line.replace('<xmin>', '').replace('</xmin>', '')))
                elif '<ymin>' in line:
                    object_ymin.append(int(line.replace('<ymin>', '').replace('</ymin>', '')))
                elif '<xmax>' in line:
                    object_xmax.append(int(line.replace('<xmax>', '').replace('</xmax>', '')))
                elif '<ymax>' in line:
                    object_ymax.append(int(line.replace('<ymax>', '').replace('</ymax>', '')))
        # onscreen_geo = []
        annotations = []
        i_anno = 0
        for object_name in object_names:
            # translation layer: translate image file geometry to image onscreen geometry
            if image_width > self.video_label_size_w:
                new_ratio = image_width / self.video_label_size_w
                new_xmin = object_xmin[i_anno] / new_ratio
                new_xmax = object_xmax[i_anno] / new_ratio
            else:
                new_xmin = object_xmin[i_anno]
                new_xmax = object_xmax[i_anno]
            if image_height > self.video_label_size_h:
                new_ratio = image_height / self.video_label_size_h
                new_ymin = object_ymin[i_anno] / new_ratio
                new_ymax = object_ymax[i_anno] / new_ratio
            else:
                new_ymin = object_ymin[i_anno]
                new_ymax = object_ymax[i_anno]
            # adjust xmax/ymax if greater than image width/height (another solution is to modify imageai/keras/tf)
            if new_xmax >= self.video_label_size_w:
                new_xmax = self.video_label_size_w-1
            if new_ymax >= self.video_label_size_h:
                new_ymax = self.video_label_size_h-1

            bounding_box = [round(new_xmin), round(new_ymin), round(new_xmax), round(new_ymax)]
            bounding_box2 = [object_xmin[i_anno], object_ymin[i_anno], object_xmax[i_anno], object_ymax[i_anno]]
            qlex_double_var[130].setText(object_names[i_anno])
            annotations.append({'name': object_names[i_anno],
                                'xmin': object_xmin[i_anno],
                                'ymin': object_ymin[i_anno],
                                'xmax': object_xmax[i_anno],
                                'ymax': object_ymax[i_anno],
                                'onscreen_geo': bounding_box,
                                'brush_r': 0,
                                'brush_g': 0,
                                'brush_b': 0,
                                'brush_a': 0
                                })
            i_anno += 1
        for annotation in annotations:
            print(f'annotation: {annotation}')

    @QtCore.pyqtSlot()
    def manual_annotation_previous_object(self):
        global index_annotation_object, annotations, bounding_box, bounding_box2, auto_iter_object

        if index_annotation_object > 0:
            index_annotation_object -= 1
        else:
            index_annotation_object = len(annotations) - 1

        i_anno = 0
        for annotation in annotations:
            if i_anno != index_annotation_object:
                annotation['brush_r'] = 0
                annotation['brush_g'] = 0
                annotation['brush_b'] = 0
                annotation['brush_a'] = 0
            elif i_anno == index_annotation_object:
                annotation['brush_r'] = 72
                annotation['brush_g'] = 0
                annotation['brush_b'] = 255
                annotation['brush_a'] = 0
                qlex_double_var[130].setText(annotation['name'])
                bounding_box = [annotation['onscreen_geo'][0], annotation['onscreen_geo'][1], annotation['onscreen_geo'][2], annotation['onscreen_geo'][3]]
                bounding_box2 = [annotation['xmin'], annotation['ymin'], annotation['xmax'], annotation['ymax']]
                auto_iter_object = True
            i_anno += 1
            self.update()

    @QtCore.pyqtSlot()
    def manual_annotation_next_object(self):
        global index_annotation_object, annotations, bounding_box, bounding_box2, auto_iter_object
        if index_annotation_object < len(annotations) - 1:
            index_annotation_object += 1
        else:
            index_annotation_object = 0

        i_anno = 0
        for annotation in annotations:
            if i_anno != index_annotation_object:
                annotation['brush_r'] = 0
                annotation['brush_g'] = 0
                annotation['brush_b'] = 0
                annotation['brush_a'] = 0
            elif i_anno == index_annotation_object:
                annotation['brush_r'] = 72
                annotation['brush_g'] = 0
                annotation['brush_b'] = 0
                annotation['brush_a'] = 0
                qlex_double_var[130].setText(annotation['name'])
                bounding_box = [annotation['onscreen_geo'][0], annotation['onscreen_geo'][1], annotation['onscreen_geo'][2], annotation['onscreen_geo'][3]]
                bounding_box2 = [annotation['xmin'], annotation['ymin'], annotation['xmax'], annotation['ymax']]
                auto_iter_object = True
            i_anno += 1
            self.update()

    @QtCore.pyqtSlot()
    def iter_input_file(self):
        global lblx_var, qlex_double_var
        global MODE_MANUAL_ANNOTATION
        global input_files_images, index_input_files_images
        global input_files_annotations
        global annotations
        if input_files_images[index_input_files_images].endswith(tuple(['.jpg', '.png'])):

            # self.set_main_label_1()
            lblx_var[self.video_label].hide()

            # display image path and corresponding annotation path
            print(f'loading image:      {input_files_images[index_input_files_images]}')
            if input_files_annotations:
                print(f'loading annotation: {input_files_annotations[index_input_files_images]}')
                self.read_annotation_file()

            # set image pixmap
            self.qimage = input_files_images[index_input_files_images]
            self.pil_img = Image.open(self.qimage)
            self.pixmap = QPixmap(self.qimage)

            # display image geometry (file)
            print('original image width, original image height:', self.pil_img.width, self.pil_img.height)
            print('available width, available height:', self.video_label_size_w, self.video_label_size_h)

            # display image geometry (app)
            self.image_size_w = self.video_label_size_w
            self.image_size_h = self.video_label_size_h
            print(f'new image geometry: {self.image_size_w} {self.image_size_h}')

            # display progress
            lblx_var[136].setText(f'{index_input_files_images+1}/{len(input_files_images)}')

            self.update()
        else:
            print('Invalid input file.')
            self.set_main_label_1()

    @QtCore.pyqtSlot()
    def new_manual_annotation(self):
        global annotations
        global bounding_box, bounding_box2, auto_iter_object
        print('_' * 50)
        obj_name = qlex_double_var[130].text()
        print(f'obj_name: {obj_name}')
        print(f'bounding_box: {bounding_box}')
        print(f'bounding_box2: {bounding_box2}')
        if self.area_in_label() is True or auto_iter_object is True:
            new_dict = {'name': obj_name,
                        'xmin': bounding_box2[0],
                        'ymin': bounding_box2[1],
                        'xmax': bounding_box2[2],
                        'ymax': bounding_box2[3],
                        'onscreen_geo': bounding_box,
                        'brush_r': self.brush_color_r,
                        'brush_g': self.brush_color_g,
                        'brush_b': self.brush_color_b,
                        'brush_a': self.brush_color_a}

            edit_existing = False
            i_anno = 0
            for annotation in annotations:
                if annotation['xmin'] == new_dict['xmin'] and annotation['ymin'] == new_dict['ymin'] and annotation['xmax'] == new_dict['xmax'] and annotation['ymax'] == new_dict['ymax']:
                    print(f'Found existing object: {annotation}')
                    edit_existing = True
                    break
                i_anno += 1
            if edit_existing is False:
                print('Adding new annotation dictionary to list.')
                annotations.append(new_dict)
            elif edit_existing is True:
                print(f'Editing existing object in annotations: {annotations[i_anno]}')
                annotations[i_anno]['name'] = new_dict['name']

            print('_'*50)

    @QtCore.pyqtSlot()
    def remove_current_manual_annotation(self):
        global annotations, index_annotation_object
        if annotations:
            print(f'Removing annotation: {annotations[index_annotation_object]}')
            annotations.remove(annotations[index_annotation_object])
        else:
            print('No annotations to remove.')

    @QtCore.pyqtSlot()
    def save_manual_annotation(self):
        global bounding_box2, annotations, input_files_images, index_input_files_images

        if annotations:
            # Annotation file heads
            print(f'file_input: {input_files_images[index_input_files_images]}')
            print(f'output_directory_path: {output_directory_path}')
            input_files_images[index_input_files_images] = input_files_images[index_input_files_images].replace('\\', '/')
            idx_filename = input_files_images[index_input_files_images].rfind('/')
            annotation_file = output_directory_path + input_files_images[index_input_files_images][idx_filename:].replace(pathlib.Path(input_files_images[index_input_files_images]).suffix, '.xml')
            print(f'annotation_file: {annotation_file}')
            print(f'output_image_path: {input_files_images[index_input_files_images]}')
            width, height = self.pil_img.width, self.pil_img.height
            print(f'width, height: {width, height}')
            annotator_video.annotation_tag_open(output_xml_path=annotation_file,
                                                output_directory_path=output_directory_path,
                                                image_filename=input_files_images[index_input_files_images][idx_filename+1:],
                                                output_image_path=input_files_images[index_input_files_images],
                                                image_h=height, image_w=width, _make_dirs=False)
            # Annotation file objects
            for annotation in annotations:
                box_points = [annotation.get("xmin"),
                              annotation.get("ymin"),
                              annotation.get("xmax"),
                              annotation.get("ymax")]
                annotator_video.annotate(output_directory=output_directory_path,
                                         name=annotation.get("name"), _verbose=True,
                                         output_xml_path=annotation_file,
                                         box_points=box_points, _make_dirs=False)
            # Annotation file tails
            annotator_video.annotation_tag_close(annotation_file)
        else:
            print('There are no annotations yet.')

    @QtCore.pyqtSlot()
    def enable_targets(self):
        global enable_target, theme_color
        if enable_target is False:
            btnx_double_var[10].setStyleSheet("""QPushButton{
                color: rgb(255, 0, 0);
                background-color: rgb""" + str(object_color_background_0) + """;
                border-right:1px solid rgb(0, 0, 0);
                border-bottom:1px solid rgb(0, 0, 0);
                border-top:1px solid rgb(0, 0, 0);
                border-left:1px solid rgb(0, 0, 0);
                 }""")
            enable_target = True
        elif enable_target is True:
            btnx_double_var[10].setStyleSheet("""QPushButton{
                color: rgb""" + str(object_color_0) + """;
                background-color: rgb""" + str(object_color_background_0) + """;
                border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
                border-right:2px solid rgb""" + str(object_color_border_0) + """;
                border-top:2px solid rgb""" + str(object_color_border_0) + """;
                border-left:2px solid rgb""" + str(object_color_border_0) + """;}
                 }""")
            enable_target = False
        print(f'enable_target: {enable_target}')

    @QtCore.pyqtSlot()
    def set_name(self):
        global target_exec

        i_exec = int(self.combo_box_exec.currentText().replace('Event: ', ''))
        print(f'-- setting target event object name for: {target_exec[int(i_exec)]}')

        if qlex_var[24].text().strip() != '':
            if qlex_var[24].text().strip() != 'Object Name: ':
                if qlex_var[24].text().strip() != 'Object Name:':

                    # update dictionary
                    target_exec[int(i_exec)].update({'name': qlex_var[24].text().strip().replace('Object Name: ', '')})
                    target_exec[int(i_exec)].update({'enabled': False})
                    target_exec[int(i_exec)].update({'exec_mode': 'run_once'})
                    target_exec[int(i_exec)].update({'allow_exec': True})

                    # set switches
                    qlex_var[24].setText(f'Object Name: {target_exec[int(i_exec)].get("name")}')
                    btnx_double_var[72].setText('Run Once')
                    btnx_double_var[124].setText('DISABLED')

                    print(f'new dictionary: {target_exec[int(i_exec)]}')
                else:
                    print('-- no name entered')
                    qlex_var[24].setText(f'Object Name: {target_exec[int(i_exec)].get("name")}')
                    btnx_double_var[72].setText('Run Once')
                    btnx_double_var[124].setText('DISABLED')
        else:
            print('-- no name entered')
            qlex_var[24].setText(f'Object Name: {target_exec[int(i_exec)].get("name")}')
            btnx_double_var[72].setText('Run Once')
            btnx_double_var[124].setText('DISABLED')

    @QtCore.pyqtSlot()
    def set_exec(self):
        global target_exec

        i_exec = int(self.combo_box_exec.currentText().replace('Event: ', ''))
        print(f'-- setting exec code for target event: {target_exec[int(i_exec)]}')

        # specify file
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select python code file:", "",
                                                  "All Files (*);;", options=options)
        if file_name:
            print(f'-- selecting python code file: {file_name}')

            # update dictionary
            target_exec[int(i_exec)].update({'file': file_name})
            target_exec[int(i_exec)].update({'enabled': False})
            target_exec[int(i_exec)].update({'exec_mode': 'run_once'})
            target_exec[int(i_exec)].update({'allow_exec': True})

            # set switches
            lblx_var[56].setText(f'File: {os.path.basename(target_exec[int(i_exec)].get("file"))}')
            btnx_double_var[72].setText('Run Once')
            btnx_double_var[124].setText('DISABLED')

            print(f'new dictionary: {target_exec[int(i_exec)]}')

    @QtCore.pyqtSlot()
    def rem_exec(self):
        global target_exec

        i_exec = int(self.combo_box_exec.currentText().replace('Event: ', ''))
        print(f'-- setting default target event: {target_exec[int(i_exec)]}')

        # set default dictionary
        target_exec[int(i_exec)].update({'event': int(i_exec), 'name': '', 'percentage_probability': 50, 'program': '', 'file': '', 'exec_mode': 'run_once', 'enabled': False, 'allow_exec': True, 'proc': False, 'detection_percentage_probability': 0})

        # set switches default
        qlex_var[24].setText(f'Object Name: ')
        self.slider_target_minimum_percentage_probability.setSliderPosition(50)
        lblx_var[56].setText(f'File: ')
        btnx_double_var[72].setText('Run Once')
        btnx_double_var[124].setText('DISABLED')

        print(f'-- updated target event: {target_exec[int(i_exec)]}')

    @QtCore.pyqtSlot()
    def add_remove_exec(self):
        i_exec = self.combo_box_exec.currentText().replace('Event: ', '')
        if i_exec.isdigit():
            lblx_var[18].show()
            lblx_var[24].show()
            lblx_var[56].setText(f'File: {os.path.basename(target_exec[int(i_exec)].get("file"))}')
            lblx_var[56].show()
            qlex_var[24].setText(f'Object Name: {target_exec[int(i_exec)].get("name")}')
            qlex_var[24].show()
            lblx_var[40].setText('Target Minimum Probability: ' + str(target_exec[int(i_exec)].get("percentage_probability")))
            lblx_var[40].show()
            self.slider_target_minimum_percentage_probability.setSliderPosition(target_exec[int(i_exec)].get("percentage_probability"))
            self.slider_target_minimum_percentage_probability.show()
            if target_exec[int(i_exec)].get('exec_mode') == 'run_every':
                btnx_double_var[72].setText('Run Every')
            elif target_exec[int(i_exec)].get('exec_mode') == 'run_complete':
                btnx_double_var[72].setText('Run Complete')
            elif target_exec[int(i_exec)].get('exec_mode') == 'run_once':
                btnx_double_var[72].setText('Run Once')
            btnx_var[77].show()
            btnx_double_var[72].show()
            tbx_var[88].show()
            btnx_var[29].show()
            btnx_double_var[74].show()
            btnx_var[61].show()
            btnx_double_var[120].show()
            if target_exec[int(i_exec)].get("enabled") is False:
                btnx_double_var[124].setText('DISABLED')
            elif target_exec[int(i_exec)].get("enabled") is True:
                btnx_double_var[124].setText('ENABLED')
            btnx_double_var[124].show()
        else:
            lblx_var[18].hide()
            lblx_var[24].hide()
            lblx_var[56].setText(f'File:')
            lblx_var[56].hide()
            qlex_var[24].setText(f'Object Name:')
            qlex_var[24].hide()
            btnx_var[77].hide()
            btnx_double_var[72].hide()
            tbx_var[88].hide()
            btnx_var[29].hide()
            lblx_var[40].hide()
            self.slider_target_minimum_percentage_probability.hide()
            btnx_double_var[74].hide()
            btnx_var[61].hide()
            btnx_double_var[120].hide()
            btnx_double_var[124].hide()
            self.combo_box_exec.setCurrentIndex(0)

    @QtCore.pyqtSlot()
    def enable_exec(self):
        global target_exec
        i_exec = self.combo_box_exec.currentText().replace('Event: ', '')
        if i_exec.isdigit():
            if target_exec[int(i_exec)].get("enabled") is False:
                target_exec[int(i_exec)].update({'enabled': True})
                btnx_double_var[124].setText('ENABLED')
            elif target_exec[int(i_exec)].get("enabled") is True:
                target_exec[int(i_exec)].update({'enabled': False})
                btnx_double_var[124].setText('DISABLED')

    @QtCore.pyqtSlot()
    def mode_exec(self):
        i_exec = self.combo_box_exec.currentText().replace('Event: ', '')
        current_mode = target_exec[int(i_exec)].get("exec_mode")
        print(f'-- modifying execution mode: {target_exec[int(i_exec)]}')
        if current_mode == 'run_once':
            target_exec[int(i_exec)].update({'exec_mode': 'run_every'})
            btnx_double_var[72].setText('Run Every')
        elif current_mode == 'run_every':
            target_exec[int(i_exec)].update({'exec_mode': 'run_complete'})
            btnx_double_var[72].setText('Run Complete')
        elif current_mode == 'run_complete':
            target_exec[int(i_exec)].update({'exec_mode': 'run_once'})
            btnx_double_var[72].setText('Run Once')

        # update dictionary
        target_exec[int(i_exec)].update({'enabled': False})
        target_exec[int(i_exec)].update({'allow_exec': True})

        # set switches
        lblx_var[56].setText(f'File: {os.path.basename(target_exec[int(i_exec)].get("file"))}')
        btnx_double_var[124].setText('DISABLED')

        print(f'new dictionary: {target_exec[int(i_exec)]}')

    @QtCore.pyqtSlot()
    def terminate_exec(self):
        global target_exec
        i_exec = self.combo_box_exec.currentText().replace('Event: ', '')
        try:
            if target_exec[int(i_exec)].get('proc').poll() is None:
                print(f'-- target event process {target_exec[int(i_exec)].get("event")} is running: attempting termination')
                target_exec[int(i_exec)].get('proc').terminate()
            else:
                print(f'-- target event process {target_exec[int(i_exec)].get("event")} is already not running.')
        except:
            pass

    @QtCore.pyqtSlot()
    def display_camera_mode(self):
        global lblx_var, btnx_double_var, qlex_double_var, theme_color

        self.stop_video()

        # Hide other tabs
        self.hide_video_mode()
        self.hide_annotation_mode()
        self.hide_training_mode()

        # Main label
        self.set_main_label_1()

        # Fill main tab empty space
        btnx_double_var[8].setText('')
        btnx_double_var[8].resize((btnx_size * 2) + btnx_sp_size, btnx_size)
        btnx_double_var[8].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[8].show()

        # Emphasize current tab
        btnx_double_var[0].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:2px solid rgb""" + str(theme_color) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;
            }
            QPushButton::hover {background-color : rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:1px solid rgb""" + str(theme_color) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;
            }
            """)

        # Targets
        btnx_double_var[10].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[10].setText('Targets')
        try:
            btnx_double_var[10].clicked.disconnect()
        except:
            pass
        btnx_double_var[10].clicked.connect(self.enable_targets)
        btnx_double_var[10].show()

        # Target event menu selection
        self.combo_box_exec.setCurrentIndex(0)
        self.combo_box_exec.show()

        # Target event background label
        lblx_var[24].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgba(0,0,0,255);
            border-top:1px solid rgb""" + str(theme_color) + """;
            border-bottom:1px solid rgb""" + str(theme_color) + """;
            border-right:1px solid rgb""" + str(theme_color) + """;
            border-left:1px solid rgb""" + str(theme_color) + """;
            }""")
        lblx_var[24].resize((btnx_size * 6) + btnx_sp_size * 7, (btnx_size * 7) + btnx_sp_size * 8)
        lblx_var[24].setAlignment(Qt.AlignCenter)
        lblx_var[24].setText(f'')
        lblx_var[24].hide()

        # Video overlay filter (lowers video frame light to reduce glare & contrast when menu open)
        lblx_var[18].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgba(0,0,0,200);
            border-top:2px solid rgb(0, 0, 0);
            border-bottom:2px solid rgb(0, 0, 0);
            border-right:2px solid rgb(0, 0, 0);
            border-left:2px solid rgb(0, 0, 0);}
            }""")
        lblx_var[18].move(lblx_var[16].pos().x(), lblx_var[16].pos().y())
        lblx_var[18].resize((btnx_size * 14) + btnx_sp_size * 13, (btnx_size * 7) + btnx_sp_size * 6)
        lblx_var[18].setAlignment(Qt.AlignCenter)
        lblx_var[18].setText(f'')
        lblx_var[18].hide()

        # Target event object name
        qlex_var[24].setStyleSheet("""
            QLineEdit{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb(0, 0, 0);
            selection-color: black;
            selection-background-color: rgb(0, 180, 0);
            border-bottom:8px solid rgb""" + str(object_color_border_0) + """;
            border-right:7px solid rgb""" + str(object_color_border_0) + """;
            border-top:8px solid rgb""" + str(object_color_border_0) + """;
            border-left:7px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        qlex_var[24].resize((btnx_size * 5) + btnx_sp_size * 4, btnx_size)
        qlex_var[24].returnPressed.connect(self.set_name)
        qlex_var[24].setText(f'')
        qlex_var[24].hide()

        # Add target name
        btnx_var[29].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_var[29].setText('+')
        try:
            btnx_var[29].clicked.disconnect()
        except:
            pass
        btnx_var[29].clicked.connect(self.set_name)
        btnx_var[29].hide()

        # Target minimum detection probability label
        lblx_var[40].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[40].resize((btnx_size * 4) + btnx_sp_size * 3, btnx_size)
        lblx_var[40].setAlignment(Qt.AlignCenter)
        lblx_var[40].setText(f'Target Minimum Probability: 0')
        lblx_var[40].hide()

        # Target minimum detection probability slider
        self.slider_target_minimum_percentage_probability.hide()
        try:
            self.slider_target_minimum_percentage_probability.valueChanged.disconnect()
        except:
            pass
        self.slider_target_minimum_percentage_probability.valueChanged.connect(self.adjust_target_minimum_percentage_probability)

        # Target event file
        lblx_var[56].setStyleSheet("""
            QLabel {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb(0, 0, 0);
            selection-background-color: rgb(0, 180, 0);
            border-bottom:8px solid rgb""" + str(object_color_border_0) + """;
            border-right:7px solid rgb""" + str(object_color_border_0) + """;
            border-top:8px solid rgb""" + str(object_color_border_0) + """;
            border-left:7px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[56].resize((btnx_size * 5) + btnx_sp_size * 4, btnx_size)
        lblx_var[56].setText(f'')
        lblx_var[56].hide()

        # Add exec
        btnx_var[61].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_var[61].setText('+')
        try:
            btnx_var[61].clicked.disconnect()
        except:
            pass
        btnx_var[61].clicked.connect(self.set_exec)

        # Execution mode
        btnx_double_var[72].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[72].setText('')
        try:
            btnx_double_var[72].clicked.disconnect()
        except:
            pass
        btnx_double_var[72].clicked.connect(self.mode_exec)

        # Convert base64 bytes image
        pixmap = QPixmap()
        pixmap.loadFromData(QtCore.QByteArray.fromBase64(application_images.terminate_small))
        self.terminate_small = QIcon(pixmap)

        # Terminate exec
        btnx_double_var[74].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[74].resize((btnx_size * 3) + btnx_sp_size * 2, btnx_size)
        # btnx_double_var[74].setIcon(QIcon(self.terminate_small))
        # btnx_double_var[74].setIconSize(QSize(titlebar_height, titlebar_height))
        btnx_double_var[74].setText('TERMINATE')
        try:
            btnx_double_var[74].clicked.disconnect()
        except:
            pass
        btnx_double_var[74].clicked.connect(self.terminate_exec)

        # Execution status
        btnx_var[77].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(170,170,170);
            border-bottom:26px solid rgb""" + str(object_color_border_0) + """;
            border-right:26px solid rgb""" + str(object_color_border_0) + """;
            border-top:26px solid rgb""" + str(object_color_border_0) + """;
            border-left:26px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_var[77].setText('')
        try:
            btnx_var[77].clicked.disconnect()
        except:
            pass

        # Execution log
        tbx_var[88].setStyleSheet("""
            QTextBrowser {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            selection-color: black;
            selection-background-color: rgb(0, 180, 0);
            border-bottom:8px solid rgb""" + str(object_color_border_0) + """;
            border-right:7px solid rgb""" + str(object_color_border_0) + """;
            border-top:8px solid rgb""" + str(object_color_border_0) + """;
            border-left:7px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        tbx_var[88].resize((btnx_size * 6) + btnx_sp_size * 5, (btnx_size * 2) + btnx_sp_size)
        tbx_var[88].setText(f'')
        tbx_var[88].setReadOnly(True)

        # Remove exec
        btnx_double_var[120].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[120].setText('DELETE')
        try:
            btnx_double_var[120].clicked.disconnect()
        except:
            pass
        btnx_double_var[120].clicked.connect(self.rem_exec)

        # Enable exec
        btnx_double_var[124].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[124].setText('-')
        try:
            btnx_double_var[124].clicked.disconnect()
        except:
            pass
        btnx_double_var[124].clicked.connect(self.enable_exec)

        # Camera select
        self.combo_box_camera.show()

        # Frame detection interval
        lblx_var[30].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[30].resize(btnx_size, btnx_size)
        lblx_var[30].setAlignment(Qt.AlignCenter)
        lblx_var[30].setText(f'FD: {frame_detection_interval}')
        lblx_var[30].show()

        # Frame detection interval slider
        self.slider_frame_detection_interval.show()
        try:
            self.slider_frame_detection_interval.valueChanged.disconnect()
        except:
            pass
        self.slider_frame_detection_interval.valueChanged.connect(self.adjust_frame_detection_interval)

        # Probability label
        lblx_var[46].setStyleSheet("""QLabel{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        lblx_var[46].resize(btnx_size, btnx_size)
        lblx_var[46].setAlignment(Qt.AlignCenter)
        lblx_var[46].setText(f'P: {minimum_percentage_probability}')
        lblx_var[46].show()

        # Probability slider
        self.slider_minimum_percentage_probability.show()
        try:
            self.slider_minimum_percentage_probability.valueChanged.disconnect()
        except:
            pass
        self.slider_minimum_percentage_probability.valueChanged.connect(self.adjust_minimum_percentage_probability)

        # Annotated files
        btnx_double_var[62].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[62].setText('AF: 0')
        btnx_double_var[62].show()

        # Image Files
        btnx_double_var[78].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[78].setText('IF: 0')
        btnx_double_var[78].show()

        # Detected Images
        btnx_double_var[94].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[94].setText('DF: 0')
        btnx_double_var[94].show()

        # Object Count
        btnx_double_var[110].resize((btnx_size * 2) + btnx_sp_size * 1, btnx_size)
        btnx_double_var[110].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[110].setText('OB: 0')
        btnx_double_var[110].show()

        # Unique objects
        btnx_double_var[126].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[126].setText('UOB: 0')
        btnx_double_var[126].show()

        # Time Elapsed
        lblx_var[142].resize((btnx_size * 2) + btnx_sp_size * 1, btnx_size)
        lblx_var[142].setStyleSheet("""QLabel{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        lblx_var[142].setText('TE: 0')
        lblx_var[142].setAlignment(Qt.AlignCenter)
        lblx_var[142].show()

        # Play/Pause
        btnx_double_var[128].setText('Start')
        btnx_double_var[128].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_double_var[128].clicked.disconnect()
        except:
            pass
        btnx_double_var[128].clicked.connect(self.start_live)
        btnx_double_var[128].show()

        # Stop video
        btnx_double_var[130].setText('Stop')
        btnx_double_var[130].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_double_var[130].clicked.disconnect()
        except:
            pass
        btnx_double_var[130].clicked.connect(self.stop_live)

        # Frame slider
        try:
            self.slider_frame_track.valueChanged.disconnect()
        except:
            pass
        self.slider_frame_track.valueChanged.connect(self.frame_camera_track)
        self.slider_frame_track.show()

        # Frame Progress
        lblx_var[136].resize((btnx_size * 3) + btnx_sp_size * 2, btnx_size)
        lblx_var[136].setStyleSheet("""QLabel{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        lblx_var[136].setText('0/0')
        lblx_var[136].setAlignment(Qt.AlignCenter)
        lblx_var[136].show()

        # FPS
        lblx_var[139].resize((btnx_size * 2) + btnx_sp_size * 1, btnx_size)
        lblx_var[139].setStyleSheet("""QLabel{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        lblx_var[139].setText('FPS: 0')
        lblx_var[139].setAlignment(Qt.AlignCenter)
        lblx_var[139].show()

        # Camera Live
        lblx_var[141].resize(btnx_size * 1, btnx_size)
        lblx_var[141].setText('')
        lblx_var[141].setAlignment(Qt.AlignCenter)
        lblx_var[141].show()

        # Main info label
        lblx_var[17].setText('')
        lblx_var[17].hide()

        btnx_double_var[130].show()

    @QtCore.pyqtSlot()
    def hide_camera_mode(self):
        global lblx_var, btnx_double_var, qlex_double_var

        # Main label
        self.set_main_label_1()

        # Remove current tab emphasis
        btnx_double_var[0].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:10px solid rgb""" + str(object_color_border_0) + """;
            border-right:10px solid rgb""" + str(object_color_border_0) + """;
            border-top:20px solid rgb""" + str(object_color_border_0) + """;
            border-left:20px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color: rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:14px solid rgb""" + str(object_color_border_0) + """;
            border-right:24px solid rgb""" + str(object_color_border_0) + """;
            border-top:14px solid rgb""" + str(object_color_border_0) + """;
            border-left:24px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)

        # Select camera
        self.combo_box_camera.hide()

        # Targets
        btnx_double_var[10].setText('')
        try:
            btnx_double_var[10].clicked.disconnect()
        except:
            pass
        btnx_double_var[10].hide()

        # Target event menu selection
        self.combo_box_exec.setCurrentIndex(0)
        self.combo_box_exec.hide()

        # Video overlay filter (lowers video frame light to reduce glare & contrast when menu open)
        lblx_var[18].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgba(0,0,0,220);
            border-top:2px solid rgb(0, 0, 0);
            border-bottom:2px solid rgb(0, 0, 0);
            border-right:2px solid rgb(0, 0, 0);
            border-left:2px solid rgb(0, 0, 0);}
            }""")
        # lblx_var[18].move(lblx_var[18].pos().x(), lblx_var[18].pos().y())
        lblx_var[18].resize(btnx_size, btnx_size)
        lblx_var[18].setAlignment(Qt.AlignCenter)
        lblx_var[18].setText(f'')
        lblx_var[18].hide()

        # Target event object name
        qlex_var[24].setStyleSheet("""
            QTextBrowser {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb(0, 0, 0);
            selection-color: black;
            selection-background-color: rgb(0, 180, 0);
            border-bottom:8px solid rgb""" + str(object_color_border_0) + """;
            border-right:7px solid rgb""" + str(object_color_border_0) + """;
            border-top:8px solid rgb""" + str(object_color_border_0) + """;
            border-left:7px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        qlex_var[24].resize(btnx_size, btnx_size)
        qlex_var[24].setText(f'')
        qlex_var[24].hide()

        # Add target name
        btnx_var[29].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_var[29].setText('')
        try:
            btnx_var[29].clicked.disconnect()
        except:
            pass
        btnx_var[29].hide()

        # Target minimum detection probability label
        lblx_var[40].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[40].resize(btnx_size, btnx_size)
        lblx_var[40].setAlignment(Qt.AlignCenter)
        lblx_var[40].setText(f'')
        lblx_var[40].hide()

        # Target minimum detection probability slider
        self.slider_target_minimum_percentage_probability.hide()
        try:
            self.slider_target_minimum_percentage_probability.valueChanged.disconnect()
        except:
            pass

        # Add exec
        btnx_var[61].setText('')
        try:
            btnx_var[61].clicked.disconnect()
        except:
            pass
        btnx_var[61].hide()

        # Target event file
        lblx_var[56].setStyleSheet("""
            QLabel {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb(0, 0, 0);
            border-bottom:8px solid rgb""" + str(object_color_border_0) + """;
            border-right:7px solid rgb""" + str(object_color_border_0) + """;
            border-top:8px solid rgb""" + str(object_color_border_0) + """;
            border-left:7px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[56].resize((btnx_size * 6) + btnx_sp_size * 5, btnx_size)
        lblx_var[56].setText(f'')
        lblx_var[56].hide()

        # Execution mode
        btnx_double_var[72].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:0px solid rgb""" + str(object_color_border_0) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[72].setText('')
        try:
            btnx_double_var[72].clicked.disconnect()
        except:
            pass
        btnx_double_var[72].hide()

        # Terminate exec
        btnx_double_var[74].setText('')
        try:
            btnx_double_var[74].clicked.disconnect()
        except:
            pass
        btnx_double_var[74].hide()

        # Execution status
        btnx_var[77].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(170,170,170);
            border-bottom:26px solid rgb""" + str(object_color_border_0) + """;
            border-right:26px solid rgb""" + str(object_color_border_0) + """;
            border-top:26px solid rgb""" + str(object_color_border_0) + """;
            border-left:26px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_var[77].setText('')
        try:
            btnx_var[77].clicked.disconnect()
        except:
            pass
        btnx_var[77].hide()

        # Execution log
        tbx_var[88].resize(btnx_size, btnx_size)
        tbx_var[88].setText(f'')

        # Remove exec
        btnx_double_var[120].setText('')
        try:
            btnx_double_var[120].clicked.disconnect()
        except:
            pass
        btnx_double_var[120].hide()

        # Enable exec
        btnx_double_var[124].setText('')
        try:
            btnx_double_var[124].clicked.disconnect()
        except:
            pass
        btnx_double_var[124].hide()

        # Frame detection interval
        lblx_var[30].setText(f'')
        lblx_var[30].show()

        # Frame detection interval slider
        self.slider_frame_detection_interval.show()
        try:
            self.slider_frame_detection_interval.valueChanged.disconnect()
        except:
            pass

        # Probability label
        lblx_var[46].hide()
        lblx_var[46].setText('')

        # Probability slider
        self.slider_minimum_percentage_probability.hide()
        try:
            self.slider_minimum_percentage_probability.valueChanged.disconnect()
        except:
            pass

        # Annotated files
        btnx_double_var[62].setText('')
        btnx_double_var[62].hide()

        # Image files
        btnx_double_var[78].setText('')
        btnx_double_var[78].hide()

        # Detected files
        btnx_double_var[94].setText('')
        btnx_double_var[94].hide()

        # Objects
        btnx_double_var[110].setText('')
        btnx_double_var[110].hide()

        # Unique objects
        btnx_double_var[126].setText('')
        btnx_double_var[126].hide()

        # Play/Pause
        btnx_double_var[128].setText('')
        try:
            btnx_double_var[128].clicked.disconnect()
        except:
            pass
        btnx_double_var[128].hide()

        # Stop video
        btnx_double_var[130].setText('')
        try:
            btnx_double_var[130].clicked.disconnect()
        except:
            pass
        btnx_double_var[130].hide()

        # Frame slider
        self.slider_frame_track.hide()
        try:
            self.slider_frame_track.valueChanged.disconnect()
        except:
            pass

        # Frame progress
        lblx_var[136].resize((btnx_size * 2) + btnx_sp_size, btnx_size)
        lblx_var[136].setText('')
        lblx_var[136].hide()

        # FPS
        lblx_var[139].setText('')
        lblx_var[139].hide()
        
        # Camera live
        lblx_var[140].hide()

        # Time elapsed
        lblx_var[142].hide()

        # Camera Live
        lblx_var[141].resize((btnx_size * 2) + btnx_sp_size, btnx_size)
        lblx_var[141].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[141].setText('')
        lblx_var[141].setAlignment(Qt.AlignCenter)
        lblx_var[141].hide()

        # Main info label
        lblx_var[17].setText('')
        lblx_var[17].hide()

    @QtCore.pyqtSlot()
    def display_video_mode(self):
        global lblx_var, btnx_double_var, qlex_double_var

        self.stop_live()

        # Hide other tabs
        self.hide_camera_mode()
        self.hide_annotation_mode()
        self.hide_training_mode()

        # Main label
        self.set_main_label_1()

        # Fill main tab empty space
        btnx_double_var[8].setText('')
        btnx_double_var[8].resize((btnx_size * 6) + btnx_sp_size * 5, btnx_size)
        btnx_double_var[8].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[8].show()

        # Emphasize current tab
        btnx_double_var[2].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:2px solid rgb""" + str(theme_color) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;
            }
            QPushButton::hover {background-color : rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:1px solid rgb""" + str(theme_color) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;
            }
            """)

        # Open video file
        try:
            btnx_double_var[14].clicked.disconnect()
        except:
            pass
        btnx_double_var[14].setText('+')
        btnx_double_var[14].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        btnx_double_var[14].clicked.connect(self.select_video_file)
        btnx_double_var[14].show()

        # Frame detection interval
        lblx_var[30].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[30].resize(btnx_size, btnx_size)
        lblx_var[30].setAlignment(Qt.AlignCenter)
        lblx_var[30].setText(f'FD: {frame_detection_interval}')
        lblx_var[30].show()

        # Frame detection interval slider
        self.slider_frame_detection_interval.show()
        try:
            self.slider_frame_detection_interval.valueChanged.disconnect()
        except:
            pass
        self.slider_frame_detection_interval.valueChanged.connect(self.adjust_frame_detection_interval)

        # Probability
        lblx_var[46].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[46].resize(btnx_size, btnx_size)
        lblx_var[46].setAlignment(Qt.AlignCenter)
        lblx_var[46].setText(f'P: {minimum_percentage_probability}')
        lblx_var[46].show()

        # Probability slider
        self.slider_minimum_percentage_probability.show()
        try:
            self.slider_minimum_percentage_probability.valueChanged.disconnect()
        except:
            pass
        self.slider_minimum_percentage_probability.valueChanged.connect(self.adjust_minimum_percentage_probability)

        # Annotated files
        btnx_double_var[62].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
                    }""")
        btnx_double_var[62].setText('AF: 0')
        btnx_double_var[62].show()

        # Image Frames
        btnx_double_var[78].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
                    }""")
        btnx_double_var[78].setText('IF: 0')
        btnx_double_var[78].show()

        # Detected Images 94
        btnx_double_var[94].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
                    }""")
        btnx_double_var[94].setText('DF: 0')
        btnx_double_var[94].show()

        # Object Count 110
        btnx_double_var[110].resize((btnx_size * 2) + btnx_sp_size * 1, btnx_size)
        btnx_double_var[110].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
                    }""")
        btnx_double_var[110].setText('OB: 0')
        btnx_double_var[110].show()

        # Unique objects
        btnx_double_var[126].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
                    }""")
        btnx_double_var[126].setText('UOB: 0')
        btnx_double_var[126].show()

        # Play/Pause
        btnx_double_var[128].setText('Start')
        try:
            btnx_double_var[128].clicked.disconnect()
        except:
            pass
        btnx_double_var[128].clicked.connect(self.pause_frame)
        btnx_double_var[128].show()

        # Stop video
        btnx_double_var[130].setText('Stop')
        try:
            btnx_double_var[130].clicked.disconnect()
        except:
            pass
        btnx_double_var[130].clicked.connect(self.stop_video)
        btnx_double_var[130].show()

        # Frame slider
        self.slider_frame_track.show()
        try:
            self.slider_frame_track.valueChanged.disconnect()
        except:
            pass
        self.slider_frame_track.valueChanged.connect(self.frame_track)

        # Frame Progress
        lblx_var[136].resize((btnx_size * 2) + btnx_sp_size * 1, btnx_size)
        lblx_var[136].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
                    }""")
        lblx_var[136].setText('0/0')
        lblx_var[136].setAlignment(Qt.AlignCenter)
        lblx_var[136].show()

        # FPS
        lblx_var[138].resize((btnx_size * 2) + btnx_sp_size * 1, btnx_size)
        lblx_var[138].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[138].setText('FPS: 0')
        lblx_var[138].setAlignment(Qt.AlignCenter)
        lblx_var[138].show()

        # ETA
        lblx_var[140].resize((btnx_size * 2) + btnx_sp_size * 1, btnx_size)
        lblx_var[140].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[140].setText('ETA: 0')
        lblx_var[140].setAlignment(Qt.AlignCenter)
        lblx_var[140].show()

        # Time Elapsed
        lblx_var[142].resize((btnx_size * 2) + btnx_sp_size * 1, btnx_size)
        lblx_var[142].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        lblx_var[142].setText('TE: 0')
        lblx_var[142].setAlignment(Qt.AlignCenter)
        lblx_var[142].show()

    @QtCore.pyqtSlot()
    def sizeof_fmt(self, num, suffix='B'):
        ''' by Fred Cirera,  https://stackoverflow.com/a/1094933/1870254, modified'''
        for unit in ['', 'Ki', 'Mi', 'Gi', 'Ti', 'Pi', 'Ei', 'Zi']:
            if abs(num) < 1024.0:
                return "%3.1f %s%s" % (num, unit, suffix)
            num /= 1024.0
        return "%.1f %s%s" % (num, 'Yi', suffix)

    @QtCore.pyqtSlot()
    def timer_00_function(self):
        print('_'*50)
        print('[LOCALS]')
        for name, size in sorted(((name, sys.getsizeof(value)) for name, value in list(
                locals().items())), key=lambda x: -x[1])[:10]:
            print("{:>30}: {:>8}".format(name, self.sizeof_fmt(size)))
        print('_'*50)
        print('[GLOBALS]')
        for name, size in sorted(((name, sys.getsizeof(value)) for name, value in list(
                globals().items())), key=lambda x: -x[1])[:10]:
            print("{:>30}: {:>8}".format(name, self.sizeof_fmt(size)))
        print('_'*50)

    @QtCore.pyqtSlot()
    def timer_00_start_function(self):
        self.timer_00.start()

    @QtCore.pyqtSlot()
    def timer_00_stop_function(self):
        self.timer_00.stop()

    @QtCore.pyqtSlot()
    def hide_video_mode(self):
        global lblx_var, btnx_double_var, qlex_double_var

        # Main label
        self.set_main_label_1()

        # Remove current tab emphasis
        btnx_double_var[2].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:10px solid rgb""" + str(object_color_border_0) + """;
            border-right:20px solid rgb""" + str(object_color_border_0) + """;
            border-top:10px solid rgb""" + str(object_color_border_0) + """;
            border-left:20px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color: rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:14px solid rgb""" + str(object_color_border_0) + """;
            border-right:240px solid rgb""" + str(object_color_border_0) + """;
            border-top:14px solid rgb""" + str(object_color_border_0) + """;
            border-left:24px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)

        # Open video file
        btnx_double_var[14].hide()
        btnx_double_var[14].setText('')
        try:
            btnx_double_var[14].clicked.disconnect()
        except:
            pass

        # Frame detection interval
        lblx_var[30].setText('')
        lblx_var[30].hide()
        
        # Frame detection interval slider
        self.slider_frame_detection_interval.hide()
        try:
            self.slider_frame_detection_interval.valueChanged.disconnect()
        except:
            pass

        # Probability
        lblx_var[46].hide()
        lblx_var[46].setText('')

        # Probability slider
        self.slider_minimum_percentage_probability.hide()
        try:
            self.slider_minimum_percentage_probability.valueChanged.disconnect()
        except:
            pass

        # Play/Pause
        btnx_double_var[128].setText('')
        try:
            btnx_double_var[128].clicked.disconnect()
        except:
            pass
        btnx_double_var[128].hide()

        # Stop video
        btnx_double_var[130].setText('')
        try:
            btnx_double_var[130].clicked.disconnect()
        except:
            pass
        btnx_double_var[130].hide()

        # Frame slider
        self.slider_frame_track.hide()
        try:
            self.slider_frame_track.valueChanged.disconnect()
        except:
            pass

        # Annotated files
        btnx_double_var[62].setText('')
        btnx_double_var[62].hide()

        # Image files
        btnx_double_var[78].setText('')
        btnx_double_var[78].hide()

        # Detected files
        btnx_double_var[94].setText('')
        btnx_double_var[94].hide()

        # Objects
        btnx_double_var[110].setText('')
        btnx_double_var[110].hide()
        
        # Unique objects
        btnx_double_var[126].setText('')
        btnx_double_var[126].hide()
        
        # Frame progress
        lblx_var[136].setText('')
        lblx_var[136].hide()

        # FPS
        lblx_var[138].setText('')
        lblx_var[138].hide()

        # ETA
        lblx_var[140].hide()

        # Time elapsed
        lblx_var[142].hide()

    @QtCore.pyqtSlot()
    def select_image_to_annotate(self):
        global input_files_images, index_input_files_images
        options = QFileDialog.Options()
        file_name, _ = QFileDialog.getOpenFileName(self, "Select image:", "", "All Files (*);;", options=options)
        if file_name:
            print(f'-- selecting input file: {file_name}')
            input_files_images = [file_name]
            self.iter_input_file()

    @QtCore.pyqtSlot()
    def select_images_to_annotate(self):
        global directory_input_image, input_files_images, index_input_files_images
        global directory_input_annotation, input_files_annotations
        cwd = os.getcwd()
        dir_name = QFileDialog.getExistingDirectory(caption='Select image directory:', directory=cwd)
        if dir_name:
            # display selected directory
            print(f'-- selecting input directory: {dir_name}')

            # scan selected directory
            selected_base = [os.path.join(dir_name, f) for f in os.listdir(dir_name)]
            print('selected_base list:', selected_base)

            # check for dataset directory structure
            selected_dataset_bool = [False, False]
            for f in selected_base:
                print(f'checking: {f}')
                if f.endswith('annotations'):
                    directory_input_annotation = f
                    selected_dataset_bool[0] = True
                if f.endswith('images'):
                    directory_input_image = f
                    selected_dataset_bool[1] = True

            # compile list of image files
            if False in selected_dataset_bool:
                print('no dataset found: setting selected directory as image directory')
                input_files_annotations = []
                input_files_images = []
                directory_input_image = dir_name
                input_files_images = [os.path.join(directory_input_image, f) for f in os.listdir(directory_input_image)]

            # otherwise compile list of annotation files and image files
            elif False not in selected_dataset_bool:
                print('possible dataset found: setting directories accordingly')

                # create lists of file paths
                tmp_input_files_annotations = [os.path.join(directory_input_annotation, f) for f in os.listdir(directory_input_annotation)]
                tmp_input_files_images = [os.path.join(directory_input_image, f) for f in os.listdir(directory_input_image)]

                # create lists of filenames for validation
                tmp_input_files_annotations_names = []
                for x in tmp_input_files_annotations:
                    file_name_idx = x.rfind('\\')
                    tmp_input_files_annotations_names.append(x[file_name_idx + 1:])
                tmp_input_files_images_names = []
                for x in tmp_input_files_images:
                    file_name_idx = x.rfind('\\')
                    tmp_input_files_images_names.append(x[file_name_idx + 1:])

                # perform dataset validation:
                input_files_annotations = []
                input_files_images = []
                invalid_files = []
                idx_validation = 0
                # iterate through annotation filenames
                for filename in tmp_input_files_annotations_names:
                    # compare filenames to image filenames
                    print(f'comparing: {filename} ({filename.replace(".xml", ".jpg")}) [->]  {tmp_input_files_images_names[idx_validation]}')
                    if filename.replace('.xml', '.jpg') == tmp_input_files_images_names[idx_validation]:
                        # place validated files in lists
                        print(f'valid: {tmp_input_files_annotations_names[idx_validation]}')
                        input_files_annotations.append(tmp_input_files_annotations[idx_validation])
                        input_files_images.append(tmp_input_files_images[idx_validation])
                    else:
                        # place invalid files in list
                        invalid_files.append(tmp_input_files_annotations[idx_validation])
                        print(f'invalid: {tmp_input_files_images[idx_validation]}')
                    idx_validation += 1
                # display results
                print('')
                print(f'valid annotation files: {len(input_files_annotations)}')
                print(f'valid image files:      {len(input_files_images)}')
                print(f'invalid files: {len(invalid_files)}')

            print('')
            print('selected_dataset_bool:', selected_dataset_bool)
            print('')
            print('directory_input_annotation:', directory_input_annotation)
            print('input_files_annotations:', input_files_annotations)
            print('')
            print('directory_input_image:', directory_input_image)
            print('input_files_images:', input_files_images)
            print('')
            index_input_files_images = 0
            self.iter_input_file()
    
    @QtCore.pyqtSlot()
    def clear_manual_annotation(self):
        global annotations
        annotations = []

    @QtCore.pyqtSlot()
    def close_manual_annotation_current_images(self):
        global input_files_images, directory_input_image, lblx_var
        try:
            tbx_var[8].setText(f'0: x1:0 y1:0 x2:0 y2:0')
            tbx_var[8].append(f'1: x1:0 y1:0 x2:0 y2:0')
        except:
            pass
        input_files_images = []
        directory_input_image = ''
        qlex_double_var[130].setText('')
        self.set_main_label_1()

    @QtCore.pyqtSlot()
    def display_annotation_mode(self):
        global lblx_var, btnx_double_var, qlex_double_var, MODE_MANUAL_ANNOTATION

        # Hide other tabs
        self.hide_camera_mode()
        self.hide_video_mode()
        self.hide_training_mode()

        # Main label
        self.set_main_label_1()
        if input_files_images:
            lblx_var[self.video_label].hide()

        # Fill main tab empty space todo
        btnx_double_var[8].setText('')
        btnx_double_var[8].resize((btnx_size * 5) + btnx_sp_size * 4, btnx_size)
        btnx_double_var[8].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[8].hide()

        # Annotation onscreen telemetry
        tbx_var[8].setStyleSheet("""
            QTextBrowser {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb(0, 0, 0);
            selection-color: black;
            selection-background-color: rgb(0, 180, 0);
            border-bottom:8px solid rgb""" + str(object_color_border_0) + """;
            border-right:7px solid rgb""" + str(object_color_border_0) + """;
            border-top:8px solid rgb""" + str(object_color_border_0) + """;
            border-left:7px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        tbx_var[8].resize((btnx_size * 5) + btnx_sp_size * 4, btnx_size)
        tbx_var[8].setText(f'')
        tbx_var[8].show()

        # Emphasize current tab
        btnx_double_var[4].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:2px solid rgb""" + str(theme_color) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;
            }
            QPushButton::hover {background-color : rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:1px solid rgb""" + str(theme_color) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;
            }
            """)

        # Close Image File(s)
        btnx_var[13].setText('x')
        btnx_var[13].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_var[13].clicked.disconnect()
        except:
            pass
        btnx_var[13].clicked.connect(self.close_manual_annotation_current_images)
        btnx_var[13].show()

        # Open Image File
        btnx_var[14].setText('+')
        btnx_var[14].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_var[14].clicked.disconnect()
        except:
            pass
        btnx_var[14].clicked.connect(self.select_image_to_annotate)
        btnx_var[14].show()

        # Open Image Directory
        btnx_var[15].setText('+')
        btnx_var[15].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_var[15].clicked.disconnect()
        except:
            pass
        btnx_var[15].clicked.connect(self.select_images_to_annotate)
        btnx_var[15].show()

        border_top = 26
        border_bottom = 26
        border_left = 54
        border_right = 54

        border_top_pressed = 27
        border_bottom_pressed = 27
        border_left_pressed = 55
        border_right_pressed = 55

        # Brush white
        btnx_double_var[30].setText('')
        btnx_double_var[30].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(255,255,255);
            border-top:""" + str(border_top) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color : rgb(255,255,255);
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(255,255,255);
            border-top:""" + str(border_top_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right_pressed) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_double_var[30].clicked.disconnect()
        except:
            pass
        btnx_double_var[30].clicked.connect(self.brush_white)
        btnx_double_var[30].show()

        # Brush pink
        btnx_double_var[46].setText('')
        btnx_double_var[46].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(255,105,180);
            border-top:""" + str(border_top) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color : rgb(255,0,255);
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(255,105,180);
            border-top:""" + str(border_top_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right_pressed) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_double_var[46].clicked.disconnect()
        except:
            pass
        btnx_double_var[46].clicked.connect(self.brush_pink)
        btnx_double_var[46].show()

        # Brush blue
        btnx_double_var[62].setText('')
        btnx_double_var[62].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(0,0,255);
            border-top:""" + str(border_top) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color : rgb(0,0,255);
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(0,0,255);
            border-top:""" + str(border_top_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom_pressed) + """px solid rrgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right_pressed) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_double_var[62].clicked.disconnect()
        except:
            pass
        btnx_double_var[62].clicked.connect(self.brush_blue)
        btnx_double_var[62].show()

        # Brush green
        btnx_double_var[78].setText('')
        btnx_double_var[78].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(0,255,0);
            border-top:""" + str(border_top) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color : rgb(0,255,0);
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(0,255,0);
            border-top:""" + str(border_top_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right_pressed) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_double_var[78].clicked.disconnect()
        except:
            pass
        btnx_double_var[78].clicked.connect(self.brush_green)
        btnx_double_var[78].show()

        # Brush yellow
        btnx_double_var[94].setText('')
        btnx_double_var[94].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(255,255,0);
            border-top:""" + str(border_top) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color : rgb(255,255,0);
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(255,255,0);
            border-top:""" + str(border_top_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right_pressed) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_double_var[94].clicked.disconnect()
        except:
            pass
        btnx_double_var[94].clicked.connect(self.brush_yellow)
        btnx_double_var[94].show()

        # Brush red
        btnx_double_var[110].setText('')
        btnx_double_var[110].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(255,0,0);
            border-top:""" + str(border_top) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {
            background-color : rgb(255,0,0);
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(255,0,0);
            border-top:""" + str(border_top_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right_pressed) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_double_var[110].clicked.disconnect()
        except:
            pass
        btnx_double_var[110].clicked.connect(self.brush_red)
        btnx_double_var[110].show()

        # Brush black
        btnx_double_var[126].setText('')
        btnx_double_var[126].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb(0,0,0);
            border-top:""" + str(border_top) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color : rgb(0,0,0);
            }
            QPushButton::pressed {
             color: rgb""" + str(object_color_0) + """;
            background-color : rgb(0,0,0);
            border-top:""" + str(border_top_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:""" + str(border_bottom_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-right:""" + str(border_left_pressed) + """px solid rgb""" + str(object_color_border_0) + """;
            border-left:""" + str(border_right_pressed) + """px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_double_var[126].clicked.disconnect()
        except:
            pass
        btnx_double_var[126].clicked.connect(self.brush_black)
        btnx_double_var[126].show()

        # Brush alpha button
        btnx_var[142].setText(str(self.brush_color_a))
        btnx_var[142].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:4px solid rgb""" + str(object_color_border_0) + """;
            border-right:4px solid rgb""" + str(object_color_border_0) + """;
            border-top:4px solid rgb""" + str(object_color_border_0) + """;
            border-left:4px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color: rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:4px solid rgb""" + str(object_color_border_0) + """;
            border-right:4px solid rgb""" + str(object_color_border_0) + """;
            border-top:4px solid rgb""" + str(object_color_border_0) + """;
            border-left:4px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_var[142].clicked.disconnect()
        except:
            pass
        btnx_var[142].clicked.connect(self.brush_alpha)
        btnx_var[142].show()

        # Brush alpha slider
        try:
            self.slider_alpha.valueChanged.disconnect()
        except:
            pass
        self.slider_alpha.valueChanged.connect(self.adjust_alpha)
        self.slider_alpha.show()

        # Remove currently selected object annotation
        btnx_var[129].setText('RM')
        btnx_var[129].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_var[129].clicked.disconnect()
        except:
            pass
        btnx_var[129].clicked.connect(self.remove_current_manual_annotation)
        btnx_var[129].show()

        # Clear current image annotations
        btnx_var[128].setText('CL')
        btnx_var[128].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_var[128].clicked.disconnect()
        except:
            pass
        btnx_var[128].clicked.connect(self.clear_manual_annotation)
        btnx_var[128].show()

        # Object Name
        lblx_var[130].resize((btnx_size * 2) + btnx_sp_size, btnx_size / 2)
        lblx_var[130].setAlignment(QtCore.Qt.AlignCenter)
        lblx_var[130].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:4px solid rgb(0, 0, 0);
            border-right:4px solid rgb""" + str(object_color_border_0) + """;
            border-top:4px solid rgb""" + str(object_color_border_0) + """;
            border-left:4px solid rgb""" + str(object_color_border_0) + """;}
            """)
        lblx_var[130].setText('Object Name')
        lblx_var[130].show()

        # Specify object name
        qlex_double_var[130].setText('')
        qlex_double_var[130].setAlignment(QtCore.Qt.AlignCenter)
        qlex_double_var[130].setStyleSheet("""QLineEdit{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:4px solid rgb""" + str(object_color_border_0) + """;
            border-left:4px solid rgb""" + str(object_color_border_0) + """;}
            """)
        qlex_double_var[130].show()

        # Add current image annotation to list
        btnx_double_var[132].setText('+')
        btnx_double_var[132].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_double_var[132].clicked.disconnect()
        except:
            pass
        btnx_double_var[132].clicked.connect(self.new_manual_annotation)
        btnx_double_var[132].show()

        # Save current image annotations
        btnx_double_var[134].setText('Save')
        btnx_double_var[134].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_double_var[134].clicked.disconnect()
        except:
            pass
        btnx_double_var[134].clicked.connect(self.save_manual_annotation)
        btnx_double_var[134].show()

        # Previous object
        btnx_var[136].setText('<')
        btnx_var[136].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_var[136].clicked.disconnect()
        except:
            pass
        btnx_var[136].clicked.connect(self.manual_annotation_previous_object)
        btnx_var[136].show()

        # Next object
        btnx_var[137].setText('>')
        btnx_var[137].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_var[137].clicked.disconnect()
        except:
            pass
        btnx_var[137].clicked.connect(self.manual_annotation_next_object)
        btnx_var[137].show()

        # Previous image
        btnx_double_var[138].setText('<')
        btnx_double_var[138].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_double_var[138].clicked.disconnect()
        except:
            pass
        btnx_double_var[138].clicked.connect(self.previous_manual_annotation)
        btnx_double_var[138].show()

        # Next image
        btnx_double_var[140].setText('>')
        btnx_double_var[140].setStyleSheet("""QPushButton{
             color: rgb""" + str(object_color_0) + """;
             background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        try:
            btnx_double_var[140].clicked.disconnect()
        except:
            pass
        btnx_double_var[140].clicked.connect(self.next_manual_annotation)
        btnx_double_var[140].show()

    def hide_annotation_mode(self):
        global lblx_var, btnx_double_var, qlex_double_var

        # Remove current tab emphasis
        btnx_double_var[4].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:10px solid rgb""" + str(object_color_border_0) + """;
            border-right:20px solid rgb""" + str(object_color_border_0) + """;
            border-top:10px solid rgb""" + str(object_color_border_0) + """;
            border-left:20px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color: rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
             color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:14px solid rgb""" + str(object_color_border_0) + """;
            border-right:24px solid rgb""" + str(object_color_border_0) + """;
            border-top:14px solid rgb""" + str(object_color_border_0) + """;
            border-left:24px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)

        # Annotation onscreen telemetry
        tbx_var[8].setStyleSheet("""
            QTextBrowser {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb(0, 0, 0);
            selection-color: black;
            selection-background-color: rgb(0, 180, 0);
            border-bottom:8px solid rgb""" + str(object_color_border_0) + """;
            border-right:7px solid rgb""" + str(object_color_border_0) + """;
            border-top:8px solid rgb""" + str(object_color_border_0) + """;
            border-left:7px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        tbx_var[8].resize(btnx_size, btnx_size)
        tbx_var[8].setText(f'')
        tbx_var[8].hide()

        # Close Image File(s)
        btnx_var[13].setText('')
        try:
            btnx_var[13].clicked.disconnect()
        except:
            pass
        btnx_var[13].hide()
        
        # Open image file
        btnx_var[14].setText('')
        try:
            btnx_var[14].clicked.disconnect()
        except:
            pass
        btnx_var[14].hide()

        # Open image directory
        btnx_var[15].setText('')
        try:
            btnx_var[15].clicked.disconnect()
        except:
            pass
        btnx_var[15].hide()

        # Brushes
        brushes = [30, 46, 62, 78, 94, 110, 126]
        for brush in brushes:
            btnx_double_var[brush].hide()
            btnx_double_var[brush].setStyleSheet("""QPushButton{
                color: rgb""" + str(object_color_0) + """;
                background-color: rgb""" + str(object_color_background_0) + """;
                border-bottom:25px solid rgb""" + str(object_color_border_0) + """;
                border-right:49px solid rgb""" + str(object_color_border_0) + """;
                border-top:25px solid rgb""" + str(object_color_border_0) + """;
                border-left:49px solid rgb""" + str(object_color_border_0) + """;}
                }
                QPushButton::hover {background-color : rgb(0,0,255);
                }
                QPushButton::pressed {
                color: rgb""" + str(object_color_0) + """;
                background-color: rgb""" + str(object_color_background_0) + """;
                border-bottom:25px solid rgb""" + str(object_color_border_0) + """;
                border-right:49px solid rgb""" + str(object_color_border_0) + """;
                border-top:25px solid rgb""" + str(object_color_border_0) + """;
                border-left:49px solid rgb""" + str(object_color_border_0) + """;}
                }
                """)

        # Undo last annotation
        btnx_var[129].setText('')
        try:
            btnx_var[129].clicked.disconnect()
        except:
            pass
        btnx_var[129].hide()

        # Clear current image annotations
        btnx_var[128].setText('')
        try:
            btnx_var[128].clicked.disconnect()
        except:
            pass
        btnx_var[128].hide()

        # Object Name
        lblx_var[130].setText('')
        lblx_var[130].hide()

        # Specify object name
        qlex_double_var[130].setText('')
        qlex_double_var[130].hide()

        # Add
        btnx_double_var[132].hide()

        # Save
        btnx_double_var[134].hide()

        # Previous object
        btnx_var[136].setText('')
        try:
            btnx_var[136].clicked.disconnect()
        except:
            pass
        btnx_var[136].hide()

        # Next object
        btnx_var[137].setText('')
        try:
            btnx_var[137].clicked.disconnect()
        except:
            pass
        btnx_var[137].hide()

        # Previous image
        btnx_double_var[138].hide()

        # Next image
        btnx_double_var[140].hide()

        # Alpha button
        btnx_var[142].hide()

        # Alpha slider
        self.slider_alpha.hide()
        try:
            self.slider_alpha.valueChanged.disconnect()
        except:
            pass

    @QtCore.pyqtSlot()
    def display_training_mode(self):
        global lblx_var, btnx_double_var, qlex_double_var, tbx_var, _batch_size, _num_experiments

        # Hide other tabs
        self.hide_camera_mode()
        self.hide_video_mode()
        self.hide_annotation_mode()

        # Main label
        self.set_main_label_1()

        # Fill main tab empty space
        btnx_double_var[8].setText('')
        btnx_double_var[8].resize((btnx_size * 8) + btnx_sp_size * 7, btnx_size)
        btnx_double_var[8].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
             }""")
        btnx_double_var[8].show()

        # Emphasize current tab
        btnx_double_var[6].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:2px solid rgb""" + str(theme_color) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;
            }
            QPushButton::hover {background-color : rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color : rgb""" + str(object_color_border_0) + """;
            border-top:0px solid rgb""" + str(object_color_border_0) + """;
            border-bottom:1px solid rgb""" + str(theme_color) + """;
            border-right:0px solid rgb""" + str(object_color_border_0) + """;
            border-left:0px solid rgb""" + str(object_color_border_0) + """;
            }
            """)

        # Output textbox
        tbx_var[16].setStyleSheet("""
            QTextBrowser {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb(0, 0, 0);
            selection-color: black;
            selection-background-color: rgb(0, 180, 0);
            border-bottom:8px solid rgb""" + str(object_color_border_0) + """;
            border-right:7px solid rgb""" + str(object_color_border_0) + """;
            border-top:8px solid rgb""" + str(object_color_border_0) + """;
            border-left:7px solid rgb""" + str(object_color_border_0) + """;}
        """)
        tbx_var[16].show()

        # Input directory
        btnx_var[30].setText('+')
        btnx_var[30].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:12px solid rgb""" + str(object_color_border_0) + """;
            border-right:12px solid rgb""" + str(object_color_border_0) + """;
            border-top:12px solid rgb""" + str(object_color_border_0) + """;
            border-left:12px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color: rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:12px solid rgb""" + str(object_color_border_0) + """;
            border-right:12px solid rgb""" + str(object_color_border_0) + """;
            border-top:12px solid rgb""" + str(object_color_border_0) + """;
            border-left:12px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_var[30].clicked.disconnect()
        except:
            pass
        btnx_var[30].clicked.connect(self.select_training_directory)
        btnx_var[30].show()

        # Select pretrained model
        btnx_var[31].setText('+')
        btnx_var[31].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:12px solid rgb""" + str(object_color_border_0) + """;
            border-right:12px solid rgb""" + str(object_color_border_0) + """;
            border-top:12px solid rgb""" + str(object_color_border_0) + """;
            border-left:12px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color: rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:12px solid rgb""" + str(object_color_border_0) + """;
            border-right:12px solid rgb""" + str(object_color_border_0) + """;
            border-top:12px solid rgb""" + str(object_color_border_0) + """;
            border-left:12px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)
        try:
            btnx_var[31].clicked.disconnect()
        except:
            pass
        btnx_var[31].clicked.connect(self.select_pre_trained_model_file)
        btnx_var[31].show()

        # Train from pre-trained model
        if _train_from_pretrained_model is True:
            btnx_double_var[46].setText('Pre-Trained (On)')
        elif _train_from_pretrained_model is False:
            btnx_double_var[46].setText('Pre-Trained (Off)')
        btnx_double_var[46].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            """)
        try:
            btnx_double_var[46].clicked.disconnect()
        except:
            pass
        btnx_double_var[46].clicked.connect(self.train_from_pre_trained_model)
        btnx_double_var[46].show()

        # Batch size
        lblx_var[62].setAlignment(QtCore.Qt.AlignCenter)
        lblx_var[62].setText('Batch Size')
        lblx_var[62].resize(int(btnx_size * 2) + btnx_sp_size, int(btnx_size))
        lblx_var[62].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            """)
        lblx_var[62].show()

        qlex_double_var[78].setText(str(_batch_size))
        qlex_double_var[78].resize((btnx_size * 2 ) + btnx_sp_size, btnx_size)
        qlex_double_var[78].setAlignment(QtCore.Qt.AlignCenter)
        # qlex_double_var[78].setAlignment(QtCore.Qt.AlignVCenter)
        qlex_double_var[78].setStyleSheet("""QLineEdit{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            """)
        qlex_double_var[78].show()

        # Number of experiments
        lblx_var[94].setAlignment(QtCore.Qt.AlignVCenter)
        lblx_var[94].setText('Experiments Num')
        lblx_var[94].setStyleSheet("""QLabel{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            """)
        lblx_var[94].show()

        qlex_double_var[110].setText(str(_num_experiments))
        qlex_double_var[110].resize((btnx_size * 2 )+ btnx_sp_size, btnx_size)
        qlex_double_var[110].setAlignment(QtCore.Qt.AlignCenter)
        # qlex_double_var[110].setAlignment(QtCore.Qt.AlignVCenter)
        qlex_double_var[110].setStyleSheet("""QLineEdit{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            """)
        qlex_double_var[110].show()

        # Fill right panel empty space
        try:
            btnx_double_var[126].clicked.disconnect()
        except:
            pass
        btnx_double_var[126].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            }""")
        btnx_double_var[126].setText('')
        btnx_double_var[126].show()

        # Start training
        btnx_double_var[128].setText('Train')
        btnx_double_var[128].resize((btnx_size * 16) + btnx_sp_size * 15, btnx_size)
        btnx_double_var[128].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:2px solid rgb""" + str(object_color_border_0) + """;
            border-right:2px solid rgb""" + str(object_color_border_0) + """;
            border-top:2px solid rgb""" + str(object_color_border_0) + """;
            border-left:2px solid rgb""" + str(object_color_border_0) + """;}
            """)
        try:
            btnx_double_var[128].clicked.disconnect()
        except:
            pass
        btnx_double_var[128].clicked.connect(self.start_training)
        btnx_double_var[128].show()

    @QtCore.pyqtSlot()
    def hide_training_mode(self):

        # Main label
        self.set_main_label_1()

        # Remove emphasis from tab
        btnx_double_var[6].setStyleSheet("""QPushButton{
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:10px solid rgb""" + str(object_color_border_0) + """;
            border-right:20px solid rgb""" + str(object_color_border_0) + """;
            border-top:10px solid rgb""" + str(object_color_border_0) + """;
            border-left:20px solid rgb""" + str(object_color_border_0) + """;}
            }
            QPushButton::hover {background-color: rgb""" + str(object_color_background_0) + """;
            }
            QPushButton::pressed {
            color: rgb""" + str(object_color_0) + """;
            background-color: rgb""" + str(object_color_background_0) + """;
            border-bottom:14px solid rgb""" + str(object_color_border_0) + """;
            border-right:24px solid rgb""" + str(object_color_border_0) + """;
            border-top:14px solid rgb""" + str(object_color_border_0) + """;
            border-left:24px solid rgb""" + str(object_color_border_0) + """;}
            }
            """)

        # Output textbox
        tbx_var[16].hide()

        # Input directory
        btnx_var[30].setText('')
        try:
            btnx_var[30].clicked.disconnect()
        except:
            pass
        btnx_var[30].hide()

        # Select pretrained model
        btnx_var[31].setText('')
        try:
            btnx_var[31].clicked.disconnect()
        except:
            pass
        btnx_var[31].hide()

        # Train from pre-trained model
        btnx_double_var[46].setText('Pre-Trained')
        try:
            btnx_double_var[46].clicked.disconnect()
        except:
            pass
        btnx_double_var[46].hide()

        # Batch size
        lblx_var[62].setText('')
        lblx_var[62].hide()
        qlex_double_var[78].setText('')
        qlex_double_var[78].hide()

        # Number of experiments
        lblx_var[94].setText('')
        lblx_var[94].hide()
        qlex_double_var[110].setText('')
        qlex_double_var[110].hide()

        # Fill right panel empty space
        btnx_double_var[126].hide()

        # Start training
        btnx_double_var[128].setText('')
        btnx_double_var[128].resize((btnx_size * 2) + btnx_sp_size, btnx_size)
        try:
            btnx_double_var[128].clicked.disconnect()
        except:
            pass
        btnx_double_var[128].hide()

    def center(self):
        try:
            qr = self.frameGeometry()
            cp = QDesktopWidget().availableGeometry().center()
            qr.moveCenter(cp)
            self.move(qr.topLeft())
        except:
            pass

    def mousePressEvent(self, event):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        global app_x_range, app_y_range, app_range_xy
        global win_pos_w, win_pos_h
        global prev_click_x, prev_click_y
        global bounding_box
        try:
            self.prev_pos = event.globalPos()
            prev_click_x = event.pos().x()
            prev_click_y = event.pos().y()
            bounding_box = [0, 0, 0, 0]
            self.update()
        except:
            pass

    def paintEvent(self, event):
        global bounding_box, MODE_MANUAL_ANNOTATION, lblx_var
        global win_pos_w, win_pos_h

        try:

            painter = QPainter(self)
            if MODE_MANUAL_ANNOTATION is True:

                # Paints image to be annotated
                if self.pixmap:
                    painter.drawPixmap(int(lblx_var[self.video_label].pos().x()),
                                       int(lblx_var[self.video_label].pos().y()),
                                       self.image_size_w,
                                       self.image_size_h,
                                       self.pixmap)

                    # Create intended user paint area (inside image bounds).
                    if self.area_in_label() is True:
                        br = QBrush(QColor(self.brush_color_r, self.brush_color_g, self.brush_color_b, self.brush_color_a))
                        painter.setBrush(br)
                        # Paint new bounding box
                        painter.drawRect(QtCore.QRect(bounding_box[0] + lblx_var[self.video_label].pos().x(),
                                                      bounding_box[1] + lblx_var[self.video_label].pos().y(),
                                                      (bounding_box[2] - bounding_box[0]),
                                                      (bounding_box[3] - bounding_box[1])))
                # Paint bounding boxes from annotation list
                for annotation in annotations:
                    br = QBrush(QColor(annotation.get('brush_r'), annotation.get('brush_g'),annotation.get('brush_b'),
                                       annotation.get('brush_a')))
                    painter.setBrush(br)
                    painter.drawRect(
                        QtCore.QRect(annotation.get('onscreen_geo')[0] + lblx_var[self.video_label].pos().x(),
                                     annotation.get('onscreen_geo')[1] + lblx_var[self.video_label].pos().y(),
                                     annotation.get('onscreen_geo')[2] - annotation.get('onscreen_geo')[0],
                                     annotation.get('onscreen_geo')[3] - annotation.get('onscreen_geo')[1]))
        except:
            pass

    def mouseMoveEvent(self, event):
        global pin_to_taskbar, titlebar_range_xy
        global MODE_MANUAL_ANNOTATION
        global win_pos_w, win_pos_h
        global prev_click_x, prev_click_y
        global bounding_box, bounding_box2
        global input_files_images, index_input_files_images, auto_iter_object
        try:
            # Application position
            delta = QPoint(event.globalPos() - self.prev_pos)
            if pin_to_taskbar is False:
                # uncomment to only move application when cursor is inside title bar area
                if titlebar_range_xy is True:
                    self.move(self.x() + delta.x(), self.y() + delta.y())
                self.prev_pos = event.globalPos()

            # Following code translates cursor position in application (with resized frame) to actual frame geometry,
            # translation layer: synchronize multiple geometries for seamless front/backend integration.
            if MODE_MANUAL_ANNOTATION is True:
                if os.path.exists(input_files_images[index_input_files_images]):
                    # translation layer: get event positions x/y to use during a translation layer
                    win_pos_w = event.pos().x()
                    win_pos_h = event.pos().y()
                    tmp_xmin = prev_click_x
                    tmp_ymin = prev_click_y
                    tmp_xmax = 0
                    tmp_ymax = 0
                    # translation layer: should be positives
                    if win_pos_w > prev_click_x and win_pos_h > prev_click_y:
                        # print(f'bounding box (xy>): xmin:{prev_click_x} ymin:{prev_click_y} xmax:{win_pos_w + prev_click_x} ymax:{win_pos_h + prev_click_y}')
                        tmp_xmax = win_pos_w
                        tmp_ymax = win_pos_h
                    # translation layer: could be negatives so convert to positives (ex. drag down left)
                    elif win_pos_w < prev_click_x and win_pos_h < prev_click_y:
                        # print(f'bounding box (xy<): xmin:{prev_click_x} ymin:{prev_click_y} xmax:{prev_click_x - abs(win_pos_w - prev_click_x)} ymax:{prev_click_y - abs(win_pos_h - prev_click_y)}')
                        tmp_xmax = prev_click_x - abs(win_pos_w - prev_click_x)
                        tmp_ymax = prev_click_y - abs(win_pos_h - prev_click_y)
                    # translation layer: could be a negative so convert to positive (ex. drag right up)
                    elif win_pos_w > prev_click_x and win_pos_h < prev_click_y:
                        # print(f'bounding box (x> y<): xmin:{prev_click_x} ymin:{prev_click_y} xmax:{win_pos_w + prev_click_x} ymax:{prev_click_y - abs(win_pos_h - prev_click_y)}')
                        tmp_xmax = win_pos_w
                        tmp_ymax = prev_click_y - abs(win_pos_h - prev_click_y)
                    # translation layer: could be a negative so convert to positive (ex. drag left up)
                    elif win_pos_w < prev_click_x and win_pos_h > prev_click_y:
                        # print(f'bounding box (x< y>): xmin:{prev_click_x} ymin:{prev_click_y} xmax:{prev_click_x - abs(win_pos_w - prev_click_x)} ymax:{win_pos_h + prev_click_y}')
                        tmp_xmax = prev_click_x - abs(win_pos_w - prev_click_x)
                        tmp_ymax = win_pos_h
                    # translation layer: adjust geometries according to image position in application
                    tmp_xmin, tmp_xmax, tmp_ymin, tmp_ymax = tmp_xmin-lblx_var[self.video_label].pos().x(),\
                        tmp_xmax-lblx_var[self.video_label].pos().x(), tmp_ymin-lblx_var[self.video_label].pos().y(),\
                        tmp_ymax-lblx_var[self.video_label].pos().y()
                    # translation layer: compliment inversion layers (abs). invert xmin with xmax if xmax less than xmin (eg. drag left past xmin)
                    if tmp_xmax > tmp_xmin:
                        xmin, xmax = tmp_xmin, tmp_xmax
                    else:
                        xmin, xmax = tmp_xmax, tmp_xmin
                    # translation layer: compliment inversion layers (abs). invert ymin with ymax if ymax less than ymin (eg. drag up past ymin)
                    if tmp_ymax > tmp_ymin:
                        ymin, ymax = tmp_ymin, tmp_ymax
                    else:
                        ymin, ymax = tmp_ymax, tmp_ymin
                    # translation layer: keep resulting values
                    bounding_box = [xmin, ymin, xmax, ymax]
                    # translation layer: translate onscreen image geometry x,y to image file geometry x,y
                    if self.pil_img.width > self.image_size_w:
                        new_ratio = self.image_size_w / self.pil_img.width
                        new_xmin = xmin / new_ratio
                        new_xmax = xmax / new_ratio
                    else:
                        new_xmin = xmin
                        new_xmax = xmax
                    if self.pil_img.height > self.image_size_h:
                        new_ratio = self.image_size_h / self.pil_img.height
                        new_ymin = ymin / new_ratio
                        new_ymax = ymax / new_ratio
                    else:
                        new_ymin = ymin
                        new_ymax = ymax
                    bounding_box2 = [round(new_xmin), round(new_ymin), round(new_xmax), round(new_ymax)]
                    print(f'[bounding_box2 (for xml)] : {bounding_box2}')
                    auto_iter_object = False
                    self.update()

        except:
            pass

    def area_in_label(self):
        global bounding_box
        try:
            if bounding_box[0] + lblx_var[self.video_label].pos().x() in range(lblx_var[self.video_label].pos().x(), lblx_var[self.video_label].pos().x() + self.video_label_size_w):
                if bounding_box[1] + lblx_var[self.video_label].pos().y() in range(lblx_var[self.video_label].pos().y(), int(lblx_var[self.video_label].pos().y() + self.video_label_size_h)):
                    if bounding_box[2] + lblx_var[self.video_label].pos().x() in range(lblx_var[self.video_label].pos().x(), lblx_var[self.video_label].pos().x() + self.video_label_size_w):
                        if bounding_box[3] + lblx_var[self.video_label].pos().y() in range(lblx_var[self.video_label].pos().y(), lblx_var[self.video_label].pos().y() + self.video_label_size_h):
                            return True
        except:
            pass

    def mouseReleaseEvent(self, event):
        global bounding_box, MODE_MANUAL_ANNOTATION
        if MODE_MANUAL_ANNOTATION is True:
            self.update()

    def poll_cursor(self):
        global user_mouse_activity
        try:
            pos = QCursor.pos()
            if pos != self.cursor:
                user_mouse_activity = True
                self.cursor = pos
                self.cursorMove.emit(pos)
            elif pos == self.cursor:
                user_mouse_activity = False
            # print(f'pos: {pos}]')
        except:
            pass

    def get_xy_wh(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h

        try:

            # cursor position xy
            cur_pos_x = int(self.cursor.x())
            cur_pos_y = int(self.cursor.y())

            # application position xy
            self_pos_x = int(self.x())
            self_pos_y = int(self.y())

            # application size wh
            app_w = int(app_width_static)
            app_h = int(app_height_static)

            # print(f'app_w: {app_w}]')
            # print(f'app_h: {app_h}]')

        except:
            pass

    def is_cursor_app_range_xy(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        global app_x_range, app_y_range, app_range_xy
        try:

            # get xy wh
            self.get_xy_wh()

            # check x range
            if cur_pos_x > self_pos_x and cur_pos_x < (self_pos_x + app_w):
                app_x_range = True
            else:
                app_x_range = False
                app_range_xy = False

            # check y range
            if cur_pos_y > self_pos_y and cur_pos_y < (self_pos_y + app_h):
                app_y_range = True
            else:
                app_x_range = False
                app_range_xy = False

            # set app range xy
            if app_x_range is True and app_y_range is True:
                app_range_xy = True
            else:
                app_range_xy = False
            # print(f'app_range_xy: {app_range_xy}]')

        except:
            pass

    def is_cursor_title_bar_range_xy(self):
        global app_height_static, app_width_static
        global cur_pos_x, cur_pos_y
        global self_pos_x, self_pos_y
        global app_w, app_h
        global titlebar_range_xy
        self.get_xy_wh()
        try:
            titlebar_range_xy = False
            if cur_pos_x > self_pos_x and cur_pos_x < (self_pos_x + app_w):
                if cur_pos_y > self_pos_y and cur_pos_y < (self_pos_y + titlebar_height):
                    titlebar_range_xy = True
            # print(f'titlebar_range_xy: {titlebar_range_xy}]')
        except:
            pass

    def handle_cursor_move(self):
        global app_x_range, app_y_range, app_range_xy
        try:
            if self.isMinimized() is False:
                self.is_cursor_app_range_xy()
                self.is_cursor_title_bar_range_xy()
        except:
            pass


class Class0(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        print('-- plugged in: Class0')
        global model_type, model_path, model_json_path
        global input_files_videos, index_input_files_videos
        t_start_perf = time.perf_counter()
        t_start_datetime = datetime.datetime.now()
        if input_files_videos[index_input_files_videos]:
            cap = cv2.VideoCapture(input_files_videos[index_input_files_videos])
            total_frames = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
            video_framerate = cap.get(cv2.CAP_PROP_FPS)
            print('')
            print('')
            print('[IMAGE AI] [OBJECT DETECTION - VIDEO]')
            print('')
            print(f'[IN FILE] {input_files_videos[index_input_files_videos]}')
            print(f'[IN FILE FRAMES] {total_frames}')
            print(f'[OUT DIRECTORY] {output_directory_path}')
            print(f'[AI MODEL] {model_type}')
            print(f'[MODEL PATH] {model_path}')
            print(f'[MODEL JSON] {model_json_path}')
            print(f'[VIDEO_FR] {video_framerate}')
            print('')
            try:
                ai_imageai_process_video.entry_point(input_file_path=input_files_videos[index_input_files_videos],
                                                     camera_input=None,
                                                     frames_per_second=frames_per_second,
                                                     frame_detection_interval=frame_detection_interval,
                                                     minimum_percentage_probability=minimum_percentage_probability,
                                                     display_percentage_probability=display_percentage_probability,
                                                     display_object_name=display_object_name,
                                                     display_box=display_box,
                                                     save_detected_video=save_detected_video,
                                                     video_complete_function=video_complete_function,
                                                     extract_detected_objects=extract_detected_objects,
                                                     custom_objects=custom_objects,
                                                     _ai_model=model_type,
                                                     _ai_model_path=model_path,
                                                     _ai_model_json=model_json_path,
                                                     _detection_speed=_detection_speed,
                                                     _dump=_dump,
                                                     _PRIMARY_TARGET=_PRIMARY_TARGET,
                                                     _SECONDARY_TARGET=_SECONDARY_TARGET,
                                                     save_in_class=save_in_class,
                                                     total_frames=total_frames,
                                                     t_start_perf=t_start_perf,
                                                     t_start_datetime=t_start_datetime,
                                                     output_directory_path=output_directory_path,
                                                     _annotate=_annotate,
                                                     start_frame=start_frame)
            except:
                pass

    def stop_thread(self):
        print('-- plugged in: Class0(stop_thread)')
        self.terminate()


class Class1(QThread):
    def __init__(self):
        QThread.__init__(self)

    def run(self):
        print('-- plugged in: Class1')
        global model_type, model_path, model_json_path
        t_start_perf = time.perf_counter()
        t_start_datetime = datetime.datetime.now()
        print('')
        print('')
        print('[IMAGE AI] [OBJECT DETECTION - LIVE FEED]')
        print('')
        print(f'[OUT DIRECTORY] {output_directory_path}')
        print(f'[AI MODEL] {model_type}')
        print(f'[MODEL PATH] {model_path}')
        print(f'[MODEL JSON] {model_json_path}')
        print('')
        ai_imageai_process_live_feed.DUMP = True
        Detection.KILL_LOOP = False
        ai_imageai_process_live_feed.KILL_LOOP = False
        ai_imageai_process_live_feed.COMPLETED = False
        ai_imageai_process_live_feed.entry_point_live_feed(camera_input=camera_input,
                                                           frames_per_second=frames_per_second,
                                                           frame_detection_interval=frame_detection_interval,
                                                           minimum_percentage_probability=minimum_percentage_probability,
                                                           display_percentage_probability=display_percentage_probability,
                                                           display_object_name=display_object_name,
                                                           save_detected_video=save_detected_video,
                                                           per_frame_function=ai_imageai_process_live_feed.entry_point_live_feed,
                                                           video_complete_function=None,
                                                           extract_detected_objects=extract_detected_objects,
                                                           _model_path=model_path,
                                                           _model=model_type,
                                                           _ai_json_path=model_json_path,
                                                           _PRIMARY_TARGET=_PRIMARY_TARGET,
                                                           _SECONDARY_TARGET=_SECONDARY_TARGET,
                                                           save_in_class=save_in_class,
                                                           t_start_perf=t_start_perf,
                                                           t_start_datetime=t_start_datetime,
                                                           output_directory_path=output_directory_path,
                                                           _annotate=_annotate)

    def stop_thread(self):
        print('-- plugged in: Class1(stop_thread)')
        self.terminate()


class Class2(QThread):
    def __init__(self):
        QThread.__init__(self)
        self.xcmd = []

    def compile_object_names_array(self):
        global directory_input_training
        object_names = []
        for d, s, fl in os.walk(directory_input_training+'/train/annotations'):
            for f in fl:
                fp = os.path.join(d, f)
                print(f'scanning: {fp}')
                with open(fp, 'r') as fo:
                    for line in fo:
                        line = line.strip()
                        if line.startswith('<name>'):
                            object_name = line.replace('<name>', '').replace('</name>', '')
                            if object_name not in object_names:
                                object_names.append(object_name)
        return object_names

    def scrollToBottom(self, minVal=None, maxVal=None):
        global tbx_var
        # Additional params 'minVal' and 'maxVal' are declared because
        # rangeChanged signal sends them, but we set it to optional
        # because we may need to call it separately (if you need).
        tbx_var[16].verticalScrollBar().setValue(
            tbx_var[16].verticalScrollBar().maximum()
        )

    def run(self):
        print('-- plugged in: Class2')
        global _batch_size, _num_experiments, _train_from_pretrained_model, _object_names_array
        global directory_input_training, tbx_message_0, tbx_var
        tbx_var[16].append(f'[ {str(datetime.datetime.now())}] Running')
        try:
            if qlex_double_var[78].text().isdigit() and qlex_double_var[110].text().isdigit():
                _batch_size = int(qlex_double_var[78].text())
                _num_experiments = int(qlex_double_var[110].text())
                if _train_from_pretrained_model is True:
                    # cmd = 'python detection_trainer.py ' + directory_input_training + ' ' + str(_batch_size) + ' ' + str(_num_experiments) + ' ' + str(model_path) + ' "' + str(_object_names_array) + '"'
                    cmd = 'detection_trainer.exe ' + directory_input_training + ' ' + str(_batch_size) + ' ' + str(_num_experiments) + ' ' + str(model_path) + ' "' + str(self.compile_object_names_array()) + '"'
                else:
                    # cmd = 'python detection_trainer.py ' + directory_input_training + ' ' + str(_batch_size) + ' ' + str(_num_experiments) + ' "' + str(_object_names_array) + '"'
                    cmd = 'detection_trainer.exe ' + directory_input_training + ' ' + str(_batch_size) + ' ' + str(_num_experiments) + ' "' + str(self.compile_object_names_array()) + '"'
                print(f'command: {cmd}')
                self.xcmd = subprocess.Popen(cmd, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                tbx_var[16].verticalScrollBar().rangeChanged.connect(
                    self.scrollToBottom,
                )
                while True:
                    output = self.xcmd.stdout.readline()
                    if output == '' and self.xcmd.poll() is not None:
                        break
                    if output:
                        stdout = str(output.decode("utf-8").strip())
                        print(stdout)
                        tbx_var[16].append(stdout)
                    else:
                        break
                rc = self.xcmd.poll()
                print('Class2: subprocess ended.')
            else:
                print('-- invalid input: batch size and experiments number must be digits.')
                tbx_var[16].append(f'[ {str(datetime.datetime.now())}] Stopped')
                btnx_double_var[126].setText('Start')
        except:
            print(f'Class2.run: {e}')
            try:
                self.xcmd.terminate()
            except:
                print(f'Class2.run: {e}')

    def stop_thread(self):
        print('-- plugged in: Class2(stop_thread)')
        try:
            tbx_var[16].append(f'[ {str(datetime.datetime.now())}] Stopped')
            self.xcmd.terminate()
        except:
            print(f'Class2.stop_thread: {e}')
        self.terminate()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())

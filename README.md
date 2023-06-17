Detectionator (Object Detection Studio using ImageAI)

-----

Detectionator is an Object Detection Studio for ImageAI, using a highly modified
version of the original ImageAI.

This software is a toolkit for training models annotating/auto-annotating images
from videos/cameras and ultimately detection of objects with target events that
can be triggered upon target detection using YOLOv3 or a custom model.

Detection, auto-annotation, manual annotation, training. Teach it what anything
is, even aliens and UAPs and setup corresponding target events.

-----

Download:

    https://drive.google.com/drive/folders/1wAuqcOAUPCxYI9UWFH4erdGI21U_LVY6?usp=sharing

-----

[ Camera ]

Plug & play object detection and auto annotation from live camera feeds.
Target detection with half a million fully programmable target events for
infinitely specified targets.
Created data-sets can be used for further mannual annotation and training.

-----

[ Video ]

Object detection and auto annotation from video files to create data-sets
that can be used for further mannual annotation and training.

![plot](./Screenshots/Video2.png)

-----

[ Annotation ]

A. Annotate a single image file. (Select a file).

B. Annotate a directory of image files. (Select a directory containing images).

C. Edit existing annotation files in a dataset. (Select a directory containing
annotation & images directories).

If the dataset was created by this software's auto-annotator, then in Annotation
open image directory as the location created during auto-annotation, directory 'auto'.

Existing annotation(s) will be loaded in with the corresponding images and displayed
with bounding boxes. The existing object name(s) can be edited/removed and new objects
can be added too.

Be sure to set the save location (File -> Save Location) to the annotation directory
for the image directory being annotated.

![plot](./Screenshots/Annotate2.png)

Existing auto/previously annotated objects can be renamed or removed entirely and new
objects can be annotated too.

-----

[ Training ]

Ensure dataset directory structure is correct before initiating training. Auto annotation
will not create the training/validation directory for you, only annotation and images
directories which would have to be split approximately 70+% training and 30+% validation.

Ensure datasets are accurate either because a dataset not created by this program is
trusted or because a dataset created by this program has been manually checked/annotated.

Directory containing dataset should be in the following structure:

                     |--------------> annotations
                 train
                 |   |--------------> images
    hololens --->
                 |   |--------------> annotations
                validation
                     |--------------> images
    
    
                     |--------------> annotations
                 train
                 |   |--------------> images
    oculus ----->
                 |   |--------------> annotations
                validation
                     |--------------> images

Train from scratch or train from pre-trained model, select a dataset and hit train.

-----

[ Targets ]

Targets should be specified one per line in the folowing format
    objectname:targetevent:probability:

    person:1:50
    car:2:50

This will run target event 1 if a person is detected with at least a 50% percentage
probability.

Multiple target events can be assigned to a single object names follows:

    person:1:50
    person:2:99
    car:3:50
    car:4:99

This will run target event 1 if a person is detected with at least a 50% percentage
probability AND run target event 2 if percentage probability is equal to or greater
than 99%. (Same for car).

Similiary the same target event can be used across multiple different object names:

    person:1:50
    person:2:99
    car:1:50
    car:2:99

-----

[ Target Events ]

A minimal knowledge of python is required to write a target event.

Target events utilize exec() and compile() so that once this program is itself
compiled, python is not required to create, compile and execute new target events.

A target event can be written in python in an IDE or even a notepad and can do
literally anything you like in python, passively/non-passively to/about the target.

Some modules are included to compliment exec() and comile(), this makes any new
plugin potentially far more powerful and even easier to create for potentially any
event and without needing python installed. (Python included).

Lock onto anything (even newly trained objects) --> triggers target event(s)
(that can do potentially anything).

Included for application functionality:

    import os
    import sys
    import ast
    import time
    import datetime
    import subprocess
    from PIL import Image
    import win32com.client
    import pathlib
    from importlib import reload
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
    
    Included specifically for exec() and compile():
    import asyncbs4
    import aiohttp
    import asyncio
    import aiofiles
    import aiomultiprocess
    import binascii
    import base64
    import bs4
    import brotlicffi
    import cuesdk
    import codecs
    import cmath
    import ctypes
    import Crypto
    import colorama
    import distutils
    import encodings
    import fileinput
    import GPUtil
    import importlib
    import keyboard
    import matplotlib
    import modulefinder
    import mouse
    import PIL
    import magic
    import math
    import multiprocessing
    import psutil
    import patoolib
    import py7zr
    import pywinauto
    import pythoncom
    import re
    import random
    import requests
    import rtlsdr
    import sklearn
    import scipy
    import screeninfo
    import socket
    import string
    import select
    import shutil
    import threading
    import tabulate
    import upnpclient
    import unicodedata
    import winrt
    import win32api
    import win32con
    import win32com
    import win32process
    import win32clipboard

Example event in example.py (does not have to be a .py file, only requires the
file contains functioning python code):

    os.startfile('cmd')

Note that an import was not necessary but can be included.
Limitless and very simple however a plugin can be as advanced & sophisticated as
you like, imagine or require.

-----

[ GUI ]

    FD:  Frame detection interval.
    P:   Minimum percentage probability.
    AF:  Annotation files.
    IF:  Image files.
    DF:  Detection files.
    OB:  Objects.
    UOB: Unique objects.
    TE:  Time elapsed.

    CL: Clear all object annotations for the current image.
    RM: Remove annotation for the currently selected object.

-----

[ Bugs ]

BETA stage however application is mostly stable and will
require crash testing to make more stable by finding issues as
they arise, are found.

-----

[ Versions ]

    Python: 3.7.
    ImageAI: Uses old Imageai backend.
    Plugins: Should be made to be compaitble with Python 3.7.

-----

[ Creator ]

    Written by Benjamin Jack Cullen

    Although this software uses a highly modified and upgraded ImageAI it is
    thanks to ImageAI that this software exists at all and my mods/upgrades are
    simple in comparison and exist only to allow for more functionality in
    specific areas of ImageAI.

    Source code may be available on request however not many things auto-annotate
    and if they do they cost money and i really need money.

-----

[ PayPal ]
    
    benjaminjc173@gmail.com :)

-----
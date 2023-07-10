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

import annotator_video
import ai_imageai_process_live_feed
import ai_imageai_process_video
import application_images
import ai_imageai_process_image
import ai_imageai_training_detection
import ai_imageai_training_prediction

# for exec
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
# import pywinauto
import pythoncom
import re
import random
import requests
# import rtlsdr
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


def multiproc_exec(file):
    try:
        code = open(file).read()
        prog = compile(code, 'program_x', 'exec')
        exec(prog)
    except Exception as e:
        print(f'multiproc_exec: {e}')


def call_exec_on_with_multiprocess(TARGET):
    p1 = multiprocessing.Process(target=multiproc_exec, args=(TARGET.get('file'),))
    p1.start()
    return p1

import os
import PyQt5
import PyQt5.QtCore
import datetime
import sol_style
import auto_gen_main_page
import auto_gen_btnx_function
import auto_gen_btnx_double_function
import auto_gen_qle_returnpressed_connect_function
import auto_gen_qle_double_returnpressed_connect_function
import auto_gen_tbx_update_function
import auto_gen_btnx_bool
import auto_gen_btnx_double_bool
import auto_gen_qle_bool
import auto_gen_qle_double_bool

var_btnx = []
var_btnx_double = []
var_lblx = []
var_qlex = []
var_qlex_double = []
var_tbx = []
var_tbx_timer = []
var_btnx_double_timer = []
var_btnx_double_timer_sub = []
var_btnx_timer = []
var_btnx_timer_sub = []
var_self = []

@PyQt5.QtCore.pyqtSlot()
def btnx_double_0_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_0_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_0_0_timer_clicked_function():
    print(btnx_double_0_0_timer_clicked_function)

def btnx_double_0_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_0_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_0_0_bool = False
            print('[btnx_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_0_0_bool) + ']')
            # btnx_double_0_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_0_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_0_0_bool = True
            print('[btnx_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_0_0_bool) + ']')
            # btnx_double_0_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[1].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[1].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_1_0_timer_clicked_function():
    print(btnx_double_1_0_timer_clicked_function)

def btnx_double_1_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_1_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_1_0_bool = False
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_0_bool) + ']')
            # btnx_double_1_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_1_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_1_0_bool = True
            print('[btnx_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_1_0_bool) + ']')
            # btnx_double_1_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[2].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[2].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_2_0_timer_clicked_function():
    print(btnx_double_2_0_timer_clicked_function)

def btnx_double_2_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_2_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_2_0_bool = False
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_0_bool) + ']')
            # btnx_double_2_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_2_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_2_0_bool = True
            print('[btnx_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_2_0_bool) + ']')
            # btnx_double_2_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[3].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[3].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_3_0_timer_clicked_function():
    print(btnx_double_3_0_timer_clicked_function)

def btnx_double_3_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_3_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_3_0_bool = False
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_0_bool) + ']')
            # btnx_double_3_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_3_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_3_0_bool = True
            print('[btnx_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_3_0_bool) + ']')
            # btnx_double_3_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[4].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[4].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_4_0_timer_clicked_function():
    print(btnx_double_4_0_timer_clicked_function)

def btnx_double_4_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_4_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_4_0_bool = False
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_0_bool) + ']')
            # btnx_double_4_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_4_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_4_0_bool = True
            print('[btnx_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_4_0_bool) + ']')
            # btnx_double_4_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[5].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[5].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_5_0_timer_clicked_function():
    print(btnx_double_5_0_timer_clicked_function)

def btnx_double_5_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_5_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_5_0_bool = False
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_0_bool) + ']')
            # btnx_double_5_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_5_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_5_0_bool = True
            print('[btnx_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_5_0_bool) + ']')
            # btnx_double_5_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[6].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[6].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_6_0_timer_clicked_function():
    print(btnx_double_6_0_timer_clicked_function)

def btnx_double_6_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_6_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_6_0_bool = False
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_0_bool) + ']')
            # btnx_double_6_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_6_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_6_0_bool = True
            print('[btnx_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_6_0_bool) + ']')
            # btnx_double_6_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[7].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[7].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_7_0_timer_clicked_function():
    print(btnx_double_7_0_timer_clicked_function)

def btnx_double_7_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_7_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_7_0_bool = False
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_0_bool) + ']')
            # btnx_double_7_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_7_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_7_0_bool = True
            print('[btnx_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_7_0_bool) + ']')
            # btnx_double_7_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[8].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[8].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_8_0_timer_clicked_function():
    print(btnx_double_8_0_timer_clicked_function)

def btnx_double_8_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_8_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_8_0_bool = False
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_0_bool) + ']')
            # btnx_double_8_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_8_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_8_0_bool = True
            print('[btnx_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_8_0_bool) + ']')
            # btnx_double_8_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[9].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[9].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_9_0_timer_clicked_function():
    print(btnx_double_9_0_timer_clicked_function)

def btnx_double_9_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_9_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_9_0_bool = False
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_0_bool) + ']')
            # btnx_double_9_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_9_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_9_0_bool = True
            print('[btnx_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_9_0_bool) + ']')
            # btnx_double_9_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[10].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[10].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_10_0_timer_clicked_function():
    print(btnx_double_10_0_timer_clicked_function)

def btnx_double_10_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_10_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_10_0_bool = False
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_0_bool) + ']')
            # btnx_double_10_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_10_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_10_0_bool = True
            print('[btnx_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_10_0_bool) + ']')
            # btnx_double_10_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[11].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[11].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_11_0_timer_clicked_function():
    print(btnx_double_11_0_timer_clicked_function)

def btnx_double_11_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_11_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_11_0_bool = False
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_0_bool) + ']')
            # btnx_double_11_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_11_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_11_0_bool = True
            print('[btnx_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_11_0_bool) + ']')
            # btnx_double_11_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[12].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[12].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_12_0_timer_clicked_function():
    print(btnx_double_12_0_timer_clicked_function)

def btnx_double_12_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_12_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_12_0_bool = False
            print('[btnx_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_12_0_bool) + ']')
            # btnx_double_12_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_12_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_12_0_bool = True
            print('[btnx_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_12_0_bool) + ']')
            # btnx_double_12_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[13].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[13].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_13_0_timer_clicked_function():
    print(btnx_double_13_0_timer_clicked_function)

def btnx_double_13_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_13_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_13_0_bool = False
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_0_bool) + ']')
            # btnx_double_13_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_13_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_13_0_bool = True
            print('[btnx_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_13_0_bool) + ']')
            # btnx_double_13_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[14].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[14].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_14_0_timer_clicked_function():
    print(btnx_double_14_0_timer_clicked_function)

def btnx_double_14_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_14_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_14_0_bool = False
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_0_bool) + ']')
            # btnx_double_14_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_14_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_14_0_bool = True
            print('[btnx_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_14_0_bool) + ']')
            # btnx_double_14_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[15].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[15].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_15_0_timer_clicked_function():
    print(btnx_double_15_0_timer_clicked_function)

def btnx_double_15_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_15_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_15_0_bool = False
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_0_bool) + ']')
            # btnx_double_15_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_15_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_15_0_bool = True
            print('[btnx_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_15_0_bool) + ']')
            # btnx_double_15_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[16].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[16].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_16_0_timer_clicked_function():
    print(btnx_double_16_0_timer_clicked_function)

def btnx_double_16_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_16_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_16_0_bool = False
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_0_bool) + ']')
            # btnx_double_16_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_16_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_16_0_bool = True
            print('[btnx_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_16_0_bool) + ']')
            # btnx_double_16_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[17].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[17].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_17_0_timer_clicked_function():
    print(btnx_double_17_0_timer_clicked_function)

def btnx_double_17_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_17_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_17_0_bool = False
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_0_bool) + ']')
            # btnx_double_17_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_17_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_17_0_bool = True
            print('[btnx_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_17_0_bool) + ']')
            # btnx_double_17_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[18].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[18].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_18_0_timer_clicked_function():
    print(btnx_double_18_0_timer_clicked_function)

def btnx_double_18_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_18_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_18_0_bool = False
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_0_bool) + ']')
            # btnx_double_18_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_18_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_18_0_bool = True
            print('[btnx_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_18_0_bool) + ']')
            # btnx_double_18_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[19].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[19].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_19_0_timer_clicked_function():
    print(btnx_double_19_0_timer_clicked_function)

def btnx_double_19_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_19_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_19_0_bool = False
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_0_bool) + ']')
            # btnx_double_19_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_19_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_19_0_bool = True
            print('[btnx_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_19_0_bool) + ']')
            # btnx_double_19_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[20].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[20].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_20_0_timer_clicked_function():
    print(btnx_double_20_0_timer_clicked_function)

def btnx_double_20_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_20_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_20_0_bool = False
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_0_bool) + ']')
            # btnx_double_20_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_20_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_20_0_bool = True
            print('[btnx_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_20_0_bool) + ']')
            # btnx_double_20_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[21].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[21].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_21_0_timer_clicked_function():
    print(btnx_double_21_0_timer_clicked_function)

def btnx_double_21_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_21_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_21_0_bool = False
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_0_bool) + ']')
            # btnx_double_21_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_21_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_21_0_bool = True
            print('[btnx_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_21_0_bool) + ']')
            # btnx_double_21_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[22].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[22].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_22_0_timer_clicked_function():
    print(btnx_double_22_0_timer_clicked_function)

def btnx_double_22_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_22_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_22_0_bool = False
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_0_bool) + ']')
            # btnx_double_22_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_22_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_22_0_bool = True
            print('[btnx_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_22_0_bool) + ']')
            # btnx_double_22_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[23].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[23].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_23_0_timer_clicked_function():
    print(btnx_double_23_0_timer_clicked_function)

def btnx_double_23_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_23_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_23_0_bool = False
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_0_bool) + ']')
            # btnx_double_23_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_23_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_23_0_bool = True
            print('[btnx_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_23_0_bool) + ']')
            # btnx_double_23_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[24].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[24].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_24_0_timer_clicked_function():
    print(btnx_double_24_0_timer_clicked_function)

def btnx_double_24_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_24_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_24_0_bool = False
            print('[btnx_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_24_0_bool) + ']')
            # btnx_double_24_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_24_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_24_0_bool = True
            print('[btnx_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_24_0_bool) + ']')
            # btnx_double_24_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[25].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[25].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_25_0_timer_clicked_function():
    print(btnx_double_25_0_timer_clicked_function)

def btnx_double_25_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_25_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_25_0_bool = False
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_0_bool) + ']')
            # btnx_double_25_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_25_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_25_0_bool = True
            print('[btnx_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_25_0_bool) + ']')
            # btnx_double_25_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[26].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[26].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_26_0_timer_clicked_function():
    print(btnx_double_26_0_timer_clicked_function)

def btnx_double_26_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_26_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_26_0_bool = False
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_0_bool) + ']')
            # btnx_double_26_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_26_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_26_0_bool = True
            print('[btnx_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_26_0_bool) + ']')
            # btnx_double_26_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[27].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[27].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_27_0_timer_clicked_function():
    print(btnx_double_27_0_timer_clicked_function)

def btnx_double_27_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_27_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_27_0_bool = False
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_0_bool) + ']')
            # btnx_double_27_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_27_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_27_0_bool = True
            print('[btnx_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_27_0_bool) + ']')
            # btnx_double_27_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[28].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[28].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_28_0_timer_clicked_function():
    print(btnx_double_28_0_timer_clicked_function)

def btnx_double_28_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_28_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_28_0_bool = False
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_0_bool) + ']')
            # btnx_double_28_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_28_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_28_0_bool = True
            print('[btnx_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_28_0_bool) + ']')
            # btnx_double_28_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[29].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[29].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_29_0_timer_clicked_function():
    print(btnx_double_29_0_timer_clicked_function)

def btnx_double_29_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_29_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_29_0_bool = False
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_0_bool) + ']')
            # btnx_double_29_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_29_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_29_0_bool = True
            print('[btnx_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_29_0_bool) + ']')
            # btnx_double_29_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[30].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[30].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_30_0_timer_clicked_function():
    print(btnx_double_30_0_timer_clicked_function)

def btnx_double_30_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_30_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_30_0_bool = False
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_0_bool) + ']')
            # btnx_double_30_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_30_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_30_0_bool = True
            print('[btnx_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_30_0_bool) + ']')
            # btnx_double_30_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[31].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[31].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_31_0_timer_clicked_function():
    print(btnx_double_31_0_timer_clicked_function)

def btnx_double_31_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_31_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_31_0_bool = False
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_0_bool) + ']')
            # btnx_double_31_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_31_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_31_0_bool = True
            print('[btnx_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_31_0_bool) + ']')
            # btnx_double_31_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[32].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[32].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_32_0_timer_clicked_function():
    print(btnx_double_32_0_timer_clicked_function)

def btnx_double_32_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_32_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_32_0_bool = False
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_0_bool) + ']')
            # btnx_double_32_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_32_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_32_0_bool = True
            print('[btnx_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_32_0_bool) + ']')
            # btnx_double_32_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[33].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[33].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_33_0_timer_clicked_function():
    print(btnx_double_33_0_timer_clicked_function)

def btnx_double_33_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_33_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_33_0_bool = False
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_0_bool) + ']')
            # btnx_double_33_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_33_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_33_0_bool = True
            print('[btnx_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_33_0_bool) + ']')
            # btnx_double_33_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[34].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[34].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_34_0_timer_clicked_function():
    print(btnx_double_34_0_timer_clicked_function)

def btnx_double_34_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_34_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_34_0_bool = False
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_0_bool) + ']')
            # btnx_double_34_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_34_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_34_0_bool = True
            print('[btnx_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_34_0_bool) + ']')
            # btnx_double_34_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[35].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[35].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_35_0_timer_clicked_function():
    print(btnx_double_35_0_timer_clicked_function)

def btnx_double_35_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_35_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_35_0_bool = False
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_0_bool) + ']')
            # btnx_double_35_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_35_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_35_0_bool = True
            print('[btnx_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_35_0_bool) + ']')
            # btnx_double_35_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[36].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[36].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_36_0_timer_clicked_function():
    print(btnx_double_36_0_timer_clicked_function)

def btnx_double_36_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_36_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_36_0_bool = False
            print('[btnx_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_36_0_bool) + ']')
            # btnx_double_36_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_36_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_36_0_bool = True
            print('[btnx_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_36_0_bool) + ']')
            # btnx_double_36_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[37].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[37].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_37_0_timer_clicked_function():
    print(btnx_double_37_0_timer_clicked_function)

def btnx_double_37_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_37_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_37_0_bool = False
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_0_bool) + ']')
            # btnx_double_37_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_37_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_37_0_bool = True
            print('[btnx_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_37_0_bool) + ']')
            # btnx_double_37_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[38].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[38].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_38_0_timer_clicked_function():
    print(btnx_double_38_0_timer_clicked_function)

def btnx_double_38_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_38_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_38_0_bool = False
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_0_bool) + ']')
            # btnx_double_38_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_38_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_38_0_bool = True
            print('[btnx_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_38_0_bool) + ']')
            # btnx_double_38_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[39].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[39].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_39_0_timer_clicked_function():
    print(btnx_double_39_0_timer_clicked_function)

def btnx_double_39_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_39_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_39_0_bool = False
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_0_bool) + ']')
            # btnx_double_39_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_39_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_39_0_bool = True
            print('[btnx_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_39_0_bool) + ']')
            # btnx_double_39_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[40].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[40].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_40_0_timer_clicked_function():
    print(btnx_double_40_0_timer_clicked_function)

def btnx_double_40_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_40_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_40_0_bool = False
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_0_bool) + ']')
            # btnx_double_40_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_40_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_40_0_bool = True
            print('[btnx_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_40_0_bool) + ']')
            # btnx_double_40_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[41].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[41].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_41_0_timer_clicked_function():
    print(btnx_double_41_0_timer_clicked_function)

def btnx_double_41_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_41_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_41_0_bool = False
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_0_bool) + ']')
            # btnx_double_41_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_41_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_41_0_bool = True
            print('[btnx_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_41_0_bool) + ']')
            # btnx_double_41_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[42].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[42].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_42_0_timer_clicked_function():
    print(btnx_double_42_0_timer_clicked_function)

def btnx_double_42_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_42_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_42_0_bool = False
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_0_bool) + ']')
            # btnx_double_42_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_42_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_42_0_bool = True
            print('[btnx_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_42_0_bool) + ']')
            # btnx_double_42_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[43].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[43].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_43_0_timer_clicked_function():
    print(btnx_double_43_0_timer_clicked_function)

def btnx_double_43_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_43_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_43_0_bool = False
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_0_bool) + ']')
            # btnx_double_43_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_43_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_43_0_bool = True
            print('[btnx_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_43_0_bool) + ']')
            # btnx_double_43_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[44].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[44].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_44_0_timer_clicked_function():
    print(btnx_double_44_0_timer_clicked_function)

def btnx_double_44_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_44_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_44_0_bool = False
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_0_bool) + ']')
            # btnx_double_44_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_44_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_44_0_bool = True
            print('[btnx_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_44_0_bool) + ']')
            # btnx_double_44_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[45].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[45].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_45_0_timer_clicked_function():
    print(btnx_double_45_0_timer_clicked_function)

def btnx_double_45_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_45_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_45_0_bool = False
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_0_bool) + ']')
            # btnx_double_45_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_45_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_45_0_bool = True
            print('[btnx_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_45_0_bool) + ']')
            # btnx_double_45_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[46].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[46].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_46_0_timer_clicked_function():
    print(btnx_double_46_0_timer_clicked_function)

def btnx_double_46_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_46_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_46_0_bool = False
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_0_bool) + ']')
            # btnx_double_46_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_46_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_46_0_bool = True
            print('[btnx_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_46_0_bool) + ']')
            # btnx_double_46_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[47].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[47].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_47_0_timer_clicked_function():
    print(btnx_double_47_0_timer_clicked_function)

def btnx_double_47_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_47_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_47_0_bool = False
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_0_bool) + ']')
            # btnx_double_47_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_47_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_47_0_bool = True
            print('[btnx_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_47_0_bool) + ']')
            # btnx_double_47_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_48_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[48].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_48_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[48].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_48_0_timer_clicked_function():
    print(btnx_double_48_0_timer_clicked_function)

def btnx_double_48_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_48_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_48_0_bool = False
            print('[btnx_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_48_0_bool) + ']')
            # btnx_double_48_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_48_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_48_0_bool = True
            print('[btnx_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_48_0_bool) + ']')
            # btnx_double_48_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[49].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[49].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_49_0_timer_clicked_function():
    print(btnx_double_49_0_timer_clicked_function)

def btnx_double_49_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_49_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_49_0_bool = False
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_0_bool) + ']')
            # btnx_double_49_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_49_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_49_0_bool = True
            print('[btnx_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_49_0_bool) + ']')
            # btnx_double_49_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[50].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[50].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_50_0_timer_clicked_function():
    print(btnx_double_50_0_timer_clicked_function)

def btnx_double_50_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_50_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_50_0_bool = False
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_0_bool) + ']')
            # btnx_double_50_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_50_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_50_0_bool = True
            print('[btnx_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_50_0_bool) + ']')
            # btnx_double_50_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[51].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[51].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_51_0_timer_clicked_function():
    print(btnx_double_51_0_timer_clicked_function)

def btnx_double_51_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_51_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_51_0_bool = False
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_0_bool) + ']')
            # btnx_double_51_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_51_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_51_0_bool = True
            print('[btnx_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_51_0_bool) + ']')
            # btnx_double_51_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[52].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[52].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_52_0_timer_clicked_function():
    print(btnx_double_52_0_timer_clicked_function)

def btnx_double_52_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_52_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_52_0_bool = False
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_0_bool) + ']')
            # btnx_double_52_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_52_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_52_0_bool = True
            print('[btnx_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_52_0_bool) + ']')
            # btnx_double_52_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[53].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[53].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_53_0_timer_clicked_function():
    print(btnx_double_53_0_timer_clicked_function)

def btnx_double_53_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_53_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_53_0_bool = False
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_0_bool) + ']')
            # btnx_double_53_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_53_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_53_0_bool = True
            print('[btnx_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_53_0_bool) + ']')
            # btnx_double_53_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[54].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[54].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_54_0_timer_clicked_function():
    print(btnx_double_54_0_timer_clicked_function)

def btnx_double_54_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_54_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_54_0_bool = False
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_0_bool) + ']')
            # btnx_double_54_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_54_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_54_0_bool = True
            print('[btnx_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_54_0_bool) + ']')
            # btnx_double_54_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[55].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[55].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_55_0_timer_clicked_function():
    print(btnx_double_55_0_timer_clicked_function)

def btnx_double_55_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_55_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_55_0_bool = False
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_0_bool) + ']')
            # btnx_double_55_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_55_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_55_0_bool = True
            print('[btnx_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_55_0_bool) + ']')
            # btnx_double_55_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[56].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[56].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_56_0_timer_clicked_function():
    print(btnx_double_56_0_timer_clicked_function)

def btnx_double_56_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_56_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_56_0_bool = False
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_0_bool) + ']')
            # btnx_double_56_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_56_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_56_0_bool = True
            print('[btnx_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_56_0_bool) + ']')
            # btnx_double_56_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[57].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[57].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_57_0_timer_clicked_function():
    print(btnx_double_57_0_timer_clicked_function)

def btnx_double_57_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_57_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_57_0_bool = False
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_0_bool) + ']')
            # btnx_double_57_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_57_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_57_0_bool = True
            print('[btnx_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_57_0_bool) + ']')
            # btnx_double_57_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[58].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[58].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_58_0_timer_clicked_function():
    print(btnx_double_58_0_timer_clicked_function)

def btnx_double_58_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_58_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_58_0_bool = False
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_0_bool) + ']')
            # btnx_double_58_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_58_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_58_0_bool = True
            print('[btnx_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_58_0_bool) + ']')
            # btnx_double_58_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[59].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[59].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_59_0_timer_clicked_function():
    print(btnx_double_59_0_timer_clicked_function)

def btnx_double_59_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_59_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_59_0_bool = False
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_0_bool) + ']')
            # btnx_double_59_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_59_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_59_0_bool = True
            print('[btnx_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_59_0_bool) + ']')
            # btnx_double_59_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_60_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[60].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_60_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[60].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_60_0_timer_clicked_function():
    print(btnx_double_60_0_timer_clicked_function)

def btnx_double_60_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_60_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_60_0_bool = False
            print('[btnx_double_60] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_60_0_bool) + ']')
            # btnx_double_60_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_60_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_60_0_bool = True
            print('[btnx_double_60] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_60_0_bool) + ']')
            # btnx_double_60_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_61_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[61].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_61_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[61].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_61_0_timer_clicked_function():
    print(btnx_double_61_0_timer_clicked_function)

def btnx_double_61_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_61_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_61_0_bool = False
            print('[btnx_double_61] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_61_0_bool) + ']')
            # btnx_double_61_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_61_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_61_0_bool = True
            print('[btnx_double_61] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_61_0_bool) + ']')
            # btnx_double_61_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_62_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[62].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_62_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[62].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_62_0_timer_clicked_function():
    print(btnx_double_62_0_timer_clicked_function)

def btnx_double_62_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_62_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_62_0_bool = False
            print('[btnx_double_62] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_62_0_bool) + ']')
            # btnx_double_62_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_62_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_62_0_bool = True
            print('[btnx_double_62] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_62_0_bool) + ']')
            # btnx_double_62_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_63_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[63].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_63_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[63].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_63_0_timer_clicked_function():
    print(btnx_double_63_0_timer_clicked_function)

def btnx_double_63_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_63_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_63_0_bool = False
            print('[btnx_double_63] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_63_0_bool) + ']')
            # btnx_double_63_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_63_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_63_0_bool = True
            print('[btnx_double_63] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_63_0_bool) + ']')
            # btnx_double_63_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_64_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[64].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_64_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[64].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_64_0_timer_clicked_function():
    print(btnx_double_64_0_timer_clicked_function)

def btnx_double_64_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_64_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_64_0_bool = False
            print('[btnx_double_64] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_64_0_bool) + ']')
            # btnx_double_64_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_64_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_64_0_bool = True
            print('[btnx_double_64] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_64_0_bool) + ']')
            # btnx_double_64_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_65_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[65].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_65_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[65].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_65_0_timer_clicked_function():
    print(btnx_double_65_0_timer_clicked_function)

def btnx_double_65_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_65_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_65_0_bool = False
            print('[btnx_double_65] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_65_0_bool) + ']')
            # btnx_double_65_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_65_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_65_0_bool = True
            print('[btnx_double_65] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_65_0_bool) + ']')
            # btnx_double_65_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_66_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[66].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_66_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[66].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_66_0_timer_clicked_function():
    print(btnx_double_66_0_timer_clicked_function)

def btnx_double_66_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_66_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_66_0_bool = False
            print('[btnx_double_66] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_66_0_bool) + ']')
            # btnx_double_66_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_66_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_66_0_bool = True
            print('[btnx_double_66] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_66_0_bool) + ']')
            # btnx_double_66_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_67_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[67].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_67_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[67].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_67_0_timer_clicked_function():
    print(btnx_double_67_0_timer_clicked_function)

def btnx_double_67_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_67_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_67_0_bool = False
            print('[btnx_double_67] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_67_0_bool) + ']')
            # btnx_double_67_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_67_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_67_0_bool = True
            print('[btnx_double_67] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_67_0_bool) + ']')
            # btnx_double_67_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_68_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[68].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_68_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[68].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_68_0_timer_clicked_function():
    print(btnx_double_68_0_timer_clicked_function)

def btnx_double_68_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_68_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_68_0_bool = False
            print('[btnx_double_68] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_68_0_bool) + ']')
            # btnx_double_68_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_68_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_68_0_bool = True
            print('[btnx_double_68] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_68_0_bool) + ']')
            # btnx_double_68_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_69_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[69].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_69_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[69].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_69_0_timer_clicked_function():
    print(btnx_double_69_0_timer_clicked_function)

def btnx_double_69_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_69_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_69_0_bool = False
            print('[btnx_double_69] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_69_0_bool) + ']')
            # btnx_double_69_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_69_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_69_0_bool = True
            print('[btnx_double_69] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_69_0_bool) + ']')
            # btnx_double_69_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_70_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[70].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_70_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[70].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_70_0_timer_clicked_function():
    print(btnx_double_70_0_timer_clicked_function)

def btnx_double_70_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_70_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_70_0_bool = False
            print('[btnx_double_70] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_70_0_bool) + ']')
            # btnx_double_70_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_70_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_70_0_bool = True
            print('[btnx_double_70] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_70_0_bool) + ']')
            # btnx_double_70_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_71_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[71].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_71_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[71].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_71_0_timer_clicked_function():
    print(btnx_double_71_0_timer_clicked_function)

def btnx_double_71_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_71_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_71_0_bool = False
            print('[btnx_double_71] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_71_0_bool) + ']')
            # btnx_double_71_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_71_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_71_0_bool = True
            print('[btnx_double_71] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_71_0_bool) + ']')
            # btnx_double_71_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_72_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[72].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_72_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[72].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_72_0_timer_clicked_function():
    print(btnx_double_72_0_timer_clicked_function)

def btnx_double_72_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_72_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_72_0_bool = False
            print('[btnx_double_72] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_72_0_bool) + ']')
            # btnx_double_72_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_72_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_72_0_bool = True
            print('[btnx_double_72] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_72_0_bool) + ']')
            # btnx_double_72_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_73_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[73].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_73_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[73].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_73_0_timer_clicked_function():
    print(btnx_double_73_0_timer_clicked_function)

def btnx_double_73_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_73_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_73_0_bool = False
            print('[btnx_double_73] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_73_0_bool) + ']')
            # btnx_double_73_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_73_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_73_0_bool = True
            print('[btnx_double_73] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_73_0_bool) + ']')
            # btnx_double_73_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_74_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[74].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_74_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[74].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_74_0_timer_clicked_function():
    print(btnx_double_74_0_timer_clicked_function)

def btnx_double_74_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_74_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_74_0_bool = False
            print('[btnx_double_74] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_74_0_bool) + ']')
            # btnx_double_74_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_74_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_74_0_bool = True
            print('[btnx_double_74] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_74_0_bool) + ']')
            # btnx_double_74_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_75_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[75].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_75_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[75].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_75_0_timer_clicked_function():
    print(btnx_double_75_0_timer_clicked_function)

def btnx_double_75_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_75_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_75_0_bool = False
            print('[btnx_double_75] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_75_0_bool) + ']')
            # btnx_double_75_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_75_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_75_0_bool = True
            print('[btnx_double_75] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_75_0_bool) + ']')
            # btnx_double_75_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_76_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[76].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_76_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[76].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_76_0_timer_clicked_function():
    print(btnx_double_76_0_timer_clicked_function)

def btnx_double_76_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_76_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_76_0_bool = False
            print('[btnx_double_76] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_76_0_bool) + ']')
            # btnx_double_76_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_76_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_76_0_bool = True
            print('[btnx_double_76] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_76_0_bool) + ']')
            # btnx_double_76_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_77_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[77].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_77_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[77].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_77_0_timer_clicked_function():
    print(btnx_double_77_0_timer_clicked_function)

def btnx_double_77_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_77_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_77_0_bool = False
            print('[btnx_double_77] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_77_0_bool) + ']')
            # btnx_double_77_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_77_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_77_0_bool = True
            print('[btnx_double_77] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_77_0_bool) + ']')
            # btnx_double_77_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_78_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[78].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_78_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[78].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_78_0_timer_clicked_function():
    print(btnx_double_78_0_timer_clicked_function)

def btnx_double_78_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_78_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_78_0_bool = False
            print('[btnx_double_78] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_78_0_bool) + ']')
            # btnx_double_78_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_78_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_78_0_bool = True
            print('[btnx_double_78] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_78_0_bool) + ']')
            # btnx_double_78_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_79_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[79].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_79_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[79].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_79_0_timer_clicked_function():
    print(btnx_double_79_0_timer_clicked_function)

def btnx_double_79_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_79_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_79_0_bool = False
            print('[btnx_double_79] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_79_0_bool) + ']')
            # btnx_double_79_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_79_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_79_0_bool = True
            print('[btnx_double_79] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_79_0_bool) + ']')
            # btnx_double_79_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_80_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[80].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_80_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[80].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_80_0_timer_clicked_function():
    print(btnx_double_80_0_timer_clicked_function)

def btnx_double_80_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_80_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_80_0_bool = False
            print('[btnx_double_80] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_80_0_bool) + ']')
            # btnx_double_80_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_80_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_80_0_bool = True
            print('[btnx_double_80] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_80_0_bool) + ']')
            # btnx_double_80_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_81_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[81].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_81_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[81].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_81_0_timer_clicked_function():
    print(btnx_double_81_0_timer_clicked_function)

def btnx_double_81_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_81_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_81_0_bool = False
            print('[btnx_double_81] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_81_0_bool) + ']')
            # btnx_double_81_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_81_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_81_0_bool = True
            print('[btnx_double_81] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_81_0_bool) + ']')
            # btnx_double_81_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_82_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[82].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_82_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[82].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_82_0_timer_clicked_function():
    print(btnx_double_82_0_timer_clicked_function)

def btnx_double_82_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_82_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_82_0_bool = False
            print('[btnx_double_82] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_82_0_bool) + ']')
            # btnx_double_82_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_82_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_82_0_bool = True
            print('[btnx_double_82] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_82_0_bool) + ']')
            # btnx_double_82_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_83_start_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_83_stop_timer_function():
    global var_btnx_double_timer
    var_btnx_double_timer[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_83_timer_clicked_function():
    print(btnx_double_83_timer_clicked_function)

def btnx_double_83_function():
    auto_gen_main_page.main_page = 0
    if auto_gen_btnx_double_bool.btnx_double_83_bool is True:
        auto_gen_btnx_double_bool.btnx_double_83_bool = False
        # btnx_double_83_stop_timer_function()
    elif auto_gen_btnx_double_bool.btnx_double_83_bool is False:
        auto_gen_btnx_double_bool.btnx_double_83_bool = True
        # btnx_double_83_start_timer_function()
    print('[btnx_double_83] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_83_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_double_84_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[83].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_84_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[83].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_84_0_timer_clicked_function():
    print(btnx_double_84_0_timer_clicked_function)

def btnx_double_84_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_84_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_84_0_bool = False
            print('[btnx_double_84] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_84_0_bool) + ']')
            # btnx_double_84_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_84_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_84_0_bool = True
            print('[btnx_double_84] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_84_0_bool) + ']')
            # btnx_double_84_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_85_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[84].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_85_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[84].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_85_0_timer_clicked_function():
    print(btnx_double_85_0_timer_clicked_function)

def btnx_double_85_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_85_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_85_0_bool = False
            print('[btnx_double_85] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_85_0_bool) + ']')
            # btnx_double_85_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_85_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_85_0_bool = True
            print('[btnx_double_85] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_85_0_bool) + ']')
            # btnx_double_85_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_86_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[85].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_86_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[85].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_86_0_timer_clicked_function():
    print(btnx_double_86_0_timer_clicked_function)

def btnx_double_86_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_86_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_86_0_bool = False
            print('[btnx_double_86] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_86_0_bool) + ']')
            # btnx_double_86_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_86_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_86_0_bool = True
            print('[btnx_double_86] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_86_0_bool) + ']')
            # btnx_double_86_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_87_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[86].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_87_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[86].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_87_0_timer_clicked_function():
    print(btnx_double_87_0_timer_clicked_function)

def btnx_double_87_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_87_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_87_0_bool = False
            print('[btnx_double_87] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_87_0_bool) + ']')
            # btnx_double_87_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_87_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_87_0_bool = True
            print('[btnx_double_87] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_87_0_bool) + ']')
            # btnx_double_87_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_88_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[87].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_88_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[87].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_88_0_timer_clicked_function():
    print(btnx_double_88_0_timer_clicked_function)

def btnx_double_88_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_88_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_88_0_bool = False
            print('[btnx_double_88] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_88_0_bool) + ']')
            # btnx_double_88_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_88_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_88_0_bool = True
            print('[btnx_double_88] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_88_0_bool) + ']')
            # btnx_double_88_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_89_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[88].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_89_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[88].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_89_0_timer_clicked_function():
    print(btnx_double_89_0_timer_clicked_function)

def btnx_double_89_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_89_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_89_0_bool = False
            print('[btnx_double_89] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_89_0_bool) + ']')
            # btnx_double_89_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_89_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_89_0_bool = True
            print('[btnx_double_89] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_89_0_bool) + ']')
            # btnx_double_89_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_90_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[89].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_90_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[89].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_90_0_timer_clicked_function():
    print(btnx_double_90_0_timer_clicked_function)

def btnx_double_90_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_90_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_90_0_bool = False
            print('[btnx_double_90] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_90_0_bool) + ']')
            # btnx_double_90_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_90_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_90_0_bool = True
            print('[btnx_double_90] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_90_0_bool) + ']')
            # btnx_double_90_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_91_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[90].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_91_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[90].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_91_0_timer_clicked_function():
    print(btnx_double_91_0_timer_clicked_function)

def btnx_double_91_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_91_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_91_0_bool = False
            print('[btnx_double_91] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_91_0_bool) + ']')
            # btnx_double_91_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_91_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_91_0_bool = True
            print('[btnx_double_91] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_91_0_bool) + ']')
            # btnx_double_91_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_92_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[91].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_92_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[91].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_92_0_timer_clicked_function():
    print(btnx_double_92_0_timer_clicked_function)

def btnx_double_92_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_92_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_92_0_bool = False
            print('[btnx_double_92] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_92_0_bool) + ']')
            # btnx_double_92_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_92_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_92_0_bool = True
            print('[btnx_double_92] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_92_0_bool) + ']')
            # btnx_double_92_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_93_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[92].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_93_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[92].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_93_0_timer_clicked_function():
    print(btnx_double_93_0_timer_clicked_function)

def btnx_double_93_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_93_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_93_0_bool = False
            print('[btnx_double_93] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_93_0_bool) + ']')
            # btnx_double_93_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_93_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_93_0_bool = True
            print('[btnx_double_93] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_93_0_bool) + ']')
            # btnx_double_93_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_94_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[93].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_94_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[93].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_94_0_timer_clicked_function():
    print(btnx_double_94_0_timer_clicked_function)

def btnx_double_94_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_94_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_94_0_bool = False
            print('[btnx_double_94] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_94_0_bool) + ']')
            # btnx_double_94_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_94_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_94_0_bool = True
            print('[btnx_double_94] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_94_0_bool) + ']')
            # btnx_double_94_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_95_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[94].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_95_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[94].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_95_0_timer_clicked_function():
    print(btnx_double_95_0_timer_clicked_function)

def btnx_double_95_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_95_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_95_0_bool = False
            print('[btnx_double_95] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_95_0_bool) + ']')
            # btnx_double_95_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_95_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_95_0_bool = True
            print('[btnx_double_95] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_95_0_bool) + ']')
            # btnx_double_95_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_96_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[95].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_96_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[95].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_96_0_timer_clicked_function():
    print(btnx_double_96_0_timer_clicked_function)

def btnx_double_96_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_96_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_96_0_bool = False
            print('[btnx_double_96] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_96_0_bool) + ']')
            # btnx_double_96_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_96_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_96_0_bool = True
            print('[btnx_double_96] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_96_0_bool) + ']')
            # btnx_double_96_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_97_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[96].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_97_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[96].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_97_0_timer_clicked_function():
    print(btnx_double_97_0_timer_clicked_function)

def btnx_double_97_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_97_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_97_0_bool = False
            print('[btnx_double_97] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_97_0_bool) + ']')
            # btnx_double_97_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_97_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_97_0_bool = True
            print('[btnx_double_97] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_97_0_bool) + ']')
            # btnx_double_97_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_98_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[97].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_98_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[97].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_98_0_timer_clicked_function():
    print(btnx_double_98_0_timer_clicked_function)

def btnx_double_98_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_98_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_98_0_bool = False
            print('[btnx_double_98] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_98_0_bool) + ']')
            # btnx_double_98_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_98_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_98_0_bool = True
            print('[btnx_double_98] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_98_0_bool) + ']')
            # btnx_double_98_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_99_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[98].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_99_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[98].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_99_0_timer_clicked_function():
    print(btnx_double_99_0_timer_clicked_function)

def btnx_double_99_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_99_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_99_0_bool = False
            print('[btnx_double_99] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_99_0_bool) + ']')
            # btnx_double_99_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_99_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_99_0_bool = True
            print('[btnx_double_99] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_99_0_bool) + ']')
            # btnx_double_99_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_100_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[99].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_100_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[99].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_100_0_timer_clicked_function():
    print(btnx_double_100_0_timer_clicked_function)

def btnx_double_100_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_100_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_100_0_bool = False
            print('[btnx_double_100] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_100_0_bool) + ']')
            # btnx_double_100_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_100_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_100_0_bool = True
            print('[btnx_double_100] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_100_0_bool) + ']')
            # btnx_double_100_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_101_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[100].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_101_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[100].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_101_0_timer_clicked_function():
    print(btnx_double_101_0_timer_clicked_function)

def btnx_double_101_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_101_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_101_0_bool = False
            print('[btnx_double_101] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_101_0_bool) + ']')
            # btnx_double_101_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_101_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_101_0_bool = True
            print('[btnx_double_101] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_101_0_bool) + ']')
            # btnx_double_101_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_102_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[101].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_102_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[101].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_102_0_timer_clicked_function():
    print(btnx_double_102_0_timer_clicked_function)

def btnx_double_102_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_102_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_102_0_bool = False
            print('[btnx_double_102] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_102_0_bool) + ']')
            # btnx_double_102_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_102_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_102_0_bool = True
            print('[btnx_double_102] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_102_0_bool) + ']')
            # btnx_double_102_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_103_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[102].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_103_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[102].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_103_0_timer_clicked_function():
    print(btnx_double_103_0_timer_clicked_function)

def btnx_double_103_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_103_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_103_0_bool = False
            print('[btnx_double_103] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_103_0_bool) + ']')
            # btnx_double_103_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_103_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_103_0_bool = True
            print('[btnx_double_103] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_103_0_bool) + ']')
            # btnx_double_103_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_104_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[103].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_104_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[103].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_104_0_timer_clicked_function():
    print(btnx_double_104_0_timer_clicked_function)

def btnx_double_104_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_104_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_104_0_bool = False
            print('[btnx_double_104] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_104_0_bool) + ']')
            # btnx_double_104_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_104_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_104_0_bool = True
            print('[btnx_double_104] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_104_0_bool) + ']')
            # btnx_double_104_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_105_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[104].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_105_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[104].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_105_0_timer_clicked_function():
    print(btnx_double_105_0_timer_clicked_function)

def btnx_double_105_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_105_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_105_0_bool = False
            print('[btnx_double_105] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_105_0_bool) + ']')
            # btnx_double_105_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_105_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_105_0_bool = True
            print('[btnx_double_105] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_105_0_bool) + ']')
            # btnx_double_105_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_106_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[105].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_106_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[105].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_106_0_timer_clicked_function():
    print(btnx_double_106_0_timer_clicked_function)

def btnx_double_106_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_106_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_106_0_bool = False
            print('[btnx_double_106] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_106_0_bool) + ']')
            # btnx_double_106_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_106_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_106_0_bool = True
            print('[btnx_double_106] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_106_0_bool) + ']')
            # btnx_double_106_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_107_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[106].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_107_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[106].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_107_0_timer_clicked_function():
    print(btnx_double_107_0_timer_clicked_function)

def btnx_double_107_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_107_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_107_0_bool = False
            print('[btnx_double_107] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_107_0_bool) + ']')
            # btnx_double_107_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_107_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_107_0_bool = True
            print('[btnx_double_107] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_107_0_bool) + ']')
            # btnx_double_107_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_108_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[107].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_108_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[107].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_108_0_timer_clicked_function():
    print(btnx_double_108_0_timer_clicked_function)

def btnx_double_108_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_108_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_108_0_bool = False
            print('[btnx_double_108] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_108_0_bool) + ']')
            # btnx_double_108_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_108_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_108_0_bool = True
            print('[btnx_double_108] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_108_0_bool) + ']')
            # btnx_double_108_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_109_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[108].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_109_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[108].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_109_0_timer_clicked_function():
    print(btnx_double_109_0_timer_clicked_function)

def btnx_double_109_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_109_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_109_0_bool = False
            print('[btnx_double_109] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_109_0_bool) + ']')
            # btnx_double_109_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_109_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_109_0_bool = True
            print('[btnx_double_109] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_109_0_bool) + ']')
            # btnx_double_109_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_110_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[109].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_110_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[109].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_110_0_timer_clicked_function():
    print(btnx_double_110_0_timer_clicked_function)

def btnx_double_110_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_110_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_110_0_bool = False
            print('[btnx_double_110] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_110_0_bool) + ']')
            # btnx_double_110_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_110_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_110_0_bool = True
            print('[btnx_double_110] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_110_0_bool) + ']')
            # btnx_double_110_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_111_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[110].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_111_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[110].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_111_0_timer_clicked_function():
    print(btnx_double_111_0_timer_clicked_function)

def btnx_double_111_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_111_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_111_0_bool = False
            print('[btnx_double_111] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_111_0_bool) + ']')
            # btnx_double_111_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_111_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_111_0_bool = True
            print('[btnx_double_111] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_111_0_bool) + ']')
            # btnx_double_111_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_112_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[111].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_112_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[111].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_112_0_timer_clicked_function():
    print(btnx_double_112_0_timer_clicked_function)

def btnx_double_112_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_112_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_112_0_bool = False
            print('[btnx_double_112] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_112_0_bool) + ']')
            # btnx_double_112_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_112_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_112_0_bool = True
            print('[btnx_double_112] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_112_0_bool) + ']')
            # btnx_double_112_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_113_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[112].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_113_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[112].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_113_0_timer_clicked_function():
    print(btnx_double_113_0_timer_clicked_function)

def btnx_double_113_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_113_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_113_0_bool = False
            print('[btnx_double_113] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_113_0_bool) + ']')
            # btnx_double_113_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_113_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_113_0_bool = True
            print('[btnx_double_113] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_113_0_bool) + ']')
            # btnx_double_113_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_114_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[113].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_114_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[113].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_114_0_timer_clicked_function():
    print(btnx_double_114_0_timer_clicked_function)

def btnx_double_114_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_114_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_114_0_bool = False
            print('[btnx_double_114] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_114_0_bool) + ']')
            # btnx_double_114_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_114_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_114_0_bool = True
            print('[btnx_double_114] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_114_0_bool) + ']')
            # btnx_double_114_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_115_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[114].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_115_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[114].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_115_0_timer_clicked_function():
    print(btnx_double_115_0_timer_clicked_function)

def btnx_double_115_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_115_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_115_0_bool = False
            print('[btnx_double_115] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_115_0_bool) + ']')
            # btnx_double_115_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_115_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_115_0_bool = True
            print('[btnx_double_115] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_115_0_bool) + ']')
            # btnx_double_115_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_116_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[115].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_116_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[115].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_116_0_timer_clicked_function():
    print(btnx_double_116_0_timer_clicked_function)

def btnx_double_116_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_116_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_116_0_bool = False
            print('[btnx_double_116] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_116_0_bool) + ']')
            # btnx_double_116_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_116_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_116_0_bool = True
            print('[btnx_double_116] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_116_0_bool) + ']')
            # btnx_double_116_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_117_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[116].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_117_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[116].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_117_0_timer_clicked_function():
    print(btnx_double_117_0_timer_clicked_function)

def btnx_double_117_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_117_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_117_0_bool = False
            print('[btnx_double_117] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_117_0_bool) + ']')
            # btnx_double_117_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_117_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_117_0_bool = True
            print('[btnx_double_117] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_117_0_bool) + ']')
            # btnx_double_117_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_118_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[117].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_118_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[117].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_118_0_timer_clicked_function():
    print(btnx_double_118_0_timer_clicked_function)

def btnx_double_118_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_118_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_118_0_bool = False
            print('[btnx_double_118] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_118_0_bool) + ']')
            # btnx_double_118_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_118_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_118_0_bool = True
            print('[btnx_double_118] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_118_0_bool) + ']')
            # btnx_double_118_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_119_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[118].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_119_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[118].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_119_0_timer_clicked_function():
    print(btnx_double_119_0_timer_clicked_function)

def btnx_double_119_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_119_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_119_0_bool = False
            print('[btnx_double_119] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_119_0_bool) + ']')
            # btnx_double_119_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_119_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_119_0_bool = True
            print('[btnx_double_119] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_119_0_bool) + ']')
            # btnx_double_119_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_120_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[119].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_120_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[119].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_120_0_timer_clicked_function():
    print(btnx_double_120_0_timer_clicked_function)

def btnx_double_120_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_120_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_120_0_bool = False
            print('[btnx_double_120] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_120_0_bool) + ']')
            # btnx_double_120_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_120_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_120_0_bool = True
            print('[btnx_double_120] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_120_0_bool) + ']')
            # btnx_double_120_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_121_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[120].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_121_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[120].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_121_0_timer_clicked_function():
    print(btnx_double_121_0_timer_clicked_function)

def btnx_double_121_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_121_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_121_0_bool = False
            print('[btnx_double_121] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_121_0_bool) + ']')
            # btnx_double_121_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_121_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_121_0_bool = True
            print('[btnx_double_121] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_121_0_bool) + ']')
            # btnx_double_121_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_122_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[121].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_122_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[121].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_122_0_timer_clicked_function():
    print(btnx_double_122_0_timer_clicked_function)

def btnx_double_122_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_122_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_122_0_bool = False
            print('[btnx_double_122] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_122_0_bool) + ']')
            # btnx_double_122_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_122_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_122_0_bool = True
            print('[btnx_double_122] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_122_0_bool) + ']')
            # btnx_double_122_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_123_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[122].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_123_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[122].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_123_0_timer_clicked_function():
    print(btnx_double_123_0_timer_clicked_function)

def btnx_double_123_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_123_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_123_0_bool = False
            print('[btnx_double_123] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_123_0_bool) + ']')
            # btnx_double_123_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_123_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_123_0_bool = True
            print('[btnx_double_123] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_123_0_bool) + ']')
            # btnx_double_123_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_124_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[123].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_124_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[123].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_124_0_timer_clicked_function():
    print(btnx_double_124_0_timer_clicked_function)

def btnx_double_124_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_124_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_124_0_bool = False
            print('[btnx_double_124] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_124_0_bool) + ']')
            # btnx_double_124_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_124_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_124_0_bool = True
            print('[btnx_double_124] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_124_0_bool) + ']')
            # btnx_double_124_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_125_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[124].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_125_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[124].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_125_0_timer_clicked_function():
    print(btnx_double_125_0_timer_clicked_function)

def btnx_double_125_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_125_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_125_0_bool = False
            print('[btnx_double_125] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_125_0_bool) + ']')
            # btnx_double_125_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_125_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_125_0_bool = True
            print('[btnx_double_125] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_125_0_bool) + ']')
            # btnx_double_125_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_126_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[125].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_126_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[125].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_126_0_timer_clicked_function():
    print(btnx_double_126_0_timer_clicked_function)

def btnx_double_126_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_126_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_126_0_bool = False
            print('[btnx_double_126] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_126_0_bool) + ']')
            # btnx_double_126_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_126_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_126_0_bool = True
            print('[btnx_double_126] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_126_0_bool) + ']')
            # btnx_double_126_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_127_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[126].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_127_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[126].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_127_0_timer_clicked_function():
    print(btnx_double_127_0_timer_clicked_function)

def btnx_double_127_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_127_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_127_0_bool = False
            print('[btnx_double_127] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_127_0_bool) + ']')
            # btnx_double_127_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_127_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_127_0_bool = True
            print('[btnx_double_127] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_127_0_bool) + ']')
            # btnx_double_127_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_128_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[127].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_128_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[127].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_128_0_timer_clicked_function():
    print(btnx_double_128_0_timer_clicked_function)

def btnx_double_128_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_128_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_128_0_bool = False
            print('[btnx_double_128] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_128_0_bool) + ']')
            # btnx_double_128_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_128_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_128_0_bool = True
            print('[btnx_double_128] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_128_0_bool) + ']')
            # btnx_double_128_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_129_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[128].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_129_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[128].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_129_0_timer_clicked_function():
    print(btnx_double_129_0_timer_clicked_function)

def btnx_double_129_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_129_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_129_0_bool = False
            print('[btnx_double_129] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_129_0_bool) + ']')
            # btnx_double_129_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_129_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_129_0_bool = True
            print('[btnx_double_129] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_129_0_bool) + ']')
            # btnx_double_129_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_130_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[129].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_130_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[129].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_130_0_timer_clicked_function():
    print(btnx_double_130_0_timer_clicked_function)

def btnx_double_130_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_130_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_130_0_bool = False
            print('[btnx_double_130] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_130_0_bool) + ']')
            # btnx_double_130_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_130_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_130_0_bool = True
            print('[btnx_double_130] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_130_0_bool) + ']')
            # btnx_double_130_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_131_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[130].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_131_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[130].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_131_0_timer_clicked_function():
    print(btnx_double_131_0_timer_clicked_function)

def btnx_double_131_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_131_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_131_0_bool = False
            print('[btnx_double_131] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_131_0_bool) + ']')
            # btnx_double_131_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_131_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_131_0_bool = True
            print('[btnx_double_131] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_131_0_bool) + ']')
            # btnx_double_131_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_132_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[131].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_132_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[131].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_132_0_timer_clicked_function():
    print(btnx_double_132_0_timer_clicked_function)

def btnx_double_132_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_132_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_132_0_bool = False
            print('[btnx_double_132] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_132_0_bool) + ']')
            # btnx_double_132_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_132_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_132_0_bool = True
            print('[btnx_double_132] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_132_0_bool) + ']')
            # btnx_double_132_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_133_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[132].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_133_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[132].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_133_0_timer_clicked_function():
    print(btnx_double_133_0_timer_clicked_function)

def btnx_double_133_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_133_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_133_0_bool = False
            print('[btnx_double_133] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_133_0_bool) + ']')
            # btnx_double_133_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_133_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_133_0_bool = True
            print('[btnx_double_133] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_133_0_bool) + ']')
            # btnx_double_133_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_134_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[133].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_134_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[133].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_134_0_timer_clicked_function():
    print(btnx_double_134_0_timer_clicked_function)

def btnx_double_134_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_134_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_134_0_bool = False
            print('[btnx_double_134] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_134_0_bool) + ']')
            # btnx_double_134_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_134_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_134_0_bool = True
            print('[btnx_double_134] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_134_0_bool) + ']')
            # btnx_double_134_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_135_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[134].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_135_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[134].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_135_0_timer_clicked_function():
    print(btnx_double_135_0_timer_clicked_function)

def btnx_double_135_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_135_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_135_0_bool = False
            print('[btnx_double_135] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_135_0_bool) + ']')
            # btnx_double_135_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_135_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_135_0_bool = True
            print('[btnx_double_135] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_135_0_bool) + ']')
            # btnx_double_135_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_136_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[135].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_136_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[135].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_136_0_timer_clicked_function():
    print(btnx_double_136_0_timer_clicked_function)

def btnx_double_136_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_136_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_136_0_bool = False
            print('[btnx_double_136] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_136_0_bool) + ']')
            # btnx_double_136_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_136_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_136_0_bool = True
            print('[btnx_double_136] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_136_0_bool) + ']')
            # btnx_double_136_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_137_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[136].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_137_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[136].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_137_0_timer_clicked_function():
    print(btnx_double_137_0_timer_clicked_function)

def btnx_double_137_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_137_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_137_0_bool = False
            print('[btnx_double_137] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_137_0_bool) + ']')
            # btnx_double_137_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_137_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_137_0_bool = True
            print('[btnx_double_137] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_137_0_bool) + ']')
            # btnx_double_137_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_138_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[137].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_138_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[137].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_138_0_timer_clicked_function():
    print(btnx_double_138_0_timer_clicked_function)

def btnx_double_138_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_138_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_138_0_bool = False
            print('[btnx_double_138] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_138_0_bool) + ']')
            # btnx_double_138_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_138_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_138_0_bool = True
            print('[btnx_double_138] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_138_0_bool) + ']')
            # btnx_double_138_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_139_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[138].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_139_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[138].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_139_0_timer_clicked_function():
    print(btnx_double_139_0_timer_clicked_function)

def btnx_double_139_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_139_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_139_0_bool = False
            print('[btnx_double_139] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_139_0_bool) + ']')
            # btnx_double_139_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_139_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_139_0_bool = True
            print('[btnx_double_139] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_139_0_bool) + ']')
            # btnx_double_139_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_140_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[139].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_140_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[139].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_140_0_timer_clicked_function():
    print(btnx_double_140_0_timer_clicked_function)

def btnx_double_140_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_140_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_140_0_bool = False
            print('[btnx_double_140] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_140_0_bool) + ']')
            # btnx_double_140_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_140_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_140_0_bool = True
            print('[btnx_double_140] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_140_0_bool) + ']')
            # btnx_double_140_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_141_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[140].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_141_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[140].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_141_0_timer_clicked_function():
    print(btnx_double_141_0_timer_clicked_function)

def btnx_double_141_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_141_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_141_0_bool = False
            print('[btnx_double_141] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_141_0_bool) + ']')
            # btnx_double_141_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_141_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_141_0_bool = True
            print('[btnx_double_141] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_141_0_bool) + ']')
            # btnx_double_141_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_142_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[141].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_142_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[141].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_142_0_timer_clicked_function():
    print(btnx_double_142_0_timer_clicked_function)

def btnx_double_142_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_142_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_142_0_bool = False
            print('[btnx_double_142] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_142_0_bool) + ']')
            # btnx_double_142_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_142_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_142_0_bool = True
            print('[btnx_double_142] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_142_0_bool) + ']')
            # btnx_double_142_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_143_0_start_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[142].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_143_0_stop_timer_function():
    global var_btnx_double_timer_sub
    var_btnx_double_timer_sub[142].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_double_143_0_timer_clicked_function():
    print(btnx_double_143_0_timer_clicked_function)

def btnx_double_143_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_double_bool.btnx_double_143_0_bool is True:
            auto_gen_btnx_double_bool.btnx_double_143_0_bool = False
            print('[btnx_double_143] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_143_0_bool) + ']')
            # btnx_double_143_0_stop_timer_function()

        elif auto_gen_btnx_double_bool.btnx_double_143_0_bool is False:
            auto_gen_btnx_double_bool.btnx_double_143_0_bool = True
            print('[btnx_double_143] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_double_bool.btnx_double_143_0_bool) + ']')
            # btnx_double_143_0_start_timer_function()


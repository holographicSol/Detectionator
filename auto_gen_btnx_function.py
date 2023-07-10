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
def btnx_0_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_0_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_0_0_timer_clicked_function():
    print(btnx_0_0_timer_clicked_function)

def btnx_0_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_0_0_bool is True:
            auto_gen_btnx_bool.btnx_0_0_bool = False
            print('[btnx_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_0_0_bool) + ']')
            # btnx_0_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_0_0_bool is False:
            auto_gen_btnx_bool.btnx_0_0_bool = True
            print('[btnx_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_0_0_bool) + ']')
            # btnx_0_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_1_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[1].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_1_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[1].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_1_0_timer_clicked_function():
    print(btnx_1_0_timer_clicked_function)

def btnx_1_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_1_0_bool is True:
            auto_gen_btnx_bool.btnx_1_0_bool = False
            print('[btnx_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_1_0_bool) + ']')
            # btnx_1_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_1_0_bool is False:
            auto_gen_btnx_bool.btnx_1_0_bool = True
            print('[btnx_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_1_0_bool) + ']')
            # btnx_1_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_2_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[2].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_2_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[2].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_2_0_timer_clicked_function():
    print(btnx_2_0_timer_clicked_function)

def btnx_2_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_2_0_bool is True:
            auto_gen_btnx_bool.btnx_2_0_bool = False
            print('[btnx_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_2_0_bool) + ']')
            # btnx_2_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_2_0_bool is False:
            auto_gen_btnx_bool.btnx_2_0_bool = True
            print('[btnx_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_2_0_bool) + ']')
            # btnx_2_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_3_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[3].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_3_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[3].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_3_0_timer_clicked_function():
    print(btnx_3_0_timer_clicked_function)

def btnx_3_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_3_0_bool is True:
            auto_gen_btnx_bool.btnx_3_0_bool = False
            print('[btnx_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_3_0_bool) + ']')
            # btnx_3_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_3_0_bool is False:
            auto_gen_btnx_bool.btnx_3_0_bool = True
            print('[btnx_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_3_0_bool) + ']')
            # btnx_3_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_4_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[4].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_4_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[4].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_4_0_timer_clicked_function():
    print(btnx_4_0_timer_clicked_function)

def btnx_4_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_4_0_bool is True:
            auto_gen_btnx_bool.btnx_4_0_bool = False
            print('[btnx_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_4_0_bool) + ']')
            # btnx_4_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_4_0_bool is False:
            auto_gen_btnx_bool.btnx_4_0_bool = True
            print('[btnx_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_4_0_bool) + ']')
            # btnx_4_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_5_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[5].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_5_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[5].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_5_0_timer_clicked_function():
    print(btnx_5_0_timer_clicked_function)

def btnx_5_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_5_0_bool is True:
            auto_gen_btnx_bool.btnx_5_0_bool = False
            print('[btnx_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_5_0_bool) + ']')
            # btnx_5_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_5_0_bool is False:
            auto_gen_btnx_bool.btnx_5_0_bool = True
            print('[btnx_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_5_0_bool) + ']')
            # btnx_5_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_6_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[6].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_6_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[6].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_6_0_timer_clicked_function():
    print(btnx_6_0_timer_clicked_function)

def btnx_6_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_6_0_bool is True:
            auto_gen_btnx_bool.btnx_6_0_bool = False
            print('[btnx_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_6_0_bool) + ']')
            # btnx_6_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_6_0_bool is False:
            auto_gen_btnx_bool.btnx_6_0_bool = True
            print('[btnx_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_6_0_bool) + ']')
            # btnx_6_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_7_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[7].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_7_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[7].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_7_0_timer_clicked_function():
    print(btnx_7_0_timer_clicked_function)

def btnx_7_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_7_0_bool is True:
            auto_gen_btnx_bool.btnx_7_0_bool = False
            print('[btnx_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_7_0_bool) + ']')
            # btnx_7_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_7_0_bool is False:
            auto_gen_btnx_bool.btnx_7_0_bool = True
            print('[btnx_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_7_0_bool) + ']')
            # btnx_7_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_8_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[8].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_8_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[8].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_8_0_timer_clicked_function():
    print(btnx_8_0_timer_clicked_function)

def btnx_8_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_8_0_bool is True:
            auto_gen_btnx_bool.btnx_8_0_bool = False
            print('[btnx_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_8_0_bool) + ']')
            # btnx_8_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_8_0_bool is False:
            auto_gen_btnx_bool.btnx_8_0_bool = True
            print('[btnx_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_8_0_bool) + ']')
            # btnx_8_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_9_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[9].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_9_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[9].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_9_0_timer_clicked_function():
    print(btnx_9_0_timer_clicked_function)

def btnx_9_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_9_0_bool is True:
            auto_gen_btnx_bool.btnx_9_0_bool = False
            print('[btnx_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_9_0_bool) + ']')
            # btnx_9_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_9_0_bool is False:
            auto_gen_btnx_bool.btnx_9_0_bool = True
            print('[btnx_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_9_0_bool) + ']')
            # btnx_9_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_10_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[10].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_10_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[10].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_10_0_timer_clicked_function():
    print(btnx_10_0_timer_clicked_function)

def btnx_10_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_10_0_bool is True:
            auto_gen_btnx_bool.btnx_10_0_bool = False
            print('[btnx_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_10_0_bool) + ']')
            # btnx_10_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_10_0_bool is False:
            auto_gen_btnx_bool.btnx_10_0_bool = True
            print('[btnx_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_10_0_bool) + ']')
            # btnx_10_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_11_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[11].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_11_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[11].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_11_0_timer_clicked_function():
    print(btnx_11_0_timer_clicked_function)

def btnx_11_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_11_0_bool is True:
            auto_gen_btnx_bool.btnx_11_0_bool = False
            print('[btnx_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_11_0_bool) + ']')
            # btnx_11_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_11_0_bool is False:
            auto_gen_btnx_bool.btnx_11_0_bool = True
            print('[btnx_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_11_0_bool) + ']')
            # btnx_11_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_12_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[12].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_12_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[12].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_12_0_timer_clicked_function():
    print(btnx_12_0_timer_clicked_function)

def btnx_12_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_12_0_bool is True:
            auto_gen_btnx_bool.btnx_12_0_bool = False
            print('[btnx_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_12_0_bool) + ']')
            # btnx_12_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_12_0_bool is False:
            auto_gen_btnx_bool.btnx_12_0_bool = True
            print('[btnx_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_12_0_bool) + ']')
            # btnx_12_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_13_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[13].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_13_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[13].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_13_0_timer_clicked_function():
    print(btnx_13_0_timer_clicked_function)

def btnx_13_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_13_0_bool is True:
            auto_gen_btnx_bool.btnx_13_0_bool = False
            print('[btnx_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_13_0_bool) + ']')
            # btnx_13_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_13_0_bool is False:
            auto_gen_btnx_bool.btnx_13_0_bool = True
            print('[btnx_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_13_0_bool) + ']')
            # btnx_13_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_14_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[14].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_14_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[14].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_14_0_timer_clicked_function():
    print(btnx_14_0_timer_clicked_function)

def btnx_14_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_14_0_bool is True:
            auto_gen_btnx_bool.btnx_14_0_bool = False
            print('[btnx_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_14_0_bool) + ']')
            # btnx_14_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_14_0_bool is False:
            auto_gen_btnx_bool.btnx_14_0_bool = True
            print('[btnx_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_14_0_bool) + ']')
            # btnx_14_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_15_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[15].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_15_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[15].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_15_0_timer_clicked_function():
    print(btnx_15_0_timer_clicked_function)

def btnx_15_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_15_0_bool is True:
            auto_gen_btnx_bool.btnx_15_0_bool = False
            print('[btnx_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_15_0_bool) + ']')
            # btnx_15_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_15_0_bool is False:
            auto_gen_btnx_bool.btnx_15_0_bool = True
            print('[btnx_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_15_0_bool) + ']')
            # btnx_15_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_16_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[16].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_16_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[16].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_16_0_timer_clicked_function():
    print(btnx_16_0_timer_clicked_function)

def btnx_16_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_16_0_bool is True:
            auto_gen_btnx_bool.btnx_16_0_bool = False
            print('[btnx_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_16_0_bool) + ']')
            # btnx_16_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_16_0_bool is False:
            auto_gen_btnx_bool.btnx_16_0_bool = True
            print('[btnx_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_16_0_bool) + ']')
            # btnx_16_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_17_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[17].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_17_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[17].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_17_0_timer_clicked_function():
    print(btnx_17_0_timer_clicked_function)

def btnx_17_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_17_0_bool is True:
            auto_gen_btnx_bool.btnx_17_0_bool = False
            print('[btnx_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_17_0_bool) + ']')
            # btnx_17_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_17_0_bool is False:
            auto_gen_btnx_bool.btnx_17_0_bool = True
            print('[btnx_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_17_0_bool) + ']')
            # btnx_17_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_18_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[18].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_18_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[18].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_18_0_timer_clicked_function():
    print(btnx_18_0_timer_clicked_function)

def btnx_18_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_18_0_bool is True:
            auto_gen_btnx_bool.btnx_18_0_bool = False
            print('[btnx_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_18_0_bool) + ']')
            # btnx_18_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_18_0_bool is False:
            auto_gen_btnx_bool.btnx_18_0_bool = True
            print('[btnx_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_18_0_bool) + ']')
            # btnx_18_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_19_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[19].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_19_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[19].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_19_0_timer_clicked_function():
    print(btnx_19_0_timer_clicked_function)

def btnx_19_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_19_0_bool is True:
            auto_gen_btnx_bool.btnx_19_0_bool = False
            print('[btnx_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_19_0_bool) + ']')
            # btnx_19_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_19_0_bool is False:
            auto_gen_btnx_bool.btnx_19_0_bool = True
            print('[btnx_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_19_0_bool) + ']')
            # btnx_19_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_20_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[20].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_20_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[20].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_20_0_timer_clicked_function():
    print(btnx_20_0_timer_clicked_function)

def btnx_20_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_20_0_bool is True:
            auto_gen_btnx_bool.btnx_20_0_bool = False
            print('[btnx_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_20_0_bool) + ']')
            # btnx_20_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_20_0_bool is False:
            auto_gen_btnx_bool.btnx_20_0_bool = True
            print('[btnx_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_20_0_bool) + ']')
            # btnx_20_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_21_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[21].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_21_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[21].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_21_0_timer_clicked_function():
    print(btnx_21_0_timer_clicked_function)

def btnx_21_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_21_0_bool is True:
            auto_gen_btnx_bool.btnx_21_0_bool = False
            print('[btnx_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_21_0_bool) + ']')
            # btnx_21_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_21_0_bool is False:
            auto_gen_btnx_bool.btnx_21_0_bool = True
            print('[btnx_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_21_0_bool) + ']')
            # btnx_21_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_22_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[22].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_22_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[22].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_22_0_timer_clicked_function():
    print(btnx_22_0_timer_clicked_function)

def btnx_22_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_22_0_bool is True:
            auto_gen_btnx_bool.btnx_22_0_bool = False
            print('[btnx_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_22_0_bool) + ']')
            # btnx_22_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_22_0_bool is False:
            auto_gen_btnx_bool.btnx_22_0_bool = True
            print('[btnx_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_22_0_bool) + ']')
            # btnx_22_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_23_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[23].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_23_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[23].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_23_0_timer_clicked_function():
    print(btnx_23_0_timer_clicked_function)

def btnx_23_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_23_0_bool is True:
            auto_gen_btnx_bool.btnx_23_0_bool = False
            print('[btnx_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_23_0_bool) + ']')
            # btnx_23_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_23_0_bool is False:
            auto_gen_btnx_bool.btnx_23_0_bool = True
            print('[btnx_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_23_0_bool) + ']')
            # btnx_23_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_24_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[24].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_24_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[24].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_24_0_timer_clicked_function():
    print(btnx_24_0_timer_clicked_function)

def btnx_24_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_24_0_bool is True:
            auto_gen_btnx_bool.btnx_24_0_bool = False
            print('[btnx_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_24_0_bool) + ']')
            # btnx_24_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_24_0_bool is False:
            auto_gen_btnx_bool.btnx_24_0_bool = True
            print('[btnx_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_24_0_bool) + ']')
            # btnx_24_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_25_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[25].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_25_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[25].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_25_0_timer_clicked_function():
    print(btnx_25_0_timer_clicked_function)

def btnx_25_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_25_0_bool is True:
            auto_gen_btnx_bool.btnx_25_0_bool = False
            print('[btnx_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_25_0_bool) + ']')
            # btnx_25_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_25_0_bool is False:
            auto_gen_btnx_bool.btnx_25_0_bool = True
            print('[btnx_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_25_0_bool) + ']')
            # btnx_25_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_26_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[26].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_26_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[26].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_26_0_timer_clicked_function():
    print(btnx_26_0_timer_clicked_function)

def btnx_26_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_26_0_bool is True:
            auto_gen_btnx_bool.btnx_26_0_bool = False
            print('[btnx_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_26_0_bool) + ']')
            # btnx_26_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_26_0_bool is False:
            auto_gen_btnx_bool.btnx_26_0_bool = True
            print('[btnx_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_26_0_bool) + ']')
            # btnx_26_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_27_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[27].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_27_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[27].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_27_0_timer_clicked_function():
    print(btnx_27_0_timer_clicked_function)

def btnx_27_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_27_0_bool is True:
            auto_gen_btnx_bool.btnx_27_0_bool = False
            print('[btnx_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_27_0_bool) + ']')
            # btnx_27_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_27_0_bool is False:
            auto_gen_btnx_bool.btnx_27_0_bool = True
            print('[btnx_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_27_0_bool) + ']')
            # btnx_27_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_28_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[28].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_28_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[28].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_28_0_timer_clicked_function():
    print(btnx_28_0_timer_clicked_function)

def btnx_28_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_28_0_bool is True:
            auto_gen_btnx_bool.btnx_28_0_bool = False
            print('[btnx_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_28_0_bool) + ']')
            # btnx_28_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_28_0_bool is False:
            auto_gen_btnx_bool.btnx_28_0_bool = True
            print('[btnx_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_28_0_bool) + ']')
            # btnx_28_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_29_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[29].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_29_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[29].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_29_0_timer_clicked_function():
    print(btnx_29_0_timer_clicked_function)

def btnx_29_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_29_0_bool is True:
            auto_gen_btnx_bool.btnx_29_0_bool = False
            print('[btnx_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_29_0_bool) + ']')
            # btnx_29_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_29_0_bool is False:
            auto_gen_btnx_bool.btnx_29_0_bool = True
            print('[btnx_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_29_0_bool) + ']')
            # btnx_29_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_30_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[30].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_30_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[30].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_30_0_timer_clicked_function():
    print(btnx_30_0_timer_clicked_function)

def btnx_30_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_30_0_bool is True:
            auto_gen_btnx_bool.btnx_30_0_bool = False
            print('[btnx_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_30_0_bool) + ']')
            # btnx_30_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_30_0_bool is False:
            auto_gen_btnx_bool.btnx_30_0_bool = True
            print('[btnx_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_30_0_bool) + ']')
            # btnx_30_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_31_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[31].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_31_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[31].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_31_0_timer_clicked_function():
    print(btnx_31_0_timer_clicked_function)

def btnx_31_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_31_0_bool is True:
            auto_gen_btnx_bool.btnx_31_0_bool = False
            print('[btnx_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_31_0_bool) + ']')
            # btnx_31_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_31_0_bool is False:
            auto_gen_btnx_bool.btnx_31_0_bool = True
            print('[btnx_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_31_0_bool) + ']')
            # btnx_31_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_32_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[32].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_32_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[32].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_32_0_timer_clicked_function():
    print(btnx_32_0_timer_clicked_function)

def btnx_32_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_32_0_bool is True:
            auto_gen_btnx_bool.btnx_32_0_bool = False
            print('[btnx_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_32_0_bool) + ']')
            # btnx_32_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_32_0_bool is False:
            auto_gen_btnx_bool.btnx_32_0_bool = True
            print('[btnx_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_32_0_bool) + ']')
            # btnx_32_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_33_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[33].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_33_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[33].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_33_0_timer_clicked_function():
    print(btnx_33_0_timer_clicked_function)

def btnx_33_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_33_0_bool is True:
            auto_gen_btnx_bool.btnx_33_0_bool = False
            print('[btnx_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_33_0_bool) + ']')
            # btnx_33_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_33_0_bool is False:
            auto_gen_btnx_bool.btnx_33_0_bool = True
            print('[btnx_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_33_0_bool) + ']')
            # btnx_33_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_34_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[34].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_34_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[34].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_34_0_timer_clicked_function():
    print(btnx_34_0_timer_clicked_function)

def btnx_34_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_34_0_bool is True:
            auto_gen_btnx_bool.btnx_34_0_bool = False
            print('[btnx_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_34_0_bool) + ']')
            # btnx_34_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_34_0_bool is False:
            auto_gen_btnx_bool.btnx_34_0_bool = True
            print('[btnx_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_34_0_bool) + ']')
            # btnx_34_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_35_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[35].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_35_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[35].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_35_0_timer_clicked_function():
    print(btnx_35_0_timer_clicked_function)

def btnx_35_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_35_0_bool is True:
            auto_gen_btnx_bool.btnx_35_0_bool = False
            print('[btnx_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_35_0_bool) + ']')
            # btnx_35_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_35_0_bool is False:
            auto_gen_btnx_bool.btnx_35_0_bool = True
            print('[btnx_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_35_0_bool) + ']')
            # btnx_35_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_36_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[36].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_36_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[36].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_36_0_timer_clicked_function():
    print(btnx_36_0_timer_clicked_function)

def btnx_36_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_36_0_bool is True:
            auto_gen_btnx_bool.btnx_36_0_bool = False
            print('[btnx_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_36_0_bool) + ']')
            # btnx_36_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_36_0_bool is False:
            auto_gen_btnx_bool.btnx_36_0_bool = True
            print('[btnx_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_36_0_bool) + ']')
            # btnx_36_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_37_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[37].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_37_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[37].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_37_0_timer_clicked_function():
    print(btnx_37_0_timer_clicked_function)

def btnx_37_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_37_0_bool is True:
            auto_gen_btnx_bool.btnx_37_0_bool = False
            print('[btnx_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_37_0_bool) + ']')
            # btnx_37_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_37_0_bool is False:
            auto_gen_btnx_bool.btnx_37_0_bool = True
            print('[btnx_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_37_0_bool) + ']')
            # btnx_37_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_38_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[38].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_38_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[38].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_38_0_timer_clicked_function():
    print(btnx_38_0_timer_clicked_function)

def btnx_38_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_38_0_bool is True:
            auto_gen_btnx_bool.btnx_38_0_bool = False
            print('[btnx_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_38_0_bool) + ']')
            # btnx_38_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_38_0_bool is False:
            auto_gen_btnx_bool.btnx_38_0_bool = True
            print('[btnx_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_38_0_bool) + ']')
            # btnx_38_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_39_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[39].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_39_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[39].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_39_0_timer_clicked_function():
    print(btnx_39_0_timer_clicked_function)

def btnx_39_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_39_0_bool is True:
            auto_gen_btnx_bool.btnx_39_0_bool = False
            print('[btnx_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_39_0_bool) + ']')
            # btnx_39_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_39_0_bool is False:
            auto_gen_btnx_bool.btnx_39_0_bool = True
            print('[btnx_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_39_0_bool) + ']')
            # btnx_39_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_40_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[40].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_40_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[40].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_40_0_timer_clicked_function():
    print(btnx_40_0_timer_clicked_function)

def btnx_40_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_40_0_bool is True:
            auto_gen_btnx_bool.btnx_40_0_bool = False
            print('[btnx_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_40_0_bool) + ']')
            # btnx_40_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_40_0_bool is False:
            auto_gen_btnx_bool.btnx_40_0_bool = True
            print('[btnx_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_40_0_bool) + ']')
            # btnx_40_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_41_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[41].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_41_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[41].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_41_0_timer_clicked_function():
    print(btnx_41_0_timer_clicked_function)

def btnx_41_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_41_0_bool is True:
            auto_gen_btnx_bool.btnx_41_0_bool = False
            print('[btnx_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_41_0_bool) + ']')
            # btnx_41_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_41_0_bool is False:
            auto_gen_btnx_bool.btnx_41_0_bool = True
            print('[btnx_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_41_0_bool) + ']')
            # btnx_41_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_42_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[42].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_42_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[42].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_42_0_timer_clicked_function():
    print(btnx_42_0_timer_clicked_function)

def btnx_42_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_42_0_bool is True:
            auto_gen_btnx_bool.btnx_42_0_bool = False
            print('[btnx_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_42_0_bool) + ']')
            # btnx_42_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_42_0_bool is False:
            auto_gen_btnx_bool.btnx_42_0_bool = True
            print('[btnx_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_42_0_bool) + ']')
            # btnx_42_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_43_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[43].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_43_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[43].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_43_0_timer_clicked_function():
    print(btnx_43_0_timer_clicked_function)

def btnx_43_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_43_0_bool is True:
            auto_gen_btnx_bool.btnx_43_0_bool = False
            print('[btnx_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_43_0_bool) + ']')
            # btnx_43_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_43_0_bool is False:
            auto_gen_btnx_bool.btnx_43_0_bool = True
            print('[btnx_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_43_0_bool) + ']')
            # btnx_43_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_44_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[44].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_44_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[44].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_44_0_timer_clicked_function():
    print(btnx_44_0_timer_clicked_function)

def btnx_44_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_44_0_bool is True:
            auto_gen_btnx_bool.btnx_44_0_bool = False
            print('[btnx_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_44_0_bool) + ']')
            # btnx_44_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_44_0_bool is False:
            auto_gen_btnx_bool.btnx_44_0_bool = True
            print('[btnx_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_44_0_bool) + ']')
            # btnx_44_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_45_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[45].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_45_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[45].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_45_0_timer_clicked_function():
    print(btnx_45_0_timer_clicked_function)

def btnx_45_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_45_0_bool is True:
            auto_gen_btnx_bool.btnx_45_0_bool = False
            print('[btnx_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_45_0_bool) + ']')
            # btnx_45_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_45_0_bool is False:
            auto_gen_btnx_bool.btnx_45_0_bool = True
            print('[btnx_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_45_0_bool) + ']')
            # btnx_45_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_46_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[46].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_46_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[46].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_46_0_timer_clicked_function():
    print(btnx_46_0_timer_clicked_function)

def btnx_46_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_46_0_bool is True:
            auto_gen_btnx_bool.btnx_46_0_bool = False
            print('[btnx_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_46_0_bool) + ']')
            # btnx_46_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_46_0_bool is False:
            auto_gen_btnx_bool.btnx_46_0_bool = True
            print('[btnx_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_46_0_bool) + ']')
            # btnx_46_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_47_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[47].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_47_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[47].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_47_0_timer_clicked_function():
    print(btnx_47_0_timer_clicked_function)

def btnx_47_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_47_0_bool is True:
            auto_gen_btnx_bool.btnx_47_0_bool = False
            print('[btnx_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_47_0_bool) + ']')
            # btnx_47_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_47_0_bool is False:
            auto_gen_btnx_bool.btnx_47_0_bool = True
            print('[btnx_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_47_0_bool) + ']')
            # btnx_47_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_48_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[48].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_48_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[48].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_48_0_timer_clicked_function():
    print(btnx_48_0_timer_clicked_function)

def btnx_48_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_48_0_bool is True:
            auto_gen_btnx_bool.btnx_48_0_bool = False
            print('[btnx_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_48_0_bool) + ']')
            # btnx_48_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_48_0_bool is False:
            auto_gen_btnx_bool.btnx_48_0_bool = True
            print('[btnx_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_48_0_bool) + ']')
            # btnx_48_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_49_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[49].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_49_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[49].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_49_0_timer_clicked_function():
    print(btnx_49_0_timer_clicked_function)

def btnx_49_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_49_0_bool is True:
            auto_gen_btnx_bool.btnx_49_0_bool = False
            print('[btnx_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_49_0_bool) + ']')
            # btnx_49_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_49_0_bool is False:
            auto_gen_btnx_bool.btnx_49_0_bool = True
            print('[btnx_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_49_0_bool) + ']')
            # btnx_49_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_50_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[50].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_50_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[50].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_50_0_timer_clicked_function():
    print(btnx_50_0_timer_clicked_function)

def btnx_50_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_50_0_bool is True:
            auto_gen_btnx_bool.btnx_50_0_bool = False
            print('[btnx_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_50_0_bool) + ']')
            # btnx_50_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_50_0_bool is False:
            auto_gen_btnx_bool.btnx_50_0_bool = True
            print('[btnx_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_50_0_bool) + ']')
            # btnx_50_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_51_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[51].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_51_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[51].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_51_0_timer_clicked_function():
    print(btnx_51_0_timer_clicked_function)

def btnx_51_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_51_0_bool is True:
            auto_gen_btnx_bool.btnx_51_0_bool = False
            print('[btnx_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_51_0_bool) + ']')
            # btnx_51_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_51_0_bool is False:
            auto_gen_btnx_bool.btnx_51_0_bool = True
            print('[btnx_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_51_0_bool) + ']')
            # btnx_51_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_52_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[52].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_52_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[52].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_52_0_timer_clicked_function():
    print(btnx_52_0_timer_clicked_function)

def btnx_52_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_52_0_bool is True:
            auto_gen_btnx_bool.btnx_52_0_bool = False
            print('[btnx_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_52_0_bool) + ']')
            # btnx_52_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_52_0_bool is False:
            auto_gen_btnx_bool.btnx_52_0_bool = True
            print('[btnx_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_52_0_bool) + ']')
            # btnx_52_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_53_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[53].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_53_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[53].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_53_0_timer_clicked_function():
    print(btnx_53_0_timer_clicked_function)

def btnx_53_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_53_0_bool is True:
            auto_gen_btnx_bool.btnx_53_0_bool = False
            print('[btnx_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_53_0_bool) + ']')
            # btnx_53_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_53_0_bool is False:
            auto_gen_btnx_bool.btnx_53_0_bool = True
            print('[btnx_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_53_0_bool) + ']')
            # btnx_53_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_54_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[54].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_54_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[54].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_54_0_timer_clicked_function():
    print(btnx_54_0_timer_clicked_function)

def btnx_54_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_54_0_bool is True:
            auto_gen_btnx_bool.btnx_54_0_bool = False
            print('[btnx_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_54_0_bool) + ']')
            # btnx_54_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_54_0_bool is False:
            auto_gen_btnx_bool.btnx_54_0_bool = True
            print('[btnx_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_54_0_bool) + ']')
            # btnx_54_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_55_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[55].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_55_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[55].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_55_0_timer_clicked_function():
    print(btnx_55_0_timer_clicked_function)

def btnx_55_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_55_0_bool is True:
            auto_gen_btnx_bool.btnx_55_0_bool = False
            print('[btnx_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_55_0_bool) + ']')
            # btnx_55_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_55_0_bool is False:
            auto_gen_btnx_bool.btnx_55_0_bool = True
            print('[btnx_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_55_0_bool) + ']')
            # btnx_55_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_56_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[56].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_56_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[56].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_56_0_timer_clicked_function():
    print(btnx_56_0_timer_clicked_function)

def btnx_56_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_56_0_bool is True:
            auto_gen_btnx_bool.btnx_56_0_bool = False
            print('[btnx_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_56_0_bool) + ']')
            # btnx_56_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_56_0_bool is False:
            auto_gen_btnx_bool.btnx_56_0_bool = True
            print('[btnx_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_56_0_bool) + ']')
            # btnx_56_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_57_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[57].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_57_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[57].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_57_0_timer_clicked_function():
    print(btnx_57_0_timer_clicked_function)

def btnx_57_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_57_0_bool is True:
            auto_gen_btnx_bool.btnx_57_0_bool = False
            print('[btnx_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_57_0_bool) + ']')
            # btnx_57_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_57_0_bool is False:
            auto_gen_btnx_bool.btnx_57_0_bool = True
            print('[btnx_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_57_0_bool) + ']')
            # btnx_57_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_58_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[58].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_58_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[58].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_58_0_timer_clicked_function():
    print(btnx_58_0_timer_clicked_function)

def btnx_58_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_58_0_bool is True:
            auto_gen_btnx_bool.btnx_58_0_bool = False
            print('[btnx_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_58_0_bool) + ']')
            # btnx_58_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_58_0_bool is False:
            auto_gen_btnx_bool.btnx_58_0_bool = True
            print('[btnx_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_58_0_bool) + ']')
            # btnx_58_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_59_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[59].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_59_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[59].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_59_0_timer_clicked_function():
    print(btnx_59_0_timer_clicked_function)

def btnx_59_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_59_0_bool is True:
            auto_gen_btnx_bool.btnx_59_0_bool = False
            print('[btnx_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_59_0_bool) + ']')
            # btnx_59_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_59_0_bool is False:
            auto_gen_btnx_bool.btnx_59_0_bool = True
            print('[btnx_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_59_0_bool) + ']')
            # btnx_59_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_60_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[60].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_60_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[60].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_60_0_timer_clicked_function():
    print(btnx_60_0_timer_clicked_function)

def btnx_60_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_60_0_bool is True:
            auto_gen_btnx_bool.btnx_60_0_bool = False
            print('[btnx_60] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_60_0_bool) + ']')
            # btnx_60_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_60_0_bool is False:
            auto_gen_btnx_bool.btnx_60_0_bool = True
            print('[btnx_60] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_60_0_bool) + ']')
            # btnx_60_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_61_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[61].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_61_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[61].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_61_0_timer_clicked_function():
    print(btnx_61_0_timer_clicked_function)

def btnx_61_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_61_0_bool is True:
            auto_gen_btnx_bool.btnx_61_0_bool = False
            print('[btnx_61] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_61_0_bool) + ']')
            # btnx_61_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_61_0_bool is False:
            auto_gen_btnx_bool.btnx_61_0_bool = True
            print('[btnx_61] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_61_0_bool) + ']')
            # btnx_61_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_62_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[62].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_62_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[62].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_62_0_timer_clicked_function():
    print(btnx_62_0_timer_clicked_function)

def btnx_62_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_62_0_bool is True:
            auto_gen_btnx_bool.btnx_62_0_bool = False
            print('[btnx_62] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_62_0_bool) + ']')
            # btnx_62_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_62_0_bool is False:
            auto_gen_btnx_bool.btnx_62_0_bool = True
            print('[btnx_62] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_62_0_bool) + ']')
            # btnx_62_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_63_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[63].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_63_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[63].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_63_0_timer_clicked_function():
    print(btnx_63_0_timer_clicked_function)

def btnx_63_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_63_0_bool is True:
            auto_gen_btnx_bool.btnx_63_0_bool = False
            print('[btnx_63] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_63_0_bool) + ']')
            # btnx_63_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_63_0_bool is False:
            auto_gen_btnx_bool.btnx_63_0_bool = True
            print('[btnx_63] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_63_0_bool) + ']')
            # btnx_63_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_64_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[64].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_64_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[64].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_64_0_timer_clicked_function():
    print(btnx_64_0_timer_clicked_function)

def btnx_64_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_64_0_bool is True:
            auto_gen_btnx_bool.btnx_64_0_bool = False
            print('[btnx_64] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_64_0_bool) + ']')
            # btnx_64_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_64_0_bool is False:
            auto_gen_btnx_bool.btnx_64_0_bool = True
            print('[btnx_64] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_64_0_bool) + ']')
            # btnx_64_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_65_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[65].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_65_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[65].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_65_0_timer_clicked_function():
    print(btnx_65_0_timer_clicked_function)

def btnx_65_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_65_0_bool is True:
            auto_gen_btnx_bool.btnx_65_0_bool = False
            print('[btnx_65] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_65_0_bool) + ']')
            # btnx_65_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_65_0_bool is False:
            auto_gen_btnx_bool.btnx_65_0_bool = True
            print('[btnx_65] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_65_0_bool) + ']')
            # btnx_65_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_66_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[66].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_66_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[66].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_66_0_timer_clicked_function():
    print(btnx_66_0_timer_clicked_function)

def btnx_66_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_66_0_bool is True:
            auto_gen_btnx_bool.btnx_66_0_bool = False
            print('[btnx_66] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_66_0_bool) + ']')
            # btnx_66_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_66_0_bool is False:
            auto_gen_btnx_bool.btnx_66_0_bool = True
            print('[btnx_66] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_66_0_bool) + ']')
            # btnx_66_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_67_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[67].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_67_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[67].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_67_0_timer_clicked_function():
    print(btnx_67_0_timer_clicked_function)

def btnx_67_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_67_0_bool is True:
            auto_gen_btnx_bool.btnx_67_0_bool = False
            print('[btnx_67] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_67_0_bool) + ']')
            # btnx_67_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_67_0_bool is False:
            auto_gen_btnx_bool.btnx_67_0_bool = True
            print('[btnx_67] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_67_0_bool) + ']')
            # btnx_67_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_68_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[68].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_68_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[68].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_68_0_timer_clicked_function():
    print(btnx_68_0_timer_clicked_function)

def btnx_68_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_68_0_bool is True:
            auto_gen_btnx_bool.btnx_68_0_bool = False
            print('[btnx_68] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_68_0_bool) + ']')
            # btnx_68_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_68_0_bool is False:
            auto_gen_btnx_bool.btnx_68_0_bool = True
            print('[btnx_68] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_68_0_bool) + ']')
            # btnx_68_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_69_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[69].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_69_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[69].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_69_0_timer_clicked_function():
    print(btnx_69_0_timer_clicked_function)

def btnx_69_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_69_0_bool is True:
            auto_gen_btnx_bool.btnx_69_0_bool = False
            print('[btnx_69] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_69_0_bool) + ']')
            # btnx_69_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_69_0_bool is False:
            auto_gen_btnx_bool.btnx_69_0_bool = True
            print('[btnx_69] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_69_0_bool) + ']')
            # btnx_69_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_70_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[70].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_70_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[70].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_70_0_timer_clicked_function():
    print(btnx_70_0_timer_clicked_function)

def btnx_70_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_70_0_bool is True:
            auto_gen_btnx_bool.btnx_70_0_bool = False
            print('[btnx_70] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_70_0_bool) + ']')
            # btnx_70_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_70_0_bool is False:
            auto_gen_btnx_bool.btnx_70_0_bool = True
            print('[btnx_70] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_70_0_bool) + ']')
            # btnx_70_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_71_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[71].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_71_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[71].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_71_0_timer_clicked_function():
    print(btnx_71_0_timer_clicked_function)

def btnx_71_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_71_0_bool is True:
            auto_gen_btnx_bool.btnx_71_0_bool = False
            print('[btnx_71] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_71_0_bool) + ']')
            # btnx_71_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_71_0_bool is False:
            auto_gen_btnx_bool.btnx_71_0_bool = True
            print('[btnx_71] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_71_0_bool) + ']')
            # btnx_71_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_72_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[72].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_72_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[72].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_72_0_timer_clicked_function():
    print(btnx_72_0_timer_clicked_function)

def btnx_72_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_72_0_bool is True:
            auto_gen_btnx_bool.btnx_72_0_bool = False
            print('[btnx_72] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_72_0_bool) + ']')
            # btnx_72_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_72_0_bool is False:
            auto_gen_btnx_bool.btnx_72_0_bool = True
            print('[btnx_72] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_72_0_bool) + ']')
            # btnx_72_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_73_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[73].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_73_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[73].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_73_0_timer_clicked_function():
    print(btnx_73_0_timer_clicked_function)

def btnx_73_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_73_0_bool is True:
            auto_gen_btnx_bool.btnx_73_0_bool = False
            print('[btnx_73] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_73_0_bool) + ']')
            # btnx_73_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_73_0_bool is False:
            auto_gen_btnx_bool.btnx_73_0_bool = True
            print('[btnx_73] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_73_0_bool) + ']')
            # btnx_73_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_74_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[74].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_74_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[74].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_74_0_timer_clicked_function():
    print(btnx_74_0_timer_clicked_function)

def btnx_74_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_74_0_bool is True:
            auto_gen_btnx_bool.btnx_74_0_bool = False
            print('[btnx_74] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_74_0_bool) + ']')
            # btnx_74_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_74_0_bool is False:
            auto_gen_btnx_bool.btnx_74_0_bool = True
            print('[btnx_74] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_74_0_bool) + ']')
            # btnx_74_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_75_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[75].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_75_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[75].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_75_0_timer_clicked_function():
    print(btnx_75_0_timer_clicked_function)

def btnx_75_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_75_0_bool is True:
            auto_gen_btnx_bool.btnx_75_0_bool = False
            print('[btnx_75] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_75_0_bool) + ']')
            # btnx_75_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_75_0_bool is False:
            auto_gen_btnx_bool.btnx_75_0_bool = True
            print('[btnx_75] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_75_0_bool) + ']')
            # btnx_75_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_76_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[76].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_76_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[76].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_76_0_timer_clicked_function():
    print(btnx_76_0_timer_clicked_function)

def btnx_76_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_76_0_bool is True:
            auto_gen_btnx_bool.btnx_76_0_bool = False
            print('[btnx_76] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_76_0_bool) + ']')
            # btnx_76_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_76_0_bool is False:
            auto_gen_btnx_bool.btnx_76_0_bool = True
            print('[btnx_76] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_76_0_bool) + ']')
            # btnx_76_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_77_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[77].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_77_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[77].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_77_0_timer_clicked_function():
    print(btnx_77_0_timer_clicked_function)

def btnx_77_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_77_0_bool is True:
            auto_gen_btnx_bool.btnx_77_0_bool = False
            print('[btnx_77] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_77_0_bool) + ']')
            # btnx_77_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_77_0_bool is False:
            auto_gen_btnx_bool.btnx_77_0_bool = True
            print('[btnx_77] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_77_0_bool) + ']')
            # btnx_77_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_78_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[78].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_78_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[78].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_78_0_timer_clicked_function():
    print(btnx_78_0_timer_clicked_function)

def btnx_78_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_78_0_bool is True:
            auto_gen_btnx_bool.btnx_78_0_bool = False
            print('[btnx_78] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_78_0_bool) + ']')
            # btnx_78_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_78_0_bool is False:
            auto_gen_btnx_bool.btnx_78_0_bool = True
            print('[btnx_78] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_78_0_bool) + ']')
            # btnx_78_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_79_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[79].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_79_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[79].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_79_0_timer_clicked_function():
    print(btnx_79_0_timer_clicked_function)

def btnx_79_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_79_0_bool is True:
            auto_gen_btnx_bool.btnx_79_0_bool = False
            print('[btnx_79] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_79_0_bool) + ']')
            # btnx_79_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_79_0_bool is False:
            auto_gen_btnx_bool.btnx_79_0_bool = True
            print('[btnx_79] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_79_0_bool) + ']')
            # btnx_79_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_80_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[80].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_80_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[80].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_80_0_timer_clicked_function():
    print(btnx_80_0_timer_clicked_function)

def btnx_80_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_80_0_bool is True:
            auto_gen_btnx_bool.btnx_80_0_bool = False
            print('[btnx_80] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_80_0_bool) + ']')
            # btnx_80_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_80_0_bool is False:
            auto_gen_btnx_bool.btnx_80_0_bool = True
            print('[btnx_80] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_80_0_bool) + ']')
            # btnx_80_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_81_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[81].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_81_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[81].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_81_0_timer_clicked_function():
    print(btnx_81_0_timer_clicked_function)

def btnx_81_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_81_0_bool is True:
            auto_gen_btnx_bool.btnx_81_0_bool = False
            print('[btnx_81] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_81_0_bool) + ']')
            # btnx_81_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_81_0_bool is False:
            auto_gen_btnx_bool.btnx_81_0_bool = True
            print('[btnx_81] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_81_0_bool) + ']')
            # btnx_81_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_82_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[82].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_82_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[82].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_82_0_timer_clicked_function():
    print(btnx_82_0_timer_clicked_function)

def btnx_82_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_82_0_bool is True:
            auto_gen_btnx_bool.btnx_82_0_bool = False
            print('[btnx_82] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_82_0_bool) + ']')
            # btnx_82_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_82_0_bool is False:
            auto_gen_btnx_bool.btnx_82_0_bool = True
            print('[btnx_82] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_82_0_bool) + ']')
            # btnx_82_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_83_start_timer_function():
    global var_btnx_timer
    var_btnx_timer[0].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_83_stop_timer_function():
    global var_btnx_timer
    var_btnx_timer[0].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_83_timer_clicked_function():
    print(btnx_83_timer_clicked_function)

def btnx_83_function():
    auto_gen_main_page.main_page = 0
    if auto_gen_btnx_bool.btnx_83_bool is True:
        auto_gen_btnx_bool.btnx_83_bool = False
        # btnx_83_stop_timer_function()
    elif auto_gen_btnx_bool.btnx_83_bool is False:
        auto_gen_btnx_bool.btnx_83_bool = True
        # btnx_83_start_timer_function()
    print('[btnx_83] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_83_bool) + ']')

@PyQt5.QtCore.pyqtSlot()
def btnx_84_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[83].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_84_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[83].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_84_0_timer_clicked_function():
    print(btnx_84_0_timer_clicked_function)

def btnx_84_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_84_0_bool is True:
            auto_gen_btnx_bool.btnx_84_0_bool = False
            print('[btnx_84] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_84_0_bool) + ']')
            # btnx_84_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_84_0_bool is False:
            auto_gen_btnx_bool.btnx_84_0_bool = True
            print('[btnx_84] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_84_0_bool) + ']')
            # btnx_84_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_85_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[84].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_85_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[84].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_85_0_timer_clicked_function():
    print(btnx_85_0_timer_clicked_function)

def btnx_85_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_85_0_bool is True:
            auto_gen_btnx_bool.btnx_85_0_bool = False
            print('[btnx_85] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_85_0_bool) + ']')
            # btnx_85_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_85_0_bool is False:
            auto_gen_btnx_bool.btnx_85_0_bool = True
            print('[btnx_85] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_85_0_bool) + ']')
            # btnx_85_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_86_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[85].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_86_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[85].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_86_0_timer_clicked_function():
    print(btnx_86_0_timer_clicked_function)

def btnx_86_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_86_0_bool is True:
            auto_gen_btnx_bool.btnx_86_0_bool = False
            print('[btnx_86] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_86_0_bool) + ']')
            # btnx_86_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_86_0_bool is False:
            auto_gen_btnx_bool.btnx_86_0_bool = True
            print('[btnx_86] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_86_0_bool) + ']')
            # btnx_86_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_87_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[86].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_87_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[86].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_87_0_timer_clicked_function():
    print(btnx_87_0_timer_clicked_function)

def btnx_87_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_87_0_bool is True:
            auto_gen_btnx_bool.btnx_87_0_bool = False
            print('[btnx_87] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_87_0_bool) + ']')
            # btnx_87_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_87_0_bool is False:
            auto_gen_btnx_bool.btnx_87_0_bool = True
            print('[btnx_87] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_87_0_bool) + ']')
            # btnx_87_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_88_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[87].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_88_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[87].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_88_0_timer_clicked_function():
    print(btnx_88_0_timer_clicked_function)

def btnx_88_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_88_0_bool is True:
            auto_gen_btnx_bool.btnx_88_0_bool = False
            print('[btnx_88] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_88_0_bool) + ']')
            # btnx_88_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_88_0_bool is False:
            auto_gen_btnx_bool.btnx_88_0_bool = True
            print('[btnx_88] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_88_0_bool) + ']')
            # btnx_88_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_89_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[88].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_89_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[88].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_89_0_timer_clicked_function():
    print(btnx_89_0_timer_clicked_function)

def btnx_89_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_89_0_bool is True:
            auto_gen_btnx_bool.btnx_89_0_bool = False
            print('[btnx_89] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_89_0_bool) + ']')
            # btnx_89_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_89_0_bool is False:
            auto_gen_btnx_bool.btnx_89_0_bool = True
            print('[btnx_89] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_89_0_bool) + ']')
            # btnx_89_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_90_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[89].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_90_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[89].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_90_0_timer_clicked_function():
    print(btnx_90_0_timer_clicked_function)

def btnx_90_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_90_0_bool is True:
            auto_gen_btnx_bool.btnx_90_0_bool = False
            print('[btnx_90] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_90_0_bool) + ']')
            # btnx_90_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_90_0_bool is False:
            auto_gen_btnx_bool.btnx_90_0_bool = True
            print('[btnx_90] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_90_0_bool) + ']')
            # btnx_90_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_91_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[90].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_91_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[90].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_91_0_timer_clicked_function():
    print(btnx_91_0_timer_clicked_function)

def btnx_91_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_91_0_bool is True:
            auto_gen_btnx_bool.btnx_91_0_bool = False
            print('[btnx_91] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_91_0_bool) + ']')
            # btnx_91_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_91_0_bool is False:
            auto_gen_btnx_bool.btnx_91_0_bool = True
            print('[btnx_91] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_91_0_bool) + ']')
            # btnx_91_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_92_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[91].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_92_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[91].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_92_0_timer_clicked_function():
    print(btnx_92_0_timer_clicked_function)

def btnx_92_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_92_0_bool is True:
            auto_gen_btnx_bool.btnx_92_0_bool = False
            print('[btnx_92] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_92_0_bool) + ']')
            # btnx_92_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_92_0_bool is False:
            auto_gen_btnx_bool.btnx_92_0_bool = True
            print('[btnx_92] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_92_0_bool) + ']')
            # btnx_92_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_93_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[92].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_93_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[92].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_93_0_timer_clicked_function():
    print(btnx_93_0_timer_clicked_function)

def btnx_93_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_93_0_bool is True:
            auto_gen_btnx_bool.btnx_93_0_bool = False
            print('[btnx_93] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_93_0_bool) + ']')
            # btnx_93_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_93_0_bool is False:
            auto_gen_btnx_bool.btnx_93_0_bool = True
            print('[btnx_93] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_93_0_bool) + ']')
            # btnx_93_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_94_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[93].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_94_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[93].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_94_0_timer_clicked_function():
    print(btnx_94_0_timer_clicked_function)

def btnx_94_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_94_0_bool is True:
            auto_gen_btnx_bool.btnx_94_0_bool = False
            print('[btnx_94] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_94_0_bool) + ']')
            # btnx_94_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_94_0_bool is False:
            auto_gen_btnx_bool.btnx_94_0_bool = True
            print('[btnx_94] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_94_0_bool) + ']')
            # btnx_94_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_95_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[94].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_95_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[94].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_95_0_timer_clicked_function():
    print(btnx_95_0_timer_clicked_function)

def btnx_95_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_95_0_bool is True:
            auto_gen_btnx_bool.btnx_95_0_bool = False
            print('[btnx_95] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_95_0_bool) + ']')
            # btnx_95_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_95_0_bool is False:
            auto_gen_btnx_bool.btnx_95_0_bool = True
            print('[btnx_95] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_95_0_bool) + ']')
            # btnx_95_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_96_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[95].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_96_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[95].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_96_0_timer_clicked_function():
    print(btnx_96_0_timer_clicked_function)

def btnx_96_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_96_0_bool is True:
            auto_gen_btnx_bool.btnx_96_0_bool = False
            print('[btnx_96] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_96_0_bool) + ']')
            # btnx_96_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_96_0_bool is False:
            auto_gen_btnx_bool.btnx_96_0_bool = True
            print('[btnx_96] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_96_0_bool) + ']')
            # btnx_96_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_97_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[96].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_97_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[96].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_97_0_timer_clicked_function():
    print(btnx_97_0_timer_clicked_function)

def btnx_97_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_97_0_bool is True:
            auto_gen_btnx_bool.btnx_97_0_bool = False
            print('[btnx_97] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_97_0_bool) + ']')
            # btnx_97_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_97_0_bool is False:
            auto_gen_btnx_bool.btnx_97_0_bool = True
            print('[btnx_97] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_97_0_bool) + ']')
            # btnx_97_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_98_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[97].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_98_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[97].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_98_0_timer_clicked_function():
    print(btnx_98_0_timer_clicked_function)

def btnx_98_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_98_0_bool is True:
            auto_gen_btnx_bool.btnx_98_0_bool = False
            print('[btnx_98] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_98_0_bool) + ']')
            # btnx_98_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_98_0_bool is False:
            auto_gen_btnx_bool.btnx_98_0_bool = True
            print('[btnx_98] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_98_0_bool) + ']')
            # btnx_98_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_99_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[98].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_99_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[98].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_99_0_timer_clicked_function():
    print(btnx_99_0_timer_clicked_function)

def btnx_99_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_99_0_bool is True:
            auto_gen_btnx_bool.btnx_99_0_bool = False
            print('[btnx_99] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_99_0_bool) + ']')
            # btnx_99_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_99_0_bool is False:
            auto_gen_btnx_bool.btnx_99_0_bool = True
            print('[btnx_99] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_99_0_bool) + ']')
            # btnx_99_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_100_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[99].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_100_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[99].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_100_0_timer_clicked_function():
    print(btnx_100_0_timer_clicked_function)

def btnx_100_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_100_0_bool is True:
            auto_gen_btnx_bool.btnx_100_0_bool = False
            print('[btnx_100] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_100_0_bool) + ']')
            # btnx_100_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_100_0_bool is False:
            auto_gen_btnx_bool.btnx_100_0_bool = True
            print('[btnx_100] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_100_0_bool) + ']')
            # btnx_100_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_101_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[100].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_101_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[100].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_101_0_timer_clicked_function():
    print(btnx_101_0_timer_clicked_function)

def btnx_101_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_101_0_bool is True:
            auto_gen_btnx_bool.btnx_101_0_bool = False
            print('[btnx_101] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_101_0_bool) + ']')
            # btnx_101_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_101_0_bool is False:
            auto_gen_btnx_bool.btnx_101_0_bool = True
            print('[btnx_101] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_101_0_bool) + ']')
            # btnx_101_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_102_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[101].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_102_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[101].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_102_0_timer_clicked_function():
    print(btnx_102_0_timer_clicked_function)

def btnx_102_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_102_0_bool is True:
            auto_gen_btnx_bool.btnx_102_0_bool = False
            print('[btnx_102] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_102_0_bool) + ']')
            # btnx_102_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_102_0_bool is False:
            auto_gen_btnx_bool.btnx_102_0_bool = True
            print('[btnx_102] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_102_0_bool) + ']')
            # btnx_102_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_103_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[102].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_103_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[102].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_103_0_timer_clicked_function():
    print(btnx_103_0_timer_clicked_function)

def btnx_103_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_103_0_bool is True:
            auto_gen_btnx_bool.btnx_103_0_bool = False
            print('[btnx_103] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_103_0_bool) + ']')
            # btnx_103_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_103_0_bool is False:
            auto_gen_btnx_bool.btnx_103_0_bool = True
            print('[btnx_103] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_103_0_bool) + ']')
            # btnx_103_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_104_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[103].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_104_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[103].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_104_0_timer_clicked_function():
    print(btnx_104_0_timer_clicked_function)

def btnx_104_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_104_0_bool is True:
            auto_gen_btnx_bool.btnx_104_0_bool = False
            print('[btnx_104] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_104_0_bool) + ']')
            # btnx_104_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_104_0_bool is False:
            auto_gen_btnx_bool.btnx_104_0_bool = True
            print('[btnx_104] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_104_0_bool) + ']')
            # btnx_104_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_105_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[104].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_105_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[104].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_105_0_timer_clicked_function():
    print(btnx_105_0_timer_clicked_function)

def btnx_105_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_105_0_bool is True:
            auto_gen_btnx_bool.btnx_105_0_bool = False
            print('[btnx_105] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_105_0_bool) + ']')
            # btnx_105_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_105_0_bool is False:
            auto_gen_btnx_bool.btnx_105_0_bool = True
            print('[btnx_105] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_105_0_bool) + ']')
            # btnx_105_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_106_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[105].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_106_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[105].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_106_0_timer_clicked_function():
    print(btnx_106_0_timer_clicked_function)

def btnx_106_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_106_0_bool is True:
            auto_gen_btnx_bool.btnx_106_0_bool = False
            print('[btnx_106] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_106_0_bool) + ']')
            # btnx_106_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_106_0_bool is False:
            auto_gen_btnx_bool.btnx_106_0_bool = True
            print('[btnx_106] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_106_0_bool) + ']')
            # btnx_106_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_107_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[106].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_107_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[106].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_107_0_timer_clicked_function():
    print(btnx_107_0_timer_clicked_function)

def btnx_107_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_107_0_bool is True:
            auto_gen_btnx_bool.btnx_107_0_bool = False
            print('[btnx_107] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_107_0_bool) + ']')
            # btnx_107_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_107_0_bool is False:
            auto_gen_btnx_bool.btnx_107_0_bool = True
            print('[btnx_107] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_107_0_bool) + ']')
            # btnx_107_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_108_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[107].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_108_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[107].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_108_0_timer_clicked_function():
    print(btnx_108_0_timer_clicked_function)

def btnx_108_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_108_0_bool is True:
            auto_gen_btnx_bool.btnx_108_0_bool = False
            print('[btnx_108] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_108_0_bool) + ']')
            # btnx_108_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_108_0_bool is False:
            auto_gen_btnx_bool.btnx_108_0_bool = True
            print('[btnx_108] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_108_0_bool) + ']')
            # btnx_108_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_109_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[108].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_109_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[108].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_109_0_timer_clicked_function():
    print(btnx_109_0_timer_clicked_function)

def btnx_109_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_109_0_bool is True:
            auto_gen_btnx_bool.btnx_109_0_bool = False
            print('[btnx_109] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_109_0_bool) + ']')
            # btnx_109_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_109_0_bool is False:
            auto_gen_btnx_bool.btnx_109_0_bool = True
            print('[btnx_109] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_109_0_bool) + ']')
            # btnx_109_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_110_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[109].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_110_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[109].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_110_0_timer_clicked_function():
    print(btnx_110_0_timer_clicked_function)

def btnx_110_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_110_0_bool is True:
            auto_gen_btnx_bool.btnx_110_0_bool = False
            print('[btnx_110] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_110_0_bool) + ']')
            # btnx_110_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_110_0_bool is False:
            auto_gen_btnx_bool.btnx_110_0_bool = True
            print('[btnx_110] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_110_0_bool) + ']')
            # btnx_110_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_111_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[110].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_111_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[110].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_111_0_timer_clicked_function():
    print(btnx_111_0_timer_clicked_function)

def btnx_111_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_111_0_bool is True:
            auto_gen_btnx_bool.btnx_111_0_bool = False
            print('[btnx_111] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_111_0_bool) + ']')
            # btnx_111_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_111_0_bool is False:
            auto_gen_btnx_bool.btnx_111_0_bool = True
            print('[btnx_111] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_111_0_bool) + ']')
            # btnx_111_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_112_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[111].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_112_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[111].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_112_0_timer_clicked_function():
    print(btnx_112_0_timer_clicked_function)

def btnx_112_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_112_0_bool is True:
            auto_gen_btnx_bool.btnx_112_0_bool = False
            print('[btnx_112] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_112_0_bool) + ']')
            # btnx_112_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_112_0_bool is False:
            auto_gen_btnx_bool.btnx_112_0_bool = True
            print('[btnx_112] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_112_0_bool) + ']')
            # btnx_112_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_113_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[112].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_113_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[112].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_113_0_timer_clicked_function():
    print(btnx_113_0_timer_clicked_function)

def btnx_113_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_113_0_bool is True:
            auto_gen_btnx_bool.btnx_113_0_bool = False
            print('[btnx_113] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_113_0_bool) + ']')
            # btnx_113_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_113_0_bool is False:
            auto_gen_btnx_bool.btnx_113_0_bool = True
            print('[btnx_113] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_113_0_bool) + ']')
            # btnx_113_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_114_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[113].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_114_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[113].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_114_0_timer_clicked_function():
    print(btnx_114_0_timer_clicked_function)

def btnx_114_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_114_0_bool is True:
            auto_gen_btnx_bool.btnx_114_0_bool = False
            print('[btnx_114] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_114_0_bool) + ']')
            # btnx_114_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_114_0_bool is False:
            auto_gen_btnx_bool.btnx_114_0_bool = True
            print('[btnx_114] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_114_0_bool) + ']')
            # btnx_114_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_115_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[114].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_115_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[114].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_115_0_timer_clicked_function():
    print(btnx_115_0_timer_clicked_function)

def btnx_115_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_115_0_bool is True:
            auto_gen_btnx_bool.btnx_115_0_bool = False
            print('[btnx_115] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_115_0_bool) + ']')
            # btnx_115_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_115_0_bool is False:
            auto_gen_btnx_bool.btnx_115_0_bool = True
            print('[btnx_115] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_115_0_bool) + ']')
            # btnx_115_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_116_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[115].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_116_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[115].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_116_0_timer_clicked_function():
    print(btnx_116_0_timer_clicked_function)

def btnx_116_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_116_0_bool is True:
            auto_gen_btnx_bool.btnx_116_0_bool = False
            print('[btnx_116] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_116_0_bool) + ']')
            # btnx_116_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_116_0_bool is False:
            auto_gen_btnx_bool.btnx_116_0_bool = True
            print('[btnx_116] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_116_0_bool) + ']')
            # btnx_116_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_117_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[116].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_117_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[116].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_117_0_timer_clicked_function():
    print(btnx_117_0_timer_clicked_function)

def btnx_117_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_117_0_bool is True:
            auto_gen_btnx_bool.btnx_117_0_bool = False
            print('[btnx_117] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_117_0_bool) + ']')
            # btnx_117_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_117_0_bool is False:
            auto_gen_btnx_bool.btnx_117_0_bool = True
            print('[btnx_117] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_117_0_bool) + ']')
            # btnx_117_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_118_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[117].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_118_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[117].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_118_0_timer_clicked_function():
    print(btnx_118_0_timer_clicked_function)

def btnx_118_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_118_0_bool is True:
            auto_gen_btnx_bool.btnx_118_0_bool = False
            print('[btnx_118] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_118_0_bool) + ']')
            # btnx_118_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_118_0_bool is False:
            auto_gen_btnx_bool.btnx_118_0_bool = True
            print('[btnx_118] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_118_0_bool) + ']')
            # btnx_118_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_119_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[118].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_119_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[118].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_119_0_timer_clicked_function():
    print(btnx_119_0_timer_clicked_function)

def btnx_119_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_119_0_bool is True:
            auto_gen_btnx_bool.btnx_119_0_bool = False
            print('[btnx_119] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_119_0_bool) + ']')
            # btnx_119_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_119_0_bool is False:
            auto_gen_btnx_bool.btnx_119_0_bool = True
            print('[btnx_119] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_119_0_bool) + ']')
            # btnx_119_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_120_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[119].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_120_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[119].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_120_0_timer_clicked_function():
    print(btnx_120_0_timer_clicked_function)

def btnx_120_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_120_0_bool is True:
            auto_gen_btnx_bool.btnx_120_0_bool = False
            print('[btnx_120] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_120_0_bool) + ']')
            # btnx_120_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_120_0_bool is False:
            auto_gen_btnx_bool.btnx_120_0_bool = True
            print('[btnx_120] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_120_0_bool) + ']')
            # btnx_120_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_121_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[120].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_121_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[120].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_121_0_timer_clicked_function():
    print(btnx_121_0_timer_clicked_function)

def btnx_121_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_121_0_bool is True:
            auto_gen_btnx_bool.btnx_121_0_bool = False
            print('[btnx_121] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_121_0_bool) + ']')
            # btnx_121_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_121_0_bool is False:
            auto_gen_btnx_bool.btnx_121_0_bool = True
            print('[btnx_121] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_121_0_bool) + ']')
            # btnx_121_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_122_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[121].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_122_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[121].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_122_0_timer_clicked_function():
    print(btnx_122_0_timer_clicked_function)

def btnx_122_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_122_0_bool is True:
            auto_gen_btnx_bool.btnx_122_0_bool = False
            print('[btnx_122] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_122_0_bool) + ']')
            # btnx_122_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_122_0_bool is False:
            auto_gen_btnx_bool.btnx_122_0_bool = True
            print('[btnx_122] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_122_0_bool) + ']')
            # btnx_122_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_123_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[122].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_123_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[122].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_123_0_timer_clicked_function():
    print(btnx_123_0_timer_clicked_function)

def btnx_123_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_123_0_bool is True:
            auto_gen_btnx_bool.btnx_123_0_bool = False
            print('[btnx_123] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_123_0_bool) + ']')
            # btnx_123_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_123_0_bool is False:
            auto_gen_btnx_bool.btnx_123_0_bool = True
            print('[btnx_123] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_123_0_bool) + ']')
            # btnx_123_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_124_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[123].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_124_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[123].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_124_0_timer_clicked_function():
    print(btnx_124_0_timer_clicked_function)

def btnx_124_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_124_0_bool is True:
            auto_gen_btnx_bool.btnx_124_0_bool = False
            print('[btnx_124] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_124_0_bool) + ']')
            # btnx_124_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_124_0_bool is False:
            auto_gen_btnx_bool.btnx_124_0_bool = True
            print('[btnx_124] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_124_0_bool) + ']')
            # btnx_124_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_125_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[124].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_125_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[124].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_125_0_timer_clicked_function():
    print(btnx_125_0_timer_clicked_function)

def btnx_125_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_125_0_bool is True:
            auto_gen_btnx_bool.btnx_125_0_bool = False
            print('[btnx_125] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_125_0_bool) + ']')
            # btnx_125_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_125_0_bool is False:
            auto_gen_btnx_bool.btnx_125_0_bool = True
            print('[btnx_125] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_125_0_bool) + ']')
            # btnx_125_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_126_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[125].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_126_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[125].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_126_0_timer_clicked_function():
    print(btnx_126_0_timer_clicked_function)

def btnx_126_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_126_0_bool is True:
            auto_gen_btnx_bool.btnx_126_0_bool = False
            print('[btnx_126] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_126_0_bool) + ']')
            # btnx_126_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_126_0_bool is False:
            auto_gen_btnx_bool.btnx_126_0_bool = True
            print('[btnx_126] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_126_0_bool) + ']')
            # btnx_126_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_127_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[126].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_127_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[126].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_127_0_timer_clicked_function():
    print(btnx_127_0_timer_clicked_function)

def btnx_127_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_127_0_bool is True:
            auto_gen_btnx_bool.btnx_127_0_bool = False
            print('[btnx_127] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_127_0_bool) + ']')
            # btnx_127_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_127_0_bool is False:
            auto_gen_btnx_bool.btnx_127_0_bool = True
            print('[btnx_127] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_127_0_bool) + ']')
            # btnx_127_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_128_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[127].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_128_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[127].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_128_0_timer_clicked_function():
    print(btnx_128_0_timer_clicked_function)

def btnx_128_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_128_0_bool is True:
            auto_gen_btnx_bool.btnx_128_0_bool = False
            print('[btnx_128] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_128_0_bool) + ']')
            # btnx_128_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_128_0_bool is False:
            auto_gen_btnx_bool.btnx_128_0_bool = True
            print('[btnx_128] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_128_0_bool) + ']')
            # btnx_128_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_129_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[128].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_129_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[128].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_129_0_timer_clicked_function():
    print(btnx_129_0_timer_clicked_function)

def btnx_129_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_129_0_bool is True:
            auto_gen_btnx_bool.btnx_129_0_bool = False
            print('[btnx_129] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_129_0_bool) + ']')
            # btnx_129_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_129_0_bool is False:
            auto_gen_btnx_bool.btnx_129_0_bool = True
            print('[btnx_129] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_129_0_bool) + ']')
            # btnx_129_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_130_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[129].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_130_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[129].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_130_0_timer_clicked_function():
    print(btnx_130_0_timer_clicked_function)

def btnx_130_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_130_0_bool is True:
            auto_gen_btnx_bool.btnx_130_0_bool = False
            print('[btnx_130] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_130_0_bool) + ']')
            # btnx_130_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_130_0_bool is False:
            auto_gen_btnx_bool.btnx_130_0_bool = True
            print('[btnx_130] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_130_0_bool) + ']')
            # btnx_130_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_131_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[130].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_131_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[130].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_131_0_timer_clicked_function():
    print(btnx_131_0_timer_clicked_function)

def btnx_131_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_131_0_bool is True:
            auto_gen_btnx_bool.btnx_131_0_bool = False
            print('[btnx_131] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_131_0_bool) + ']')
            # btnx_131_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_131_0_bool is False:
            auto_gen_btnx_bool.btnx_131_0_bool = True
            print('[btnx_131] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_131_0_bool) + ']')
            # btnx_131_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_132_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[131].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_132_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[131].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_132_0_timer_clicked_function():
    print(btnx_132_0_timer_clicked_function)

def btnx_132_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_132_0_bool is True:
            auto_gen_btnx_bool.btnx_132_0_bool = False
            print('[btnx_132] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_132_0_bool) + ']')
            # btnx_132_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_132_0_bool is False:
            auto_gen_btnx_bool.btnx_132_0_bool = True
            print('[btnx_132] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_132_0_bool) + ']')
            # btnx_132_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_133_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[132].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_133_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[132].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_133_0_timer_clicked_function():
    print(btnx_133_0_timer_clicked_function)

def btnx_133_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_133_0_bool is True:
            auto_gen_btnx_bool.btnx_133_0_bool = False
            print('[btnx_133] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_133_0_bool) + ']')
            # btnx_133_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_133_0_bool is False:
            auto_gen_btnx_bool.btnx_133_0_bool = True
            print('[btnx_133] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_133_0_bool) + ']')
            # btnx_133_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_134_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[133].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_134_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[133].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_134_0_timer_clicked_function():
    print(btnx_134_0_timer_clicked_function)

def btnx_134_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_134_0_bool is True:
            auto_gen_btnx_bool.btnx_134_0_bool = False
            print('[btnx_134] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_134_0_bool) + ']')
            # btnx_134_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_134_0_bool is False:
            auto_gen_btnx_bool.btnx_134_0_bool = True
            print('[btnx_134] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_134_0_bool) + ']')
            # btnx_134_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_135_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[134].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_135_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[134].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_135_0_timer_clicked_function():
    print(btnx_135_0_timer_clicked_function)

def btnx_135_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_135_0_bool is True:
            auto_gen_btnx_bool.btnx_135_0_bool = False
            print('[btnx_135] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_135_0_bool) + ']')
            # btnx_135_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_135_0_bool is False:
            auto_gen_btnx_bool.btnx_135_0_bool = True
            print('[btnx_135] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_135_0_bool) + ']')
            # btnx_135_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_136_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[135].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_136_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[135].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_136_0_timer_clicked_function():
    print(btnx_136_0_timer_clicked_function)

def btnx_136_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_136_0_bool is True:
            auto_gen_btnx_bool.btnx_136_0_bool = False
            print('[btnx_136] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_136_0_bool) + ']')
            # btnx_136_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_136_0_bool is False:
            auto_gen_btnx_bool.btnx_136_0_bool = True
            print('[btnx_136] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_136_0_bool) + ']')
            # btnx_136_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_137_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[136].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_137_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[136].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_137_0_timer_clicked_function():
    print(btnx_137_0_timer_clicked_function)

def btnx_137_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_137_0_bool is True:
            auto_gen_btnx_bool.btnx_137_0_bool = False
            print('[btnx_137] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_137_0_bool) + ']')
            # btnx_137_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_137_0_bool is False:
            auto_gen_btnx_bool.btnx_137_0_bool = True
            print('[btnx_137] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_137_0_bool) + ']')
            # btnx_137_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_138_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[137].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_138_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[137].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_138_0_timer_clicked_function():
    print(btnx_138_0_timer_clicked_function)

def btnx_138_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_138_0_bool is True:
            auto_gen_btnx_bool.btnx_138_0_bool = False
            print('[btnx_138] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_138_0_bool) + ']')
            # btnx_138_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_138_0_bool is False:
            auto_gen_btnx_bool.btnx_138_0_bool = True
            print('[btnx_138] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_138_0_bool) + ']')
            # btnx_138_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_139_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[138].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_139_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[138].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_139_0_timer_clicked_function():
    print(btnx_139_0_timer_clicked_function)

def btnx_139_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_139_0_bool is True:
            auto_gen_btnx_bool.btnx_139_0_bool = False
            print('[btnx_139] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_139_0_bool) + ']')
            # btnx_139_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_139_0_bool is False:
            auto_gen_btnx_bool.btnx_139_0_bool = True
            print('[btnx_139] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_139_0_bool) + ']')
            # btnx_139_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_140_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[139].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_140_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[139].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_140_0_timer_clicked_function():
    print(btnx_140_0_timer_clicked_function)

def btnx_140_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_140_0_bool is True:
            auto_gen_btnx_bool.btnx_140_0_bool = False
            print('[btnx_140] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_140_0_bool) + ']')
            # btnx_140_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_140_0_bool is False:
            auto_gen_btnx_bool.btnx_140_0_bool = True
            print('[btnx_140] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_140_0_bool) + ']')
            # btnx_140_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_141_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[140].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_141_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[140].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_141_0_timer_clicked_function():
    print(btnx_141_0_timer_clicked_function)

def btnx_141_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_141_0_bool is True:
            auto_gen_btnx_bool.btnx_141_0_bool = False
            print('[btnx_141] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_141_0_bool) + ']')
            # btnx_141_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_141_0_bool is False:
            auto_gen_btnx_bool.btnx_141_0_bool = True
            print('[btnx_141] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_141_0_bool) + ']')
            # btnx_141_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_142_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[141].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_142_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[141].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_142_0_timer_clicked_function():
    print(btnx_142_0_timer_clicked_function)

def btnx_142_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_142_0_bool is True:
            auto_gen_btnx_bool.btnx_142_0_bool = False
            print('[btnx_142] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_142_0_bool) + ']')
            # btnx_142_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_142_0_bool is False:
            auto_gen_btnx_bool.btnx_142_0_bool = True
            print('[btnx_142] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_142_0_bool) + ']')
            # btnx_142_0_start_timer_function()

@PyQt5.QtCore.pyqtSlot()
def btnx_143_0_start_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[142].start()

@PyQt5.QtCore.pyqtSlot()
def btnx_143_0_stop_timer_function():
    global var_btnx_timer_sub
    var_btnx_timer_sub[142].stop()

@PyQt5.QtCore.pyqtSlot()
def btnx_143_0_timer_clicked_function():
    print(btnx_143_0_timer_clicked_function)

def btnx_143_function():
    if auto_gen_main_page.main_page == 0:
        if auto_gen_btnx_bool.btnx_143_0_bool is True:
            auto_gen_btnx_bool.btnx_143_0_bool = False
            print('[btnx_143] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_143_0_bool) + ']')
            # btnx_143_0_stop_timer_function()

        elif auto_gen_btnx_bool.btnx_143_0_bool is False:
            auto_gen_btnx_bool.btnx_143_0_bool = True
            print('[btnx_143] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_btnx_bool.btnx_143_0_bool) + ']')
            # btnx_143_0_start_timer_function()


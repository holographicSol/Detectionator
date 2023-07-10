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

def qlex_double_0_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_0'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_0_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_0_0_bool = False
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_0_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_0_0_bool = True
            print('[qlex_double_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_0_0_bool) + ']')

def qlex_double_1_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_1'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_1_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_1_0_bool = False
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_1_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_1_0_bool = True
            print('[qlex_double_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_1_0_bool) + ']')

def qlex_double_2_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_2'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_2_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_2_0_bool = False
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_2_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_2_0_bool = True
            print('[qlex_double_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_2_0_bool) + ']')

def qlex_double_3_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_3'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_3_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_3_0_bool = False
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_3_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_3_0_bool = True
            print('[qlex_double_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_3_0_bool) + ']')

def qlex_double_4_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_4'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_4_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_4_0_bool = False
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_4_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_4_0_bool = True
            print('[qlex_double_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_4_0_bool) + ']')

def qlex_double_5_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_5'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_5_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_5_0_bool = False
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_5_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_5_0_bool = True
            print('[qlex_double_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_5_0_bool) + ']')

def qlex_double_6_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_6'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_6_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_6_0_bool = False
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_6_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_6_0_bool = True
            print('[qlex_double_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_6_0_bool) + ']')

def qlex_double_7_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_7'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_7_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_7_0_bool = False
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_7_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_7_0_bool = True
            print('[qlex_double_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_7_0_bool) + ']')

def qlex_double_8_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_8'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_8_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_8_0_bool = False
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_8_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_8_0_bool = True
            print('[qlex_double_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_8_0_bool) + ']')

def qlex_double_9_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_9'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_9_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_9_0_bool = False
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_9_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_9_0_bool = True
            print('[qlex_double_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_9_0_bool) + ']')

def qlex_double_10_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_10'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_10_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_10_0_bool = False
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_10_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_10_0_bool = True
            print('[qlex_double_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_10_0_bool) + ']')

def qlex_double_11_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_11'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_11_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_11_0_bool = False
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_11_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_11_0_bool = True
            print('[qlex_double_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_11_0_bool) + ']')

def qlex_double_12_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_12'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_12_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_12_0_bool = False
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_12_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_12_0_bool = True
            print('[qlex_double_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_12_0_bool) + ']')

def qlex_double_13_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_13'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_13_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_13_0_bool = False
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_13_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_13_0_bool = True
            print('[qlex_double_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_13_0_bool) + ']')

def qlex_double_14_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_14'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_14_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_14_0_bool = False
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_14_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_14_0_bool = True
            print('[qlex_double_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_14_0_bool) + ']')

def qlex_double_15_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_15'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_15_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_15_0_bool = False
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_15_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_15_0_bool = True
            print('[qlex_double_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_15_0_bool) + ']')

def qlex_double_16_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_16'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_16_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_16_0_bool = False
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_16_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_16_0_bool = True
            print('[qlex_double_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_16_0_bool) + ']')

def qlex_double_17_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_17'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_17_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_17_0_bool = False
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_17_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_17_0_bool = True
            print('[qlex_double_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_17_0_bool) + ']')

def qlex_double_18_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_18'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_18_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_18_0_bool = False
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_18_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_18_0_bool = True
            print('[qlex_double_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_18_0_bool) + ']')

def qlex_double_19_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_19'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_19_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_19_0_bool = False
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_19_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_19_0_bool = True
            print('[qlex_double_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_19_0_bool) + ']')

def qlex_double_20_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_20'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_20_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_20_0_bool = False
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_20_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_20_0_bool = True
            print('[qlex_double_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_20_0_bool) + ']')

def qlex_double_21_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_21'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_21_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_21_0_bool = False
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_21_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_21_0_bool = True
            print('[qlex_double_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_21_0_bool) + ']')

def qlex_double_22_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_22'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_22_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_22_0_bool = False
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_22_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_22_0_bool = True
            print('[qlex_double_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_22_0_bool) + ']')

def qlex_double_23_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_23'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_23_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_23_0_bool = False
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_23_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_23_0_bool = True
            print('[qlex_double_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_23_0_bool) + ']')

def qlex_double_24_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_24'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_24_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_24_0_bool = False
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_24_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_24_0_bool = True
            print('[qlex_double_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_24_0_bool) + ']')

def qlex_double_25_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_25'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_25_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_25_0_bool = False
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_25_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_25_0_bool = True
            print('[qlex_double_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_25_0_bool) + ']')

def qlex_double_26_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_26'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_26_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_26_0_bool = False
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_26_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_26_0_bool = True
            print('[qlex_double_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_26_0_bool) + ']')

def qlex_double_27_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_27'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_27_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_27_0_bool = False
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_27_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_27_0_bool = True
            print('[qlex_double_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_27_0_bool) + ']')

def qlex_double_28_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_28'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_28_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_28_0_bool = False
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_28_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_28_0_bool = True
            print('[qlex_double_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_28_0_bool) + ']')

def qlex_double_29_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_29'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_29_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_29_0_bool = False
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_29_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_29_0_bool = True
            print('[qlex_double_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_29_0_bool) + ']')

def qlex_double_30_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_30'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_30_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_30_0_bool = False
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_30_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_30_0_bool = True
            print('[qlex_double_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_30_0_bool) + ']')

def qlex_double_31_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_31'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_31_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_31_0_bool = False
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_31_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_31_0_bool = True
            print('[qlex_double_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_31_0_bool) + ']')

def qlex_double_32_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_32'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_32_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_32_0_bool = False
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_32_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_32_0_bool = True
            print('[qlex_double_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_32_0_bool) + ']')

def qlex_double_33_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_33'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_33_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_33_0_bool = False
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_33_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_33_0_bool = True
            print('[qlex_double_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_33_0_bool) + ']')

def qlex_double_34_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_34'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_34_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_34_0_bool = False
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_34_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_34_0_bool = True
            print('[qlex_double_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_34_0_bool) + ']')

def qlex_double_35_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_35'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_35_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_35_0_bool = False
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_35_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_35_0_bool = True
            print('[qlex_double_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_35_0_bool) + ']')

def qlex_double_36_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_36'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_36_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_36_0_bool = False
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_36_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_36_0_bool = True
            print('[qlex_double_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_36_0_bool) + ']')

def qlex_double_37_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_37'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_37_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_37_0_bool = False
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_37_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_37_0_bool = True
            print('[qlex_double_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_37_0_bool) + ']')

def qlex_double_38_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_38'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_38_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_38_0_bool = False
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_38_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_38_0_bool = True
            print('[qlex_double_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_38_0_bool) + ']')

def qlex_double_39_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_39'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_39_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_39_0_bool = False
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_39_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_39_0_bool = True
            print('[qlex_double_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_39_0_bool) + ']')

def qlex_double_40_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_40'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_40_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_40_0_bool = False
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_40_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_40_0_bool = True
            print('[qlex_double_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_40_0_bool) + ']')

def qlex_double_41_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_41'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_41_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_41_0_bool = False
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_41_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_41_0_bool = True
            print('[qlex_double_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_41_0_bool) + ']')

def qlex_double_42_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_42'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_42_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_42_0_bool = False
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_42_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_42_0_bool = True
            print('[qlex_double_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_42_0_bool) + ']')

def qlex_double_43_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_43'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_43_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_43_0_bool = False
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_43_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_43_0_bool = True
            print('[qlex_double_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_43_0_bool) + ']')

def qlex_double_44_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_44'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_44_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_44_0_bool = False
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_44_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_44_0_bool = True
            print('[qlex_double_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_44_0_bool) + ']')

def qlex_double_45_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_45'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_45_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_45_0_bool = False
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_45_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_45_0_bool = True
            print('[qlex_double_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_45_0_bool) + ']')

def qlex_double_46_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_46'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_46_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_46_0_bool = False
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_46_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_46_0_bool = True
            print('[qlex_double_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_46_0_bool) + ']')

def qlex_double_47_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_47'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_47_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_47_0_bool = False
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_47_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_47_0_bool = True
            print('[qlex_double_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_47_0_bool) + ']')

def qlex_double_48_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_48'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_48_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_48_0_bool = False
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_48_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_48_0_bool = True
            print('[qlex_double_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_48_0_bool) + ']')

def qlex_double_49_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_49'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_49_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_49_0_bool = False
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_49_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_49_0_bool = True
            print('[qlex_double_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_49_0_bool) + ']')

def qlex_double_50_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_50'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_50_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_50_0_bool = False
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_50_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_50_0_bool = True
            print('[qlex_double_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_50_0_bool) + ']')

def qlex_double_51_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_51'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_51_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_51_0_bool = False
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_51_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_51_0_bool = True
            print('[qlex_double_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_51_0_bool) + ']')

def qlex_double_52_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_52'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_52_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_52_0_bool = False
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_52_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_52_0_bool = True
            print('[qlex_double_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_52_0_bool) + ']')

def qlex_double_53_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_53'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_53_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_53_0_bool = False
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_53_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_53_0_bool = True
            print('[qlex_double_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_53_0_bool) + ']')

def qlex_double_54_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_54'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_54_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_54_0_bool = False
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_54_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_54_0_bool = True
            print('[qlex_double_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_54_0_bool) + ']')

def qlex_double_55_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_55'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_55_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_55_0_bool = False
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_55_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_55_0_bool = True
            print('[qlex_double_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_55_0_bool) + ']')

def qlex_double_56_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_56'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_56_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_56_0_bool = False
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_56_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_56_0_bool = True
            print('[qlex_double_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_56_0_bool) + ']')

def qlex_double_57_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_57'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_57_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_57_0_bool = False
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_57_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_57_0_bool = True
            print('[qlex_double_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_57_0_bool) + ']')

def qlex_double_58_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_58'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_58_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_58_0_bool = False
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_58_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_58_0_bool = True
            print('[qlex_double_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_58_0_bool) + ']')

def qlex_double_59_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_59'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_59_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_59_0_bool = False
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_59_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_59_0_bool = True
            print('[qlex_double_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_59_0_bool) + ']')

def qlex_double_60_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_60'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_60_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_60_0_bool = False
            print('[qlex_double_60] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_60_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_60_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_60_0_bool = True
            print('[qlex_double_60] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_60_0_bool) + ']')

def qlex_double_61_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_61'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_61_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_61_0_bool = False
            print('[qlex_double_61] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_61_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_61_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_61_0_bool = True
            print('[qlex_double_61] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_61_0_bool) + ']')

def qlex_double_62_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_62'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_62_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_62_0_bool = False
            print('[qlex_double_62] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_62_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_62_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_62_0_bool = True
            print('[qlex_double_62] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_62_0_bool) + ']')

def qlex_double_63_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_63'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_63_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_63_0_bool = False
            print('[qlex_double_63] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_63_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_63_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_63_0_bool = True
            print('[qlex_double_63] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_63_0_bool) + ']')

def qlex_double_64_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_64'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_64_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_64_0_bool = False
            print('[qlex_double_64] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_64_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_64_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_64_0_bool = True
            print('[qlex_double_64] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_64_0_bool) + ']')

def qlex_double_65_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_65'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_65_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_65_0_bool = False
            print('[qlex_double_65] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_65_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_65_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_65_0_bool = True
            print('[qlex_double_65] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_65_0_bool) + ']')

def qlex_double_66_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_66'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_66_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_66_0_bool = False
            print('[qlex_double_66] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_66_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_66_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_66_0_bool = True
            print('[qlex_double_66] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_66_0_bool) + ']')

def qlex_double_67_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_67'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_67_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_67_0_bool = False
            print('[qlex_double_67] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_67_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_67_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_67_0_bool = True
            print('[qlex_double_67] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_67_0_bool) + ']')

def qlex_double_68_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_68'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_68_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_68_0_bool = False
            print('[qlex_double_68] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_68_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_68_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_68_0_bool = True
            print('[qlex_double_68] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_68_0_bool) + ']')

def qlex_double_69_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_69'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_69_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_69_0_bool = False
            print('[qlex_double_69] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_69_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_69_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_69_0_bool = True
            print('[qlex_double_69] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_69_0_bool) + ']')

def qlex_double_70_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_70'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_70_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_70_0_bool = False
            print('[qlex_double_70] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_70_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_70_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_70_0_bool = True
            print('[qlex_double_70] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_70_0_bool) + ']')

def qlex_double_71_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_71'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_71_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_71_0_bool = False
            print('[qlex_double_71] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_71_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_71_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_71_0_bool = True
            print('[qlex_double_71] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_71_0_bool) + ']')

def qlex_double_72_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_72'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_72_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_72_0_bool = False
            print('[qlex_double_72] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_72_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_72_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_72_0_bool = True
            print('[qlex_double_72] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_72_0_bool) + ']')

def qlex_double_73_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_73'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_73_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_73_0_bool = False
            print('[qlex_double_73] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_73_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_73_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_73_0_bool = True
            print('[qlex_double_73] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_73_0_bool) + ']')

def qlex_double_74_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_74'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_74_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_74_0_bool = False
            print('[qlex_double_74] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_74_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_74_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_74_0_bool = True
            print('[qlex_double_74] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_74_0_bool) + ']')

def qlex_double_75_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_75'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_75_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_75_0_bool = False
            print('[qlex_double_75] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_75_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_75_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_75_0_bool = True
            print('[qlex_double_75] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_75_0_bool) + ']')

def qlex_double_76_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_76'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_76_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_76_0_bool = False
            print('[qlex_double_76] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_76_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_76_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_76_0_bool = True
            print('[qlex_double_76] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_76_0_bool) + ']')

def qlex_double_77_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_77'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_77_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_77_0_bool = False
            print('[qlex_double_77] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_77_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_77_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_77_0_bool = True
            print('[qlex_double_77] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_77_0_bool) + ']')

def qlex_double_78_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_78'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_78_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_78_0_bool = False
            print('[qlex_double_78] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_78_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_78_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_78_0_bool = True
            print('[qlex_double_78] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_78_0_bool) + ']')

def qlex_double_79_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_79'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_79_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_79_0_bool = False
            print('[qlex_double_79] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_79_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_79_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_79_0_bool = True
            print('[qlex_double_79] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_79_0_bool) + ']')

def qlex_double_80_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_80'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_80_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_80_0_bool = False
            print('[qlex_double_80] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_80_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_80_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_80_0_bool = True
            print('[qlex_double_80] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_80_0_bool) + ']')

def qlex_double_81_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_81'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_81_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_81_0_bool = False
            print('[qlex_double_81] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_81_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_81_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_81_0_bool = True
            print('[qlex_double_81] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_81_0_bool) + ']')

def qlex_double_82_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_82'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_82_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_82_0_bool = False
            print('[qlex_double_82] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_82_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_82_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_82_0_bool = True
            print('[qlex_double_82] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_82_0_bool) + ']')

def qlex_double_83_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_83'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_83_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_83_0_bool = False
            print('[qlex_double_83] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_83_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_83_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_83_0_bool = True
            print('[qlex_double_83] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_83_0_bool) + ']')

def qlex_double_84_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_84'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_84_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_84_0_bool = False
            print('[qlex_double_84] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_84_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_84_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_84_0_bool = True
            print('[qlex_double_84] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_84_0_bool) + ']')

def qlex_double_85_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_85'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_85_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_85_0_bool = False
            print('[qlex_double_85] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_85_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_85_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_85_0_bool = True
            print('[qlex_double_85] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_85_0_bool) + ']')

def qlex_double_86_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_86'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_86_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_86_0_bool = False
            print('[qlex_double_86] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_86_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_86_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_86_0_bool = True
            print('[qlex_double_86] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_86_0_bool) + ']')

def qlex_double_87_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_87'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_87_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_87_0_bool = False
            print('[qlex_double_87] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_87_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_87_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_87_0_bool = True
            print('[qlex_double_87] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_87_0_bool) + ']')

def qlex_double_88_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_88'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_88_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_88_0_bool = False
            print('[qlex_double_88] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_88_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_88_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_88_0_bool = True
            print('[qlex_double_88] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_88_0_bool) + ']')

def qlex_double_89_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_89'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_89_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_89_0_bool = False
            print('[qlex_double_89] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_89_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_89_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_89_0_bool = True
            print('[qlex_double_89] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_89_0_bool) + ']')

def qlex_double_90_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_90'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_90_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_90_0_bool = False
            print('[qlex_double_90] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_90_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_90_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_90_0_bool = True
            print('[qlex_double_90] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_90_0_bool) + ']')

def qlex_double_91_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_91'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_91_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_91_0_bool = False
            print('[qlex_double_91] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_91_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_91_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_91_0_bool = True
            print('[qlex_double_91] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_91_0_bool) + ']')

def qlex_double_92_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_92'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_92_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_92_0_bool = False
            print('[qlex_double_92] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_92_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_92_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_92_0_bool = True
            print('[qlex_double_92] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_92_0_bool) + ']')

def qlex_double_93_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_93'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_93_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_93_0_bool = False
            print('[qlex_double_93] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_93_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_93_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_93_0_bool = True
            print('[qlex_double_93] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_93_0_bool) + ']')

def qlex_double_94_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_94'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_94_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_94_0_bool = False
            print('[qlex_double_94] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_94_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_94_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_94_0_bool = True
            print('[qlex_double_94] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_94_0_bool) + ']')

def qlex_double_95_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_95'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_95_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_95_0_bool = False
            print('[qlex_double_95] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_95_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_95_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_95_0_bool = True
            print('[qlex_double_95] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_95_0_bool) + ']')

def qlex_double_96_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_96'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_96_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_96_0_bool = False
            print('[qlex_double_96] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_96_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_96_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_96_0_bool = True
            print('[qlex_double_96] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_96_0_bool) + ']')

def qlex_double_97_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_97'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_97_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_97_0_bool = False
            print('[qlex_double_97] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_97_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_97_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_97_0_bool = True
            print('[qlex_double_97] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_97_0_bool) + ']')

def qlex_double_98_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_98'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_98_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_98_0_bool = False
            print('[qlex_double_98] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_98_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_98_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_98_0_bool = True
            print('[qlex_double_98] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_98_0_bool) + ']')

def qlex_double_99_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_99'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_99_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_99_0_bool = False
            print('[qlex_double_99] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_99_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_99_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_99_0_bool = True
            print('[qlex_double_99] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_99_0_bool) + ']')

def qlex_double_100_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_100'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_100_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_100_0_bool = False
            print('[qlex_double_100] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_100_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_100_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_100_0_bool = True
            print('[qlex_double_100] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_100_0_bool) + ']')

def qlex_double_101_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_101'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_101_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_101_0_bool = False
            print('[qlex_double_101] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_101_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_101_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_101_0_bool = True
            print('[qlex_double_101] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_101_0_bool) + ']')

def qlex_double_102_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_102'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_102_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_102_0_bool = False
            print('[qlex_double_102] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_102_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_102_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_102_0_bool = True
            print('[qlex_double_102] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_102_0_bool) + ']')

def qlex_double_103_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_103'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_103_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_103_0_bool = False
            print('[qlex_double_103] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_103_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_103_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_103_0_bool = True
            print('[qlex_double_103] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_103_0_bool) + ']')

def qlex_double_104_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_104'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_104_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_104_0_bool = False
            print('[qlex_double_104] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_104_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_104_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_104_0_bool = True
            print('[qlex_double_104] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_104_0_bool) + ']')

def qlex_double_105_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_105'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_105_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_105_0_bool = False
            print('[qlex_double_105] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_105_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_105_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_105_0_bool = True
            print('[qlex_double_105] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_105_0_bool) + ']')

def qlex_double_106_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_106'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_106_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_106_0_bool = False
            print('[qlex_double_106] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_106_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_106_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_106_0_bool = True
            print('[qlex_double_106] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_106_0_bool) + ']')

def qlex_double_107_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_107'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_107_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_107_0_bool = False
            print('[qlex_double_107] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_107_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_107_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_107_0_bool = True
            print('[qlex_double_107] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_107_0_bool) + ']')

def qlex_double_108_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_108'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_108_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_108_0_bool = False
            print('[qlex_double_108] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_108_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_108_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_108_0_bool = True
            print('[qlex_double_108] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_108_0_bool) + ']')

def qlex_double_109_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_109'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_109_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_109_0_bool = False
            print('[qlex_double_109] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_109_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_109_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_109_0_bool = True
            print('[qlex_double_109] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_109_0_bool) + ']')

def qlex_double_110_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_110'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_110_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_110_0_bool = False
            print('[qlex_double_110] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_110_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_110_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_110_0_bool = True
            print('[qlex_double_110] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_110_0_bool) + ']')

def qlex_double_111_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_111'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_111_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_111_0_bool = False
            print('[qlex_double_111] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_111_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_111_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_111_0_bool = True
            print('[qlex_double_111] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_111_0_bool) + ']')

def qlex_double_112_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_112'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_112_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_112_0_bool = False
            print('[qlex_double_112] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_112_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_112_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_112_0_bool = True
            print('[qlex_double_112] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_112_0_bool) + ']')

def qlex_double_113_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_113'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_113_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_113_0_bool = False
            print('[qlex_double_113] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_113_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_113_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_113_0_bool = True
            print('[qlex_double_113] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_113_0_bool) + ']')

def qlex_double_114_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_114'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_114_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_114_0_bool = False
            print('[qlex_double_114] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_114_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_114_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_114_0_bool = True
            print('[qlex_double_114] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_114_0_bool) + ']')

def qlex_double_115_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_115'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_115_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_115_0_bool = False
            print('[qlex_double_115] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_115_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_115_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_115_0_bool = True
            print('[qlex_double_115] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_115_0_bool) + ']')

def qlex_double_116_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_116'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_116_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_116_0_bool = False
            print('[qlex_double_116] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_116_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_116_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_116_0_bool = True
            print('[qlex_double_116] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_116_0_bool) + ']')

def qlex_double_117_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_117'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_117_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_117_0_bool = False
            print('[qlex_double_117] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_117_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_117_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_117_0_bool = True
            print('[qlex_double_117] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_117_0_bool) + ']')

def qlex_double_118_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_118'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_118_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_118_0_bool = False
            print('[qlex_double_118] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_118_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_118_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_118_0_bool = True
            print('[qlex_double_118] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_118_0_bool) + ']')

def qlex_double_119_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_119'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_119_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_119_0_bool = False
            print('[qlex_double_119] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_119_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_119_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_119_0_bool = True
            print('[qlex_double_119] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_119_0_bool) + ']')

def qlex_double_120_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_120'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_120_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_120_0_bool = False
            print('[qlex_double_120] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_120_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_120_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_120_0_bool = True
            print('[qlex_double_120] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_120_0_bool) + ']')

def qlex_double_121_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_121'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_121_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_121_0_bool = False
            print('[qlex_double_121] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_121_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_121_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_121_0_bool = True
            print('[qlex_double_121] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_121_0_bool) + ']')

def qlex_double_122_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_122'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_122_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_122_0_bool = False
            print('[qlex_double_122] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_122_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_122_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_122_0_bool = True
            print('[qlex_double_122] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_122_0_bool) + ']')

def qlex_double_123_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_123'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_123_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_123_0_bool = False
            print('[qlex_double_123] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_123_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_123_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_123_0_bool = True
            print('[qlex_double_123] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_123_0_bool) + ']')

def qlex_double_124_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_124'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_124_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_124_0_bool = False
            print('[qlex_double_124] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_124_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_124_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_124_0_bool = True
            print('[qlex_double_124] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_124_0_bool) + ']')

def qlex_double_125_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_125'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_125_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_125_0_bool = False
            print('[qlex_double_125] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_125_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_125_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_125_0_bool = True
            print('[qlex_double_125] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_125_0_bool) + ']')

def qlex_double_126_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_126'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_126_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_126_0_bool = False
            print('[qlex_double_126] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_126_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_126_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_126_0_bool = True
            print('[qlex_double_126] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_126_0_bool) + ']')

def qlex_double_127_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_127'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_127_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_127_0_bool = False
            print('[qlex_double_127] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_127_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_127_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_127_0_bool = True
            print('[qlex_double_127] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_127_0_bool) + ']')

def qlex_double_128_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_128'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_128_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_128_0_bool = False
            print('[qlex_double_128] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_128_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_128_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_128_0_bool = True
            print('[qlex_double_128] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_128_0_bool) + ']')

def qlex_double_129_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_129'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_129_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_129_0_bool = False
            print('[qlex_double_129] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_129_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_129_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_129_0_bool = True
            print('[qlex_double_129] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_129_0_bool) + ']')

def qlex_double_130_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_130'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_130_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_130_0_bool = False
            print('[qlex_double_130] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_130_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_130_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_130_0_bool = True
            print('[qlex_double_130] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_130_0_bool) + ']')

def qlex_double_131_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_131'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_131_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_131_0_bool = False
            print('[qlex_double_131] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_131_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_131_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_131_0_bool = True
            print('[qlex_double_131] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_131_0_bool) + ']')

def qlex_double_132_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_132'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_132_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_132_0_bool = False
            print('[qlex_double_132] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_132_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_132_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_132_0_bool = True
            print('[qlex_double_132] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_132_0_bool) + ']')

def qlex_double_133_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_133'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_133_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_133_0_bool = False
            print('[qlex_double_133] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_133_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_133_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_133_0_bool = True
            print('[qlex_double_133] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_133_0_bool) + ']')

def qlex_double_134_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_134'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_134_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_134_0_bool = False
            print('[qlex_double_134] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_134_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_134_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_134_0_bool = True
            print('[qlex_double_134] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_134_0_bool) + ']')

def qlex_double_135_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_135'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_135_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_135_0_bool = False
            print('[qlex_double_135] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_135_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_135_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_135_0_bool = True
            print('[qlex_double_135] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_135_0_bool) + ']')

def qlex_double_136_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_136'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_136_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_136_0_bool = False
            print('[qlex_double_136] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_136_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_136_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_136_0_bool = True
            print('[qlex_double_136] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_136_0_bool) + ']')

def qlex_double_137_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_137'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_137_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_137_0_bool = False
            print('[qlex_double_137] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_137_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_137_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_137_0_bool = True
            print('[qlex_double_137] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_137_0_bool) + ']')

def qlex_double_138_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_138'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_138_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_138_0_bool = False
            print('[qlex_double_138] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_138_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_138_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_138_0_bool = True
            print('[qlex_double_138] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_138_0_bool) + ']')

def qlex_double_139_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_139'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_139_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_139_0_bool = False
            print('[qlex_double_139] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_139_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_139_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_139_0_bool = True
            print('[qlex_double_139] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_139_0_bool) + ']')

def qlex_double_140_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_140'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_140_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_140_0_bool = False
            print('[qlex_double_140] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_140_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_140_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_140_0_bool = True
            print('[qlex_double_140] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_140_0_bool) + ']')

def qlex_double_141_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_141'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_141_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_141_0_bool = False
            print('[qlex_double_141] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_141_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_141_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_141_0_bool = True
            print('[qlex_double_141] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_141_0_bool) + ']')

def qlex_double_142_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_142'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_142_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_142_0_bool = False
            print('[qlex_double_142] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_142_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_142_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_142_0_bool = True
            print('[qlex_double_142] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_142_0_bool) + ']')

def qlex_double_143_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_double_143'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_double_bool.qlex_double_143_0_bool is True:
            auto_gen_qle_double_bool.qlex_double_143_0_bool = False
            print('[qlex_double_143] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_143_0_bool) + ']')

        elif auto_gen_qle_double_bool.qlex_double_143_0_bool is False:
            auto_gen_qle_double_bool.qlex_double_143_0_bool = True
            print('[qlex_double_143] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_double_bool.qlex_double_143_0_bool) + ']')


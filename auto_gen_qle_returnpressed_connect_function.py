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

def qlex_0_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_0'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_0_0_bool is True:
            auto_gen_qle_bool.qlex_0_0_bool = False
            print('[qlex_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_0_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_0_0_bool is False:
            auto_gen_qle_bool.qlex_0_0_bool = True
            print('[qlex_0] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_0_0_bool) + ']')

def qlex_1_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_1'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_1_0_bool is True:
            auto_gen_qle_bool.qlex_1_0_bool = False
            print('[qlex_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_1_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_1_0_bool is False:
            auto_gen_qle_bool.qlex_1_0_bool = True
            print('[qlex_1] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_1_0_bool) + ']')

def qlex_2_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_2'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_2_0_bool is True:
            auto_gen_qle_bool.qlex_2_0_bool = False
            print('[qlex_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_2_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_2_0_bool is False:
            auto_gen_qle_bool.qlex_2_0_bool = True
            print('[qlex_2] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_2_0_bool) + ']')

def qlex_3_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_3'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_3_0_bool is True:
            auto_gen_qle_bool.qlex_3_0_bool = False
            print('[qlex_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_3_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_3_0_bool is False:
            auto_gen_qle_bool.qlex_3_0_bool = True
            print('[qlex_3] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_3_0_bool) + ']')

def qlex_4_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_4'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_4_0_bool is True:
            auto_gen_qle_bool.qlex_4_0_bool = False
            print('[qlex_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_4_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_4_0_bool is False:
            auto_gen_qle_bool.qlex_4_0_bool = True
            print('[qlex_4] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_4_0_bool) + ']')

def qlex_5_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_5'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_5_0_bool is True:
            auto_gen_qle_bool.qlex_5_0_bool = False
            print('[qlex_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_5_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_5_0_bool is False:
            auto_gen_qle_bool.qlex_5_0_bool = True
            print('[qlex_5] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_5_0_bool) + ']')

def qlex_6_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_6'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_6_0_bool is True:
            auto_gen_qle_bool.qlex_6_0_bool = False
            print('[qlex_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_6_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_6_0_bool is False:
            auto_gen_qle_bool.qlex_6_0_bool = True
            print('[qlex_6] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_6_0_bool) + ']')

def qlex_7_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_7'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_7_0_bool is True:
            auto_gen_qle_bool.qlex_7_0_bool = False
            print('[qlex_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_7_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_7_0_bool is False:
            auto_gen_qle_bool.qlex_7_0_bool = True
            print('[qlex_7] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_7_0_bool) + ']')

def qlex_8_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_8'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_8_0_bool is True:
            auto_gen_qle_bool.qlex_8_0_bool = False
            print('[qlex_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_8_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_8_0_bool is False:
            auto_gen_qle_bool.qlex_8_0_bool = True
            print('[qlex_8] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_8_0_bool) + ']')

def qlex_9_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_9'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_9_0_bool is True:
            auto_gen_qle_bool.qlex_9_0_bool = False
            print('[qlex_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_9_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_9_0_bool is False:
            auto_gen_qle_bool.qlex_9_0_bool = True
            print('[qlex_9] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_9_0_bool) + ']')

def qlex_10_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_10'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_10_0_bool is True:
            auto_gen_qle_bool.qlex_10_0_bool = False
            print('[qlex_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_10_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_10_0_bool is False:
            auto_gen_qle_bool.qlex_10_0_bool = True
            print('[qlex_10] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_10_0_bool) + ']')

def qlex_11_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_11'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_11_0_bool is True:
            auto_gen_qle_bool.qlex_11_0_bool = False
            print('[qlex_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_11_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_11_0_bool is False:
            auto_gen_qle_bool.qlex_11_0_bool = True
            print('[qlex_11] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_11_0_bool) + ']')

def qlex_12_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_12'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_12_0_bool is True:
            auto_gen_qle_bool.qlex_12_0_bool = False
            print('[qlex_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_12_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_12_0_bool is False:
            auto_gen_qle_bool.qlex_12_0_bool = True
            print('[qlex_12] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_12_0_bool) + ']')

def qlex_13_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_13'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_13_0_bool is True:
            auto_gen_qle_bool.qlex_13_0_bool = False
            print('[qlex_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_13_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_13_0_bool is False:
            auto_gen_qle_bool.qlex_13_0_bool = True
            print('[qlex_13] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_13_0_bool) + ']')

def qlex_14_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_14'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_14_0_bool is True:
            auto_gen_qle_bool.qlex_14_0_bool = False
            print('[qlex_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_14_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_14_0_bool is False:
            auto_gen_qle_bool.qlex_14_0_bool = True
            print('[qlex_14] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_14_0_bool) + ']')

def qlex_15_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_15'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_15_0_bool is True:
            auto_gen_qle_bool.qlex_15_0_bool = False
            print('[qlex_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_15_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_15_0_bool is False:
            auto_gen_qle_bool.qlex_15_0_bool = True
            print('[qlex_15] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_15_0_bool) + ']')

def qlex_16_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_16'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_16_0_bool is True:
            auto_gen_qle_bool.qlex_16_0_bool = False
            print('[qlex_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_16_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_16_0_bool is False:
            auto_gen_qle_bool.qlex_16_0_bool = True
            print('[qlex_16] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_16_0_bool) + ']')

def qlex_17_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_17'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_17_0_bool is True:
            auto_gen_qle_bool.qlex_17_0_bool = False
            print('[qlex_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_17_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_17_0_bool is False:
            auto_gen_qle_bool.qlex_17_0_bool = True
            print('[qlex_17] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_17_0_bool) + ']')

def qlex_18_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_18'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_18_0_bool is True:
            auto_gen_qle_bool.qlex_18_0_bool = False
            print('[qlex_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_18_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_18_0_bool is False:
            auto_gen_qle_bool.qlex_18_0_bool = True
            print('[qlex_18] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_18_0_bool) + ']')

def qlex_19_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_19'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_19_0_bool is True:
            auto_gen_qle_bool.qlex_19_0_bool = False
            print('[qlex_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_19_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_19_0_bool is False:
            auto_gen_qle_bool.qlex_19_0_bool = True
            print('[qlex_19] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_19_0_bool) + ']')

def qlex_20_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_20'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_20_0_bool is True:
            auto_gen_qle_bool.qlex_20_0_bool = False
            print('[qlex_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_20_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_20_0_bool is False:
            auto_gen_qle_bool.qlex_20_0_bool = True
            print('[qlex_20] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_20_0_bool) + ']')

def qlex_21_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_21'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_21_0_bool is True:
            auto_gen_qle_bool.qlex_21_0_bool = False
            print('[qlex_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_21_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_21_0_bool is False:
            auto_gen_qle_bool.qlex_21_0_bool = True
            print('[qlex_21] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_21_0_bool) + ']')

def qlex_22_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_22'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_22_0_bool is True:
            auto_gen_qle_bool.qlex_22_0_bool = False
            print('[qlex_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_22_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_22_0_bool is False:
            auto_gen_qle_bool.qlex_22_0_bool = True
            print('[qlex_22] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_22_0_bool) + ']')

def qlex_23_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_23'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_23_0_bool is True:
            auto_gen_qle_bool.qlex_23_0_bool = False
            print('[qlex_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_23_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_23_0_bool is False:
            auto_gen_qle_bool.qlex_23_0_bool = True
            print('[qlex_23] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_23_0_bool) + ']')

def qlex_24_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_24'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_24_0_bool is True:
            auto_gen_qle_bool.qlex_24_0_bool = False
            print('[qlex_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_24_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_24_0_bool is False:
            auto_gen_qle_bool.qlex_24_0_bool = True
            print('[qlex_24] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_24_0_bool) + ']')

def qlex_25_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_25'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_25_0_bool is True:
            auto_gen_qle_bool.qlex_25_0_bool = False
            print('[qlex_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_25_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_25_0_bool is False:
            auto_gen_qle_bool.qlex_25_0_bool = True
            print('[qlex_25] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_25_0_bool) + ']')

def qlex_26_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_26'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_26_0_bool is True:
            auto_gen_qle_bool.qlex_26_0_bool = False
            print('[qlex_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_26_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_26_0_bool is False:
            auto_gen_qle_bool.qlex_26_0_bool = True
            print('[qlex_26] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_26_0_bool) + ']')

def qlex_27_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_27'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_27_0_bool is True:
            auto_gen_qle_bool.qlex_27_0_bool = False
            print('[qlex_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_27_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_27_0_bool is False:
            auto_gen_qle_bool.qlex_27_0_bool = True
            print('[qlex_27] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_27_0_bool) + ']')

def qlex_28_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_28'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_28_0_bool is True:
            auto_gen_qle_bool.qlex_28_0_bool = False
            print('[qlex_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_28_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_28_0_bool is False:
            auto_gen_qle_bool.qlex_28_0_bool = True
            print('[qlex_28] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_28_0_bool) + ']')

def qlex_29_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_29'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_29_0_bool is True:
            auto_gen_qle_bool.qlex_29_0_bool = False
            print('[qlex_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_29_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_29_0_bool is False:
            auto_gen_qle_bool.qlex_29_0_bool = True
            print('[qlex_29] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_29_0_bool) + ']')

def qlex_30_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_30'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_30_0_bool is True:
            auto_gen_qle_bool.qlex_30_0_bool = False
            print('[qlex_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_30_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_30_0_bool is False:
            auto_gen_qle_bool.qlex_30_0_bool = True
            print('[qlex_30] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_30_0_bool) + ']')

def qlex_31_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_31'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_31_0_bool is True:
            auto_gen_qle_bool.qlex_31_0_bool = False
            print('[qlex_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_31_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_31_0_bool is False:
            auto_gen_qle_bool.qlex_31_0_bool = True
            print('[qlex_31] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_31_0_bool) + ']')

def qlex_32_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_32'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_32_0_bool is True:
            auto_gen_qle_bool.qlex_32_0_bool = False
            print('[qlex_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_32_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_32_0_bool is False:
            auto_gen_qle_bool.qlex_32_0_bool = True
            print('[qlex_32] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_32_0_bool) + ']')

def qlex_33_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_33'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_33_0_bool is True:
            auto_gen_qle_bool.qlex_33_0_bool = False
            print('[qlex_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_33_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_33_0_bool is False:
            auto_gen_qle_bool.qlex_33_0_bool = True
            print('[qlex_33] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_33_0_bool) + ']')

def qlex_34_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_34'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_34_0_bool is True:
            auto_gen_qle_bool.qlex_34_0_bool = False
            print('[qlex_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_34_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_34_0_bool is False:
            auto_gen_qle_bool.qlex_34_0_bool = True
            print('[qlex_34] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_34_0_bool) + ']')

def qlex_35_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_35'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_35_0_bool is True:
            auto_gen_qle_bool.qlex_35_0_bool = False
            print('[qlex_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_35_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_35_0_bool is False:
            auto_gen_qle_bool.qlex_35_0_bool = True
            print('[qlex_35] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_35_0_bool) + ']')

def qlex_36_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_36'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_36_0_bool is True:
            auto_gen_qle_bool.qlex_36_0_bool = False
            print('[qlex_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_36_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_36_0_bool is False:
            auto_gen_qle_bool.qlex_36_0_bool = True
            print('[qlex_36] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_36_0_bool) + ']')

def qlex_37_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_37'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_37_0_bool is True:
            auto_gen_qle_bool.qlex_37_0_bool = False
            print('[qlex_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_37_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_37_0_bool is False:
            auto_gen_qle_bool.qlex_37_0_bool = True
            print('[qlex_37] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_37_0_bool) + ']')

def qlex_38_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_38'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_38_0_bool is True:
            auto_gen_qle_bool.qlex_38_0_bool = False
            print('[qlex_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_38_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_38_0_bool is False:
            auto_gen_qle_bool.qlex_38_0_bool = True
            print('[qlex_38] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_38_0_bool) + ']')

def qlex_39_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_39'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_39_0_bool is True:
            auto_gen_qle_bool.qlex_39_0_bool = False
            print('[qlex_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_39_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_39_0_bool is False:
            auto_gen_qle_bool.qlex_39_0_bool = True
            print('[qlex_39] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_39_0_bool) + ']')

def qlex_40_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_40'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_40_0_bool is True:
            auto_gen_qle_bool.qlex_40_0_bool = False
            print('[qlex_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_40_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_40_0_bool is False:
            auto_gen_qle_bool.qlex_40_0_bool = True
            print('[qlex_40] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_40_0_bool) + ']')

def qlex_41_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_41'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_41_0_bool is True:
            auto_gen_qle_bool.qlex_41_0_bool = False
            print('[qlex_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_41_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_41_0_bool is False:
            auto_gen_qle_bool.qlex_41_0_bool = True
            print('[qlex_41] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_41_0_bool) + ']')

def qlex_42_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_42'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_42_0_bool is True:
            auto_gen_qle_bool.qlex_42_0_bool = False
            print('[qlex_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_42_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_42_0_bool is False:
            auto_gen_qle_bool.qlex_42_0_bool = True
            print('[qlex_42] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_42_0_bool) + ']')

def qlex_43_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_43'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_43_0_bool is True:
            auto_gen_qle_bool.qlex_43_0_bool = False
            print('[qlex_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_43_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_43_0_bool is False:
            auto_gen_qle_bool.qlex_43_0_bool = True
            print('[qlex_43] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_43_0_bool) + ']')

def qlex_44_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_44'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_44_0_bool is True:
            auto_gen_qle_bool.qlex_44_0_bool = False
            print('[qlex_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_44_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_44_0_bool is False:
            auto_gen_qle_bool.qlex_44_0_bool = True
            print('[qlex_44] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_44_0_bool) + ']')

def qlex_45_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_45'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_45_0_bool is True:
            auto_gen_qle_bool.qlex_45_0_bool = False
            print('[qlex_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_45_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_45_0_bool is False:
            auto_gen_qle_bool.qlex_45_0_bool = True
            print('[qlex_45] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_45_0_bool) + ']')

def qlex_46_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_46'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_46_0_bool is True:
            auto_gen_qle_bool.qlex_46_0_bool = False
            print('[qlex_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_46_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_46_0_bool is False:
            auto_gen_qle_bool.qlex_46_0_bool = True
            print('[qlex_46] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_46_0_bool) + ']')

def qlex_47_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_47'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_47_0_bool is True:
            auto_gen_qle_bool.qlex_47_0_bool = False
            print('[qlex_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_47_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_47_0_bool is False:
            auto_gen_qle_bool.qlex_47_0_bool = True
            print('[qlex_47] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_47_0_bool) + ']')

def qlex_48_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_48'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_48_0_bool is True:
            auto_gen_qle_bool.qlex_48_0_bool = False
            print('[qlex_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_48_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_48_0_bool is False:
            auto_gen_qle_bool.qlex_48_0_bool = True
            print('[qlex_48] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_48_0_bool) + ']')

def qlex_49_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_49'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_49_0_bool is True:
            auto_gen_qle_bool.qlex_49_0_bool = False
            print('[qlex_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_49_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_49_0_bool is False:
            auto_gen_qle_bool.qlex_49_0_bool = True
            print('[qlex_49] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_49_0_bool) + ']')

def qlex_50_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_50'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_50_0_bool is True:
            auto_gen_qle_bool.qlex_50_0_bool = False
            print('[qlex_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_50_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_50_0_bool is False:
            auto_gen_qle_bool.qlex_50_0_bool = True
            print('[qlex_50] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_50_0_bool) + ']')

def qlex_51_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_51'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_51_0_bool is True:
            auto_gen_qle_bool.qlex_51_0_bool = False
            print('[qlex_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_51_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_51_0_bool is False:
            auto_gen_qle_bool.qlex_51_0_bool = True
            print('[qlex_51] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_51_0_bool) + ']')

def qlex_52_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_52'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_52_0_bool is True:
            auto_gen_qle_bool.qlex_52_0_bool = False
            print('[qlex_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_52_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_52_0_bool is False:
            auto_gen_qle_bool.qlex_52_0_bool = True
            print('[qlex_52] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_52_0_bool) + ']')

def qlex_53_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_53'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_53_0_bool is True:
            auto_gen_qle_bool.qlex_53_0_bool = False
            print('[qlex_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_53_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_53_0_bool is False:
            auto_gen_qle_bool.qlex_53_0_bool = True
            print('[qlex_53] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_53_0_bool) + ']')

def qlex_54_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_54'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_54_0_bool is True:
            auto_gen_qle_bool.qlex_54_0_bool = False
            print('[qlex_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_54_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_54_0_bool is False:
            auto_gen_qle_bool.qlex_54_0_bool = True
            print('[qlex_54] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_54_0_bool) + ']')

def qlex_55_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_55'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_55_0_bool is True:
            auto_gen_qle_bool.qlex_55_0_bool = False
            print('[qlex_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_55_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_55_0_bool is False:
            auto_gen_qle_bool.qlex_55_0_bool = True
            print('[qlex_55] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_55_0_bool) + ']')

def qlex_56_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_56'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_56_0_bool is True:
            auto_gen_qle_bool.qlex_56_0_bool = False
            print('[qlex_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_56_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_56_0_bool is False:
            auto_gen_qle_bool.qlex_56_0_bool = True
            print('[qlex_56] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_56_0_bool) + ']')

def qlex_57_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_57'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_57_0_bool is True:
            auto_gen_qle_bool.qlex_57_0_bool = False
            print('[qlex_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_57_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_57_0_bool is False:
            auto_gen_qle_bool.qlex_57_0_bool = True
            print('[qlex_57] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_57_0_bool) + ']')

def qlex_58_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_58'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_58_0_bool is True:
            auto_gen_qle_bool.qlex_58_0_bool = False
            print('[qlex_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_58_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_58_0_bool is False:
            auto_gen_qle_bool.qlex_58_0_bool = True
            print('[qlex_58] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_58_0_bool) + ']')

def qlex_59_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_59'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_59_0_bool is True:
            auto_gen_qle_bool.qlex_59_0_bool = False
            print('[qlex_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_59_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_59_0_bool is False:
            auto_gen_qle_bool.qlex_59_0_bool = True
            print('[qlex_59] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_59_0_bool) + ']')

def qlex_60_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_60'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_60_0_bool is True:
            auto_gen_qle_bool.qlex_60_0_bool = False
            print('[qlex_60] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_60_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_60_0_bool is False:
            auto_gen_qle_bool.qlex_60_0_bool = True
            print('[qlex_60] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_60_0_bool) + ']')

def qlex_61_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_61'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_61_0_bool is True:
            auto_gen_qle_bool.qlex_61_0_bool = False
            print('[qlex_61] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_61_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_61_0_bool is False:
            auto_gen_qle_bool.qlex_61_0_bool = True
            print('[qlex_61] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_61_0_bool) + ']')

def qlex_62_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_62'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_62_0_bool is True:
            auto_gen_qle_bool.qlex_62_0_bool = False
            print('[qlex_62] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_62_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_62_0_bool is False:
            auto_gen_qle_bool.qlex_62_0_bool = True
            print('[qlex_62] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_62_0_bool) + ']')

def qlex_63_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_63'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_63_0_bool is True:
            auto_gen_qle_bool.qlex_63_0_bool = False
            print('[qlex_63] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_63_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_63_0_bool is False:
            auto_gen_qle_bool.qlex_63_0_bool = True
            print('[qlex_63] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_63_0_bool) + ']')

def qlex_64_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_64'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_64_0_bool is True:
            auto_gen_qle_bool.qlex_64_0_bool = False
            print('[qlex_64] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_64_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_64_0_bool is False:
            auto_gen_qle_bool.qlex_64_0_bool = True
            print('[qlex_64] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_64_0_bool) + ']')

def qlex_65_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_65'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_65_0_bool is True:
            auto_gen_qle_bool.qlex_65_0_bool = False
            print('[qlex_65] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_65_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_65_0_bool is False:
            auto_gen_qle_bool.qlex_65_0_bool = True
            print('[qlex_65] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_65_0_bool) + ']')

def qlex_66_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_66'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_66_0_bool is True:
            auto_gen_qle_bool.qlex_66_0_bool = False
            print('[qlex_66] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_66_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_66_0_bool is False:
            auto_gen_qle_bool.qlex_66_0_bool = True
            print('[qlex_66] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_66_0_bool) + ']')

def qlex_67_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_67'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_67_0_bool is True:
            auto_gen_qle_bool.qlex_67_0_bool = False
            print('[qlex_67] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_67_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_67_0_bool is False:
            auto_gen_qle_bool.qlex_67_0_bool = True
            print('[qlex_67] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_67_0_bool) + ']')

def qlex_68_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_68'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_68_0_bool is True:
            auto_gen_qle_bool.qlex_68_0_bool = False
            print('[qlex_68] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_68_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_68_0_bool is False:
            auto_gen_qle_bool.qlex_68_0_bool = True
            print('[qlex_68] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_68_0_bool) + ']')

def qlex_69_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_69'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_69_0_bool is True:
            auto_gen_qle_bool.qlex_69_0_bool = False
            print('[qlex_69] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_69_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_69_0_bool is False:
            auto_gen_qle_bool.qlex_69_0_bool = True
            print('[qlex_69] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_69_0_bool) + ']')

def qlex_70_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_70'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_70_0_bool is True:
            auto_gen_qle_bool.qlex_70_0_bool = False
            print('[qlex_70] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_70_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_70_0_bool is False:
            auto_gen_qle_bool.qlex_70_0_bool = True
            print('[qlex_70] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_70_0_bool) + ']')

def qlex_71_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_71'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_71_0_bool is True:
            auto_gen_qle_bool.qlex_71_0_bool = False
            print('[qlex_71] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_71_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_71_0_bool is False:
            auto_gen_qle_bool.qlex_71_0_bool = True
            print('[qlex_71] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_71_0_bool) + ']')

def qlex_72_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_72'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_72_0_bool is True:
            auto_gen_qle_bool.qlex_72_0_bool = False
            print('[qlex_72] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_72_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_72_0_bool is False:
            auto_gen_qle_bool.qlex_72_0_bool = True
            print('[qlex_72] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_72_0_bool) + ']')

def qlex_73_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_73'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_73_0_bool is True:
            auto_gen_qle_bool.qlex_73_0_bool = False
            print('[qlex_73] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_73_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_73_0_bool is False:
            auto_gen_qle_bool.qlex_73_0_bool = True
            print('[qlex_73] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_73_0_bool) + ']')

def qlex_74_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_74'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_74_0_bool is True:
            auto_gen_qle_bool.qlex_74_0_bool = False
            print('[qlex_74] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_74_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_74_0_bool is False:
            auto_gen_qle_bool.qlex_74_0_bool = True
            print('[qlex_74] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_74_0_bool) + ']')

def qlex_75_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_75'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_75_0_bool is True:
            auto_gen_qle_bool.qlex_75_0_bool = False
            print('[qlex_75] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_75_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_75_0_bool is False:
            auto_gen_qle_bool.qlex_75_0_bool = True
            print('[qlex_75] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_75_0_bool) + ']')

def qlex_76_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_76'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_76_0_bool is True:
            auto_gen_qle_bool.qlex_76_0_bool = False
            print('[qlex_76] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_76_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_76_0_bool is False:
            auto_gen_qle_bool.qlex_76_0_bool = True
            print('[qlex_76] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_76_0_bool) + ']')

def qlex_77_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_77'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_77_0_bool is True:
            auto_gen_qle_bool.qlex_77_0_bool = False
            print('[qlex_77] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_77_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_77_0_bool is False:
            auto_gen_qle_bool.qlex_77_0_bool = True
            print('[qlex_77] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_77_0_bool) + ']')

def qlex_78_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_78'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_78_0_bool is True:
            auto_gen_qle_bool.qlex_78_0_bool = False
            print('[qlex_78] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_78_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_78_0_bool is False:
            auto_gen_qle_bool.qlex_78_0_bool = True
            print('[qlex_78] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_78_0_bool) + ']')

def qlex_79_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_79'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_79_0_bool is True:
            auto_gen_qle_bool.qlex_79_0_bool = False
            print('[qlex_79] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_79_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_79_0_bool is False:
            auto_gen_qle_bool.qlex_79_0_bool = True
            print('[qlex_79] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_79_0_bool) + ']')

def qlex_80_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_80'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_80_0_bool is True:
            auto_gen_qle_bool.qlex_80_0_bool = False
            print('[qlex_80] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_80_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_80_0_bool is False:
            auto_gen_qle_bool.qlex_80_0_bool = True
            print('[qlex_80] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_80_0_bool) + ']')

def qlex_81_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_81'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_81_0_bool is True:
            auto_gen_qle_bool.qlex_81_0_bool = False
            print('[qlex_81] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_81_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_81_0_bool is False:
            auto_gen_qle_bool.qlex_81_0_bool = True
            print('[qlex_81] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_81_0_bool) + ']')

def qlex_82_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_82'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_82_0_bool is True:
            auto_gen_qle_bool.qlex_82_0_bool = False
            print('[qlex_82] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_82_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_82_0_bool is False:
            auto_gen_qle_bool.qlex_82_0_bool = True
            print('[qlex_82] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_82_0_bool) + ']')

def qlex_83_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_83'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_83_0_bool is True:
            auto_gen_qle_bool.qlex_83_0_bool = False
            print('[qlex_83] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_83_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_83_0_bool is False:
            auto_gen_qle_bool.qlex_83_0_bool = True
            print('[qlex_83] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_83_0_bool) + ']')

def qlex_84_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_84'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_84_0_bool is True:
            auto_gen_qle_bool.qlex_84_0_bool = False
            print('[qlex_84] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_84_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_84_0_bool is False:
            auto_gen_qle_bool.qlex_84_0_bool = True
            print('[qlex_84] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_84_0_bool) + ']')

def qlex_85_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_85'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_85_0_bool is True:
            auto_gen_qle_bool.qlex_85_0_bool = False
            print('[qlex_85] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_85_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_85_0_bool is False:
            auto_gen_qle_bool.qlex_85_0_bool = True
            print('[qlex_85] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_85_0_bool) + ']')

def qlex_86_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_86'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_86_0_bool is True:
            auto_gen_qle_bool.qlex_86_0_bool = False
            print('[qlex_86] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_86_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_86_0_bool is False:
            auto_gen_qle_bool.qlex_86_0_bool = True
            print('[qlex_86] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_86_0_bool) + ']')

def qlex_87_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_87'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_87_0_bool is True:
            auto_gen_qle_bool.qlex_87_0_bool = False
            print('[qlex_87] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_87_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_87_0_bool is False:
            auto_gen_qle_bool.qlex_87_0_bool = True
            print('[qlex_87] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_87_0_bool) + ']')

def qlex_88_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_88'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_88_0_bool is True:
            auto_gen_qle_bool.qlex_88_0_bool = False
            print('[qlex_88] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_88_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_88_0_bool is False:
            auto_gen_qle_bool.qlex_88_0_bool = True
            print('[qlex_88] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_88_0_bool) + ']')

def qlex_89_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_89'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_89_0_bool is True:
            auto_gen_qle_bool.qlex_89_0_bool = False
            print('[qlex_89] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_89_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_89_0_bool is False:
            auto_gen_qle_bool.qlex_89_0_bool = True
            print('[qlex_89] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_89_0_bool) + ']')

def qlex_90_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_90'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_90_0_bool is True:
            auto_gen_qle_bool.qlex_90_0_bool = False
            print('[qlex_90] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_90_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_90_0_bool is False:
            auto_gen_qle_bool.qlex_90_0_bool = True
            print('[qlex_90] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_90_0_bool) + ']')

def qlex_91_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_91'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_91_0_bool is True:
            auto_gen_qle_bool.qlex_91_0_bool = False
            print('[qlex_91] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_91_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_91_0_bool is False:
            auto_gen_qle_bool.qlex_91_0_bool = True
            print('[qlex_91] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_91_0_bool) + ']')

def qlex_92_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_92'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_92_0_bool is True:
            auto_gen_qle_bool.qlex_92_0_bool = False
            print('[qlex_92] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_92_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_92_0_bool is False:
            auto_gen_qle_bool.qlex_92_0_bool = True
            print('[qlex_92] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_92_0_bool) + ']')

def qlex_93_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_93'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_93_0_bool is True:
            auto_gen_qle_bool.qlex_93_0_bool = False
            print('[qlex_93] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_93_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_93_0_bool is False:
            auto_gen_qle_bool.qlex_93_0_bool = True
            print('[qlex_93] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_93_0_bool) + ']')

def qlex_94_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_94'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_94_0_bool is True:
            auto_gen_qle_bool.qlex_94_0_bool = False
            print('[qlex_94] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_94_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_94_0_bool is False:
            auto_gen_qle_bool.qlex_94_0_bool = True
            print('[qlex_94] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_94_0_bool) + ']')

def qlex_95_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_95'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_95_0_bool is True:
            auto_gen_qle_bool.qlex_95_0_bool = False
            print('[qlex_95] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_95_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_95_0_bool is False:
            auto_gen_qle_bool.qlex_95_0_bool = True
            print('[qlex_95] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_95_0_bool) + ']')

def qlex_96_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_96'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_96_0_bool is True:
            auto_gen_qle_bool.qlex_96_0_bool = False
            print('[qlex_96] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_96_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_96_0_bool is False:
            auto_gen_qle_bool.qlex_96_0_bool = True
            print('[qlex_96] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_96_0_bool) + ']')

def qlex_97_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_97'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_97_0_bool is True:
            auto_gen_qle_bool.qlex_97_0_bool = False
            print('[qlex_97] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_97_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_97_0_bool is False:
            auto_gen_qle_bool.qlex_97_0_bool = True
            print('[qlex_97] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_97_0_bool) + ']')

def qlex_98_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_98'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_98_0_bool is True:
            auto_gen_qle_bool.qlex_98_0_bool = False
            print('[qlex_98] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_98_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_98_0_bool is False:
            auto_gen_qle_bool.qlex_98_0_bool = True
            print('[qlex_98] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_98_0_bool) + ']')

def qlex_99_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_99'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_99_0_bool is True:
            auto_gen_qle_bool.qlex_99_0_bool = False
            print('[qlex_99] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_99_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_99_0_bool is False:
            auto_gen_qle_bool.qlex_99_0_bool = True
            print('[qlex_99] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_99_0_bool) + ']')

def qlex_100_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_100'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_100_0_bool is True:
            auto_gen_qle_bool.qlex_100_0_bool = False
            print('[qlex_100] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_100_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_100_0_bool is False:
            auto_gen_qle_bool.qlex_100_0_bool = True
            print('[qlex_100] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_100_0_bool) + ']')

def qlex_101_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_101'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_101_0_bool is True:
            auto_gen_qle_bool.qlex_101_0_bool = False
            print('[qlex_101] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_101_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_101_0_bool is False:
            auto_gen_qle_bool.qlex_101_0_bool = True
            print('[qlex_101] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_101_0_bool) + ']')

def qlex_102_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_102'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_102_0_bool is True:
            auto_gen_qle_bool.qlex_102_0_bool = False
            print('[qlex_102] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_102_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_102_0_bool is False:
            auto_gen_qle_bool.qlex_102_0_bool = True
            print('[qlex_102] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_102_0_bool) + ']')

def qlex_103_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_103'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_103_0_bool is True:
            auto_gen_qle_bool.qlex_103_0_bool = False
            print('[qlex_103] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_103_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_103_0_bool is False:
            auto_gen_qle_bool.qlex_103_0_bool = True
            print('[qlex_103] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_103_0_bool) + ']')

def qlex_104_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_104'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_104_0_bool is True:
            auto_gen_qle_bool.qlex_104_0_bool = False
            print('[qlex_104] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_104_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_104_0_bool is False:
            auto_gen_qle_bool.qlex_104_0_bool = True
            print('[qlex_104] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_104_0_bool) + ']')

def qlex_105_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_105'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_105_0_bool is True:
            auto_gen_qle_bool.qlex_105_0_bool = False
            print('[qlex_105] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_105_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_105_0_bool is False:
            auto_gen_qle_bool.qlex_105_0_bool = True
            print('[qlex_105] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_105_0_bool) + ']')

def qlex_106_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_106'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_106_0_bool is True:
            auto_gen_qle_bool.qlex_106_0_bool = False
            print('[qlex_106] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_106_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_106_0_bool is False:
            auto_gen_qle_bool.qlex_106_0_bool = True
            print('[qlex_106] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_106_0_bool) + ']')

def qlex_107_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_107'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_107_0_bool is True:
            auto_gen_qle_bool.qlex_107_0_bool = False
            print('[qlex_107] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_107_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_107_0_bool is False:
            auto_gen_qle_bool.qlex_107_0_bool = True
            print('[qlex_107] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_107_0_bool) + ']')

def qlex_108_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_108'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_108_0_bool is True:
            auto_gen_qle_bool.qlex_108_0_bool = False
            print('[qlex_108] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_108_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_108_0_bool is False:
            auto_gen_qle_bool.qlex_108_0_bool = True
            print('[qlex_108] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_108_0_bool) + ']')

def qlex_109_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_109'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_109_0_bool is True:
            auto_gen_qle_bool.qlex_109_0_bool = False
            print('[qlex_109] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_109_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_109_0_bool is False:
            auto_gen_qle_bool.qlex_109_0_bool = True
            print('[qlex_109] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_109_0_bool) + ']')

def qlex_110_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_110'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_110_0_bool is True:
            auto_gen_qle_bool.qlex_110_0_bool = False
            print('[qlex_110] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_110_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_110_0_bool is False:
            auto_gen_qle_bool.qlex_110_0_bool = True
            print('[qlex_110] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_110_0_bool) + ']')

def qlex_111_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_111'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_111_0_bool is True:
            auto_gen_qle_bool.qlex_111_0_bool = False
            print('[qlex_111] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_111_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_111_0_bool is False:
            auto_gen_qle_bool.qlex_111_0_bool = True
            print('[qlex_111] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_111_0_bool) + ']')

def qlex_112_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_112'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_112_0_bool is True:
            auto_gen_qle_bool.qlex_112_0_bool = False
            print('[qlex_112] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_112_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_112_0_bool is False:
            auto_gen_qle_bool.qlex_112_0_bool = True
            print('[qlex_112] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_112_0_bool) + ']')

def qlex_113_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_113'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_113_0_bool is True:
            auto_gen_qle_bool.qlex_113_0_bool = False
            print('[qlex_113] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_113_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_113_0_bool is False:
            auto_gen_qle_bool.qlex_113_0_bool = True
            print('[qlex_113] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_113_0_bool) + ']')

def qlex_114_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_114'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_114_0_bool is True:
            auto_gen_qle_bool.qlex_114_0_bool = False
            print('[qlex_114] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_114_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_114_0_bool is False:
            auto_gen_qle_bool.qlex_114_0_bool = True
            print('[qlex_114] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_114_0_bool) + ']')

def qlex_115_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_115'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_115_0_bool is True:
            auto_gen_qle_bool.qlex_115_0_bool = False
            print('[qlex_115] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_115_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_115_0_bool is False:
            auto_gen_qle_bool.qlex_115_0_bool = True
            print('[qlex_115] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_115_0_bool) + ']')

def qlex_116_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_116'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_116_0_bool is True:
            auto_gen_qle_bool.qlex_116_0_bool = False
            print('[qlex_116] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_116_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_116_0_bool is False:
            auto_gen_qle_bool.qlex_116_0_bool = True
            print('[qlex_116] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_116_0_bool) + ']')

def qlex_117_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_117'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_117_0_bool is True:
            auto_gen_qle_bool.qlex_117_0_bool = False
            print('[qlex_117] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_117_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_117_0_bool is False:
            auto_gen_qle_bool.qlex_117_0_bool = True
            print('[qlex_117] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_117_0_bool) + ']')

def qlex_118_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_118'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_118_0_bool is True:
            auto_gen_qle_bool.qlex_118_0_bool = False
            print('[qlex_118] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_118_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_118_0_bool is False:
            auto_gen_qle_bool.qlex_118_0_bool = True
            print('[qlex_118] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_118_0_bool) + ']')

def qlex_119_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_119'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_119_0_bool is True:
            auto_gen_qle_bool.qlex_119_0_bool = False
            print('[qlex_119] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_119_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_119_0_bool is False:
            auto_gen_qle_bool.qlex_119_0_bool = True
            print('[qlex_119] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_119_0_bool) + ']')

def qlex_120_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_120'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_120_0_bool is True:
            auto_gen_qle_bool.qlex_120_0_bool = False
            print('[qlex_120] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_120_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_120_0_bool is False:
            auto_gen_qle_bool.qlex_120_0_bool = True
            print('[qlex_120] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_120_0_bool) + ']')

def qlex_121_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_121'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_121_0_bool is True:
            auto_gen_qle_bool.qlex_121_0_bool = False
            print('[qlex_121] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_121_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_121_0_bool is False:
            auto_gen_qle_bool.qlex_121_0_bool = True
            print('[qlex_121] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_121_0_bool) + ']')

def qlex_122_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_122'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_122_0_bool is True:
            auto_gen_qle_bool.qlex_122_0_bool = False
            print('[qlex_122] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_122_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_122_0_bool is False:
            auto_gen_qle_bool.qlex_122_0_bool = True
            print('[qlex_122] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_122_0_bool) + ']')

def qlex_123_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_123'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_123_0_bool is True:
            auto_gen_qle_bool.qlex_123_0_bool = False
            print('[qlex_123] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_123_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_123_0_bool is False:
            auto_gen_qle_bool.qlex_123_0_bool = True
            print('[qlex_123] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_123_0_bool) + ']')

def qlex_124_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_124'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_124_0_bool is True:
            auto_gen_qle_bool.qlex_124_0_bool = False
            print('[qlex_124] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_124_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_124_0_bool is False:
            auto_gen_qle_bool.qlex_124_0_bool = True
            print('[qlex_124] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_124_0_bool) + ']')

def qlex_125_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_125'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_125_0_bool is True:
            auto_gen_qle_bool.qlex_125_0_bool = False
            print('[qlex_125] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_125_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_125_0_bool is False:
            auto_gen_qle_bool.qlex_125_0_bool = True
            print('[qlex_125] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_125_0_bool) + ']')

def qlex_126_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_126'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_126_0_bool is True:
            auto_gen_qle_bool.qlex_126_0_bool = False
            print('[qlex_126] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_126_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_126_0_bool is False:
            auto_gen_qle_bool.qlex_126_0_bool = True
            print('[qlex_126] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_126_0_bool) + ']')

def qlex_127_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_127'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_127_0_bool is True:
            auto_gen_qle_bool.qlex_127_0_bool = False
            print('[qlex_127] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_127_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_127_0_bool is False:
            auto_gen_qle_bool.qlex_127_0_bool = True
            print('[qlex_127] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_127_0_bool) + ']')

def qlex_128_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_128'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_128_0_bool is True:
            auto_gen_qle_bool.qlex_128_0_bool = False
            print('[qlex_128] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_128_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_128_0_bool is False:
            auto_gen_qle_bool.qlex_128_0_bool = True
            print('[qlex_128] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_128_0_bool) + ']')

def qlex_129_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_129'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_129_0_bool is True:
            auto_gen_qle_bool.qlex_129_0_bool = False
            print('[qlex_129] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_129_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_129_0_bool is False:
            auto_gen_qle_bool.qlex_129_0_bool = True
            print('[qlex_129] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_129_0_bool) + ']')

def qlex_130_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_130'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_130_0_bool is True:
            auto_gen_qle_bool.qlex_130_0_bool = False
            print('[qlex_130] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_130_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_130_0_bool is False:
            auto_gen_qle_bool.qlex_130_0_bool = True
            print('[qlex_130] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_130_0_bool) + ']')

def qlex_131_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_131'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_131_0_bool is True:
            auto_gen_qle_bool.qlex_131_0_bool = False
            print('[qlex_131] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_131_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_131_0_bool is False:
            auto_gen_qle_bool.qlex_131_0_bool = True
            print('[qlex_131] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_131_0_bool) + ']')

def qlex_132_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_132'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_132_0_bool is True:
            auto_gen_qle_bool.qlex_132_0_bool = False
            print('[qlex_132] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_132_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_132_0_bool is False:
            auto_gen_qle_bool.qlex_132_0_bool = True
            print('[qlex_132] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_132_0_bool) + ']')

def qlex_133_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_133'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_133_0_bool is True:
            auto_gen_qle_bool.qlex_133_0_bool = False
            print('[qlex_133] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_133_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_133_0_bool is False:
            auto_gen_qle_bool.qlex_133_0_bool = True
            print('[qlex_133] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_133_0_bool) + ']')

def qlex_134_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_134'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_134_0_bool is True:
            auto_gen_qle_bool.qlex_134_0_bool = False
            print('[qlex_134] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_134_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_134_0_bool is False:
            auto_gen_qle_bool.qlex_134_0_bool = True
            print('[qlex_134] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_134_0_bool) + ']')

def qlex_135_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_135'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_135_0_bool is True:
            auto_gen_qle_bool.qlex_135_0_bool = False
            print('[qlex_135] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_135_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_135_0_bool is False:
            auto_gen_qle_bool.qlex_135_0_bool = True
            print('[qlex_135] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_135_0_bool) + ']')

def qlex_136_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_136'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_136_0_bool is True:
            auto_gen_qle_bool.qlex_136_0_bool = False
            print('[qlex_136] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_136_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_136_0_bool is False:
            auto_gen_qle_bool.qlex_136_0_bool = True
            print('[qlex_136] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_136_0_bool) + ']')

def qlex_137_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_137'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_137_0_bool is True:
            auto_gen_qle_bool.qlex_137_0_bool = False
            print('[qlex_137] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_137_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_137_0_bool is False:
            auto_gen_qle_bool.qlex_137_0_bool = True
            print('[qlex_137] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_137_0_bool) + ']')

def qlex_138_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_138'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_138_0_bool is True:
            auto_gen_qle_bool.qlex_138_0_bool = False
            print('[qlex_138] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_138_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_138_0_bool is False:
            auto_gen_qle_bool.qlex_138_0_bool = True
            print('[qlex_138] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_138_0_bool) + ']')

def qlex_139_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_139'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_139_0_bool is True:
            auto_gen_qle_bool.qlex_139_0_bool = False
            print('[qlex_139] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_139_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_139_0_bool is False:
            auto_gen_qle_bool.qlex_139_0_bool = True
            print('[qlex_139] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_139_0_bool) + ']')

def qlex_140_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_140'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_140_0_bool is True:
            auto_gen_qle_bool.qlex_140_0_bool = False
            print('[qlex_140] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_140_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_140_0_bool is False:
            auto_gen_qle_bool.qlex_140_0_bool = True
            print('[qlex_140] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_140_0_bool) + ']')

def qlex_141_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_141'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_141_0_bool is True:
            auto_gen_qle_bool.qlex_141_0_bool = False
            print('[qlex_141] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_141_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_141_0_bool is False:
            auto_gen_qle_bool.qlex_141_0_bool = True
            print('[qlex_141] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_141_0_bool) + ']')

def qlex_142_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_142'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_142_0_bool is True:
            auto_gen_qle_bool.qlex_142_0_bool = False
            print('[qlex_142] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_142_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_142_0_bool is False:
            auto_gen_qle_bool.qlex_142_0_bool = True
            print('[qlex_142] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_142_0_bool) + ']')

def qlex_143_returnPressed_connect_function():
    print(str('[' + str(datetime.datetime.now()) + '] return pressed: qlex_143'))
    if auto_gen_main_page.main_page == 0:
        if auto_gen_qle_bool.qlex_143_0_bool is True:
            auto_gen_qle_bool.qlex_143_0_bool = False
            print('[qlex_143] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_143_0_bool) + ']')

        elif auto_gen_qle_bool.qlex_143_0_bool is False:
            auto_gen_qle_bool.qlex_143_0_bool = True
            print('[qlex_143] [Page ' + str(auto_gen_main_page.main_page) + '] [Bool ' + str(auto_gen_qle_bool.qlex_143_0_bool) + ']')


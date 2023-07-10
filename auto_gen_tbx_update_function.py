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
def tbx_0_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[0].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_0_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[0].stop()

message_0 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_0_timer_append_function():
    global message_0
    global var_tbx
    if message_0:
        var_tbx[0].append(message_0[0])
        message_0.remove(message_0[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_1_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[1].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_1_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[1].stop()

message_1 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_1_timer_append_function():
    global message_1
    global var_tbx
    if message_1:
        var_tbx[1].append(message_1[0])
        message_1.remove(message_1[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_2_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[2].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_2_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[2].stop()

message_2 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_2_timer_append_function():
    global message_2
    global var_tbx
    if message_2:
        var_tbx[2].append(message_2[0])
        message_2.remove(message_2[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_3_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[3].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_3_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[3].stop()

message_3 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_3_timer_append_function():
    global message_3
    global var_tbx
    if message_3:
        var_tbx[3].append(message_3[0])
        message_3.remove(message_3[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_4_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[4].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_4_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[4].stop()

message_4 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_4_timer_append_function():
    global message_4
    global var_tbx
    if message_4:
        var_tbx[4].append(message_4[0])
        message_4.remove(message_4[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_5_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[5].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_5_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[5].stop()

message_5 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_5_timer_append_function():
    global message_5
    global var_tbx
    if message_5:
        var_tbx[5].append(message_5[0])
        message_5.remove(message_5[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_6_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[6].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_6_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[6].stop()

message_6 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_6_timer_append_function():
    global message_6
    global var_tbx
    if message_6:
        var_tbx[6].append(message_6[0])
        message_6.remove(message_6[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_7_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[7].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_7_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[7].stop()

message_7 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_7_timer_append_function():
    global message_7
    global var_tbx
    if message_7:
        var_tbx[7].append(message_7[0])
        message_7.remove(message_7[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_8_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[8].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_8_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[8].stop()

message_8 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_8_timer_append_function():
    global message_8
    global var_tbx
    if message_8:
        var_tbx[8].append(message_8[0])
        message_8.remove(message_8[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_9_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[9].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_9_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[9].stop()

message_9 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_9_timer_append_function():
    global message_9
    global var_tbx
    if message_9:
        var_tbx[9].append(message_9[0])
        message_9.remove(message_9[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_10_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[10].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_10_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[10].stop()

message_10 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_10_timer_append_function():
    global message_10
    global var_tbx
    if message_10:
        var_tbx[10].append(message_10[0])
        message_10.remove(message_10[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_11_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[11].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_11_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[11].stop()

message_11 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_11_timer_append_function():
    global message_11
    global var_tbx
    if message_11:
        var_tbx[11].append(message_11[0])
        message_11.remove(message_11[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_12_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[12].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_12_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[12].stop()

message_12 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_12_timer_append_function():
    global message_12
    global var_tbx
    if message_12:
        var_tbx[12].append(message_12[0])
        message_12.remove(message_12[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_13_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[13].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_13_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[13].stop()

message_13 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_13_timer_append_function():
    global message_13
    global var_tbx
    if message_13:
        var_tbx[13].append(message_13[0])
        message_13.remove(message_13[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_14_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[14].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_14_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[14].stop()

message_14 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_14_timer_append_function():
    global message_14
    global var_tbx
    if message_14:
        var_tbx[14].append(message_14[0])
        message_14.remove(message_14[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_15_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[15].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_15_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[15].stop()

message_15 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_15_timer_append_function():
    global message_15
    global var_tbx
    if message_15:
        var_tbx[15].append(message_15[0])
        message_15.remove(message_15[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_16_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[16].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_16_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[16].stop()

message_16 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_16_timer_append_function():
    global message_16
    global var_tbx
    if message_16:
        var_tbx[16].append(message_16[0])
        message_16.remove(message_16[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_17_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[17].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_17_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[17].stop()

message_17 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_17_timer_append_function():
    global message_17
    global var_tbx
    if message_17:
        var_tbx[17].append(message_17[0])
        message_17.remove(message_17[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_18_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[18].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_18_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[18].stop()

message_18 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_18_timer_append_function():
    global message_18
    global var_tbx
    if message_18:
        var_tbx[18].append(message_18[0])
        message_18.remove(message_18[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_19_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[19].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_19_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[19].stop()

message_19 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_19_timer_append_function():
    global message_19
    global var_tbx
    if message_19:
        var_tbx[19].append(message_19[0])
        message_19.remove(message_19[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_20_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[20].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_20_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[20].stop()

message_20 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_20_timer_append_function():
    global message_20
    global var_tbx
    if message_20:
        var_tbx[20].append(message_20[0])
        message_20.remove(message_20[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_21_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[21].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_21_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[21].stop()

message_21 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_21_timer_append_function():
    global message_21
    global var_tbx
    if message_21:
        var_tbx[21].append(message_21[0])
        message_21.remove(message_21[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_22_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[22].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_22_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[22].stop()

message_22 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_22_timer_append_function():
    global message_22
    global var_tbx
    if message_22:
        var_tbx[22].append(message_22[0])
        message_22.remove(message_22[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_23_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[23].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_23_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[23].stop()

message_23 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_23_timer_append_function():
    global message_23
    global var_tbx
    if message_23:
        var_tbx[23].append(message_23[0])
        message_23.remove(message_23[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_24_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[24].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_24_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[24].stop()

message_24 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_24_timer_append_function():
    global message_24
    global var_tbx
    if message_24:
        var_tbx[24].append(message_24[0])
        message_24.remove(message_24[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_25_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[25].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_25_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[25].stop()

message_25 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_25_timer_append_function():
    global message_25
    global var_tbx
    if message_25:
        var_tbx[25].append(message_25[0])
        message_25.remove(message_25[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_26_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[26].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_26_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[26].stop()

message_26 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_26_timer_append_function():
    global message_26
    global var_tbx
    if message_26:
        var_tbx[26].append(message_26[0])
        message_26.remove(message_26[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_27_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[27].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_27_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[27].stop()

message_27 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_27_timer_append_function():
    global message_27
    global var_tbx
    if message_27:
        var_tbx[27].append(message_27[0])
        message_27.remove(message_27[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_28_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[28].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_28_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[28].stop()

message_28 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_28_timer_append_function():
    global message_28
    global var_tbx
    if message_28:
        var_tbx[28].append(message_28[0])
        message_28.remove(message_28[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_29_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[29].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_29_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[29].stop()

message_29 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_29_timer_append_function():
    global message_29
    global var_tbx
    if message_29:
        var_tbx[29].append(message_29[0])
        message_29.remove(message_29[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_30_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[30].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_30_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[30].stop()

message_30 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_30_timer_append_function():
    global message_30
    global var_tbx
    if message_30:
        var_tbx[30].append(message_30[0])
        message_30.remove(message_30[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_31_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[31].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_31_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[31].stop()

message_31 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_31_timer_append_function():
    global message_31
    global var_tbx
    if message_31:
        var_tbx[31].append(message_31[0])
        message_31.remove(message_31[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_32_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[32].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_32_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[32].stop()

message_32 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_32_timer_append_function():
    global message_32
    global var_tbx
    if message_32:
        var_tbx[32].append(message_32[0])
        message_32.remove(message_32[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_33_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[33].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_33_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[33].stop()

message_33 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_33_timer_append_function():
    global message_33
    global var_tbx
    if message_33:
        var_tbx[33].append(message_33[0])
        message_33.remove(message_33[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_34_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[34].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_34_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[34].stop()

message_34 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_34_timer_append_function():
    global message_34
    global var_tbx
    if message_34:
        var_tbx[34].append(message_34[0])
        message_34.remove(message_34[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_35_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[35].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_35_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[35].stop()

message_35 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_35_timer_append_function():
    global message_35
    global var_tbx
    if message_35:
        var_tbx[35].append(message_35[0])
        message_35.remove(message_35[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_36_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[36].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_36_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[36].stop()

message_36 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_36_timer_append_function():
    global message_36
    global var_tbx
    if message_36:
        var_tbx[36].append(message_36[0])
        message_36.remove(message_36[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_37_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[37].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_37_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[37].stop()

message_37 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_37_timer_append_function():
    global message_37
    global var_tbx
    if message_37:
        var_tbx[37].append(message_37[0])
        message_37.remove(message_37[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_38_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[38].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_38_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[38].stop()

message_38 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_38_timer_append_function():
    global message_38
    global var_tbx
    if message_38:
        var_tbx[38].append(message_38[0])
        message_38.remove(message_38[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_39_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[39].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_39_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[39].stop()

message_39 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_39_timer_append_function():
    global message_39
    global var_tbx
    if message_39:
        var_tbx[39].append(message_39[0])
        message_39.remove(message_39[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_40_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[40].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_40_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[40].stop()

message_40 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_40_timer_append_function():
    global message_40
    global var_tbx
    if message_40:
        var_tbx[40].append(message_40[0])
        message_40.remove(message_40[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_41_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[41].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_41_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[41].stop()

message_41 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_41_timer_append_function():
    global message_41
    global var_tbx
    if message_41:
        var_tbx[41].append(message_41[0])
        message_41.remove(message_41[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_42_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[42].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_42_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[42].stop()

message_42 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_42_timer_append_function():
    global message_42
    global var_tbx
    if message_42:
        var_tbx[42].append(message_42[0])
        message_42.remove(message_42[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_43_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[43].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_43_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[43].stop()

message_43 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_43_timer_append_function():
    global message_43
    global var_tbx
    if message_43:
        var_tbx[43].append(message_43[0])
        message_43.remove(message_43[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_44_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[44].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_44_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[44].stop()

message_44 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_44_timer_append_function():
    global message_44
    global var_tbx
    if message_44:
        var_tbx[44].append(message_44[0])
        message_44.remove(message_44[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_45_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[45].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_45_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[45].stop()

message_45 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_45_timer_append_function():
    global message_45
    global var_tbx
    if message_45:
        var_tbx[45].append(message_45[0])
        message_45.remove(message_45[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_46_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[46].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_46_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[46].stop()

message_46 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_46_timer_append_function():
    global message_46
    global var_tbx
    if message_46:
        var_tbx[46].append(message_46[0])
        message_46.remove(message_46[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_47_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[47].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_47_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[47].stop()

message_47 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_47_timer_append_function():
    global message_47
    global var_tbx
    if message_47:
        var_tbx[47].append(message_47[0])
        message_47.remove(message_47[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_48_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[48].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_48_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[48].stop()

message_48 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_48_timer_append_function():
    global message_48
    global var_tbx
    if message_48:
        var_tbx[48].append(message_48[0])
        message_48.remove(message_48[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_49_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[49].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_49_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[49].stop()

message_49 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_49_timer_append_function():
    global message_49
    global var_tbx
    if message_49:
        var_tbx[49].append(message_49[0])
        message_49.remove(message_49[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_50_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[50].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_50_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[50].stop()

message_50 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_50_timer_append_function():
    global message_50
    global var_tbx
    if message_50:
        var_tbx[50].append(message_50[0])
        message_50.remove(message_50[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_51_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[51].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_51_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[51].stop()

message_51 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_51_timer_append_function():
    global message_51
    global var_tbx
    if message_51:
        var_tbx[51].append(message_51[0])
        message_51.remove(message_51[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_52_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[52].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_52_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[52].stop()

message_52 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_52_timer_append_function():
    global message_52
    global var_tbx
    if message_52:
        var_tbx[52].append(message_52[0])
        message_52.remove(message_52[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_53_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[53].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_53_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[53].stop()

message_53 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_53_timer_append_function():
    global message_53
    global var_tbx
    if message_53:
        var_tbx[53].append(message_53[0])
        message_53.remove(message_53[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_54_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[54].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_54_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[54].stop()

message_54 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_54_timer_append_function():
    global message_54
    global var_tbx
    if message_54:
        var_tbx[54].append(message_54[0])
        message_54.remove(message_54[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_55_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[55].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_55_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[55].stop()

message_55 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_55_timer_append_function():
    global message_55
    global var_tbx
    if message_55:
        var_tbx[55].append(message_55[0])
        message_55.remove(message_55[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_56_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[56].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_56_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[56].stop()

message_56 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_56_timer_append_function():
    global message_56
    global var_tbx
    if message_56:
        var_tbx[56].append(message_56[0])
        message_56.remove(message_56[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_57_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[57].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_57_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[57].stop()

message_57 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_57_timer_append_function():
    global message_57
    global var_tbx
    if message_57:
        var_tbx[57].append(message_57[0])
        message_57.remove(message_57[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_58_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[58].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_58_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[58].stop()

message_58 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_58_timer_append_function():
    global message_58
    global var_tbx
    if message_58:
        var_tbx[58].append(message_58[0])
        message_58.remove(message_58[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_59_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[59].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_59_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[59].stop()

message_59 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_59_timer_append_function():
    global message_59
    global var_tbx
    if message_59:
        var_tbx[59].append(message_59[0])
        message_59.remove(message_59[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_60_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[60].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_60_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[60].stop()

message_60 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_60_timer_append_function():
    global message_60
    global var_tbx
    if message_60:
        var_tbx[60].append(message_60[0])
        message_60.remove(message_60[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_61_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[61].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_61_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[61].stop()

message_61 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_61_timer_append_function():
    global message_61
    global var_tbx
    if message_61:
        var_tbx[61].append(message_61[0])
        message_61.remove(message_61[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_62_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[62].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_62_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[62].stop()

message_62 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_62_timer_append_function():
    global message_62
    global var_tbx
    if message_62:
        var_tbx[62].append(message_62[0])
        message_62.remove(message_62[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_63_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[63].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_63_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[63].stop()

message_63 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_63_timer_append_function():
    global message_63
    global var_tbx
    if message_63:
        var_tbx[63].append(message_63[0])
        message_63.remove(message_63[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_64_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[64].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_64_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[64].stop()

message_64 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_64_timer_append_function():
    global message_64
    global var_tbx
    if message_64:
        var_tbx[64].append(message_64[0])
        message_64.remove(message_64[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_65_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[65].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_65_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[65].stop()

message_65 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_65_timer_append_function():
    global message_65
    global var_tbx
    if message_65:
        var_tbx[65].append(message_65[0])
        message_65.remove(message_65[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_66_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[66].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_66_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[66].stop()

message_66 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_66_timer_append_function():
    global message_66
    global var_tbx
    if message_66:
        var_tbx[66].append(message_66[0])
        message_66.remove(message_66[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_67_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[67].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_67_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[67].stop()

message_67 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_67_timer_append_function():
    global message_67
    global var_tbx
    if message_67:
        var_tbx[67].append(message_67[0])
        message_67.remove(message_67[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_68_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[68].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_68_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[68].stop()

message_68 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_68_timer_append_function():
    global message_68
    global var_tbx
    if message_68:
        var_tbx[68].append(message_68[0])
        message_68.remove(message_68[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_69_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[69].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_69_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[69].stop()

message_69 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_69_timer_append_function():
    global message_69
    global var_tbx
    if message_69:
        var_tbx[69].append(message_69[0])
        message_69.remove(message_69[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_70_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[70].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_70_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[70].stop()

message_70 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_70_timer_append_function():
    global message_70
    global var_tbx
    if message_70:
        var_tbx[70].append(message_70[0])
        message_70.remove(message_70[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_71_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[71].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_71_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[71].stop()

message_71 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_71_timer_append_function():
    global message_71
    global var_tbx
    if message_71:
        var_tbx[71].append(message_71[0])
        message_71.remove(message_71[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_72_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[72].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_72_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[72].stop()

message_72 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_72_timer_append_function():
    global message_72
    global var_tbx
    if message_72:
        var_tbx[72].append(message_72[0])
        message_72.remove(message_72[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_73_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[73].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_73_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[73].stop()

message_73 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_73_timer_append_function():
    global message_73
    global var_tbx
    if message_73:
        var_tbx[73].append(message_73[0])
        message_73.remove(message_73[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_74_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[74].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_74_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[74].stop()

message_74 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_74_timer_append_function():
    global message_74
    global var_tbx
    if message_74:
        var_tbx[74].append(message_74[0])
        message_74.remove(message_74[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_75_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[75].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_75_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[75].stop()

message_75 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_75_timer_append_function():
    global message_75
    global var_tbx
    if message_75:
        var_tbx[75].append(message_75[0])
        message_75.remove(message_75[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_76_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[76].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_76_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[76].stop()

message_76 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_76_timer_append_function():
    global message_76
    global var_tbx
    if message_76:
        var_tbx[76].append(message_76[0])
        message_76.remove(message_76[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_77_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[77].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_77_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[77].stop()

message_77 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_77_timer_append_function():
    global message_77
    global var_tbx
    if message_77:
        var_tbx[77].append(message_77[0])
        message_77.remove(message_77[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_78_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[78].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_78_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[78].stop()

message_78 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_78_timer_append_function():
    global message_78
    global var_tbx
    if message_78:
        var_tbx[78].append(message_78[0])
        message_78.remove(message_78[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_79_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[79].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_79_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[79].stop()

message_79 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_79_timer_append_function():
    global message_79
    global var_tbx
    if message_79:
        var_tbx[79].append(message_79[0])
        message_79.remove(message_79[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_80_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[80].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_80_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[80].stop()

message_80 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_80_timer_append_function():
    global message_80
    global var_tbx
    if message_80:
        var_tbx[80].append(message_80[0])
        message_80.remove(message_80[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_81_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[81].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_81_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[81].stop()

message_81 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_81_timer_append_function():
    global message_81
    global var_tbx
    if message_81:
        var_tbx[81].append(message_81[0])
        message_81.remove(message_81[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_82_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[82].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_82_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[82].stop()

message_82 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_82_timer_append_function():
    global message_82
    global var_tbx
    if message_82:
        var_tbx[82].append(message_82[0])
        message_82.remove(message_82[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_83_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[83].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_83_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[83].stop()

message_83 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_83_timer_append_function():
    global message_83
    global var_tbx
    if message_83:
        var_tbx[83].append(message_83[0])
        message_83.remove(message_83[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_84_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[84].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_84_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[84].stop()

message_84 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_84_timer_append_function():
    global message_84
    global var_tbx
    if message_84:
        var_tbx[84].append(message_84[0])
        message_84.remove(message_84[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_85_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[85].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_85_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[85].stop()

message_85 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_85_timer_append_function():
    global message_85
    global var_tbx
    if message_85:
        var_tbx[85].append(message_85[0])
        message_85.remove(message_85[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_86_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[86].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_86_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[86].stop()

message_86 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_86_timer_append_function():
    global message_86
    global var_tbx
    if message_86:
        var_tbx[86].append(message_86[0])
        message_86.remove(message_86[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_87_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[87].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_87_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[87].stop()

message_87 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_87_timer_append_function():
    global message_87
    global var_tbx
    if message_87:
        var_tbx[87].append(message_87[0])
        message_87.remove(message_87[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_88_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[88].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_88_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[88].stop()

message_88 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_88_timer_append_function():
    global message_88
    global var_tbx
    if message_88:
        var_tbx[88].append(message_88[0])
        message_88.remove(message_88[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_89_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[89].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_89_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[89].stop()

message_89 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_89_timer_append_function():
    global message_89
    global var_tbx
    if message_89:
        var_tbx[89].append(message_89[0])
        message_89.remove(message_89[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_90_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[90].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_90_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[90].stop()

message_90 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_90_timer_append_function():
    global message_90
    global var_tbx
    if message_90:
        var_tbx[90].append(message_90[0])
        message_90.remove(message_90[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_91_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[91].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_91_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[91].stop()

message_91 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_91_timer_append_function():
    global message_91
    global var_tbx
    if message_91:
        var_tbx[91].append(message_91[0])
        message_91.remove(message_91[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_92_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[92].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_92_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[92].stop()

message_92 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_92_timer_append_function():
    global message_92
    global var_tbx
    if message_92:
        var_tbx[92].append(message_92[0])
        message_92.remove(message_92[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_93_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[93].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_93_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[93].stop()

message_93 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_93_timer_append_function():
    global message_93
    global var_tbx
    if message_93:
        var_tbx[93].append(message_93[0])
        message_93.remove(message_93[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_94_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[94].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_94_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[94].stop()

message_94 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_94_timer_append_function():
    global message_94
    global var_tbx
    if message_94:
        var_tbx[94].append(message_94[0])
        message_94.remove(message_94[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_95_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[95].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_95_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[95].stop()

message_95 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_95_timer_append_function():
    global message_95
    global var_tbx
    if message_95:
        var_tbx[95].append(message_95[0])
        message_95.remove(message_95[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_96_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[96].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_96_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[96].stop()

message_96 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_96_timer_append_function():
    global message_96
    global var_tbx
    if message_96:
        var_tbx[96].append(message_96[0])
        message_96.remove(message_96[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_97_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[97].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_97_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[97].stop()

message_97 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_97_timer_append_function():
    global message_97
    global var_tbx
    if message_97:
        var_tbx[97].append(message_97[0])
        message_97.remove(message_97[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_98_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[98].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_98_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[98].stop()

message_98 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_98_timer_append_function():
    global message_98
    global var_tbx
    if message_98:
        var_tbx[98].append(message_98[0])
        message_98.remove(message_98[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_99_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[99].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_99_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[99].stop()

message_99 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_99_timer_append_function():
    global message_99
    global var_tbx
    if message_99:
        var_tbx[99].append(message_99[0])
        message_99.remove(message_99[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_100_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[100].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_100_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[100].stop()

message_100 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_100_timer_append_function():
    global message_100
    global var_tbx
    if message_100:
        var_tbx[100].append(message_100[0])
        message_100.remove(message_100[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_101_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[101].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_101_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[101].stop()

message_101 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_101_timer_append_function():
    global message_101
    global var_tbx
    if message_101:
        var_tbx[101].append(message_101[0])
        message_101.remove(message_101[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_102_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[102].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_102_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[102].stop()

message_102 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_102_timer_append_function():
    global message_102
    global var_tbx
    if message_102:
        var_tbx[102].append(message_102[0])
        message_102.remove(message_102[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_103_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[103].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_103_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[103].stop()

message_103 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_103_timer_append_function():
    global message_103
    global var_tbx
    if message_103:
        var_tbx[103].append(message_103[0])
        message_103.remove(message_103[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_104_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[104].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_104_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[104].stop()

message_104 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_104_timer_append_function():
    global message_104
    global var_tbx
    if message_104:
        var_tbx[104].append(message_104[0])
        message_104.remove(message_104[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_105_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[105].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_105_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[105].stop()

message_105 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_105_timer_append_function():
    global message_105
    global var_tbx
    if message_105:
        var_tbx[105].append(message_105[0])
        message_105.remove(message_105[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_106_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[106].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_106_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[106].stop()

message_106 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_106_timer_append_function():
    global message_106
    global var_tbx
    if message_106:
        var_tbx[106].append(message_106[0])
        message_106.remove(message_106[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_107_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[107].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_107_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[107].stop()

message_107 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_107_timer_append_function():
    global message_107
    global var_tbx
    if message_107:
        var_tbx[107].append(message_107[0])
        message_107.remove(message_107[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_108_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[108].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_108_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[108].stop()

message_108 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_108_timer_append_function():
    global message_108
    global var_tbx
    if message_108:
        var_tbx[108].append(message_108[0])
        message_108.remove(message_108[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_109_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[109].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_109_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[109].stop()

message_109 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_109_timer_append_function():
    global message_109
    global var_tbx
    if message_109:
        var_tbx[109].append(message_109[0])
        message_109.remove(message_109[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_110_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[110].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_110_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[110].stop()

message_110 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_110_timer_append_function():
    global message_110
    global var_tbx
    if message_110:
        var_tbx[110].append(message_110[0])
        message_110.remove(message_110[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_111_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[111].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_111_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[111].stop()

message_111 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_111_timer_append_function():
    global message_111
    global var_tbx
    if message_111:
        var_tbx[111].append(message_111[0])
        message_111.remove(message_111[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_112_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[112].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_112_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[112].stop()

message_112 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_112_timer_append_function():
    global message_112
    global var_tbx
    if message_112:
        var_tbx[112].append(message_112[0])
        message_112.remove(message_112[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_113_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[113].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_113_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[113].stop()

message_113 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_113_timer_append_function():
    global message_113
    global var_tbx
    if message_113:
        var_tbx[113].append(message_113[0])
        message_113.remove(message_113[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_114_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[114].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_114_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[114].stop()

message_114 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_114_timer_append_function():
    global message_114
    global var_tbx
    if message_114:
        var_tbx[114].append(message_114[0])
        message_114.remove(message_114[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_115_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[115].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_115_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[115].stop()

message_115 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_115_timer_append_function():
    global message_115
    global var_tbx
    if message_115:
        var_tbx[115].append(message_115[0])
        message_115.remove(message_115[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_116_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[116].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_116_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[116].stop()

message_116 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_116_timer_append_function():
    global message_116
    global var_tbx
    if message_116:
        var_tbx[116].append(message_116[0])
        message_116.remove(message_116[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_117_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[117].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_117_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[117].stop()

message_117 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_117_timer_append_function():
    global message_117
    global var_tbx
    if message_117:
        var_tbx[117].append(message_117[0])
        message_117.remove(message_117[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_118_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[118].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_118_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[118].stop()

message_118 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_118_timer_append_function():
    global message_118
    global var_tbx
    if message_118:
        var_tbx[118].append(message_118[0])
        message_118.remove(message_118[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_119_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[119].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_119_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[119].stop()

message_119 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_119_timer_append_function():
    global message_119
    global var_tbx
    if message_119:
        var_tbx[119].append(message_119[0])
        message_119.remove(message_119[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_120_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[120].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_120_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[120].stop()

message_120 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_120_timer_append_function():
    global message_120
    global var_tbx
    if message_120:
        var_tbx[120].append(message_120[0])
        message_120.remove(message_120[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_121_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[121].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_121_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[121].stop()

message_121 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_121_timer_append_function():
    global message_121
    global var_tbx
    if message_121:
        var_tbx[121].append(message_121[0])
        message_121.remove(message_121[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_122_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[122].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_122_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[122].stop()

message_122 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_122_timer_append_function():
    global message_122
    global var_tbx
    if message_122:
        var_tbx[122].append(message_122[0])
        message_122.remove(message_122[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_123_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[123].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_123_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[123].stop()

message_123 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_123_timer_append_function():
    global message_123
    global var_tbx
    if message_123:
        var_tbx[123].append(message_123[0])
        message_123.remove(message_123[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_124_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[124].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_124_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[124].stop()

message_124 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_124_timer_append_function():
    global message_124
    global var_tbx
    if message_124:
        var_tbx[124].append(message_124[0])
        message_124.remove(message_124[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_125_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[125].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_125_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[125].stop()

message_125 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_125_timer_append_function():
    global message_125
    global var_tbx
    if message_125:
        var_tbx[125].append(message_125[0])
        message_125.remove(message_125[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_126_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[126].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_126_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[126].stop()

message_126 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_126_timer_append_function():
    global message_126
    global var_tbx
    if message_126:
        var_tbx[126].append(message_126[0])
        message_126.remove(message_126[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_127_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[127].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_127_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[127].stop()

message_127 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_127_timer_append_function():
    global message_127
    global var_tbx
    if message_127:
        var_tbx[127].append(message_127[0])
        message_127.remove(message_127[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_128_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[128].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_128_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[128].stop()

message_128 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_128_timer_append_function():
    global message_128
    global var_tbx
    if message_128:
        var_tbx[128].append(message_128[0])
        message_128.remove(message_128[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_129_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[129].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_129_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[129].stop()

message_129 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_129_timer_append_function():
    global message_129
    global var_tbx
    if message_129:
        var_tbx[129].append(message_129[0])
        message_129.remove(message_129[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_130_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[130].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_130_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[130].stop()

message_130 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_130_timer_append_function():
    global message_130
    global var_tbx
    if message_130:
        var_tbx[130].append(message_130[0])
        message_130.remove(message_130[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_131_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[131].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_131_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[131].stop()

message_131 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_131_timer_append_function():
    global message_131
    global var_tbx
    if message_131:
        var_tbx[131].append(message_131[0])
        message_131.remove(message_131[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_132_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[132].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_132_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[132].stop()

message_132 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_132_timer_append_function():
    global message_132
    global var_tbx
    if message_132:
        var_tbx[132].append(message_132[0])
        message_132.remove(message_132[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_133_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[133].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_133_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[133].stop()

message_133 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_133_timer_append_function():
    global message_133
    global var_tbx
    if message_133:
        var_tbx[133].append(message_133[0])
        message_133.remove(message_133[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_134_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[134].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_134_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[134].stop()

message_134 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_134_timer_append_function():
    global message_134
    global var_tbx
    if message_134:
        var_tbx[134].append(message_134[0])
        message_134.remove(message_134[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_135_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[135].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_135_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[135].stop()

message_135 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_135_timer_append_function():
    global message_135
    global var_tbx
    if message_135:
        var_tbx[135].append(message_135[0])
        message_135.remove(message_135[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_136_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[136].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_136_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[136].stop()

message_136 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_136_timer_append_function():
    global message_136
    global var_tbx
    if message_136:
        var_tbx[136].append(message_136[0])
        message_136.remove(message_136[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_137_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[137].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_137_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[137].stop()

message_137 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_137_timer_append_function():
    global message_137
    global var_tbx
    if message_137:
        var_tbx[137].append(message_137[0])
        message_137.remove(message_137[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_138_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[138].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_138_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[138].stop()

message_138 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_138_timer_append_function():
    global message_138
    global var_tbx
    if message_138:
        var_tbx[138].append(message_138[0])
        message_138.remove(message_138[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_139_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[139].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_139_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[139].stop()

message_139 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_139_timer_append_function():
    global message_139
    global var_tbx
    if message_139:
        var_tbx[139].append(message_139[0])
        message_139.remove(message_139[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_140_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[140].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_140_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[140].stop()

message_140 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_140_timer_append_function():
    global message_140
    global var_tbx
    if message_140:
        var_tbx[140].append(message_140[0])
        message_140.remove(message_140[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_141_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[141].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_141_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[141].stop()

message_141 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_141_timer_append_function():
    global message_141
    global var_tbx
    if message_141:
        var_tbx[141].append(message_141[0])
        message_141.remove(message_141[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_142_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[142].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_142_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[142].stop()

message_142 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_142_timer_append_function():
    global message_142
    global var_tbx
    if message_142:
        var_tbx[142].append(message_142[0])
        message_142.remove(message_142[0])

@PyQt5.QtCore.pyqtSlot()
def tbx_143_start_timer_function():
    global var_tbx_timer
    var_tbx_timer[143].start()

@PyQt5.QtCore.pyqtSlot()
def tbx_143_stop_timer_function():
    global var_tbx_timer
    var_tbx_timer[143].stop()

message_143 = []
@PyQt5.QtCore.pyqtSlot()
def tbx_143_timer_append_function():
    global message_143
    global var_tbx
    if message_143:
        var_tbx[143].append(message_143[0])
        message_143.remove(message_143[0])


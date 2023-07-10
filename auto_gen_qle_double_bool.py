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

qlex_double_0_0_bool = False
qlex_double_1_0_bool = False
qlex_double_2_0_bool = False
qlex_double_3_0_bool = False
qlex_double_4_0_bool = False
qlex_double_5_0_bool = False
qlex_double_6_0_bool = False
qlex_double_7_0_bool = False
qlex_double_8_0_bool = False
qlex_double_9_0_bool = False
qlex_double_10_0_bool = False
qlex_double_11_0_bool = False
qlex_double_12_0_bool = False
qlex_double_13_0_bool = False
qlex_double_14_0_bool = False
qlex_double_15_0_bool = False
qlex_double_16_0_bool = False
qlex_double_17_0_bool = False
qlex_double_18_0_bool = False
qlex_double_19_0_bool = False
qlex_double_20_0_bool = False
qlex_double_21_0_bool = False
qlex_double_22_0_bool = False
qlex_double_23_0_bool = False
qlex_double_24_0_bool = False
qlex_double_25_0_bool = False
qlex_double_26_0_bool = False
qlex_double_27_0_bool = False
qlex_double_28_0_bool = False
qlex_double_29_0_bool = False
qlex_double_30_0_bool = False
qlex_double_31_0_bool = False
qlex_double_32_0_bool = False
qlex_double_33_0_bool = False
qlex_double_34_0_bool = False
qlex_double_35_0_bool = False
qlex_double_36_0_bool = False
qlex_double_37_0_bool = False
qlex_double_38_0_bool = False
qlex_double_39_0_bool = False
qlex_double_40_0_bool = False
qlex_double_41_0_bool = False
qlex_double_42_0_bool = False
qlex_double_43_0_bool = False
qlex_double_44_0_bool = False
qlex_double_45_0_bool = False
qlex_double_46_0_bool = False
qlex_double_47_0_bool = False
qlex_double_48_0_bool = False
qlex_double_49_0_bool = False
qlex_double_50_0_bool = False
qlex_double_51_0_bool = False
qlex_double_52_0_bool = False
qlex_double_53_0_bool = False
qlex_double_54_0_bool = False
qlex_double_55_0_bool = False
qlex_double_56_0_bool = False
qlex_double_57_0_bool = False
qlex_double_58_0_bool = False
qlex_double_59_0_bool = False
qlex_double_60_0_bool = False
qlex_double_61_0_bool = False
qlex_double_62_0_bool = False
qlex_double_63_0_bool = False
qlex_double_64_0_bool = False
qlex_double_65_0_bool = False
qlex_double_66_0_bool = False
qlex_double_67_0_bool = False
qlex_double_68_0_bool = False
qlex_double_69_0_bool = False
qlex_double_70_0_bool = False
qlex_double_71_0_bool = False
qlex_double_72_0_bool = False
qlex_double_73_0_bool = False
qlex_double_74_0_bool = False
qlex_double_75_0_bool = False
qlex_double_76_0_bool = False
qlex_double_77_0_bool = False
qlex_double_78_0_bool = False
qlex_double_79_0_bool = False
qlex_double_80_0_bool = False
qlex_double_81_0_bool = False
qlex_double_82_0_bool = False
qlex_double_83_0_bool = False
qlex_double_84_0_bool = False
qlex_double_85_0_bool = False
qlex_double_86_0_bool = False
qlex_double_87_0_bool = False
qlex_double_88_0_bool = False
qlex_double_89_0_bool = False
qlex_double_90_0_bool = False
qlex_double_91_0_bool = False
qlex_double_92_0_bool = False
qlex_double_93_0_bool = False
qlex_double_94_0_bool = False
qlex_double_95_0_bool = False
qlex_double_96_0_bool = False
qlex_double_97_0_bool = False
qlex_double_98_0_bool = False
qlex_double_99_0_bool = False
qlex_double_100_0_bool = False
qlex_double_101_0_bool = False
qlex_double_102_0_bool = False
qlex_double_103_0_bool = False
qlex_double_104_0_bool = False
qlex_double_105_0_bool = False
qlex_double_106_0_bool = False
qlex_double_107_0_bool = False
qlex_double_108_0_bool = False
qlex_double_109_0_bool = False
qlex_double_110_0_bool = False
qlex_double_111_0_bool = False
qlex_double_112_0_bool = False
qlex_double_113_0_bool = False
qlex_double_114_0_bool = False
qlex_double_115_0_bool = False
qlex_double_116_0_bool = False
qlex_double_117_0_bool = False
qlex_double_118_0_bool = False
qlex_double_119_0_bool = False
qlex_double_120_0_bool = False
qlex_double_121_0_bool = False
qlex_double_122_0_bool = False
qlex_double_123_0_bool = False
qlex_double_124_0_bool = False
qlex_double_125_0_bool = False
qlex_double_126_0_bool = False
qlex_double_127_0_bool = False
qlex_double_128_0_bool = False
qlex_double_129_0_bool = False
qlex_double_130_0_bool = False
qlex_double_131_0_bool = False
qlex_double_132_0_bool = False
qlex_double_133_0_bool = False
qlex_double_134_0_bool = False
qlex_double_135_0_bool = False
qlex_double_136_0_bool = False
qlex_double_137_0_bool = False
qlex_double_138_0_bool = False
qlex_double_139_0_bool = False
qlex_double_140_0_bool = False
qlex_double_141_0_bool = False
qlex_double_142_0_bool = False
qlex_double_143_0_bool = False

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

qlex_0_0_bool = False
qlex_1_0_bool = False
qlex_2_0_bool = False
qlex_3_0_bool = False
qlex_4_0_bool = False
qlex_5_0_bool = False
qlex_6_0_bool = False
qlex_7_0_bool = False
qlex_8_0_bool = False
qlex_9_0_bool = False
qlex_10_0_bool = False
qlex_11_0_bool = False
qlex_12_0_bool = False
qlex_13_0_bool = False
qlex_14_0_bool = False
qlex_15_0_bool = False
qlex_16_0_bool = False
qlex_17_0_bool = False
qlex_18_0_bool = False
qlex_19_0_bool = False
qlex_20_0_bool = False
qlex_21_0_bool = False
qlex_22_0_bool = False
qlex_23_0_bool = False
qlex_24_0_bool = False
qlex_25_0_bool = False
qlex_26_0_bool = False
qlex_27_0_bool = False
qlex_28_0_bool = False
qlex_29_0_bool = False
qlex_30_0_bool = False
qlex_31_0_bool = False
qlex_32_0_bool = False
qlex_33_0_bool = False
qlex_34_0_bool = False
qlex_35_0_bool = False
qlex_36_0_bool = False
qlex_37_0_bool = False
qlex_38_0_bool = False
qlex_39_0_bool = False
qlex_40_0_bool = False
qlex_41_0_bool = False
qlex_42_0_bool = False
qlex_43_0_bool = False
qlex_44_0_bool = False
qlex_45_0_bool = False
qlex_46_0_bool = False
qlex_47_0_bool = False
qlex_48_0_bool = False
qlex_49_0_bool = False
qlex_50_0_bool = False
qlex_51_0_bool = False
qlex_52_0_bool = False
qlex_53_0_bool = False
qlex_54_0_bool = False
qlex_55_0_bool = False
qlex_56_0_bool = False
qlex_57_0_bool = False
qlex_58_0_bool = False
qlex_59_0_bool = False
qlex_60_0_bool = False
qlex_61_0_bool = False
qlex_62_0_bool = False
qlex_63_0_bool = False
qlex_64_0_bool = False
qlex_65_0_bool = False
qlex_66_0_bool = False
qlex_67_0_bool = False
qlex_68_0_bool = False
qlex_69_0_bool = False
qlex_70_0_bool = False
qlex_71_0_bool = False
qlex_72_0_bool = False
qlex_73_0_bool = False
qlex_74_0_bool = False
qlex_75_0_bool = False
qlex_76_0_bool = False
qlex_77_0_bool = False
qlex_78_0_bool = False
qlex_79_0_bool = False
qlex_80_0_bool = False
qlex_81_0_bool = False
qlex_82_0_bool = False
qlex_83_0_bool = False
qlex_84_0_bool = False
qlex_85_0_bool = False
qlex_86_0_bool = False
qlex_87_0_bool = False
qlex_88_0_bool = False
qlex_89_0_bool = False
qlex_90_0_bool = False
qlex_91_0_bool = False
qlex_92_0_bool = False
qlex_93_0_bool = False
qlex_94_0_bool = False
qlex_95_0_bool = False
qlex_96_0_bool = False
qlex_97_0_bool = False
qlex_98_0_bool = False
qlex_99_0_bool = False
qlex_100_0_bool = False
qlex_101_0_bool = False
qlex_102_0_bool = False
qlex_103_0_bool = False
qlex_104_0_bool = False
qlex_105_0_bool = False
qlex_106_0_bool = False
qlex_107_0_bool = False
qlex_108_0_bool = False
qlex_109_0_bool = False
qlex_110_0_bool = False
qlex_111_0_bool = False
qlex_112_0_bool = False
qlex_113_0_bool = False
qlex_114_0_bool = False
qlex_115_0_bool = False
qlex_116_0_bool = False
qlex_117_0_bool = False
qlex_118_0_bool = False
qlex_119_0_bool = False
qlex_120_0_bool = False
qlex_121_0_bool = False
qlex_122_0_bool = False
qlex_123_0_bool = False
qlex_124_0_bool = False
qlex_125_0_bool = False
qlex_126_0_bool = False
qlex_127_0_bool = False
qlex_128_0_bool = False
qlex_129_0_bool = False
qlex_130_0_bool = False
qlex_131_0_bool = False
qlex_132_0_bool = False
qlex_133_0_bool = False
qlex_134_0_bool = False
qlex_135_0_bool = False
qlex_136_0_bool = False
qlex_137_0_bool = False
qlex_138_0_bool = False
qlex_139_0_bool = False
qlex_140_0_bool = False
qlex_141_0_bool = False
qlex_142_0_bool = False
qlex_143_0_bool = False

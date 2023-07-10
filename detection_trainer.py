""" Written by Benjamin Jack Cullen

download pre-trained model via https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/pretrained-yolov3.h5
If you are training to detect more than 1 object, set names of objects above like object_names_array=["hololens", "google-glass", "oculus", "magic-leap"]

"""
import os.path
import sys
import ast
from imageai.Detection.Custom import DetectionModelTrainer


def begin_training(_data_directory=None, _object_names_array=None, _batch_size=4, _num_experiments=100,
                   _train_from_pretrained_model=""):
    trainer = DetectionModelTrainer()
    trainer.setModelTypeAsYOLOv3()
    trainer.setDataDirectory(data_directory=_data_directory)
    if _train_from_pretrained_model:
        trainer.setTrainConfig(object_names_array=_object_names_array,
                               batch_size=_batch_size,
                               num_experiments=_num_experiments,
                               train_from_pretrained_model=_train_from_pretrained_model)
    else:
        trainer.setTrainConfig(object_names_array=_object_names_array,
                               batch_size=_batch_size,
                               num_experiments=_num_experiments)
    trainer.trainModel()


stdin = sys.argv
if '-h' in stdin:
    print('[Object Detection Trainer]')
    print()
    print('args order:')
    print('PATH BATCH_SIZE EXPERIMENTS_NUM PRETRAINED_MODEL OBJECTS,OBJECTS')
    print()

else:
    p = ''
    if len(stdin) == 6:
        d = stdin[1]
        b = int(stdin[2])
        n = int(stdin[3])
        p = stdin[4]
        o = ast.literal_eval(stdin[5])
    elif len(stdin) == 5:
        d = stdin[1]
        b = int(stdin[2])
        n = int(stdin[3])
        o = ast.literal_eval(stdin[4])
    if os.path.exists(d):
        print('Directory:', d)
        print('Batch Size:', b)
        print('Number of Experiments:', n)
        print('Use Pretrained Model:', p)
        print('Objects:', o)
        begin_training(_data_directory=d,
                       _object_names_array=o,
                       _batch_size=b,
                       _num_experiments=n,
                       _train_from_pretrained_model=p)
    else:
        print('-- invalid path.')
print('')

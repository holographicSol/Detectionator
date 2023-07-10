""" Written by Benjamin Jack Cullen

download pre-trained model via https://github.com/OlafenwaMoses/ImageAI/releases/download/essential-v4/pretrained-yolov3.h5
If you are training to detect more than 1 object, set names of objects above like object_names_array=["hololens", "google-glass", "oculus", "magic-leap"]

"""

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

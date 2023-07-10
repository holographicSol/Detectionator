""" Written by Benjamin Jack Cullen """

from imageai.Classification.Custom import ClassificationModelTrainer


def begin_training(_num_objects=None, _num_experiments=200,
                   _enhance_data=False, _batch_size=32, _initial_learning_rate=1e-3,
                   _show_network_summary=False, _training_image_size=224,
                   _continue_from_model=None,
                   _transfer_from_model=None,
                   _transfer_with_full_training=True,
                   _initial_num_objects=None,
                   _save_full_model=False, _model_type='file', _data_directory='',
                   _train_subdirectory='train',
                   _test_subdirectory='test',
                   _models_subdirectory='models',
                   _json_subdirectory='json'):

    model_trainer = ClassificationModelTrainer()
    if 'densenet121' in _model_type:
        model_trainer.setModelTypeAsDenseNet121()
    elif 'densenet' in _model_type:
        model_trainer.setModelTypeAsDenseNet()
    elif 'resnet50' in _model_type:
        model_trainer.setModelTypeAsResNet50()
    elif 'resnet' in _model_type:
        model_trainer.setModelTypeAsResNet()
    elif 'inceptionv3' in _model_type:
        model_trainer.setModelTypeAsInceptionV3()
    elif 'mobilenetv2' in _model_type:
        model_trainer.setModelTypeAsMobileNetV2()
    model_trainer.setDataDirectory(data_directory=_data_directory,
                                   train_subdirectory=_train_subdirectory,
                                   test_subdirectory=_test_subdirectory,
                                   models_subdirectory=_models_subdirectory,
                                   json_subdirectory=_json_subdirectory)
    model_trainer.trainModel(num_objects=_num_objects,
                             num_experiments=_num_experiments,
                             enhance_data=_enhance_data,
                             batch_size=_batch_size,
                             initial_learning_rate=_initial_learning_rate,
                             show_network_summary=_show_network_summary,
                             training_image_size=_training_image_size,
                             continue_from_model=_continue_from_model,
                             transfer_from_model=_transfer_from_model,
                             transfer_with_full_training=_transfer_with_full_training,
                             initial_num_objects=_initial_num_objects,
                             save_full_model=_save_full_model)

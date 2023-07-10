

def help():
    print('')
    print('')
    print('[AIMASTER]')
    print('')
    print('')
    print('    [IMAGEAI]')
    print('')
    print('                           quickcam INDEX (optional: dump)')
    print('                           quickimage PATH')
    print('                           quickvideo PATH (optional: dump)')
    print('')
    print('    --video-detect-obj     Detect objects in video.')
    print('                               --yolov3 PATH')
    print('                               --resnet50 PATH')
    print('                               --model-json PATH')
    print('                               --in PATH')
    print('                               --out PATH DIRECTORY')
    print('                               --fps DIGITS')
    print('                               --min (Minimum probability percentage)')
    print('                               --extract')
    print('                               --speed (normal, fast, faster, fastest, flash)')
    print('                               --frame-detection-timeout')
    print('                               --dump (aka headless)')
    print('                               --log')
    print('                               --display-object-name-off')
    print('                               --display-percentage-probability-off')
    print('                               --detection-timeout')
    print('                               --display-box-off')
    print('                               --custom-objects')
    print('                               --save-in-class')
    print('                               --annotate')
    print('                               --start-frame DIGITS')
    print('                               --primary-target TARGET:PRIORITY_DIGIT,TARGET:PRIORITY_DIGIT')
    print('                               --secondary-target TARGET:PRIORITY_DIGIT,TARGET:PRIORITY_DIGIT')
    print('    --image-detect-obj     Detect objects in image.')
    print('                               --yolov3 PATH')
    print('                               --model-json PATH')
    print('                               --in PATH')
    print('                               --out PATH DIRECTORY')
    print('                               --input-type-file')
    print('                               --input-type-array')
    print('                               --output-type-file')
    print('                               --output-type-array')
    print('                               --nms-threshold FLOAT')
    print('                               --dump (aka headless)')
    print('                               --display-object-name-off')
    print('                               --display-percentage-probability-off')
    print('                               --extract')
    print('                               --thread-safe')
    print('                               --save-in-class')
    print('                               --annotate')
    print('                               --primary-target TARGET:PRIORITY_DIGIT,TARGET:PRIORITY_DIGIT')
    print('                               --secondary-target TARGET:PRIORITY_DIGIT,TARGET:PRIORITY_DIGIT')
    print('    --image-predict-obj    Predict objects in image.')
    print('                               --resnet50 PATH')
    print('                               --densenet121 PATH')
    print('                               --inceptionv3 PATH')
    print('                               --mobilenetv2 PATH')
    print('                               --model-json PATH')
    print('                               --in PATH')
    print('                               --out PATH')
    print('                               --input-type-file')
    print('                               --input-type-array')
    print('                               --speed (normal, fast, faster, fastest, flash)')
    print('                               --result-count (Digits)')
    print('                               --primary-target TARGET:PRIORITY_DIGIT,TARGET:PRIORITY_DIGIT')
    print('                               --secondary-target TARGET:PRIORITY_DIGIT,TARGET:PRIORITY_DIGIT')
    print('    --live-detect-obj      Detect objects in live stream.')
    print('                               --yolov3 PATH')
    print('                               --model-json PATH')
    print('                               --out PATH DIRECTORY')
    print('                               --fps DIGITS')
    print('                               --min (Minimum probability percentage)')
    print('                               --extract')
    print('                               --log')
    print('                               --cam DIGITS')
    print('                               --frame-detection-timeout DIGITS')
    print('                               --detection-timeout')
    print('                               --dump (aka headless)')
    print('                               --log')
    print('                               --display-object-name-off')
    print('                               --display-percentage-probability-off')
    print('                               --save-video-off')
    print('                               --save-in-class')
    print('                               --annotate')
    print('                               --primary-target TARGET:PRIORITY_DIGIT,TARGET:PRIORITY_DIGIT')
    print('                               --secondary-target TARGET:PRIORITY_DIGIT,TARGET:PRIORITY_DIGIT')
    print('    --train-detection      Train object detection. Requires annotated datasets.')
    print('                               --yolov3 PATH (Enables transfer learning from a pretrained YOLOv3 model.)')
    print('                               --data PATH')
    print('                               --object-names-array CLASS0,CLASS1,CLASS2')
    print('                               --batch-size DIGITS')
    print('                               --experiments-number DIGITS')
    print('    --train-prediction     Train object prediction. Does not require annotated datasets.')
    print('                               --densenet PATH')
    print('                               --densenet121 PATH')
    print('                               --resnet PATH')
    print('                               --resnet50 PATH')
    print('                               --inceptionv3 PATH')
    print('                               --mobilenetv2 PATH')
    print('                               --data PATH')
    print('                               --objects-number DIGITS')
    print('                               --batch-size DIGITS')
    print('                               --experiments-number DIGITS')
    print('                               --enhance')
    print('                               --show-network-summary')
    print('                               --train-sub PATH')
    print('                               --test-sub PATH')
    print('                               --models-sub PATH')
    print('                               --json-sub PATH')
    print('                               --initial-learning-rate')
    print('                               --training-image-size')
    print('                               --continue-from-model')
    print('                               --transfer-from-model')
    print('                               --transfer-with-full-training')
    print('                               --initial-num-objects')
    print('                               --save-full-model')
    # print('')
    print('    --convert-video        Convert video frame rate.')
    print('                               -s (Source Directory)')
    print('                               -o (Output Directory)')
    print('                               -f (FPS)')
    print('')
    print('Written and developed by Benjamin Jack Cullen using a highly modified ImageAI module.')
    print('')
    print('')
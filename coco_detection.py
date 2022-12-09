# dataset settings
dataset_type = 'CocoDataset'
data_root = 'C:/Git_dir/mmdetection/Mask_RCNN_dataset/'
img_norm_cfg = dict(
    mean=[123.675, 116.28, 103.53], std=[58.395, 57.12, 57.375], to_rgb=True)
train_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(type='LoadAnnotations', with_bbox=True),
    dict(type='Resize', img_scale=(1333, 800), keep_ratio=True),
    dict(type='RandomFlip', flip_ratio=0.5),
    dict(type='Normalize', **img_norm_cfg),
    dict(type='Pad', size_divisor=32),
    dict(type='DefaultFormatBundle'),
    dict(type='Collect', keys=['img', 'gt_bboxes', 'gt_labels']),
]
test_pipeline = [
    dict(type='LoadImageFromFile'),
    dict(
        type='MultiScaleFlipAug',
        img_scale=(1333, 800),
        flip=False,
        transforms=[
            dict(type='Resize', keep_ratio=True),
            dict(type='RandomFlip'),
            dict(type='Normalize', **img_norm_cfg),
            dict(type='Pad', size_divisor=32),
            dict(type='ImageToTensor', keys=['img']),
            dict(type='Collect', keys=['img']),
        ])
]
data = dict(
    train=[
        {'type' : dataset_type, 'ann_file' : data_root + 'onepiece(dress)_1/annotations/instances_default.json', 'img_prefix' : data_root + 'onepiece(dress)_1/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'onepiece(dress)_3/annotations/instances_default.json', 'img_prefix' : data_root + 'onepiece(dress)_3/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'skirt_2/annotations/instances_default.json', 'img_prefix' : data_root + 'skirt_2/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'pants_1/annotations/instances_default.json', 'img_prefix' : data_root + 'pants_1/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'pants_2/annotations/instances_default.json', 'img_prefix' : data_root + 'pants_2/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'jumpsuite_1/annotations/instances_default.json', 'img_prefix' : data_root + 'jumpsuite_1/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'shirt_1/annotations/instances_default.json', 'img_prefix' : data_root + 'skirt_1/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'shirt_2/annotations/instances_default.json', 'img_prefix' : data_root + 'skirt_2/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'shirt_4/annotations/instances_default.json', 'img_prefix' : data_root + 'skirt_4/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'sweater_1/annotations/instances_default.json', 'img_prefix' : data_root + 'sweater_1/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'blouse_2/annotations/instances_default.json', 'img_prefix' : data_root + 'blouse_2/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'cardigan_1/annotations/instances_default.json', 'img_prefix' : data_root + 'cardigan_1/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'jumper_1/annotations/instances_default.json', 'img_prefix' : data_root + 'jumper_1/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'jacket_1/annotations/instances_default.json', 'img_prefix' : data_root + 'jacket_1/images/', 'pipeline' : train_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'coat_1/annotations/instances_default.json', 'img_prefix' : data_root + 'coat_1/images/', 'pipeline' : train_pipeline},
    ],
    val=[
        {'type' : dataset_type, 'ann_file' : data_root + 'onepiece(dress)_2/annotations/instances_default.json', 'img_prefix' : data_root + 'onepiece(dress)_2/images/', 'pipeline' : test_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'skirt_1/annotations/instances_default.json', 'img_prefix' : data_root + 'skirt_1/images/', 'pipeline' : test_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'blouse_1/annotations/instances_default.json', 'img_prefix' : data_root + 'blouse_1/images/', 'pipeline' : test_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'jacket_2/annotations/instances_default.json', 'img_prefix' : data_root + 'jacket_2/images/', 'pipeline' : test_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'coat-2/annotations/instances_default.json', 'img_prefix' : data_root + 'coat_2/images/', 'pipeline' : test_pipeline},
    ],
    test=[
        {'type' : dataset_type, 'ann_file' : data_root + 'sweater_2/annotations/instances_default.json', 'img_prefix' : data_root + 'sweater_2/images/', 'pipeline' : test_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'jumper_2/annotations/instances_default.json', 'img_prefix' : data_root + 'jumper_2/images/', 'pipeline' : test_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'shirt_3/annotations/instances_default.json', 'img_prefix' : data_root + 'skirt_3/images/', 'pipeline' : test_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'onepiece(dress)_4/annotations/instances_default.json', 'img_prefix' : data_root + 'onepiece(dress)_4/images/', 'pipeline' : test_pipeline},
        {'type' : dataset_type, 'ann_file' : data_root + 'cardigan_2/annotations/instances_default.json', 'img_prefix' : data_root + 'cardigan_2/images/', 'pipeline' : test_pipeline},
    ]
)
evaluation = dict(interval=1, metric='bbox')

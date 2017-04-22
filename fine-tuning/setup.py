#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Apr 15 23:45:49 2017

@author: http://aidiary.hatenablog.com/entry/20170131/1485864665
"""

import os
import shutil
import random

IN_DIR = 'dataset/jpg'
TRAIN_DIR = 'dataset/train_images'
TEST_DIR = 'dataset/test_images'

if not os.path.exists(TRAIN_DIR):
    os.mkdir(TRAIN_DIR)

if not os.path.exists(TEST_DIR):
    os.mkdir(TEST_DIR)

# name => (start idx, end idx)
flower_dics = {}

with open('dataset/labels.txt') as fp:
    for line in fp:
        line = line.rstrip()
        cols = line.split()

        assert len(cols) == 3

        start = int(cols[0])
        end = int(cols[1])
        name = cols[2]

        flower_dics[name] = (start, end)

# 花ごとのディレクトリを作成
for name in flower_dics:
    os.mkdir(os.path.join(TRAIN_DIR, name))
    os.mkdir(os.path.join(TEST_DIR, name))

# jpgをスキャン
jpg_files = [f for f in sorted(os.listdir(IN_DIR)) if f.endswith('.jpg')]
for f in jpg_files:
    # image_0001.jpg => 1
    prefix = f.replace('.jpg', '')
    idx = int(prefix.split('_')[1])

    for name in flower_dics:
        start, end = flower_dics[name]
        if idx in range(start, end + 1):
            source = os.path.join(IN_DIR, f)
            dest = os.path.join(TRAIN_DIR, name)
            shutil.copy(source, dest)
            continue

# 訓練データの各ディレクトリからランダムに10枚をテストとする
for d in os.listdir(TRAIN_DIR):
    files = os.listdir(os.path.join(TRAIN_DIR, d))
    random.shuffle(files)
    for f in files[:10]:
        source = os.path.join(TRAIN_DIR, d, f)
        dest = os.path.join(TEST_DIR, d)
        shutil.move(source, dest)
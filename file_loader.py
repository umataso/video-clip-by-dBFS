# ファイルの読み込みの記述を簡易化するためのモジュール
from tkinter import filedialog
import os
import numpy as np
import cv2

def load_dir():
    dir = "./"
    filePath = filedialog.askdirectory(
        initialdir = dir)

    print(filePath)
    return filePath

def load_img():
    typ = [("画像ファイル", "*.jpg"), ("画像ファイル", "*.png")]
    dir = "./"
    filePath = filedialog.askopenfilename(
        filetypes = typ,
        initialdir = dir)

    print(filePath)
    return filePath

def load_video():
    typ = [("動画ファイル", "*.mp4")]
    dir = "./"
    filePath = filedialog.askopenfilename(
        filetypes = typ,
        initialdir = dir)

    print(filePath)
    return filePath

def cv2_imread(filename, flags=cv2.IMREAD_COLOR, dtype=np.uint8):
    try:
        n = np.fromfile(filename, dtype)
        img = cv2.imdecode(n, flags)
        return img
    except Exception as e:
        print(e)
        return None

def cv2_imwrite(filename, img, params=None):
    try:
        ext = os.path.splitext(filename)[1]
        result, n = cv2.imencode(ext, img, params)

        if result:
            with open(filename, mode='w+b') as f:
                n.tofile(f)
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False
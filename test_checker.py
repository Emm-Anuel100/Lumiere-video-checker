import pytest
import numpy as np
import cv2
import os
from checker import VideoConsistencyChecker

def test_checker_init():
    checker = VideoConsistencyChecker("dummy.mp4")
    assert checker.video_path == "dummy.mp4"

def test_blur_logic():
    # Create a perfectly sharp checkerboard
    img = np.zeros((100, 100), dtype=np.uint8)
    img[0:50, 0:50] = 255
    img[50:100, 50:100] = 255
    
    # Create a blurry version
    blurry = cv2.GaussianBlur(img, (15, 15), 0)
    
    score_sharp = cv2.Laplacian(img, cv2.CV_64F).var()
    score_blurry = cv2.Laplacian(blurry, cv2.CV_64F).var()
    
    assert score_sharp > score_blurry

def test_video_not_found():
    checker = VideoConsistencyChecker("non_existent.mp4")
    res = checker.analyze()
    assert "error" in res

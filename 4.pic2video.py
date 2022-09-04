import os
from tokenize import String
from typing import Any 
import cv2

def pic2video(filepath,videopath) -> Any:
    """
    Make the picture to a video

    Args:
        filepath (String): filepath of picture
        videopath (String): filepath of video which include file name
    such as:
        filepath = "D:/SourceTree/MakeYourStarsky/output/1_gz_chazhi/"
        videopath = "D:/SourceTree/MakeYourStarsky/finalVideo/1.mp4"
    Returns:
        any: video file
    """
    list = []
    for root,dirs,files in os.walk(filepath):
        for file in files:
            list.append(file)
    video = cv2.VideoWriter(videopath, cv2.VideoWriter_fourcc('M', 'P', '4', 'V'),5,(1920,1080))
    for i in range(1,len(list)):
        img = cv2.imread(filepath + list[i-1])
        img = cv2.resize(img,(1920,1080))
        video.write(img)

    video.release()

if __name__ == '__main__':
    filepath = "D:/SourceTree/MakeYourStarsky/output/1_gz_chazhi/"
    videopath = "D:/SourceTree/MakeYourStarsky/finalVideo/1.mp4"
    pic2video(filepath=filepath, videopath=videopath)

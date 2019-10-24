from moviepy.editor import *
import cv2
import imutils

clip = VideoFileClip("./videoclips/clip_2.mp4")

resize = clip.resize(width=1280,height=720)
resize.write_videofile("./videoclips/reshape.mp4")




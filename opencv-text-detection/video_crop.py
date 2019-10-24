from moviepy.editor import *
from pathlib import Path
import numpy as np
BASE_FOLDER = "./videoclips/"

path = Path(BASE_FOLDER)
video_paths = list(path.glob('*.mp4'))
video_paths = sorted(video_paths)
list_videos = []
this_vid =""
for vid in video_paths:
    read_video = VideoFileClip(str(vid))
    list_videos.append(read_video)
    
# video = VideoFileClip("airplanes.mp4").subclip(15,22)
# video.write_videofile(BASE_FOLDER+"clip-0.mp4",fps=25) 

# clip1 = VideoFileClip('clip_0.mp4')
# clip2 = VideoFileClip('clip_1.mp4')
# clip2 = VideoFileClip('clip_2.mp4')
# final_clip = concatenate_videoclips(list_videos)

# final_clip.write_videofile("merged_version.mp4",fps=20)
this_vid = read_video
this_vid.write_videofile("fuckkyes.mp4",fps=20)
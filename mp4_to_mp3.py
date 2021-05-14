from moviepy.editor import *
mp4_file = r"C:\Users\Max.000\Desktop\art\VES.mp4"
mp3_file = r"C:\Users\Max.000\Desktop\art\VES.mp3"
videoclip = VideoFileClip(mp4_file)
audioclip = videoclip.audio
audioclip.write_audiofile(mp3_file)
audioclip.close()
videoclip.close()

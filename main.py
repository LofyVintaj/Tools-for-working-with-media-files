import moviepy.editor

file = "Как начать.mp4"
video = moviepy.editor.VideoFileClip(file)
audio = video.audio
audio.write_audiofile('my_audio.mp3')
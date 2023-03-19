import moviepy.editor


def extracting_an_audio_track_from_a_video():
	file = "Как начать.mp4"
	video = moviepy.editor.VideoFileClip(file)
	audio = video.audio
	audio.write_audiofile('my_audio.mp3')
from pytube import YouTube

video_url = 'https://www.youtube.com/watch?v=6WOqOH3y95w'
yt = YouTube(video_url)
video_stream = yt.streams.get_highest_resolution()
video_stream.download()
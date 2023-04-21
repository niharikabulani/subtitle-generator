import speech_recognition as sr
import moviepy.editor as mp


video_path = "C:/Users/bulan/OneDrive/Desktop/python/lbs.mp4"
clip = mp.VideoFileClip(video_path)


subtitle_duration = 2


r = sr.Recognizer()


for i, interval in enumerate(range(0, int(clip.duration), subtitle_duration)):
    start_time = interval
    end_time = interval + subtitle_duration


    audio = clip.subclip(start_time, end_time).audio
    audio.write_audiofile("temp_audio.wav")

    with sr.AudioFile("temp_audio.wav") as source:
        audio_data = r.record(source)
    
 
    text = r.recognize_google(audio_data, show_all=True)
    if text:
        alternative_text = text.get("alternative")
        text = alternative_text[0].get("transcript")
    else:
        print("Empty list")
        continue


    with open(f"subtitle_{i}.srt", "w") as f:
        f.write(f"{i}\n{start_time} --> {end_time}\n{text}\n\n")

import os
os.remove("temp_audio.wav")
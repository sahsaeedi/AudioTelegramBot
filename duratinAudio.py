from mutagen.wave import WAVE
  
# function to convert the information into 
# some readable format
def audio_duration(path):

    audio = WAVE(path)
    audio_info = audio.info
    length = int(audio_info.length)
    hours = length // 3600  # calculate in hours
    length %= 3600
    mins = length // 60  # calculate in minutes
    length %= 60
    seconds = length  # calculate in seconds
  
    return hours, mins, seconds  # returns the duration

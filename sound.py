from pydub import AudioSegment
from pydub.playback import play

song = AudioSegment.from_wav("F:\hack\bells-tibetian-daniel_simon.wav")
play(song)

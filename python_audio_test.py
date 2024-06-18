#!/usr/bin/env python3

import rospy
from marine_radio_msgs.msg import AudioDataStamped
from sound_play.msg import SoundRequest
from sound_play.libsoundplay import SoundClient
import numpy as np
import pyaudio
import sounddevice as sd

def callback(audio_data):
     # Decode audio data
    audio_array = np.frombuffer(audio_data.audio.audio.data, dtype=np.int16)
    
    stream.write(audio_array)

def listener():
    rospy.init_node('audiodecodetest', anonymous=True)
  
    rospy.Subscriber('/garmin_cortex/audio', AudioDataStamped, callback)
    
    rospy.spin()

if __name__ == "__main__":
    stream = sd.RawStream(samplerate=16000, channels=1, dtype='int16', blocksize=1024) 
    stream.start() 
    listener()



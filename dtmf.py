import wave
import struct
import math
import sys

__author__ = '@Faid Amine'

class color:
	P    =  '\033[95m' # purple
	B    =  '\033[94m' # Blue
	BOLD =  '\033[1m'  # Bold
	G    =  '\033[92m' # Green
	Y    =  '\033[93m' # Yellow
	R    =  '\033[91m' # Red
	W    =  '\033[97m' # White
	BL   =  '\033[90m' # Black
	M    =  '\033[95m' # Magenta
	C    =  '\033[96m' # Cyan
	ENDC =  '\033[0m'  # end colors


def __logo__():

	print (color.BOLD+color.Y+" ____ _____ __  __ _____   ____       _            _             ")
	print (color.BOLD+color.Y+"|  _ \_   _|  \/  |  ___| |  _ \  ___| |_ ___  ___| |_ ___  _ __ ")
	print (color.BOLD+color.Y+"| | | || | | |\/| | |_    | | | |/ _ \ __/ _ \/ __| __/ _ \| '__|")
	print (color.BOLD+color.Y+"| |_| || | | |  | |  _|   | |_| |  __/ ||  __/ (__| || (_) | |   ")
	print (color.BOLD+color.Y+"|____/ |_| |_|  |_|_|     |____/ \___|\__\___|\___|\__\___/|_|   ")
	print (color.W+color.BOLD+"{"+color.R+__author__+color.W+"}"+color.ENDC+"\n")
 

class Detector:

    def __init__(self, samplerate):
        self.samplerate = samplerate
        self.goertzel_freq = [1209.0,1336.0,1477.0,1633.0,697.0,770.0,852.0,941.0]
        self.s_prev = {}
        self.s_prev2 = {}
        self.totalpower = {}
        self.N = {}
        self.coeff = {}
        
        for k in self.goertzel_freq:
            self.s_prev[k] = 0.0
            self.s_prev2[k] = 0.0
            self.totalpower[k] = 0.0
            self.N[k] = 0.0
            normalizedfreq = k / self.samplerate
            self.coeff[k] = 2.0*math.cos(2.0 * math.pi * normalizedfreq)

    def get_n(self, freqs):
        hi = [1209.0,1336.0,1477.0,1633.0]
        lo = [697.0,770.0,852.0,941.0]
        
        hifreq = 0.0
        hifreq_v = 0.0
        for f in hi:
            if freqs[f]>hifreq_v:
                hifreq_v = freqs[f]
                hifreq = f
        
        lofreq = 0.0
        lofreq_v = 0.0
        for f in lo:
            if freqs[f]>lofreq_v:
                lofreq_v = freqs[f]
                lofreq = f
        if lofreq==697.0:
            if hifreq==1209.0:
                return "1"
            elif hifreq==1336.0:
                return "2"
            elif hifreq==1477.0:
                return "3"
            elif hifreq==1633.0:
                return "A"
        elif lofreq==770.0:
            if hifreq==1209.0:
                return "4"
            elif hifreq==1336.0:
                return "5"
            elif hifreq==1477.0:
                return "6"
            elif hifreq==1633.0:
                return "B"
        elif lofreq==852.0:
            if hifreq==1209.0:
                return "7"
            elif hifreq==1336.0:
                return "8"
            elif hifreq==1477.0:
                return "9"
            elif hifreq==1633.0:
                return "C"
        elif lofreq==941.0:
            if hifreq==1209.0:
                return "*"
            elif hifreq==1336.0:
                return "0"
            elif hifreq==1477.0:
                return "#"
            elif hifreq==1633.0:
                return "D"
    def show(self, sample):
        freqs = {}
        for freq in self.goertzel_freq:
            s = sample + (self.coeff[freq] * self.s_prev[freq]) - self.s_prev2[freq]
            self.s_prev2[freq] = self.s_prev[freq]
            self.s_prev[freq] = s
            self.N[freq]+=1
            power = (self.s_prev2[freq]*self.s_prev2[freq]) + (self.s_prev[freq]*self.s_prev[freq]) - (self.coeff[freq]*self.s_prev[freq]*self.s_prev2[freq])
            self.totalpower[freq]+=sample*sample
            if (self.totalpower[freq] == 0):
                self.totalpower[freq] = 1
            freqs[freq] = power / self.totalpower[freq] / self.N[freq]
        return self.get_n(freqs)

 


if __name__ == '__main__':
    
    __logo__()
    wavfile = raw_input("Enter Your Wav File : ")
    wav = wave.open(wavfile, 'r')
    (nchannels, sampwidth, framerate, nframes, comptype, compname) = wav.getparams()
    frames = wav.readframes(nframes * nchannels)
    
    frames = struct.unpack_from("%dH" % nframes * nchannels, frames)
    
    if nchannels == 2:
        left = [frames[i] for i in range(0,len(frames),2)]
        right = [frames[i] for i in range(1,len(frames),2)]
    else:
        left = frames
        right = left
    binsize = 400
    
    binsize_split = 4
    prevvalue = ""
    prevcounter = 0
    for i in range(0,len(left)-binsize,binsize/binsize_split):
        goertzel = Detector(framerate)
        for j in left[i:i+binsize]:
            value = goertzel.show(j)
        if value==prevvalue:
            prevcounter+=1
            if prevcounter==10:
                print value
        else:
            prevcounter=0
            prevvalue=value
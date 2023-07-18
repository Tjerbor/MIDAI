from utils.external_utils.midi2audio import *
from utils.utils import get_project_root
import os

fs = FluidSynth(get_project_root() + '\\data\\soundfonts\\mg_symphony_hall_bank.SF2')

'''
If data/exports folder doesn't exist yet
'''


def createExports():
    os.system('"mkdir ' + get_project_root() + '\\data\\exports"')


'''
Example of converting midi to audio file and
'''


def convert():
    fs.midi_to_audio(
        get_project_root() + '\\data\\midis\\Cymatics - MIDI 21 - C# - chords.mid',
        get_project_root() + '\\data\\exports\\chords.wav'
    )

    fs.midi_to_audio(
        get_project_root() + '\\data\\midis\\Cymatics - MIDI 22 - C# - melody.mid',
        get_project_root() + '\\data\\exports\\melody.wav'
    )


'''
Example of combining two audio clips
'''


def combine():
    os.system('"sox.exe -m '
              + get_project_root() + '"\\data\\exports\\chords.wav" '
              + get_project_root() + '"\\data\\exports\\melody.wav" '
              + get_project_root() + '"\\data\\exports\\combined.wav""'
              )


if __name__ == '__main__':
    createExports()
    convert()
    combine()

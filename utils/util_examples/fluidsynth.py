from utils.external_utils.midi2audio import *
from utils.constants import ROOT
import os

fs = FluidSynth(ROOT + '\\data\\soundfonts\\mg_symphony_hall_bank.SF2')  # soundfont file

def create_exports_folder():
    """
    If data/exports folder doesn't exist yet
    """

    os.system('"mkdir ' + ROOT + '\\data\\exports"')


def convert():
    """
    Example of converting midi to audio file and
    """

    fs.midi_to_audio(
        ROOT + '\\data\\midis\\Cymatics - MIDI 21 - C# - chords.mid',  # Input File
        ROOT + '\\data\\exports\\chords.wav'  # Output File
    )

    fs.midi_to_audio(
        ROOT + '\\data\\midis\\Cymatics - MIDI 22 - C# - melody.mid',
        ROOT + '\\data\\exports\\melody.wav'
    )


def combine():
    """
    Example of combining two audio clips
    """

    os.system(
        '"sox.exe -m '
        # -m: mix two audioclips, results in 2 channels (stereo)
        # -M: merge two audioclips, results in 4 channels
        + ROOT + '"\\data\\exports\\chords.wav" '  # First Input File
        + ROOT + '"\\data\\exports\\melody.wav" '  # Second Input File
        + ROOT + '"\\data\\exports\\combined.wav""'  # Output File
    )


def play_midi():
    """
    Example of playing a midi file
    """

    fs.play_midi(ROOT + '\\data\\midis\\Cymatics - MIDI 21 - C# - chords.mid')


if __name__ == '__main__':
    """
    Example main
    """
    create_exports_folder()
    convert()
    combine()
    #play_midi()

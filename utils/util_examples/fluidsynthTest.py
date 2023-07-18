from utils.external_utils.midi2audio import *
from utils.utils import get_project_root
import os

root = str(get_project_root())
fs = FluidSynth(root + '\\data\\soundfonts\\mg_symphony_hall_bank.SF2')  # soundfont file


def createExportsFolder():
    """
    If data/exports folder doesn't exist yet
    """

    os.system('"mkdir ' + root + '\\data\\exports"')


def convert():
    """
    Example of converting midi to audio file and
    """

    fs.midi_to_audio(
        root + '\\data\\midis\\Cymatics - MIDI 21 - C# - chords.mid',  # Input File
        root + '\\data\\exports\\chords.wav'  # Output File
    )

    fs.midi_to_audio(
        root + '\\data\\midis\\Cymatics - MIDI 22 - C# - melody.mid',
        root + '\\data\\exports\\melody.wav'
    )


def combine():
    """
    Example of combining two audio clips
    """

    os.system(
        '"sox.exe -m '  # -m: mix two audioclips, results in 2 channels; -M: merge two audioclips, results in 4 channels
        + root + '"\\data\\exports\\chords.wav" '  # First Input File
        + root + '"\\data\\exports\\melody.wav" '  # Second Input File
        + root + '"\\data\\exports\\combined.wav""'  # Output File
    )


def playMidi():
    """
    Example of playing a midi file
    """

    fs.play_midi(root + '\\data\\midis\\Cymatics - MIDI 21 - C# - chords.mid')


if __name__ == '__main__':
    createExportsFolder()
    convert()
    combine()
    playMidi()

from pathlib import Path
import os

from utils.constants import ROOT

def get_project_root() -> str:
    """
    Returns project root path
    :rtype: str
    """
    return str(Path(__file__).absolute().parent.parent)

def midi2csv(file_path: str, output_path: str = None):
    """
    Converts .mid(i) file to .csv file using midicsv.exe
    :param file_path: Input midi filepath
    :param output_path: Output csv filepath. If not given, will be written in input folder.
    """
    if output_path == None:
        output_path = file_path[:len(file_path) - 3] + "csv"

    os.system(
        f"\"{ROOT}\\utils\\external_utils\\midicsv-1.1\\midicsv.exe\" \"{file_path}\" \"{output_path}\""
    )


def csv2midi(file_path: str, output_path: str = None):
    """
    Converts .sv file to .midi file using csvmidi.exe
    :param file_path: Input csv filepath
    :param output_path: Output mid(i) filepath. If not given, will be written in input folder.
    """
    if output_path == None:
        output_path = file_path[:len(file_path) - 3] + "mid"

    os.system(
        f"\"{ROOT}\\utils\\external_utils\\midicsv-1.1\\midicsv.exe\" \"{file_path}\" \"{output_path}\""
    )

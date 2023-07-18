from pathlib import Path
import os


def get_project_root() -> str:
    """
    Returns project root path
    """
    return str(Path(__file__).absolute().parent.parent)


def midi2csv(filePath: str, outputPath: str = None):
    """
    Converts .mid(i) file to .csv file using midicsv.exe
    :param filePath: Input midi filepath
    :param outputPath: Output csv filepath. If not given, will be written in input folder.
    """
    if outputPath == None:
        outputPath = filePath[:len(filePath) - 3] + "csv"
    os.system(
        "cd \"" + get_project_root() + "\\utils\\external_utils\\midicsv-1.1\""
                                       "&& midicsv \"" + filePath + "\" \"" + outputPath + "\""
    )


def csv2midi(filePath: str, outputPath: str = None):
    """
    Converts .sv file to .midi file using csvmidi.exe
    :param filePath: Input csv filepath
    :param outputPath: Output mid(i) filepath. If not given, will be written in input folder.
    """
    if outputPath == None:
        outputPath = filePath[:len(filePath) - 3] + "mid"
    os.system(
        "cd \"" + get_project_root() + "\\utils\\external_utils\\midicsv-1.1\""
                                       "&& csvmidi \"" + filePath + "\" \"" + outputPath + "\""
    )

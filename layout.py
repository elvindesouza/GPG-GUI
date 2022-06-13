import PySimpleGUI as sg

layout = [
    [sg.Text("Encryption-Decryption made easy!")],
    [sg.Button("Encrypt file(s)", key="-FILE-")],
    [sg.Button("Encrypt folder(s)", key="-FOLD-")],
    [sg.Button("Decrypt file(s)", key="-DFILE-")],
    [sg.Button("Decrypt folder(s)", key="-DFOLD-")],
    [sg.Button("Alternate recipient", key="-HOME-")],
    [sg.Button("Beginner? Click here!", key="-BEGIN-")],
    [sg.Button("Close")],
]


def get_window() -> sg.Window:
    # sg.ChangeLookAndFeel("topanga")
    return sg.Window("GPG-GUI", layout)

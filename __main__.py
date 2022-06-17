from .Decrypt.decrypt_files import decrypt_files
from .Decrypt.decrypt_folders import decrypt_folders
from .Encrypt.encrypt_files import encrypt_files
from .Encrypt.encrypt_folders import encrypt_folders
from .Utils.gpggui_utils import create_keys

from .layout import get_window


if __name__ == "__main__":
    win = get_window()
    import PySimpleGUI as sg

    while True:
        event, values = win.read()
        if (
            event == sg.WIN_CLOSED or event == "Close"
        ):  # if user closes window or clicks cancel
            break
        # implement match statement instead
        match event:
            case "-FILE-":
                encrypt_files()
            case "-FOLD-": encrypt_folders()
            case "-DFILE-":
                decrypt_files()
            case "-DFOLD-":
                decrypt_folders()
            case "-BEGIN-":
                create_keys()
            case _:
                pass
    win.close()

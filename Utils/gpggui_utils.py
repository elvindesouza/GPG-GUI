from pathlib import Path
import PySimpleGUI as sg


def choose_folders() -> list[str] | None:
    res: str = "Yes"
    folder_list: list[str] = []
    while res == "Yes":
        folder: str = sg.popup_get_folder(
            "Choose folders",
            title="Select one folder at a time",
            default_path=Path(__file__).parent,
        )
        if not folder or folder == str(Path(__file__).parent):
            break
        if folder not in folder_list:
            folder_list.append(folder)
        res = sg.popup_yes_no("Add one more folder?")
    if len(folder_list) == 0:
        return None
    return folder_list


def choose_files() -> list[str] | None:
    file_selection: str = sg.popup_get_file(
        "Choose files",
        "Select file(s)",
        default_path=Path(__file__).parent,
        multiple_files=True,
        background_color="black",
    )
    if not file_selection:
        return None
    file_list: list[str] = file_selection.split(";")
    if len(file_list) == 1 and Path(file_list[0]).is_dir():
        return None
    return file_list


def get_email() -> str | None:
    inpt = sg.popup_get_text("Enter email: ")
    if inpt and (inpt == "" or "@" not in inpt or "." not in inpt):
        return None
    return inpt


def get_pubkey():
    pass


def get_privkey():
    pass


def trash():
    pass


def find():
    pass


def create_keys():
    pass

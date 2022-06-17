from pathlib import Path
from shutil import copytree
from subprocess import run
import PySimpleGUI as sg
from . import glob_trash_cmd
from .. import GPG_NOPUBKEYS


def choose_folders(
    title_str: str = "Choose Folders", dst_action: str = ""
) -> list[tuple[str, str]] | None:
    res: str = "Yes"
    folders: list[tuple[str, str]] = []
    while res == "Yes":
        src: str = sg.popup_get_folder(
            title=title_str,
            message="Select one folder at a time",
            default_path=Path(__file__).parent,
            background_color="black",
            size=(100, 100),
        )
        if not src or src == str(Path(__file__).parent):
            break

        dst: str = sg.popup_get_folder(
            message=f"Directory to {dst_action} {src} to-",
            title="Select OK without selecting directory to use same path(merge)",
            default_path=Path(src).parent,
            background_color="brown",
            size=(100, 100),
        )
        if not dst:
            break
        if Path(dst) == Path(src).parent:
            dst = str(Path(src)) + f"_{dst_action}ed"
            copytree(src, dst, dirs_exist_ok=True)
        else:
            dst = dst + "/" + Path(src).name

        if src not in folders:
            folders.append((src, dst))
        res: str = sg.popup_yes_no("Add one more folder?")
    if len(folders) == 0:
        return None
    return folders


def choose_files(title_string: str = "Choose files") -> list[str] | None:
    file_selection: str = sg.popup_get_file(
        title=title_string,
        message="Select file(s)",
        default_path=Path(__file__).parent,
        multiple_files=True,
        background_color="black",
        size=(100, 100),
    )
    if not file_selection:
        return None
    file_list: list[str] = file_selection.split(";")
    if len(file_list) == 1 and Path(file_list[0]).is_dir():
        return None
    return file_list


def get_email() -> str | None:
    if GPG_NOPUBKEYS:
        return get_pubkey()
    inpt: str = sg.popup_get_text("Enter email: ")
    if inpt and (inpt == "" or "@" not in inpt or "." not in inpt):
        return None
    return inpt


# TODO
def get_pubkey() -> str | None:
    keyfile = sg.popup_get_file()
    run("gpg", "--import", keyfile)


def trash(file: str):
    if Path(file).is_file():
        run([glob_trash_cmd, file])


def create_keys():
    pass

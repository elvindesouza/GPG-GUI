from .decrypt_files import decrypt_files
from ..Utils.gpggui_utils import choose_folders, trash
from shutil import copytree
from pathlib import Path


# TODO edit sel_folds() to ask for dst for every src, and be tuple[str,str] instead
def decrypt_folders(folders: list[tuple[str, str]] = None):
    if not folders:
        folders: list[tuple[str, str]] = choose_folders(
            "Decrypting Folders",
            "decrypt",
        )
    if not folders:
        return
    for src, dst in folders:
        copytree(src, dst, dirs_exist_ok=True)
        files = [
            str(x) for x in Path(dst).rglob("*") if x.is_file() and x.suffix == ".gpg"
        ]
        if not decrypt_files(files):
            return
        for file in files:
            trash(file)

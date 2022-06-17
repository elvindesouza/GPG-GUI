from ..Utils.gpggui_utils import choose_folders, get_email
from ..Encrypt.encrypt_files import encrypt_files
from shutil import copytree
from pathlib import Path

# TODO implement pubkey

# direct way to encrypt full folders w/ GPG
def encrypt_folders(folders: list[tuple[str, str]] = None) -> None:
    if not folders:
        folders = choose_folders("Encrypting Folders", "encrypt")
    if not folders:
        return

    email = get_email()
    if not email:
        return

    for src, dst in folders:
        copytree(src, dst, dirs_exist_ok=True)
        files = [
            str(x) for x in Path(dst).rglob("*") if x.is_file() and x.suffix != ".gpg"
        ]
        if not encrypt_files(files, email):
            return
        for file in files:
            trash(file)

# choose better approach? like create  a separate folder like decompressing an archive
def decrypt_folders(folders: list[str] = None):
    from pathlib import Path
    from Decrypt.decrypt_files import decrypt_files
    from Utils.gpggui_utils import choose_folders
    from PySimpleGUI import popup_get_folder

    if not folders:
        folders: list[str] = choose_folders()
    if not folders:
        return
    print(folders)
    for folder in folders:
        target_folder: str = popup_get_folder(
            "Cancel to use same path(merge)",
            title=f"Directory to decrypt {folder} to-",
            default_path=Path(folder).parent,
        )
        if not target_folder:
            target_folder = (Path(folder).parent)
        decrypt_files(
            [str(x) for x in Path(folder).rglob("*") if x.is_file()],target_folder
        )

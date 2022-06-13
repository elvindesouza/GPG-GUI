# direct way to encrypt full folders w/ GPG


def encrypt_folders(folders=None):
    from Utils.gpggui_utils import choose_folders, get_email, get_pubkey
    from PySimpleGUI import popup,popup_yes_no
    from pathlib import Path
    from subprocess import CompletedProcess, run

    if not folders:
        folders:list[str]|None=choose_folders()
    if not folders:
        return

    email = get_email()
    if not email:
        get_pubkey()

    for folder in folders:
        ps = run(["find", f"{folder}"], capture_output=True, encoding="utf-8")
        files:list[str] = ps.stdout.split("\n")
        ps:CompletedProcess[str] = run(
            f"find . | /usr/bin/gpg --multifile --yes --encrypt-files -r {email}",
            cwd=folder,
            shell=True,
            encoding="utf-8",
            capture_output=True,
        )
        if ps.stderr:
            popup(
                "There were a few errors\nReview errors and see if you want to delete files\n"
                + ps.stderr
            )
        should_del:str = popup_yes_no("Delete the original file(s)?")
        if should_del != "Yes":
            return
        for file in files:
            if Path(file).is_file():
                run(["/usr/bin/trash", f"{file}"], cwd=Path(folder).parent)
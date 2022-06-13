def encrypt_files(files:list[str]=None):
    from pathlib import Path
    from subprocess import run
    from Utils.gpggui_utils import choose_files, get_email, get_pubkey
    from PySimpleGUI import popup,popup_yes_no

    if not files:
        files = choose_files()
    if not files:
        return

    email = get_email()
    if not email:
        global pubkey
        pubkey=get_pubkey()

    for file in files:
        ps = run(
            ["gpg", "-r", email, "-e", file],
            cwd=Path(file).parent,
            capture_output=True,
            encoding="utf-8",
        )
        if ps.stderr:
            popup("There was an error encrypting the file(s)\n" + ps.stderr)
            return
    ask_to_del = popup_yes_no(
        "Completed without errors, delete the original file(s)?"
    )

    if ask_to_del == "Yes":
        for file in files:
            run()(["trash", f"{file}"], cwd=Path(file).parent)

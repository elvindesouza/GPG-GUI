from pathlib import Path
from subprocess import run
from ..Utils.gpggui_utils import choose_files, get_email
from PySimpleGUI import popup


def encrypt_files(files: list[str] = None, email: str = None) -> bool:
    if not files:
        files = choose_files("Encrypt Files")
    if not files:
        return False

    if not email:
        email = get_email()
    if not email:
        return False

    for file in files:
        ps: CompletedProcess[str] = run(
            ["gpg", "--yes", "-r", email, "-e", file],
            cwd=Path(file).parent,
            capture_output=True,
            encoding="utf-8",
        )
        if ps.stderr:
            popup("There was an error encrypting the file(s)\n" + ps.stderr)
            return False
    return True

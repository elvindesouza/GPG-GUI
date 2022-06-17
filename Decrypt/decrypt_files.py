from ..Utils.gpggui_utils import choose_files
from subprocess import CompletedProcess
from pathlib import Path
from subprocess import run
from PySimpleGUI import popup


# returns bool: False->a file could not be decrypted, True-> all decrypted successfully
def decrypt_files(files: list[str] = None) -> bool:
    if not files:
        files = choose_files("Decrypting Files")
    if not files:
        return False

    files: list[str]

    for file in files:
        ps: CompletedProcess[str] = run(
            ["/usr/bin/gpg", "--yes", "-o", Path(file).stem, "-d", file],
            cwd=Path(file).parent,
            capture_output=True,
            encoding="utf-8",
        )
        if ps.stderr:
            popup("There was an error decrypting the file(s)\n" + ps.stderr)
            return False
    return True

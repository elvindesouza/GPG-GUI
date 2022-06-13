from os import mkdir
from pathlib import Path
from subprocess import run
from Utils.gpggui_utils import choose_files, get_privkey


# reimplement decrypt directory
def decrypt_files(files: list[str] = None, target: str = ""):
    if not files:
        files = choose_files()
    if not files:
        return

    files: list[str]
    # get_privkey()

    if target:
        mkdir(Path(file).stem)
    for file in files:
        ps = run(
            ["/usr/bin/gpg", "-o", target + Path(file).stem, "-d", f"{file}"],
            cwd=Path(file).parent,
            encoding="utf-8",
        )

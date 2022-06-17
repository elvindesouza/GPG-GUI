from pathlib import Path
from subprocess import run
from PySimpleGUI import popup
from sys import exit, stdout

print("----Welcome to GPG-GUI!----")


class GPG_Profile:
    gpg_binary = "/usr/bin/gpg"
    gpg_pubkey = ""


profile = GPG_Profile()
if not Path(profile.gpg_binary).exists():
    popup("You do not seem to have GnuPG installed!")
    exit()


_gpg_pubkeys = run(
    ["gpg", "--list-public-keys"],
    capture_output=True,
    encoding="utf-8",
)
if "pub" not in _gpg_pubkeys.stdout:
    GPG_NOPUBKEYS = True
    stdout.write("You do not have any public keys in your keyring!")
else:
    GPG_NOPUBKEYS = False

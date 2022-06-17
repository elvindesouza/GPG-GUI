from pathlib import Path
from sys import stderr

glob_trash_bin_exists = False
glob_trash_cmd = "/usr/bin/rm"

if Path("/usr/bin/trash").exists():
    glob_trash_bin_exists = True
    glob_trash_cmd = "/usr/bin/trash"
else:
    stderr.write(
        "Consider installing trash-cli to send deleted files to your trash(Recycle Bin), deleting files normally for now"
    )

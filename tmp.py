from pathlib import Path
file="/home/user/Downloads/MyFolder/file2.txt.gpg.gpg"
f = Path("/home/user/Documents")
fp=Path(file)
print(fp.parent)

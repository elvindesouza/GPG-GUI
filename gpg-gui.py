#! /usr/bin/env python
# -*- coding: utf-8 -*-
import os
import argparse
from pathlib import Path

# Error message global constants

# main
def main():
    # create parser object
    parser = argparse.ArgumentParser(
        description="GPG-GUI- A graphical front-end to GnuPG."
    )

    # defining arguments for parser object
    parser.add_argument(
        "-e",
        "--encrypt",
        type=str,
        nargs=1,
        metavar="file_name",
        default=None,
        help="Opens and reads the specified text file.",
    )

    parser.add_argument(
        "-d",
        "--decrypt",
        type=str,
        nargs=1,
        metavar="path",
        default=None,
        help="Shows all the text files on specified directory path.\
                        Type '.' for current directory.",
    )

    # parser.add_argument("-d", "--pubkey", type = str, nargs = 1,
    #                     metavar = "file_name", default = None,
    #                     help = "Deletes the specified text file.")

    # parser.add_argument("-c", "--copy", type = str, nargs = 2,
    #                     metavar = ('file1','file2'), help = "Copy file1 contents to \
    #                     file2 Warning: file2 will get overwritten.")

    # parser.add_argument("--rename", type = str, nargs = 2,
    #                     metavar = ('old_name','new_name'),
    #                     help = "Renames the specified file to a new name.")

    # parse the arguments from standard input
    args = parser.parse_args()

    # calling functions depending on type of argument
    if args.encrypt != None:
        encrypt(args)
    elif args.decrypt != None:
        decrypt(args)
    # elif args.delete !=None:
    #     delete(args)
    # elif args.copy != None:
    #     copy(args)
    # elif args.rename != None:
    #     rename(args)


def encrypt(args):
    from Encrypt import encrypt_files, encrypt_folders

    obj: str = args.encrypt[0]
    if Path(obj).is_file():
        print("is a file")
        encrypt_files.encrypt_files([obj])
    if Path(obj).is_dir():
        encrypt_folders.encrypt_folders([obj])


def decrypt(args):
    pass


if __name__ == "__main__":
    # calling the main function
    main()


class GPG_Profile:
    gpg_binary = "/usr/bin/gpg"
    gpg_pubkey = ""
    trash_binary = None
    find_binary = None


def cli_parse():
    pass


# not implemented yet
def altHome():
    pass

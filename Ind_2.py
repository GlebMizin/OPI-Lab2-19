#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import argparse
import os
from pathlib import Path


def tree_size(path, seen, head="", tail=""):
    if path.resolve() not in seen:
        seen.add(path.resolve())
        size = float('{:.3f}'.format(os.path.getsize(path)/1024))
        print(head + path.name + " " + str(size) + "KB")
        dirs = []
        files = []
        if path.is_dir():
            dirs = sorted(filter(Path.is_dir, path.iterdir()))
            files = sorted(filter(Path.is_file, path.iterdir()))
        entries = dirs + files
        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                tree_size(entry, seen, tail + "├──", tail + "│  ")
            else:
                tree_size(entry, seen, tail + "└──", tail + "   ")


def tree_a(path, seen, head="", tail=""):
    if path.resolve() not in seen:
        seen.add(path.resolve())
        print(head + path.name)
        dirs = []
        files = []
        if path.is_dir():
            dirs = sorted(filter(Path.is_dir, path.iterdir()))
            files = sorted(filter(Path.is_file, path.iterdir()))
        entries = dirs + files
        for i, entry in enumerate(entries):
            if i < len(entries) - 1:
                tree_a(entry, seen, tail + "├──", tail + "│  ")
            else:
                tree_a(entry, seen, tail + "└──", tail + "   ")


def main(command_line=None):
    parser = argparse.ArgumentParser(description="tree")

    parser.add_argument(
        "path",
        help="path, cwd - Path.cwd(), home - Path.home()"
    )
    subparser_1 = parser.add_subparsers(dest="command", required=False)

    subparser_1.add_parser('s', help='display file sizes in human-readable format')

    subparser_1.add_parser('a', help='display file sizes in human-readable format')

    args = parser.parse_args()

    if args.path == "cwd":
        path = Path.cwd()
    elif args.path == "home":
        path = Path.home()
    else:
        path = Path(args.path)

    if path.exists():
        if args.command == "s":
            tree_size(path, set())
        if args.command == "a":
            tree_a(path, set())

    else:
        print("err")


if __name__ == "__main__":
    main()
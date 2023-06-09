#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import pathlib


def unique_path(directory, name_pattern):
    counter = 0
    while True:
        counter += 1
        path = directory / name_pattern.format(counter)
        if not path.exists():
            return path


if __name__ == "__main__":
    # Создать уникальное имя файла
    # {:03d} - принимает целое число в качестве аргумента,
    # задает минимальную ширину 3
    # и заполняет оставшиеся места нулями
    path = unique_path(pathlib.Path.cwd(), "test{:03d}.txt")
    print(path)
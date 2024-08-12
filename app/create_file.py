import sys
import os
from datetime import datetime
from typing import List


def create_path(path_dir: List[str]) -> str:
    full_path = os.path.join(*path_dir)
    os.makedirs(full_path, exist_ok=True)
    print(f"Directory created: {full_path}")
    return full_path


def create_file(file_path: str) -> None:
    with open(file_path, "a") as source_file:
        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"\n{timestamp}\n")
        line_number = 1
        while True:
            content = input(f"Enter content line {line_number}: ")
            if content.lower() == "stop":
                break
            source_file.write(f"{line_number} {content}\n")
            line_number += 1


def main() -> None:
    if len(sys.argv) < 2:
        print("Usage: python create_file [-d directory_path] [-f file_name]")
        return
    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        dir_parts = sys.argv[d_index + 1:]
        if "-f" in dir_parts:
            f_index = dir_parts.index("-f")
            dir_parts, file_name = dir_parts[:f_index], dir_parts[f_index + 1]
        else:
            file_name = None

        dir_path = create_path(dir_parts)

        if file_name:
            file_path = os.path.join(dir_path, file_name)
            create_file(file_path)

    elif "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]
        create_file(file_name)
    else:
        print(
            "No valid flags provided."
            " Use -d for directories or -f for files"
        )

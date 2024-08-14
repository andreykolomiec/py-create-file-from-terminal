import sys
import os
from datetime import datetime
from typing import List, Optional


def create_path(path_dir: List[str]) -> str:
    full_path = os.path.join(*path_dir)
    os.makedirs(full_path, exist_ok=True)
    print(f"Directory created: {full_path}")
    return str(full_path)


def create_file(file_path: str) -> None:
    with open(file_path, "a") as source_file:
        if os.path.getsize(file_path) > 0:
            source_file.write("\n\n")

        timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        source_file.write(f"{timestamp}")
        line_number = 1
        while True:
            content = input("Enter content line: ")
            if content.lower() == "stop":
                break
            source_file.write(f"\n{line_number} {content}")
            line_number += 1


def main() -> None:
    if len(sys.argv) < 2:
        print(
            "Usage:"
            " python create_file.py [-d directory_path] [-f file_name]"
        )
        return

    dir_parts: List[str] = []
    file_name: Optional[str] = None

    if "-d" in sys.argv:
        d_index = sys.argv.index("-d")
        dir_parts = sys.argv[d_index + 1:]

        if "-f" in dir_parts:
            f_index = dir_parts.index("-f")
            file_name = dir_parts[f_index + 1]
            dir_parts = dir_parts[:f_index]

    if "-f" in sys.argv:
        f_index = sys.argv.index("-f")
        file_name = sys.argv[f_index + 1]

        if "-d" in sys.argv and not dir_parts:
            d_index = sys.argv.index("-d")
            dir_parts = sys.argv[d_index + 1:]

            if "-f" in dir_parts:
                f_index = dir_parts.index("-f")
                dir_parts = dir_parts[:f_index]

    if dir_parts:
        dir_path = create_path(dir_parts)
        file_path = (
            os.path.join(dir_path, file_name)
            if file_name else dir_path
        )
    else:
        file_path = file_name

    if file_name:
        create_file(file_path)


if __name__ == "__main__":
    main()

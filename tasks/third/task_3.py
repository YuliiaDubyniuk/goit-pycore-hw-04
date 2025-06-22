from pathlib import Path
import sys
from colorama import init, Fore


def get_root_folder() -> Path:
    if len(sys.argv) >= 2:
        folder_path = Path(sys.argv[1])
        return folder_path
    else:
        print("Folder path has not been provided.")


folder_path = get_root_folder()


def parse_folder(f_path: Path):
    init(autoreset=True)
    if f_path:
        for el in f_path.iterdir():
            if el.is_dir():
                print(f"{Fore.BLUE}{el.name}/")
                parse_folder(f_path / el)
            else:
                print(f"{Fore.GREEN}{el.name}")


parse_folder(folder_path)

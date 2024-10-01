import sys
from pathlib import Path
from colorama import init, Fore, Style

init(autoreset=True)

def display_directory_structure(directory: Path, prefix=""):
    try:
        for path in directory.iterdir():
            if path.is_dir():
                print(f"{prefix}{Fore.BLUE}{path.name}/")
                
                display_directory_structure(path, prefix + "    ")
            else:
                print(f"{prefix}{Fore.GREEN}{path.name}")
    except Exception as e:
        print(f"{Fore.RED}Error: {str(e)}")

def main():
    if len(sys.argv) != 2:
        print(f"{Fore.RED}Usage: python {sys.argv[0]} <directory>")
        return

    directory_path = Path(sys.argv[1])

    if not directory_path.exists():
        print(f"{Fore.RED}Error: The directory '{directory_path}' does not exist.")
        return

    if not directory_path.is_dir():
        print(f"{Fore.RED}Error: '{directory_path}' is not a directory.")
        return

    print(f"Directory structure for {directory_path}:\n")
    display_directory_structure(directory_path)

if __name__ == "__main__":
    main()
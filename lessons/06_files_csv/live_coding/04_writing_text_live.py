from pathlib import Path
import argparse

parser = argparse.ArgumentParser()
parser.add_argument("mode", choices=["w", "a", "r"], nargs="?", default="w")
parser.add_argument("text", nargs="?", default="Rīga")
args = parser.parse_args()
path = Path("output/lesson06/modes.txt")
path.parent.mkdir(parents=True, exist_ok=True)
if args.mode == "r":
    if not path.is_file():
        print("Vispirms izveido failu ar w.")
    else:
        print(path.read_text(encoding="utf-8"), end="")
else:
    with path.open(args.mode, encoding="utf-8") as file:
        file.write(args.text + "\n")
    print(path.read_text(encoding="utf-8"), end="")

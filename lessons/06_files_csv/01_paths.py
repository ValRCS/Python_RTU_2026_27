from pathlib import Path

print("Darba mape:", Path.cwd())
path = Path("datasets") / "pilsetas.txt"
print("Relatīvais ceļš:", path)
print("Absolūtais ceļš:", path.resolve())
print("Vai fails pastāv?", path.is_file())

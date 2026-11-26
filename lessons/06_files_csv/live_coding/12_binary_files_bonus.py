from pathlib import Path

path = Path("output/lesson06/demo.bin")
path.parent.mkdir(parents=True, exist_ok=True)
with path.open("wb") as file:
    file.write("Rīga".encode("utf-8"))
with path.open("rb") as file:
    data = file.read()
print(type(data), data, len(data))
assert data.decode("utf-8") == "Rīga"
copy = path.with_name("demo_copy.bin")
copy.write_bytes(data)
assert copy.read_bytes() == data

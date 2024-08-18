import requests, os

current_dir = os.getcwd()

# Join the current directory with the filename
flie_data = os.path.join(current_dir, "core\\!Main.py")
versions_file = os.path.join(current_dir, "data\\version")
print("Updating...")

update = requests.get(
    "https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/core/!Main.py"
)
version = requests.get(
    "https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/data/version"
)
versions = version.text.strip()
with open(flie_data, "wb") as f:
    f.write(update.content)
    f.close()
with open(versions_file, "rb") as fs:
    version = fs.read()
    fs.close()
if versions != version:
    with open(flie_data, "wb") as ff:
        ff.write(versions)
        ff.close()

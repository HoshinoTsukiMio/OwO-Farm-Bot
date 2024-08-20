import requests, os

current_dir = os.getcwd()

# Join the current directory with the filename
flie_data = os.path.join(current_dir, "core\\!Main.py")
versions_file = os.path.join(current_dir, "data\\version")
print("Updating...")
version = requests.get(
    "https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/data/version"
)
update = requests.get(
    "https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/core/!Main.py"
)
versions = version.text.strip()
with open(flie_data, "wb") as f:
    f.write(update.content)
    f.close()
with open(versions_file, "r") as fs:
    version = fs.read()
    fs.close()
if versions != version:
    print("new version")
    with open(versions_file, "w") as ff:
        ff.write(versions)
        ff.close()

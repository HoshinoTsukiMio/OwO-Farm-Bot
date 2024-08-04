import requests, os
current_dir = os.getcwd()

# Join the current directory with the filename
flie_data = os.path.join(current_dir, 'core\\!Main.py')
print("Updating...")
update = requests.get("https://raw.githubusercontent.com/HoshinoTsukiMio/OwO-Farm-Bot/main/OwO%20Console/core/!Main.py")
with open(flie_data, "wb") as f:
    f.write(update.content)
    f.close()

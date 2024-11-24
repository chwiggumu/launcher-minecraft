import minecraft_launcher_lib as mc
import subprocess


mc_dir = mc.utils.get_minecraft_directory()
all_ver_info = mc.utils.get_available_versions(mc_dir)

ver_list = []
av_ver_list = []

def install_version():
    for version in all_ver_info:
        if version["type"] == "release":
            ver_list.append(version["id"])
            
  
    for index, version in enumerate(ver_list):
        print(index, version)
        
    version = int(input("What version you want install?"))
    mc.install.install_minecraft_version(ver_list[version], mc_dir)
    print("Installed successfully")
    
    
def launch_version():
    setting = {
        "username": input("Write your username ->"),
        "uuid": "80aec8d6-5207-41b4-b923-b7e60e050e88",
        "token": "token",
    }
  
    for index, version in enumerate(mc.utils.get_installed_versions(mc_dir)):
        print(index, version["id"])
        av_ver_list.append(version["id"])
        
    sel_ver = int(input("Select the version for play ->"))

    minecraft_command = mc.command.get_minecraft_command(av_ver_list[sel_ver], mc_dir, setting)

    subprocess.run(minecraft_command)


def main():
    if input("Want to install any version [Y/N]").upper() == "y".upper():
        install_version()
        
    launch_version() 
    
    
if __name__ == "__main__":
    main()
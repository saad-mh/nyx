import platform
import os

def system_status():
    return {
        "os": platform.system(),
        "hostname": platform.node(),
        "user": os.getlogin()
    }

# print("system status: ", system_status())
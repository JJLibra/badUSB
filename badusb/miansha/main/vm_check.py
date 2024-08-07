import os
import psutil
from multiprocessing import cpu_count


def check_file():
    vmFile = [
        'C:/windows/System32/Drivers/Vmmouse.sys',
        'C:/windows/System32/Drivers/vmtray.dll',
        'C:/windows/System32/Drivers/VMToolsHook.dll',
        'C:/windows/System32/Drivers/vmmousever.dll',
        'C:/windows/System32/Drivers/vmhgfs.dll',
        'C:/windows/System32/Drivers/vmGuestLib.dll',
        'C:/windows/System32/Drivers/VBoxMouse.sys',
        'C:/windows/System32/Drivers/VBoxGuest.sys',
        'C:/windows/System32/Drivers/VBoxSF.sys',
        'C:/windows/System32/Drivers/VBoxVideo.sys',
        'C:/windows/System32/vboxdisp.dll',
        'C:/windows/System32/vboxhook.dll',
        'C:/windows/System32/vboxoglerrorspu.dll',
        'C:/windows/System32/vboxoglpassthroughspu.dll',
        'C:/windows/System32/vboxservice.exe',
        'C:/windows/System32/vboxtray.exe',
        'C:/windows/System32/VBoxControl.exe',
    ]

    for data in vmFile:
        result = os.path.exists(data)
        if result:
            return 0
    return 1


def check_virtual():  # 检查名称
    vmName = os.popen('wmic path Win32_ComputerSystem get Model')
    text = vmName.read()
    if 'vmware' in text:
        return 0
    return 1


def numberOfCPU():  # 检查CPU个数
    if int(format(cpu_count())) < 4:
        return 0
    return 1


def physicalMemory():
    data = psutil.virtual_memory()
    total = data.total
    n = int(total / 1024 / 1024 / 1024) + 1  # GB
    if n < 4:
        return 0
    return 1

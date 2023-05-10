import modules.shell_runner as shell_runner
from subprocess import check_output
import json
import time
import re

def get_adb_devices():
    output = check_output(['adb', 'devices']).decode()
    pattern = re.compile(r'^(.*)\tdevice$', re.MULTILINE)
    device_names = [match.group(1) for match in pattern.finditer(output)]
    if not device_names:
        print("No devices found.")
    return device_names

def iterate_device(device_names):
    for device in device_names:
        response = input(f"Do you want to change the environment of {device}? (y/n):")
        if (len(response) < 1 or response[0] != "y"):
            continue
        else:
            change_env(device)
            
def select_preset():
    with open("./presets/system_preset.json", "r") as f:
        preset_list = json.load(f)
    iter = 1
    for preset in preset_list:
        print(str(iter) + ". " + preset['PRESET_NAME'])
        iter += 1
    preset = input("Please Select a preset:\n")
    return int(preset)
    

def change_env(device):
    print(f"Changing Environment of {device}")
    preset_number = select_preset() - 1
    with open("./presets/system_preset.json", "r") as f:
        preset = json.load(f)[preset_number]
    try:
        # TODO: make avd writable system 
        # shell_runner.run(f"adb -s {device} emu kill")
        # shell_runner.run(f'/Users/mossdinger/Library/Android/sdk/emulator -avd Generic -writable-system')
        print("reopening the emulator with writable system")
        # time.sleep(15)
        shell_runner.run(f"adb -s {device} root")
        time.sleep(3)
        shell_runner.run(f"adb -s {device} remount")
        shell_runner.run(f"adb -s {device} pull /system/build.prop ./temp/build.prop")
        
        new_prop = {}
        with open("./temp/build.prop", "r") as f:
            old_prop_strings = f.read()
            lines = old_prop_strings.split('\n')
            for line in lines:
                if not line or line.startswith('#') or '=' not in line:
                    continue

                key, value = line.split('=', 1)
                key = key.strip()
                value = value.strip()

                # Add the key-value pair to the dictionary
                new_prop[key] = value
        
        new_prop.update(preset)
        # print(new_prop)

        with open('temp/new_build.prop', 'w') as f:
            for key, value in new_prop.items():
                f.write(f"{key}={value}\n")


        shell_runner.run(f"adb -s {device} push ./temp/new_build.prop /system/build.prop")
        # shell_runner.run(f"adb -s {device} shell 'chmod 644 /system/build.prop'")
        shell_runner.run(f"adb -s {device} reboot")
    except SyntaxError:
        print("Failed to pusgh device configuration")


    print(f"Changed {device} environment to match {preset['PRESET_NAME']}")
    print("Please wait for your emulator to reboot")


def main():
    device_names = get_adb_devices()
    iterate_device(device_names)

if __name__ == "__main__":
    main()



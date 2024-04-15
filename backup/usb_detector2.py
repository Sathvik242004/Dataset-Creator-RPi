import pyudev
import subprocess

def mount_usb(device_path, mount_point):
    try:
        subprocess.run(['sudo', 'mount', device_path, mount_point], check=True)
        print(f"USB drive mounted at {mount_point}")
        # Example: Copying 'captures' directory to the USB drive
        subprocess.run(['sudo', 'cp', '-r', '/home/bee/beesetup/capture_images', mount_point+'/data'], check=True)
        print("Data copied to USB drive")
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def check_and_copy_existing_drives(mount_point):
    try:
        # List mounted drives
        result = subprocess.run(['lsblk', '-o', 'NAME,MOUNTPOINT'], stdout=subprocess.PIPE)
        output = result.stdout.decode('utf-8')
        lines = output.strip().split('\n')
        for line in lines[1:]:
            parts = line.split()
            if len(parts) == 2 and parts[1] == mount_point:
                print(f"Found existing drive at {parts[1]}")
                # Example: Copying 'captures' directory to the USB drive
                subprocess.run(['sudo', 'cp', '-r', '/home/bee/beesetup/capture_images', mount_point+'/data'], check=True)
                print("Data copied to existing USB drive")
                return True
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
    return False

def monitor_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='block', device_type='disk')

    print("Monitoring USB drives...")

    mount_point = '/mnt/usb'

    # Check for existing drives when the script starts
    if not check_and_copy_existing_drives(mount_point):
        print("No existing USB drives found.")

    for device in iter(monitor.poll, None):
        if device.action == 'add':
            print("USB drive connected")
            # Modify the device path and mount point as per your system
            device_path = '/dev/' + device.sys_name + "1"
            mount_usb(device_path, mount_point)
        elif device.action == 'remove':
            print("USB drive disconnected")

if __name__ == "__main__":
    monitor_usb()

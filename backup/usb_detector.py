import pyudev
import subprocess
import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)
status = 2

GPIO.setup(status, GPIO.OUT)

def mount_usb(device_path, mount_point):
    try:
        GPIO.output(status, GPIO.LOW)
        subprocess.run(['sudo', 'mount', device_path, mount_point], check=True)
        print(f"USB drive mounted at {mount_point}")
        GPIO.output(status, GPIO.HIGH)
        time.sleep(0.5)
        GPIO.output(status, GPIO.LOW)
        # Example: Copying 'captures' directory to the USB drive
        subprocess.run(['sudo', 'cp', '-r', '/home/bee/captured_images', mount_point+'/data'], check=True)
        time.sleep(5)
        print("Data copied to USB drive")
        time.sleep(60)
        GPIO.output(status, GPIO.HIGH)

    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")

def monitor_usb():
    context = pyudev.Context()
    monitor = pyudev.Monitor.from_netlink(context)
    monitor.filter_by(subsystem='block', device_type='disk')

    print("Monitoring USB drives...")
    GPIO.output(status, GPIO.HIGH)
    time.sleep(0.3)
    GPIO.output(status, GPIO.LOW)


    for device in iter(monitor.poll, None):
        if device.action == 'add':
            print("USB drive connected")
            GPIO.output(status, GPIO.HIGH)
            # Modify the device path and mount point as per your system
            device_path = '/dev/' + device.sys_name+"1"
            print(device.sys_name)
            mount_point = '/mnt/usb'
            mount_usb(device_path, mount_point)
        elif device.action == 'remove':
            print("USB drive disconnected")
            GPIO.output(status, GPIO.LOW)

if __name__ == "__main__":
    try:
        monitor_usb()
    except:
        print("exiting...")
    finally:
        GPIO.cleanup()

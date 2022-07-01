import sys
import os

serial_api_path = "nrf_sdk/serial_api/"

if serial_api_path not in sys.path:
    sys.path.append(serial_api_path)

from pyaci import pyaci

def change_dir(newPath):
  try:
    os.chdir(newPath)
    print("Directory moved:", newPath)
  except OSError:
    print("Directory ", newPath, "does not exist.")

change_dir(serial_api_path)
pyaci()

# BatteryMenu

A lightweight macOS menu bar application that displays the battery levels of a Bluetooth keyboard and mouse.

## Features

- Displays keyboard and mouse battery percentages in the macOS menu bar.
- Automatically refreshes battery information every 60 seconds.
- Provides a manual Refresh option.
- Uses built-in macOS command-line utilities.
- No Accessibility or Input Monitoring permissions required.

## Requirements

- macOS
- Python 3.9 or newer
- A Bluetooth keyboard supported by AppleBluetoothHIDKeyboard
- A Bluetooth mouse whose battery level is reported by pmset
- Python package: rumps

## Installation

Clone the repository:

    git clone https://github.com/YOUR_USERNAME/BatteryMenu.git
    cd BatteryMenu

Create a virtual environment:

    python3 -m venv .venv
    source .venv/bin/activate

Install dependencies:

    pip install -r requirements.txt

## Configuration

Open battery_menu.py and edit:

    MOUSE_DEVICE_NAME = "BT5.0 Mouse"
    UPDATE_INTERVAL = 60

Set MOUSE_DEVICE_NAME to the mouse name reported by macOS.

To check connected accessory battery information:

    pmset -g accps

## Run

Activate the virtual environment and run:

    python battery_menu.py

The application will appear in the macOS menu bar.

## How It Works

BatteryMenu uses two macOS system utilities:

- ioreg reads the battery percentage reported by compatible Apple Bluetooth keyboards.
- pmset -g accps reads battery information reported for supported Bluetooth accessories.

The application does not communicate directly with Bluetooth devices.

## Compatibility

Battery reporting depends on the device and the information exposed by macOS.

Tested with:

- Apple Bluetooth keyboard
- BT5.0 Mouse (BEKEN)

Other devices may require code or configuration changes.

## License

MIT License. See LICENSE for details.

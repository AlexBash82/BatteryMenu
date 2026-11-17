import re
import subprocess
import rumps


# Configuration
MOUSE_DEVICE_NAME = "BT5.0 Mouse"
UPDATE_INTERVAL = 60


class BatteryMenuApp(rumps.App):
    def __init__(self):
        super().__init__("⌨️ --%  🖱 --%", quit_button="Quit")

        self.keyboard_item = rumps.MenuItem("Keyboard: reading...")
        self.mouse_item = rumps.MenuItem("Mouse: reading...")

        self.menu = [
            self.keyboard_item,
            self.mouse_item,
            None,
            rumps.MenuItem("Refresh", callback=self.refresh),
        ]

        self.refresh(None)

        self.timer = rumps.Timer(self.refresh, UPDATE_INTERVAL)
        self.timer.start()

    def run_command(self, command):
        try:
            return subprocess.check_output(
                command,
                text=True,
                encoding="utf-8",
                errors="replace",
                stderr=subprocess.DEVNULL,
                timeout=5,
            )
        except (subprocess.SubprocessError, OSError):
            return ""

    def get_keyboard_battery(self):
        output = self.run_command([
            "ioreg",
            "-c",
            "AppleBluetoothHIDKeyboard",
            "-l",
            "-w0",
        ])

        match = re.search(r'"BatteryPercent"\s*=\s*(\d+)', output)
        return int(match.group(1)) if match else None

    def get_mouse_battery(self):
        output = self.run_command(["pmset", "-g", "accps"])

        for line in output.splitlines():
            if MOUSE_DEVICE_NAME in line:
                match = re.search(r"(\d+)%", line)
                return int(match.group(1)) if match else None

        return None

    @staticmethod
    def format_battery(value):
        return f"{value}%" if value is not None else "--"

    def refresh(self, _):
        keyboard = self.get_keyboard_battery()
        mouse = self.get_mouse_battery()

        self.title = (
            f"⌨️ {self.format_battery(keyboard)}  "
            f"🖱 {self.format_battery(mouse)}"
        )

        self.keyboard_item.title = (
            f"Keyboard: {self.format_battery(keyboard)}"
        )

        self.mouse_item.title = (
            f"Mouse: {self.format_battery(mouse)}"
        )


if __name__ == "__main__":
    BatteryMenuApp().run()


class WindowManager:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def get_screens(self, screen_name):
        win32gui.EnumWindows(enum_cb, winlist)
        screens = [(hwnd, title) for hwnd, title in winlist if screen_name in title]
        while len(screens) == 0:
            screens = [(hwnd, title) for hwnd, title in winlist if screen_name in title]
            win32gui.EnumWindows(enum_cb, winlist)

        return screens

    def set_screen(self, window_name):
        try:
                win32gui.SetForegroundWindow(window_name)
        except:
                print("There was an error...Wrong Window selected")



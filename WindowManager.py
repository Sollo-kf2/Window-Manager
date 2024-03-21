import win32gui
import pywintypes

class WindowManager:
    """Encapsulates some calls to the winapi for window management"""

    def __init__ (self):
        """Constructor"""
        self._handle = None

    def get_windows(self):
        """Retrieve a list of all open windows."""
        windows = []
        win32gui.EnumWindows(self._enum_windows_callback, windows)
        return windows

    def _enum_windows_callback(self, hwnd, windows):
        """Callback function for enumerating windows."""
        title = win32gui.GetWindowText(hwnd)
        if title:
            windows.append((hwnd, title))

    def set_foreground_window(self, window_name):
        """Set the specified window as the foreground window."""
        try:
            windows = self.get_windows()
            target_window = [(hwnd, title) for hwnd, title in windows if window_name in title]
            if target_window:
                win32gui.SetForegroundWindow(target_window[0][0])
            else:
                print("Window '{}' not found.".format(window_name))
        except pywintypes.error:
            print("Error: Failed to set foreground window.")

    def minimize_window(self, window_name):
        """Minimize the specified window."""
        try:
            self.set_foreground_window(window_name)
            win32gui.ShowWindow(window_name, win32gui.SW_MINIMIZE)
        except pywintypes.error:
            print("Error: Failed to minimize window.")

    def maximize_window(self, window_name):
        """Maximize the specified window."""
        try:
            self.set_foreground_window(window_name)
            win32gui.ShowWindow(window_name, win32gui.SW_MAXIMIZE)
        except pywintypes.error:
            print("Error: Failed to maximize window.")

    def restore_window(self, window_name):
        """Restore the specified window."""
        try:
            self.set_foreground_window(window_name)
            win32gui.ShowWindow(window_name, win32gui.SW_RESTORE)
        except pywintypes.error:
            print("Error: Failed to restore window.")

    def close_window(self, window_name):
        """Close the specified window."""
        try:
            self.set_foreground_window(window_name)
            win32gui.PostMessage(window_name, win32con.WM_CLOSE, 0, 0)
        except pywintypes.error:
            print("Error: Failed to close window.")

    def move_window(self, window_name, x, y):
        """Move the specified window to the specified position."""
        try:
            self.set_foreground_window(window_name)
            win32gui.MoveWindow(window_name, x, y, -1, -1, True)
        except pywintypes.error:
            print("Error: Failed to move window.")

    def resize_window(self, window_name, width, height):
        """Resize the specified window to the specified dimensions."""
        try:
            self.set_foreground_window(window_name)
            win32gui.MoveWindow(window_name, -1, -1, width, height, True)
        except pywintypes.error:
            print("Error: Failed to resize window.")

    def get_window_rect(self, window_name):
        """Get the bounding rectangle of the specified window."""
        try:
            windows = self.get_windows()
            target_window = [(hwnd, title) for hwnd, title in windows if window_name in title]
            if target_window:
                rect = win32gui.GetWindowRect(target_window[0][0])
                return rect
            else:
                print("Window '{}' not found.".format(window_name))
                return None
        except pywintypes.error:
            print("Error: Failed to get window rectangle.")
            return None

    def get_window_text(self, window_name):
        """Get the text content of the specified window."""
        try:
            self.set_foreground_window(window_name)
            text = win32gui.GetWindowText(window_name)
            return text
        except pywintypes.error:
            print("Error: Failed to get window text.")
            return None

    def get_window_class_name(self, window_name):
        """Get the class name of the specified window."""
        try:
            self.set_foreground_window(window_name)
            class_name = win32gui.GetClassName(window_name)
            return class_name
        except pywintypes.error:
            print("Error: Failed to get window class name.")
            return None

    def get_window_info(self, window_name):
        """Retrieve detailed information about the specified window."""
        try:
            windows = self.get_windows()
            target_window = [(hwnd, title) for hwnd, title in windows if window_name in title]
            if target_window:
                hwnd = target_window[0][0]
                rect = win32gui.GetWindowRect(hwnd)
                class_name = win32gui.GetClassName(hwnd)
                text = win32gui.GetWindowText(hwnd)
                thread_id, process_id = win32gui.GetWindowThreadProcessId(hwnd)
                style = win32gui.GetWindowLong(hwnd, win32con.GWL_STYLE)
                ex_style = win32gui.GetWindowLong(hwnd, win32con.GWL_EXSTYLE)
                return {
                    "hwnd": hwnd,
                    "title": title,
                    "class_name": class_name,
                    "text": text,
                    "rect": rect,
                    "thread_id": thread_id,
                    "process_id": process_id,
                    "style": style,
                    "ex_style": ex_style
                }
            else:
                print("Window '{}' not found.".format(window_name))
                return None
        except pywintypes.error:
            print("Error: Failed to retrieve window info.")
            return None

    def set_window_style(self, window_name, style_flags):
        """Set the window style flags for the specified window."""
        try:
            windows = self.get_windows()
            target_window = [(hwnd, title) for hwnd, title in windows if window_name in title]
            if target_window:
                hwnd = target_window[0][0]
                win32gui.SetWindowLong(hwnd, win32con.GWL_STYLE, style_flags)
            else:
                print("Window '{}' not found.".format(window_name))
        except pywintypes.error:
            print("Error: Failed to set window style.")

    def set_window_ex_style(self, window_name, ex_style_flags):
        """Set the extended window style flags for the specified window."""
        try:
            windows = self.get_windows()
            target_window = [(hwnd, title) for hwnd, title in windows if window_name in title]
            if target_window:
                hwnd = target_window[0][0]
                win32gui.SetWindowLong(hwnd, win32con.GWL_EXSTYLE, ex_style_flags)
            else:
                print("Window '{}' not found.".format(window_name))
        except pywintypes.error:
            print("Error: Failed to set window extended style.")

    def get_window_process_path(self, window_name):
        """Get the process path of the application associated with the specified window."""
        try:
            windows = self.get_windows()
            target_window = [(hwnd, title) for hwnd, title in windows if window_name in title]
            if target_window:
                hwnd = target_window[0][0]
                _, process_id = win32gui.GetWindowThreadProcessId(hwnd)
                process_handle = win32api.OpenProcess(win32con.PROCESS_QUERY_INFORMATION | win32con.PROCESS_VM_READ, False, process_id)
                path = win32process.GetModuleFileNameEx(process_handle, 0)
                win32api.CloseHandle(process_handle)
                return path
            else:
                print("Window '{}' not found.".format(window_name))
                return None
        except pywintypes.error:
            print("Error: Failed to retrieve process path.")
            return None


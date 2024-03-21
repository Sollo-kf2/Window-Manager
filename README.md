# Window Manager Class

The `WindowManager` class is an open-source Python utility for managing and manipulating windows in the Windows operating system. It provides a wide range of useful functions for interacting with windows, such as retrieving window information, setting window styles, and getting process paths associated with windows. This README provides comprehensive documentation on how to use the `WindowManager` class effectively.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
  - [Getting Started](#getting-started)
  - [Retrieving Window Information](#retrieving-window-information)
  - [Setting Window Styles](#setting-window-styles)
  - [Getting Process Paths](#getting-process-paths)
- [Contributing](#contributing)
- [License](#license)

## Introduction

The `WindowManager` class is designed to simplify window management tasks in Windows environments. It offers an intuitive interface for performing various operations on windows, such as minimizing, maximizing, moving, resizing, and querying window properties.

## Installation

To use the `WindowManager` class, follow these steps:

1. Clone the repository to your local machine:

```bash
git clone https://github.com/Sollo-kf2/window-manager.git
```

2. Install the required dependencies:

```bash
pip install pywin32
```

3. Import the `WindowManager` class into your Python scripts:

```python
from window_manager import WindowManager
```

## Usage

### Getting Started

To begin using the `WindowManager` class, create an instance of the class:

```python
window_manager = WindowManager()
```

### Retrieving Window Information

You can retrieve detailed information about a specific window using the `get_window_info` method:

```python
window_info = window_manager.get_window_info("Window Name")
print(window_info)
```

### Setting Window Styles

Modify the window styles or extended window styles using the `set_window_style` and `set_window_ex_style` methods:

```python
# Set window style flags
window_manager.set_window_style("Window Name", style_flags)

# Set extended window style flags
window_manager.set_window_ex_style("Window Name", ex_style_flags)
```

### Getting Process Paths

Retrieve the process path associated with a window using the `get_window_process_path` method:

```python
process_path = window_manager.get_window_process_path("Window Name")
print(process_path)
```

### Additional Usage Examples

#### Minimize Window

```python
window_manager.minimize_window("Window Name")
```

#### Maximize Window

```python
window_manager.maximize_window("Window Name")
```

#### Move Window

```python
window_manager.move_window("Window Name", x, y)
```

#### Resize Window

```python
window_manager.resize_window("Window Name", width, height)
```

#### Get Window Position

```python
window_position = window_manager.get_window_position("Window Name")
print(window_position)
```

#### Close Window

```python
window_manager.close_window("Window Name")
```

#### Get All Windows

```python
all_windows = window_manager.get_windows()
print(all_windows)
```

#### Bring Window to Front

```python
window_manager.bring_window_to_front("Window Name")
```

#### Send Window to Back

```python
window_manager.send_window_to_back("Window Name")
```

## Contributing

Contributions to the `WindowManager` project are welcome! If you have any ideas for improvements or new features, feel free to open an issue or submit a pull request. For major changes, please open an issue first to discuss your ideas.

## License

The `WindowManager` class is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

Thank you for using the `WindowManager` class! If you encounter any issues or have any questions, don't hesitate to reach out to us. Happy window managing! 🪟✨

# 🌐 I-Mon — Internet Monitor & Speed Test

I-Mon is a lightweight desktop application built with **Python and Tkinter** that allows you to test internet speed and monitor network information in real time through a clean, dark-themed interface.

The application displays **download speed, upload speed, ping, server location, ISP details, public IP address**, and **local Wi-Fi IP address (wlan0)**.

---

## ✨ Features

- ⚡ Internet speed test
  - Download speed (Mbps)
  - Upload speed (Mbps)
  - Ping (ms)
- 🌍 Network details
  - Speedtest server location
  - Internet Service Provider (ISP)
- 🌐 Public IP address
- 📶 Local Wi-Fi IP address (example: `192.168.110.1`)
- 🧵 Non-blocking UI using threading
- 🎨 Modern dark-themed interface
- ⌨ Press **Enter** to start the speed test

---

## 📦 Requirements

- Python 3.8 or newer

Install dependencies with:

```bash
pip install speedtest-cli psutil
```

# 🚀 How to Run

1. Download or clone the project.

2. Open a terminal in the project directory.

3. Run the application:
```bash
   > python app.py
```

or, if your system uses python3:
```bash
   > python3 app.py
```

The application window will open.

Click the Start Speed Test button or press Enter to begin testing.

Results will show download/upload speed, ping, server info, ISP, public IP, and local Wi-Fi IP.
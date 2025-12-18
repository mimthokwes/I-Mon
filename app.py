import tkinter as tk
from tkinter import ttk
import speedtest
import threading
import psutil
import socket

def get_wlan_ip(interface="wlan0"):
    try:
        addrs = psutil.net_if_addrs()
        if interface not in addrs:
            return "Interface Not Found"
        
        for addr in addrs[interface]:
            if addr.family == socket.AF_INET:
                return addr.address
        
        return "No IPv4"
    except Exception as e:
        return "Unknown"

wlan_ip = get_wlan_ip("wlan0")

def run_speedtest():
    status_label.config(text="Testing...")
    button.config(state="disabled")

    try:
        st = speedtest.Speedtest()
        server = st.get_best_server()

        download = st.download() / 1_000_000
        upload = st.upload() / 1_000_000
        ping = st.results.ping

        isp = st.config["client"]["isp"]
        ip = st.config["client"]["ip"]
        location = f"{server['name']}, {server['country']}"
        wlan_ip = get_wlan_ip("wlan0")

        result_label.config(
            text=(
                f"⬇ Download : {download:.2f} Mbps\n"
                f"⬆ Upload   : {upload:.2f} Mbps\n"
                f"📡 Ping     : {ping:.2f} ms\n\n"
                f"🌍 Server   : {location}\n"
                f"🏢 ISP      : {isp}\n"
                f"🌐 IP       : {ip}\n"
                f"📶 WLAN IP  : {wlan_ip}"
            )
        )

        status_label.config(text="Done")
    except Exception as e:
        result_label.config(text=f"Error:\n{e}")
        status_label.config(text="Failed")

    button.config(state="normal")


def start_test():
    threading.Thread(target=run_speedtest, daemon=True).start()

def on_enter(event):
    start_test()

# ================= WINDOW =================
root = tk.Tk()
root.title("Internet Speed Test")
root.geometry("400x400")
root.resizable(False, False)
root.configure(bg="#121212")

# ================= STYLE =================
style = ttk.Style()
style.theme_use("clam")

style.configure(
    "TButton",
    font=("Segoe UI", 11, "bold"),
    padding=10,
    background="#1f6feb",
    foreground="white"
)
style.map("TButton", background=[("active", "#388bfd")])

style.configure(
    "Title.TLabel",
    background="#121212",
    foreground="white",
    font=("Segoe UI", 20, "bold")
)

style.configure(
    "Status.TLabel",
    background="#121212",
    foreground="#aaaaaa",
    font=("Segoe UI", 10)
)

style.configure(
    "Result.TLabel",
    background="#121212",
    foreground="white",
    font=("Segoe UI", 13)
)

# ================= UI =================
ttk.Label(
    root,
    text="Internet Speed Test",
    style="Title.TLabel"
).pack(pady=20)

button = ttk.Button(
    root,
    text="Start Speed Test",
    command=start_test
)
button.pack(pady=10)

status_label = ttk.Label(
    root,
    text="Idle",
    style="Status.TLabel"
)
status_label.pack(pady=5)

result_label = ttk.Label(
    root,
    text=(
        "⬇ Download : - Mbps\n"
        "⬆ Upload   : - Mbps\n"
        "📡 Ping     : - ms\n\n"
        "🌍 Server   : -\n"
        "🏢 ISP      : -\n"
        "🌐 IP       : -\n"
        "📶 WLAN IP  : -"
    ),
    style="Result.TLabel",
    justify="left"
)
result_label.pack(pady=25)

root.bind("<Return>", on_enter)



root.mainloop()

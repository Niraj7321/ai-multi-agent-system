"""
Stop Blogger Background Service
"""
import subprocess
import sys
from pathlib import Path

def main():
    print("="*80)
    print("🛑 STOPPING BLOGGER BACKGROUND SERVICE")
    print("="*80)

    pid_file = Path("blogger_service.pid")

    if not pid_file.exists():
        print("\n❌ No running service found (PID file not found)")
        return

    with open(pid_file, 'r') as f:
        pid = f.read().strip()

    print(f"\n📌 Found service with PID: {pid}")
    print("   Stopping...")

    if sys.platform == 'win32':
        result = subprocess.run(['taskkill', '/PID', pid, '/F'], capture_output=True)
        if result.returncode == 0:
            print(f"✅ Service stopped successfully")
            pid_file.unlink()
        else:
            print(f"❌ Failed to stop service")
            print(f"   Try manually: taskkill /PID {pid} /F")
    else:
        result = subprocess.run(['kill', pid], capture_output=True)
        if result.returncode == 0:
            print(f"✅ Service stopped successfully")
            pid_file.unlink()
        else:
            print(f"❌ Failed to stop service")

    print("="*80)

if __name__ == "__main__":
    main()

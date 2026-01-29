"""
Restart Blogger Background Service
Quick script to restart the automated blog publishing service
"""
import subprocess
import sys
import io
import time
from pathlib import Path

# Fix Windows console encoding issues
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8', errors='replace')

def main():
    print("="*80)
    print("🔄 RESTARTING BLOGGER BACKGROUND SERVICE")
    print("="*80)

    # Check if service is running
    pid_file = Path("blogger_service.pid")
    if pid_file.exists():
        print("\n📌 Found running service, stopping it...")
        with open(pid_file, 'r') as f:
            pid = f.read().strip()

        # Kill the process
        if sys.platform == 'win32':
            subprocess.run(['taskkill', '/PID', pid, '/F'], capture_output=True)
        else:
            subprocess.run(['kill', pid], capture_output=True)

        pid_file.unlink()
        print("✅ Service stopped")
        time.sleep(2)

    # Start the service
    print("\n🚀 Starting background service...")

    if sys.platform == 'win32':
        # Windows: Run in background
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0  # SW_HIDE

        process = subprocess.Popen(
            [sys.executable, 'trending_blogger_background.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS
        )
    else:
        # Linux/Mac: Run in background
        process = subprocess.Popen(
            [sys.executable, 'trending_blogger_background.py'],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )

    # Save PID
    with open(pid_file, 'w') as f:
        f.write(str(process.pid))

    print(f"✅ Service started successfully!")
    print(f"   Process ID: {process.pid}")
    print(f"   Logs: logs/background_service.log")
    print(f"\n📊 The service will:")
    print(f"   • Run daily at 09:00")
    print(f"   • Publish 5 trending blog posts")
    print(f"   • Find topics from GitHub, Reddit, Hacker News")
    print(f"\n📝 To stop: python stop_blogger_service.py")
    print(f"   Or: taskkill /PID {process.pid} /F")
    print("="*80)

if __name__ == "__main__":
    main()

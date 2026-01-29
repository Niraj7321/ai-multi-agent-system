"""
Background Service Runner for Automated Blog Publishing
Runs trending blogger as a Windows background service
"""
import sys
import os
import subprocess
import time
from pathlib import Path

def run_as_background_service():
    """
    Run the trending blogger as a background service
    """
    script_dir = Path(__file__).parent

    # Get python executable path
    python_exe = sys.executable

    # Script to run
    trending_script = script_dir / "trending_blogger.py"

    print("="*80)
    print("🚀 BACKGROUND SERVICE LAUNCHER")
    print("="*80)
    print(f"Python: {python_exe}")
    print(f"Script: {trending_script}")
    print(f"Working Directory: {script_dir}")
    print("="*80)

    # Check if script exists
    if not trending_script.exists():
        print(f"❌ Error: Script not found at {trending_script}")
        return

    # Create startup info to hide window
    if sys.platform == 'win32':
        startupinfo = subprocess.STARTUPINFO()
        startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
        startupinfo.wShowWindow = 0  # SW_HIDE

        # Run the script in the background
        process = subprocess.Popen(
            [python_exe, str(trending_script)],
            cwd=str(script_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE,
            startupinfo=startupinfo,
            creationflags=subprocess.CREATE_NO_WINDOW | subprocess.DETACHED_PROCESS
        )

        print(f"✅ Background service started!")
        print(f"   Process ID: {process.pid}")
        print(f"   Logs: logs/app.log")
        print(f"\n📝 To stop the service, kill process ID: {process.pid}")
        print(f"   Command: taskkill /PID {process.pid} /F")

        # Save PID to file
        pid_file = script_dir / "blogger_service.pid"
        with open(pid_file, 'w') as f:
            f.write(str(process.pid))

        print(f"\n💾 PID saved to: {pid_file}")

    else:
        # For Linux/Mac
        process = subprocess.Popen(
            [python_exe, str(trending_script)],
            cwd=str(script_dir),
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            stdin=subprocess.PIPE
        )

        print(f"✅ Background service started!")
        print(f"   Process ID: {process.pid}")
        print(f"\n📝 To stop the service: kill {process.pid}")

def stop_background_service():
    """
    Stop the background service
    """
    script_dir = Path(__file__).parent
    pid_file = script_dir / "blogger_service.pid"

    if not pid_file.exists():
        print("❌ No running service found (PID file not found)")
        return

    with open(pid_file, 'r') as f:
        pid = f.read().strip()

    if sys.platform == 'win32':
        result = subprocess.run(['taskkill', '/PID', pid, '/F'], capture_output=True)
        if result.returncode == 0:
            print(f"✅ Service stopped (PID: {pid})")
            pid_file.unlink()
        else:
            print(f"❌ Failed to stop service (PID: {pid})")
            print(f"   Try manually: taskkill /PID {pid} /F")
    else:
        result = subprocess.run(['kill', pid], capture_output=True)
        if result.returncode == 0:
            print(f"✅ Service stopped (PID: {pid})")
            pid_file.unlink()
        else:
            print(f"❌ Failed to stop service (PID: {pid})")

def check_service_status():
    """
    Check if service is running
    """
    script_dir = Path(__file__).parent
    pid_file = script_dir / "blogger_service.pid"

    if not pid_file.exists():
        print("❌ Service is not running")
        return

    with open(pid_file, 'r') as f:
        pid = f.read().strip()

    if sys.platform == 'win32':
        result = subprocess.run(['tasklist', '/FI', f'PID eq {pid}'], capture_output=True, text=True)
        if pid in result.stdout:
            print(f"✅ Service is running (PID: {pid})")
            print(f"   Check logs: logs/app.log")
        else:
            print(f"❌ Service is not running (stale PID file)")
            pid_file.unlink()
    else:
        result = subprocess.run(['ps', '-p', pid], capture_output=True)
        if result.returncode == 0:
            print(f"✅ Service is running (PID: {pid})")
        else:
            print(f"❌ Service is not running (stale PID file)")
            pid_file.unlink()

def main():
    """
    Main menu
    """
    print("\n" + "="*80)
    print("🤖 AUTOMATED BLOGGER - BACKGROUND SERVICE MANAGER")
    print("="*80)
    print("\nOptions:")
    print("  1. Start background service")
    print("  2. Stop background service")
    print("  3. Check service status")
    print("  4. Exit")
    print("="*80)

    choice = input("\nEnter choice (1-4): ").strip()

    if choice == "1":
        print("\n🚀 Starting background service...")
        run_as_background_service()
    elif choice == "2":
        print("\n🛑 Stopping background service...")
        stop_background_service()
    elif choice == "3":
        print("\n🔍 Checking service status...")
        check_service_status()
    elif choice == "4":
        print("\n👋 Goodbye!")
    else:
        print("\n❌ Invalid choice")

if __name__ == "__main__":
    main()

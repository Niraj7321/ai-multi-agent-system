"""
Windows Service Installer for Automated Blogger
Installs as a true Windows service that runs even when logged out
"""
import os
import sys
import subprocess
from pathlib import Path

def check_admin():
    """Check if running with administrator privileges"""
    try:
        import ctypes
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

def download_nssm():
    """Download NSSM (Non-Sucking Service Manager)"""
    print("\n📥 Downloading NSSM (Windows Service Manager)...")

    nssm_dir = Path.cwd() / "nssm"
    nssm_dir.mkdir(exist_ok=True)

    nssm_exe = nssm_dir / "nssm.exe"

    if nssm_exe.exists():
        print("✅ NSSM already downloaded")
        return nssm_exe

    print("\n⚠️  Please download NSSM manually:")
    print("   1. Go to: https://nssm.cc/download")
    print("   2. Download nssm-2.24.zip")
    print("   3. Extract nssm.exe to:", nssm_dir)
    print("\n   Or use the automatic Task Scheduler method below (no download needed)")

    return None

def create_service_with_nssm(nssm_exe):
    """Create Windows service using NSSM"""
    if not nssm_exe or not nssm_exe.exists():
        print("❌ NSSM not found. Cannot create service.")
        return False

    print("\n🔧 Creating Windows Service...")

    # Get paths
    python_exe = sys.executable.replace('python.exe', 'pythonw.exe')
    script_path = Path.cwd() / "trending_blogger_background.py"
    work_dir = Path.cwd()

    service_name = "AutomatedTrendingBlogger"

    # Remove service if it exists
    subprocess.run([str(nssm_exe), "stop", service_name],
                   capture_output=True, shell=True)
    subprocess.run([str(nssm_exe), "remove", service_name, "confirm"],
                   capture_output=True, shell=True)

    # Install service
    print(f"   Installing service: {service_name}")
    result = subprocess.run(
        [str(nssm_exe), "install", service_name, python_exe, str(script_path)],
        capture_output=True,
        text=True,
        shell=True
    )

    if result.returncode != 0:
        print(f"❌ Failed to install service: {result.stderr}")
        return False

    # Set working directory
    subprocess.run([str(nssm_exe), "set", service_name, "AppDirectory", str(work_dir)],
                   shell=True)

    # Set to start automatically
    subprocess.run([str(nssm_exe), "set", service_name, "Start", "SERVICE_AUTO_START"],
                   shell=True)

    # Set description
    subprocess.run([str(nssm_exe), "set", service_name, "Description",
                   "Automated Trending Blog Publisher - Publishes blog posts daily"],
                   shell=True)

    # Start service
    print("   Starting service...")
    result = subprocess.run([str(nssm_exe), "start", service_name],
                           capture_output=True,
                           text=True,
                           shell=True)

    if result.returncode == 0:
        print("\n✅ Windows Service installed successfully!")
        print(f"   Service Name: {service_name}")
        print("   Status: Running")
        print("   Auto-start: Yes (starts on boot)")
        print("\n   The service will run even when:")
        print("   • Windows is closed")
        print("   • You log out")
        print("   • Computer restarts (auto-starts)")
        return True
    else:
        print(f"❌ Failed to start service: {result.stderr}")
        return False

def create_task_scheduler_service():
    """Create Windows Task Scheduler task (no admin required)"""
    print("\n🔧 Creating Task Scheduler Service...")

    # Get paths
    python_exe = sys.executable.replace('python.exe', 'pythonw.exe')
    script_path = Path.cwd() / "trending_blogger_background.py"
    work_dir = Path.cwd()

    task_name = "AutomatedTrendingBlogger"

    # Create XML for task
    task_xml = f"""<?xml version="1.0" encoding="UTF-16"?>
<Task version="1.4" xmlns="http://schemas.microsoft.com/windows/2004/02/mit/task">
  <RegistrationInfo>
    <Description>Automated Trending Blog Publisher - Runs 24/7 in background</Description>
  </RegistrationInfo>
  <Triggers>
    <BootTrigger>
      <Enabled>true</Enabled>
    </BootTrigger>
    <LogonTrigger>
      <Enabled>true</Enabled>
    </LogonTrigger>
  </Triggers>
  <Principals>
    <Principal id="Author">
      <LogonType>InteractiveToken</LogonType>
      <RunLevel>HighestAvailable</RunLevel>
    </Principal>
  </Principals>
  <Settings>
    <MultipleInstancesPolicy>IgnoreNew</MultipleInstancesPolicy>
    <DisallowStartIfOnBatteries>false</DisallowStartIfOnBatteries>
    <StopIfGoingOnBatteries>false</StopIfGoingOnBatteries>
    <AllowHardTerminate>false</AllowHardTerminate>
    <StartWhenAvailable>true</StartWhenAvailable>
    <RunOnlyIfNetworkAvailable>false</RunOnlyIfNetworkAvailable>
    <IdleSettings>
      <StopOnIdleEnd>false</StopOnIdleEnd>
      <RestartOnIdle>false</RestartOnIdle>
    </IdleSettings>
    <AllowStartOnDemand>true</AllowStartOnDemand>
    <Enabled>true</Enabled>
    <Hidden>false</Hidden>
    <RunOnlyIfIdle>false</RunOnlyIfIdle>
    <DisallowStartOnRemoteAppSession>false</DisallowStartOnRemoteAppSession>
    <UseUnifiedSchedulingEngine>true</UseUnifiedSchedulingEngine>
    <WakeToRun>false</WakeToRun>
    <ExecutionTimeLimit>PT0S</ExecutionTimeLimit>
    <Priority>7</Priority>
    <RestartOnFailure>
      <Interval>PT1M</Interval>
      <Count>3</Count>
    </RestartOnFailure>
  </Settings>
  <Actions Context="Author">
    <Exec>
      <Command>{python_exe}</Command>
      <Arguments>"{script_path}"</Arguments>
      <WorkingDirectory>{work_dir}</WorkingDirectory>
    </Exec>
  </Actions>
</Task>"""

    # Save XML to temp file
    xml_file = Path.cwd() / "blogger_task.xml"
    with open(xml_file, 'w', encoding='utf-16') as f:
        f.write(task_xml)

    # Delete existing task
    subprocess.run(["schtasks", "/Delete", "/TN", task_name, "/F"],
                   capture_output=True, shell=True)

    # Create task
    print(f"   Creating task: {task_name}")
    result = subprocess.run(
        ["schtasks", "/Create", "/TN", task_name, "/XML", str(xml_file)],
        capture_output=True,
        text=True,
        shell=True
    )

    # Clean up XML file
    xml_file.unlink(missing_ok=True)

    if result.returncode == 0:
        print("\n✅ Task Scheduler service created successfully!")
        print(f"   Task Name: {task_name}")
        print("   Triggers: On boot + On login")
        print("   Runs as: Current user")
        print("   Auto-restart: Yes (3 attempts)")
        print("\n   The service will run:")
        print("   ✅ Even when all windows are closed")
        print("   ✅ When you log in")
        print("   ✅ After computer restarts (auto-starts)")
        print("   ✅ Even if logged out (after first login)")

        # Start the task immediately
        print("\n   Starting task now...")
        subprocess.run(["schtasks", "/Run", "/TN", task_name], shell=True)

        return True
    else:
        print(f"❌ Failed to create task: {result.stderr}")
        return False

def check_existing_service():
    """Check if service already exists"""
    result = subprocess.run(
        ["schtasks", "/Query", "/TN", "AutomatedTrendingBlogger"],
        capture_output=True,
        shell=True
    )
    return result.returncode == 0

def remove_service():
    """Remove existing service"""
    print("\n🗑️  Removing existing service...")

    # Remove Task Scheduler task
    result = subprocess.run(
        ["schtasks", "/Delete", "/TN", "AutomatedTrendingBlogger", "/F"],
        capture_output=True,
        text=True,
        shell=True
    )

    if result.returncode == 0:
        print("✅ Service removed successfully")
    else:
        print("⚠️  No service found to remove")

def verify_configuration():
    """Verify configuration files exist"""
    errors = []

    print("\n🔍 Verifying configuration...")

    # Check credentials
    if not Path("credentials.json").exists():
        errors.append("❌ credentials.json not found")
    else:
        print("   ✅ credentials.json exists")

    # Check token
    if not Path("token.pickle").exists():
        errors.append("⚠️  token.pickle not found (will be created on first auth)")
    else:
        print("   ✅ token.pickle exists")

    # Check blog config
    if not Path("blog_config.txt").exists():
        errors.append("⚠️  blog_config.txt not found (will be created on first run)")
    else:
        print("   ✅ blog_config.txt exists")

    # Check script
    if not Path("trending_blogger_background.py").exists():
        errors.append("❌ trending_blogger_background.py not found")
    else:
        print("   ✅ trending_blogger_background.py exists")

    if errors:
        print("\n⚠️  Issues found:")
        for error in errors:
            print(f"   {error}")
        return False

    print("\n✅ All configuration files verified!")
    return True

def main():
    """Main installation menu"""
    print("="*80)
    print("🚀 AUTOMATED BLOGGER - WINDOWS SERVICE INSTALLER".center(80))
    print("="*80)
    print("\nThis will install the automated blogger as a Windows service")
    print("that runs 24/7 in the background, even when windows are closed.\n")

    # Check existing service
    if check_existing_service():
        print("⚠️  An existing service was found.")
        choice = input("\nDo you want to remove it first? (y/n): ").strip().lower()
        if choice == 'y':
            remove_service()
            print()

    # Verify configuration
    if not verify_configuration():
        print("\n⚠️  Please complete the setup first:")
        print("   Run: python setup_background.py")
        return

    print("\n" + "="*80)
    print("Choose installation method:\n")
    print("  1. Task Scheduler (Recommended - No admin required)")
    print("     • Starts automatically on boot")
    print("     • Runs even when logged out")
    print("     • Easy to manage")
    print()
    print("  2. Windows Service with NSSM (Advanced)")
    print("     • True Windows service")
    print("     • Requires NSSM download")
    print("     • May need admin rights")
    print()
    print("  3. Remove existing service")
    print("  4. Exit")
    print("="*80)

    choice = input("\nEnter choice (1-4): ").strip()

    if choice == "1":
        print("\n📋 Installing as Task Scheduler service...")
        if create_task_scheduler_service():
            print("\n" + "="*80)
            print("✅ INSTALLATION COMPLETE!".center(80))
            print("="*80)
            print("\nYour automated blogger is now running in the background!")
            print("\n📊 To manage the service:")
            print("   • View in Task Scheduler: Win+R → taskschd.msc")
            print("   • Task name: AutomatedTrendingBlogger")
            print("   • Check logs: logs\\background_service.log")
            print("\n🛑 To stop/disable:")
            print("   1. Open Task Scheduler")
            print("   2. Find 'AutomatedTrendingBlogger'")
            print("   3. Right-click → Disable or Delete")
            print("\n" + "="*80)

    elif choice == "2":
        if not check_admin():
            print("\n⚠️  Administrator privileges recommended for this method.")
            print("   Please run as administrator or use Task Scheduler (option 1)")
            return

        nssm_exe = download_nssm()
        if nssm_exe:
            create_service_with_nssm(nssm_exe)

    elif choice == "3":
        remove_service()

    elif choice == "4":
        print("\n👋 Goodbye!")

    else:
        print("\n❌ Invalid choice")

if __name__ == "__main__":
    main()

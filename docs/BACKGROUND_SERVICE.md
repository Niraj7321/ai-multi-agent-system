# 🔄 Running Automated Blogger in Background

Complete guide to run your automated blog publisher in the background on Windows, so it keeps running even after you close the terminal.

## 📋 Quick Start

### Option 1: Simple Double-Click (Easiest)

1. **Double-click**: `start_background_trending.bat`
2. **Done!** The service starts in background
3. **Check logs**: `logs/background_service.log`

To stop:
- **Double-click**: `stop_background.bat`

---

### Option 2: Python Service Manager

```bash
python run_background.py
# Choose option 1: Start background service
```

---

### Option 3: Windows Task Scheduler (Most Reliable)

See "Method 3" below for full setup.

---

## 🎯 Three Methods Explained

## Method 1: Batch File Launcher (Simplest)

### Start the Service

**Double-click** `start_background_trending.bat` or run:

```bash
start_background_trending.bat
```

**What happens:**
- Service starts in background
- No console window stays open
- Runs until system reboot or manual stop
- Logs to `logs/background_service.log`

### Stop the Service

**Double-click** `stop_background.bat` or run:

```bash
stop_background.bat
```

### Configuration

Edit `blog_config.txt` (auto-created on first run):
```
YOUR_BLOG_ID_HERE
```

Set environment variables (optional):
```bash
set BLOGGER_SCHEDULE_TIME=09:00
set BLOGGER_NUM_POSTS=5
set BLOGGER_BLOG_ID=your_blog_id
```

---

## Method 2: Python Service Manager (Interactive)

### Start Service

```bash
python run_background.py
# Choose option 1: Start background service
```

### Stop Service

```bash
python run_background.py
# Choose option 2: Stop background service
```

### Check Status

```bash
python run_background.py
# Choose option 3: Check service status
```

### Features
- ✅ Interactive menu
- ✅ PID tracking (stores in `blogger_service.pid`)
- ✅ Status checking
- ✅ Clean shutdown

---

## Method 3: Windows Task Scheduler (Production)

This is the **most reliable** method for long-term background operation.

### Step-by-Step Setup

#### 1. Open Task Scheduler

- Press `Win + R`
- Type: `taskschd.msc`
- Press Enter

#### 2. Create New Task

- Click **"Create Basic Task"**
- Name: `Automated Trending Blogger`
- Description: `Publishes 5 trending blog posts daily`
- Click **Next**

#### 3. Set Trigger

- Select: **Daily**
- Click **Next**
- Start date: Today
- Start time: **09:00:00** (or your preferred time)
- Recur every: **1 days**
- Click **Next**

#### 4. Set Action

- Select: **Start a program**
- Click **Next**

- **Program/script**: `pythonw.exe`

- **Add arguments**:
  ```
  "C:\Users\Niraj\ai-multi-agent-system\trending_blogger_background.py"
  ```

- **Start in**:
  ```
  C:\Users\Niraj\ai-multi-agent-system
  ```

- Click **Next**

#### 5. Configure Advanced Settings

- Click **Finish**
- Right-click your new task → **Properties**

**General Tab:**
- ✅ Check: **Run whether user is logged on or not**
- ✅ Check: **Run with highest privileges**
- ✅ Check: **Hidden** (optional, hides from task list)

**Conditions Tab:**
- ⬜ Uncheck: **Start the task only if the computer is on AC power**
- ✅ Check: **Wake the computer to run this task** (optional)

**Settings Tab:**
- ✅ Check: **Allow task to be run on demand**
- ✅ Check: **Run task as soon as possible after a scheduled start is missed**
- ✅ Check: **If the task fails, restart every**: **15 minutes**
- ✅ Set **Attempt to restart up to**: **3 times**

#### 6. Test the Task

- Right-click your task
- Click **Run**
- Check logs: `logs/background_service.log`

#### 7. Verify

- Wait 1 minute
- Check: `logs/background_service.log`
- You should see service start messages

---

## 📊 Monitoring the Service

### Check Logs

#### Background Service Log
```bash
type logs\background_service.log
```

Or use Notepad:
```bash
notepad logs\background_service.log
```

#### Application Log
```bash
type logs\app.log
```

### Real-Time Log Monitoring

**PowerShell:**
```powershell
Get-Content logs\background_service.log -Wait -Tail 20
```

**CMD:**
```bash
powershell -command "Get-Content logs\background_service.log -Wait -Tail 20"
```

### What to Look For

**Healthy service:**
```
2026-01-21 09:00:00 - INFO - Starting scheduled trending topics batch
2026-01-21 09:02:15 - INFO - Published trending post #1: Complete Guide to...
2026-01-21 09:04:30 - INFO - Published trending post #2: Getting Started with...
```

**Problems:**
```
2026-01-21 09:00:00 - ERROR - Failed to get blog ID: ...
2026-01-21 09:00:00 - ERROR - Authentication failed: ...
```

---

## ⚙️ Configuration

### Configuration File: `blog_config.txt`

Created automatically on first run:
```
YOUR_BLOG_ID_HERE
```

**To set manually:**
```bash
echo YOUR_BLOG_ID > blog_config.txt
```

### Environment Variables

Set these for custom configuration:

```bash
# Windows CMD
set BLOGGER_BLOG_ID=your_blog_id
set BLOGGER_SCHEDULE_TIME=09:00
set BLOGGER_NUM_POSTS=5

# Windows PowerShell
$env:BLOGGER_BLOG_ID = "your_blog_id"
$env:BLOGGER_SCHEDULE_TIME = "09:00"
$env:BLOGGER_NUM_POSTS = "5"
```

**Make permanent** (Windows):
1. Search: "Environment Variables"
2. Click "Edit the system environment variables"
3. Click "Environment Variables"
4. Under "User variables", click "New"
5. Add your variables

---

## 🔧 Troubleshooting

### Service Not Starting

**Check 1: Python Path**
```bash
where python
where pythonw
```

Both should return valid paths.

**Check 2: Dependencies**
```bash
pip install -r requirements.txt
```

**Check 3: Authentication**
```bash
# Delete token and re-authenticate
del token.pickle
python trending_blogger.py
# Complete authentication
```

**Check 4: Logs**
```bash
type logs\background_service.log
```

---

### Service Starts But Doesn't Publish

**Check 1: Blog ID**
```bash
type blog_config.txt
```

Should contain valid blog ID.

**Check 2: Schedule Time**
```bash
# Check current time matches schedule
echo %TIME%
```

**Check 3: API Credentials**
```bash
# Verify credentials.json exists
dir credentials.json
```

---

### Service Crashes

**Check 1: Error Logs**
```bash
type logs\background_service.log
# Look for ERROR or CRITICAL messages
```

**Check 2: Disk Space**
```bash
# Ensure you have enough space for logs
dir
```

**Check 3: Restart Service**
```bash
# Stop
python run_background.py
# Option 2: Stop

# Start again
python run_background.py
# Option 1: Start
```

---

### Cannot Stop Service

**Method 1: Use stop script**
```bash
stop_background.bat
```

**Method 2: Find and kill process**
```bash
# Find PID
type blogger_service.pid

# Kill process
taskkill /PID YOUR_PID /F
```

**Method 3: Kill all Python processes** (nuclear option)
```bash
taskkill /IM pythonw.exe /F
```

---

## 📱 Remote Monitoring

### Set Up Email Notifications

Edit `trending_blogger_background.py` and add:

```python
import smtplib
from email.mime.text import MIMEText

def send_notification(subject, body):
    """Send email notification"""
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = 'your_email@gmail.com'
    msg['To'] = 'your_email@gmail.com'

    # Use Gmail SMTP
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
        smtp.login('your_email@gmail.com', 'your_app_password')
        smtp.send_message(msg)

# Call in run_scheduled_batch():
try:
    # ... publish posts ...
    send_notification("Blog Published", f"Successfully published {num_posts} posts")
except Exception as e:
    send_notification("Blog Error", f"Failed: {str(e)}")
```

### Monitor from Phone

**Option 1: Access logs via file sharing**
- Share `logs` folder on network
- Access from phone using file explorer

**Option 2: Upload logs to cloud**
```python
# Add to trending_blogger_background.py
import dropbox  # pip install dropbox

def upload_log_to_dropbox():
    dbx = dropbox.Dropbox('YOUR_ACCESS_TOKEN')
    with open('logs/background_service.log', 'rb') as f:
        dbx.files_upload(f.read(), '/blogger_log.txt', mode=WriteMode('overwrite'))
```

---

## 🎯 Best Practices

### 1. Regular Log Cleanup

Create `cleanup_logs.bat`:
```batch
@echo off
REM Keep only last 7 days of logs
forfiles /P "logs" /M *.log /D -7 /C "cmd /c del @path"
echo Old logs cleaned up!
```

Schedule this weekly in Task Scheduler.

### 2. Monitor Disk Space

```batch
@echo off
REM Check disk space
for /f "tokens=3" %%a in ('dir C:\ ^| find "bytes free"') do set FREE_SPACE=%%a
echo Free space: %FREE_SPACE%
```

### 3. Backup Configuration

```batch
@echo off
REM Backup important files
xcopy credentials.json backup\ /Y
xcopy blog_config.txt backup\ /Y
xcopy token.pickle backup\ /Y
echo Configuration backed up!
```

### 4. Health Check Script

Create `health_check.bat`:
```batch
@echo off
echo Checking service health...

REM Check if PID file exists
if exist blogger_service.pid (
    echo ✓ Service PID file exists
) else (
    echo ✗ Service PID file missing
)

REM Check recent log activity
powershell -command "Get-Content logs\background_service.log -Tail 5"

pause
```

---

## 🔄 Auto-Start on Boot

### Method A: Task Scheduler (Recommended)

In Task Scheduler:
1. Edit your task
2. Go to **Triggers** tab
3. Click **New**
4. Select: **At startup**
5. Click **OK**

### Method B: Startup Folder

1. Press `Win + R`
2. Type: `shell:startup`
3. Press Enter
4. Copy `start_background_trending.bat` to this folder

**Note:** This only works when you log in to Windows.

### Method C: Windows Service (Advanced)

Use NSSM (Non-Sucking Service Manager):

```bash
# Download NSSM from nssm.cc
# Extract to C:\nssm

# Install service
C:\nssm\nssm.exe install AutomatedBlogger "C:\Users\Niraj\AppData\Local\Programs\Python\Python313\pythonw.exe" "C:\Users\Niraj\ai-multi-agent-system\trending_blogger_background.py"

# Set working directory
C:\nssm\nssm.exe set AutomatedBlogger AppDirectory "C:\Users\Niraj\ai-multi-agent-system"

# Start service
net start AutomatedBlogger
```

---

## 📊 Performance Monitoring

### CPU and Memory Usage

```bash
# Check Python processes
tasklist /FI "IMAGENAME eq pythonw.exe" /V
```

### Network Usage

Monitor in Task Manager:
1. Open Task Manager (`Ctrl+Shift+Esc`)
2. Go to "Performance" tab
3. Click "Open Resource Monitor"
4. Go to "Network" tab
5. Find your Python process

---

## 🔐 Security Considerations

### 1. Protect Credentials

```bash
# Set file permissions to read-only
attrib +R credentials.json
attrib +R token.pickle
attrib +R blog_config.txt
```

### 2. Encrypt Sensitive Files

Use Windows EFS:
1. Right-click file
2. Properties → Advanced
3. Check "Encrypt contents to secure data"

### 3. Use Environment Variables

Instead of storing in files:
```bash
setx BLOGGER_BLOG_ID "your_blog_id"
setx ANTHROPIC_API_KEY "your_api_key"
```

---

## 📈 Scaling Up

### Run Multiple Services

**For multiple blogs:**

1. Copy config:
   ```bash
   copy trending_blogger_background.py blog1_service.py
   copy trending_blogger_background.py blog2_service.py
   ```

2. Edit each to use different blog IDs

3. Schedule both in Task Scheduler with different names

### High Volume Publishing

**For 20+ posts per day:**

1. Schedule multiple times:
   - 09:00 - 5 posts
   - 12:00 - 5 posts
   - 15:00 - 5 posts
   - 18:00 - 5 posts

2. Create separate Task Scheduler entries for each time

---

## 🆘 Emergency Commands

### Stop Everything

```bash
# Kill all Python processes
taskkill /IM python.exe /F
taskkill /IM pythonw.exe /F

# Clean up PID file
del blogger_service.pid
```

### Reset Service

```bash
# Stop service
stop_background.bat

# Delete logs
del logs\*.log

# Delete token (re-auth required)
del token.pickle

# Start fresh
start_background_trending.bat
```

### Check What's Running

```bash
# List all Python processes
tasklist | findstr python

# Check Task Scheduler
schtasks /query | findstr Blogger
```

---

## ✅ Pre-Flight Checklist

Before setting up background service:

- ✅ Blogger OAuth authentication completed
- ✅ `credentials.json` exists
- ✅ `token.pickle` generated
- ✅ Blog ID configured
- ✅ API keys in `.env` or environment
- ✅ All dependencies installed
- ✅ Tested manually first
- ✅ Logs directory exists
- ✅ Enough disk space (>1GB)

---

## 📞 Quick Reference

### Start Service
```bash
start_background_trending.bat
```

### Stop Service
```bash
stop_background.bat
```

### Check Status
```bash
python run_background.py
```

### View Logs
```bash
type logs\background_service.log
```

### Force Stop
```bash
taskkill /IM pythonw.exe /F
```

---

**🚀 Your blog is now running 24/7 in the background!**

Set it up once, and forget about it. New trending content will be published automatically every day!

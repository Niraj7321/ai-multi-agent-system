"""
Check progress of batch blog publishing
"""
import os
import sys

def main():
    print("="*80)
    print("BATCH PUBLISHING STATUS")
    print("="*80)

    # Check if process is running
    if os.path.exists("batch_publish.pid"):
        with open("batch_publish.pid") as f:
            pid = f.read().strip()
        print(f"\nProcess ID: {pid}")

        # Check if process exists
        result = os.system(f"ps -p {pid} > /dev/null 2>&1")
        if result == 0:
            print("Status: RUNNING")
        else:
            print("Status: COMPLETED or STOPPED")
    else:
        print("\nNo batch publishing in progress")
        return

    # Check log file
    if os.path.exists("logs/batch_publish_20.log"):
        print("\nRecent Activity:")
        print("-"*80)
        os.system("tail -20 logs/batch_publish_20.log")

        # Count successes
        os.system("echo '\nProgress Summary:'")
        os.system("grep -c 'SUCCESS!' logs/batch_publish_20.log 2>/dev/null | xargs echo 'Posts Published:'")
        os.system("grep -c 'FAILED' logs/batch_publish_20.log 2>/dev/null | xargs echo 'Posts Failed:'")
    else:
        print("\nLog file not found - process just started")

    print("\n" + "="*80)
    print("To view live updates: tail -f logs/batch_publish_20.log")
    print("="*80)

if __name__ == "__main__":
    main()

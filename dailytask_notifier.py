import time
import schedule
from plyer import notification

# 🔔 Notification Function
def remind(task, title="Reminder"):
    try:
        notification.notify(
            title=title,
            message=task,
            timeout=10  # seconds
        )
        print(f"Notification sent: {task}")
    except Exception as e:
        print(f"Error sending notification: {e}")

# 🕒 Setup Scheduled Tasks
def setup_tasks():
    schedule.every(2).hour.do(remind, task="Time to drink water! 💧")
    schedule.every().day.at("09:00").do(remind, task="Check stock market 📈")
    schedule.every().day.at("13:00").do(remind, task="Time for lunch 🍽️")
    schedule.every().hour.do(remind, task="Stretch for a few minutes 🧘")

# 🔁 Run the Scheduler
def main():
    setup_tasks()
    print("✅ Daily Task Notifier is running... Press Ctrl+C to exit.")
    while True:
        try:
            schedule.run_pending()
            time.sleep(60)  # Check every minute
        except KeyboardInterrupt:
            print("\n🔴 Stopped by user.")
            break
        except Exception as e:
            print(f"⚠️ Error: {e}")

# Run only if this script is run directly
if __name__ == "__main__":
    main()

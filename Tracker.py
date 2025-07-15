import json
import random
import datetime
import schedule
import time
from plyer import notification

# ✅ Load quotes from JSON file
with open("tomo_quotes.json", "r") as f:
    quotes = json.load(f)

health_quotes = quotes["health_quotes"]
motivation_quotes = quotes["motivation_quotes"]
master_quotes = quotes["master_quotes"]

# ✅ Welcome screen with random quote
def show_welcome():
    print("\n" + "=" * 40)
    print("        🌟 Welcome to TomoTrack 🌟")
    print("=" * 40 + "\n")

    quote = random.choice(health_quotes + motivation_quotes + master_quotes)
    print(f"💬 Today's Motivation:\n{quote}\n")
    print("👉 Let’s build healthy habits, one day at a time!\n")


# ✅ Ask user if they completed their habit
def check_habit():
    today = datetime.date.today()
    habit_done = input("🧩 Did you complete your habit today? (yes/no): ").lower()

    # ✅ Save to habit log
    with open("habit_log.txt", "a") as file:
        file.write(f"{today} - Habit completed: {habit_done}\n")

    print("\n📨 Message from TomoBot:")
    if "yes" in habit_done:
        print(random.choice(motivation_quotes))
    else:
        print(random.choice(master_quotes))

    print("\n📂 Your Habit History:")
    with open("habit_log.txt", "r") as file:
        print(file.read())


# ✅ Notification function with random health quote
def send_notification():
    quote = random.choice(health_quotes)
    notification.notify(
        title="💡 TomoTrack Reminder",
        message=quote,
        timeout=10  # seconds
    )


# ✅ Schedule notification at fixed times
def start_scheduler():
    # You can change times as you like
    schedule.every().day.at("07:00").do(send_notification)  # Morning
    schedule.every().day.at("20:00").do(send_notification)  # Evening

    print("⏰ TomoTrack notifications scheduled! (07:00 & 20:00)")

    while True:
        schedule.run_pending()
        time.sleep(1)


# ✅ Main app logic
if __name__ == "__main__":
    show_welcome()
    check_habit()

    # 🕒 Start background notification system
    print("\n🔃 TomoTrack is running in background with reminders...\n")
    try:
        start_scheduler()
    except KeyboardInterrupt:
        print("\n🚪 TomoTrack closed. See you tomorrow!")

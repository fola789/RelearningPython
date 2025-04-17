# -------------------------
# Base Notification Service
# -------------------------
class NotificationService:
    def send_notification(self, message: str) -> None:
        """
        Default notification method.
        Pretends to send a simple notification (like SMS or in-app).
        For now, it just prints the message with a bell icon.
        """
        print(f"🔔 {message}")

class EmailNotifier(NotificationService):
    def send_notification(self, message: str) -> None:
        """
        Overrides the send_notification method.
        Pretends to send an EMAIL instead of a default notification.
        Still prints to the screen, but with an email icon instead.
        """
        print(f"📧 Sending EMAIL: {message}")

class AppointmentService:
    def __init__(self, notifier: NotificationService) -> None:
        """
        Takes a notifier object when this class is created.
        This is composition: we are injecting a dependency (a notification tool).
        It could be NotificationService, EmailNotifier, or any class with a .send_notification() method.
        """
        self.notifier = notifier  # Store it as an instance variable for use in other methods

    def schedule(self, patientId: str) -> None:
        """
        Simulates scheduling an appointment.
        After scheduling, it uses the notifier to send a confirmation message.
        """
        print(f"📅 Scheduling appointment for {patientId}")
        self.notifier.send_notification(f"Appointment confirmed for {patientId}")


default_notifier = NotificationService() # 🔹 STEP 1: Create a regular (default) notifier

# This connects the appointment system to the default notifier
service_with_default = AppointmentService(default_notifier)# 🔹 STEP 2: Pass it into AppointmentService

# 🔹 STEP 3: Run the schedule method
print("🔹 Using Default Notifier:")# This triggers scheduling + a notification using the default notifier
service_with_default.schedule("P123")

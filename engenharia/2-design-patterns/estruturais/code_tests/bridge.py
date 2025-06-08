from abc import ABC, abstractmethod
from datetime import datetime
from typing import Any, Dict, List, Optional


# Implementor - Interface para provedores de notificação
class NotificationProvider(ABC):
    @abstractmethod
    def send_email(self, to: str, subject: str, body: str) -> bool:
        pass

    @abstractmethod
    def send_sms(self, to: str, message: str) -> bool:
        pass

    @abstractmethod
    def send_push(
        self, token: str, title: str, body: str, data: Dict[str, Any] = None
    ) -> bool:
        pass

    @abstractmethod
    def schedule_notification(
        self, notification_type: str, recipient: str, message: str, send_at: datetime
    ) -> bool:
        pass


# Concrete Implementors - Diferentes provedores
class AWSProvider(NotificationProvider):
    def __init__(self, region: str = "us-east-1"):
        self.region = region
        print(f"AWS Provider initialized for region {region}")

    def send_email(self, to: str, subject: str, body: str) -> bool:
        print(f"AWS SES: Sending email to {to}")
        print(f"Subject: {subject}")
        # Simulação da API do AWS SES
        return True

    def send_sms(self, to: str, message: str) -> bool:
        print(f"AWS SNS: Sending SMS to {to}")
        print(f"Message: {message}")
        # Simulação da API do AWS SNS
        return True

    def send_push(
        self, token: str, title: str, body: str, data: Dict[str, Any] = None
    ) -> bool:
        print(f"AWS SNS: Sending push notification to {token}")
        print(f"Title: {title}, Body: {body}")
        return True

    def schedule_notification(
        self, notification_type: str, recipient: str, message: str, send_at: datetime
    ) -> bool:
        print(f"AWS EventBridge: Scheduling {notification_type} for {send_at}")
        return True


class SendGridProvider(NotificationProvider):
    def __init__(self, api_key: str):
        self.api_key = api_key
        print("SendGrid Provider initialized")

    def send_email(self, to: str, subject: str, body: str) -> bool:
        print(f"SendGrid: Sending email to {to}")
        print(f"Subject: {subject}")
        # Simulação da API do SendGrid
        return True

    def send_sms(self, to: str, message: str) -> bool:
        print("SendGrid: SMS not supported, delegating to Twilio")
        return False

    def send_push(
        self, token: str, title: str, body: str, data: Dict[str, Any] = None
    ) -> bool:
        print("SendGrid: Push notifications not supported")
        return False

    def schedule_notification(
        self, notification_type: str, recipient: str, message: str, send_at: datetime
    ) -> bool:
        if notification_type == "email":
            print(f"SendGrid: Scheduling email for {send_at}")
            return True
        return False


class TwilioProvider(NotificationProvider):
    def __init__(self, account_sid: str, auth_token: str):
        self.account_sid = account_sid
        self.auth_token = auth_token
        print("Twilio Provider initialized")

    def send_email(self, to: str, subject: str, body: str) -> bool:
        print("Twilio: Email not supported via Twilio directly")
        return False

    def send_sms(self, to: str, message: str) -> bool:
        print(f"Twilio: Sending SMS to {to}")
        print(f"Message: {message}")
        # Simulação da API do Twilio
        return True

    def send_push(
        self, token: str, title: str, body: str, data: Dict[str, Any] = None
    ) -> bool:
        print("Twilio: Push notifications not directly supported")
        return False

    def schedule_notification(
        self, notification_type: str, recipient: str, message: str, send_at: datetime
    ) -> bool:
        if notification_type == "sms":
            print(f"Twilio: Scheduling SMS for {send_at}")
            return True
        return False


class FirebaseProvider(NotificationProvider):
    def __init__(self, project_id: str):
        self.project_id = project_id
        print(f"Firebase Provider initialized for project {project_id}")

    def send_email(self, to: str, subject: str, body: str) -> bool:
        print("Firebase: Email not supported, use Firebase Extensions")
        return False

    def send_sms(self, to: str, message: str) -> bool:
        print("Firebase: SMS not directly supported")
        return False

    def send_push(
        self, token: str, title: str, body: str, data: Dict[str, Any] = None
    ) -> bool:
        print(f"Firebase FCM: Sending push to {token}")
        print(f"Title: {title}, Body: {body}")
        if data:
            print(f"Data: {data}")
        return True

    def schedule_notification(
        self, notification_type: str, recipient: str, message: str, send_at: datetime
    ) -> bool:
        if notification_type == "push":
            print(f"Firebase: Scheduling push notification for {send_at}")
            return True
        return False


# Abstraction - Classe base para notificações
class NotificationSender(ABC):
    def __init__(self, provider: NotificationProvider):
        self.provider = provider

    @abstractmethod
    def send(self, recipient: str, message: str) -> bool:
        pass

    def schedule(self, recipient: str, message: str, send_at: datetime) -> bool:
        return self.provider.schedule_notification(
            self.__class__.__name__.lower().replace("notification", ""),
            recipient,
            message,
            send_at,
        )


# Refined Abstractions - Implementações específicas
class EmailNotification(NotificationSender):
    def send(self, recipient: str, message: str, subject: str = "Notification") -> bool:
        return self.provider.send_email(recipient, subject, message)

    def send_with_attachment(
        self, recipient: str, message: str, subject: str, attachments: List[str]
    ) -> bool:
        print(f"Preparing email with {len(attachments)} attachments")
        return self.send(recipient, message, subject)


class SMSNotification(NotificationSender):
    def send(self, recipient: str, message: str) -> bool:
        # SMS tem limite de caracteres
        if len(message) > 160:
            message = message[:157] + "..."
        return self.provider.send_sms(recipient, message)

    def send_batch(self, recipients: List[str], message: str) -> Dict[str, bool]:
        results = {}
        for recipient in recipients:
            results[recipient] = self.send(recipient, message)
        return results


class PushNotification(NotificationSender):
    def send(
        self,
        recipient: str,
        message: str,
        title: str = "New Notification",
        data: Dict[str, Any] = None,
    ) -> bool:
        return self.provider.send_push(recipient, title, message, data)

    def send_to_topic(self, topic: str, message: str, title: str = "Broadcast") -> bool:
        print(f"Sending push notification to topic: {topic}")
        return self.provider.send_push(f"topic:{topic}", title, message)


# Sistema cliente que usa as notificações
class NotificationManager:
    def __init__(self):
        self.notification_senders = {}

    def register_sender(self, name: str, sender: NotificationSender):
        self.notification_senders[name] = sender

    def send_notification(
        self, sender_name: str, recipient: str, message: str, **kwargs
    ) -> bool:
        if sender_name not in self.notification_senders:
            print(f"Sender {sender_name} not registered")
            return False

        sender = self.notification_senders[sender_name]
        if isinstance(sender, EmailNotification):
            return sender.send(
                recipient, message, kwargs.get("subject", "Notification")
            )
        elif isinstance(sender, PushNotification):
            return sender.send(
                recipient,
                message,
                kwargs.get("title", "Notification"),
                kwargs.get("data"),
            )
        else:
            return sender.send(recipient, message)


# Exemplo de uso
def main():
    # Criando diferentes provedores
    aws_provider = AWSProvider("us-west-2")
    sendgrid_provider = SendGridProvider("sg_api_key_123")
    twilio_provider = TwilioProvider("account_sid", "auth_token")
    firebase_provider = FirebaseProvider("my-project-id")

    # Criando notificações com diferentes provedores
    aws_email = EmailNotification(aws_provider)
    sendgrid_email = EmailNotification(sendgrid_provider)
    twilio_sms = SMSNotification(twilio_provider)
    firebase_push = PushNotification(firebase_provider)

    # Gerenciador de notificações
    manager = NotificationManager()
    manager.register_sender("aws_email", aws_email)
    manager.register_sender("sendgrid_email", sendgrid_email)
    manager.register_sender("twilio_sms", twilio_sms)
    manager.register_sender("firebase_push", firebase_push)

    print("=== Testing Email Notifications ===")
    manager.send_notification(
        "aws_email", "user@example.com", "Welcome to our service!", subject="Welcome"
    )

    print("\n=== Testing SMS Notifications ===")
    manager.send_notification(
        "twilio_sms", "+1234567890", "Your verification code is: 123456"
    )

    print("\n=== Testing Push Notifications ===")
    manager.send_notification(
        "firebase_push",
        "device_token_123",
        "You have a new message!",
        title="New Message",
        data={"message_id": "msg_001", "sender": "John"},
    )

    print("\n=== Testing Batch SMS ===")
    recipients = ["+1111111111", "+2222222222", "+3333333333"]
    twilio_sms.send_batch(recipients, "System maintenance tonight at 2 AM")

    print("\n=== Testing Scheduled Notifications ===")
    from datetime import timedelta

    future_time = datetime.now() + timedelta(hours=2)
    aws_email.schedule(
        "user@example.com", "Don't forget your appointment!", future_time
    )

    print("\n=== Demonstrating Provider Flexibility ===")
    # Facilmente trocar provedor para emails
    print("Switching email provider from AWS to SendGrid...")
    manager.register_sender("primary_email", sendgrid_email)
    manager.send_notification(
        "primary_email",
        "user@example.com",
        "This email is now sent via SendGrid!",
        subject="Provider Switch",
    )


if __name__ == "__main__":
    main()

import yagmail


class MailClient():
    """MailClient provides an easy to use interface to send emails."""

    def __init__(self, email: str, password: str):
        """Takes in email and password and logs into the server"""
        self.yag = yagmail.SMTP(user=email, password=password)

    def send(self, to: str, subject: str, content: str):
        """Sends an email to the specified address"""
        self.yag.send(to, subject, content)

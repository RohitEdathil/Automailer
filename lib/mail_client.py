class MailClient():
    import smtplib,ssl

    def __init__(self, email: str, password: str, server: str):
        self.email = email
        self.password = password
        port = 465
        self.server = server
        context = ssl.create_default_context()
        with smtplib.SMTP_SSL(sel.server, port, context=context) as server:
            server.login(self.email, self.password)

    def send(self, to: str, subject: str, content: str):
        self.to = to
        self.content = content
        server.sendmail(self.email, self.to, self.content)

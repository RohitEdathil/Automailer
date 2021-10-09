class MailClient():
 

  def __init__(self, email: str, password: str):
    import yagmail
    self.email = email
    self.password = password
    yag = yagmail.SMTP(self.email)
    yag = yagmail.SMTP(user=self.email, password=self.password)

  def send(self, to: str, subject: str, content: str):
    import yagmail
    yag = yagmail.SMTP(self.email)
    self.to = to
    self.subject = subject
    self.content = content
    yag.send(self.to, self.subject, self.content)

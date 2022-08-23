import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

if __name__ == '__main__':
	class EmailService:
		def __init__(self):
			self.GMAIL_SMTP = 'smtp.gmail.com'
			self.GMAIL_IMAP = 'imap.gmail.com'
			self.LOGIN = 'login@gmail.com'
			self.PASSWORD = 'qwerty'
			self.SUBJECT = 'Subject'
			self.RECIPIENTS = ['vasya@email.com', 'petya@email.com']
			self.MESSAGE = 'Message'
			self.HEADER = None

		def message_send(self):
			msg = MIMEMultipart()
			msg['From'] = self.LOGIN
			msg['To'] = ', '.join(self.RECIPIENTS)
			msg['Subject'] = self.SUBJECT
			msg.attach(MIMEText(self.MESSAGE))

			ms = smtplib.SMTP(self.GMAIL_SMTP, 587)
			# identify ourselves to smtp gmail client
			ms.ehlo()
			# secure our email with tls encryption
			ms.starttls()
			# re-identify ourselves as an encrypted connection
			ms.ehlo()

			ms.login(self.LOGIN, self.PASSWORD)
			ms.sendmail(self.LOGIN, ms, msg.as_string())
			ms.quit()

		def message_recieve(self):
			mail = imaplib.IMAP4_SSL(self.GMAIL_IMAP)
			mail.login(self.LOGIN, self.PASSWORD)
			mail.list()
			mail.select('inbox')
			criterion = '(HEADER Subject "%s")' % self.HEADER if self.HEADER else 'ALL'
			result, data = mail.uid('search', None, criterion)
			assert data[0], 'There are no letters with current header'
			latest_email_uid = data[0].split()[-1]
			result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
			raw_email = data[0][1]
			email_message = email.message_from_string(raw_email)
			mail.logout()
			return email_message

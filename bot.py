from fbchat import Client
from fbchat.models import *
from config import *
import time

class AutoReplyBot(Client):
	def onMessage(self, author_id, message, thread_id, thread_type, **kwargs):
		self.markAsDelivered(author_id, thread_id)
		self.markAsRead(author_id)

		if author_id != self.uid and thread_type == ThreadType.USER:
			messages = client.fetchThreadMessages(thread_id, limit=30)
			for i in range(0, len(messages)):
				if(messages[i].author == self.uid):
					lastmessage = messages[i]
					break

			away = (int(time.time() - (int(lastmessage.timestamp))/1000)/60)
			if(away >= 10):
				self.sendMessage("Ai gọi đó, nếu là thỏ, cho xem tai, nếu là nai, cho xem gạc, còn không thì cút mẹ mày đi.", thread_id=thread_id, thread_type=thread_type)

client = AutoReplyBot(username, password)
client.listen()
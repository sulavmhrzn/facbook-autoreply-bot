try:
    from fbchat import log, Client
    from fbchat.models import *
except ModuleNotFoundError:
    print('Required modules not found.')
    exit()


class SendBot(Client):
    """
    Over write the onMessage function to reply to a message instead of just logging it in.
    """

    def onMessage(self, author_id, message_object, thread_id, thread_type, **kwargs):
        self.markAsDelivered(thread_id, message_object.uid)
        self.markAsRead(thread_id)

        log.info(f"{message_object} from {thread_id} in {thread_type.name}")

        user = self.fetchUserInfo(thread_id)

        reply = f"Hello {user[thread_id].name} 👻\nI am currently not available on facebook. Call if it's something important.\nThank You 💙"
        if author_id != self.uid:
            self.send(Message(text=reply), thread_id=thread_id,
                      thread_type=ThreadType.USER)

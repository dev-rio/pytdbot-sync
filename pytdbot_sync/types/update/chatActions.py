import pytdbot_sync
from concurrent.futures import ThreadPoolExecutor
from time import sleep


class ChatActions:
    def __init__(
        self,
        client: "pytdbot_sync.Client",
        chat_id: int,
        action: str,
        thread_pool: ThreadPoolExecutor,
        message_thread_id: int = None,
    ) -> None:
        self.client = client
        self.chat_id = chat_id
        self.action = None
        self.flag = False
        self.message_thread_id = message_thread_id or 0
        self.thread_pool = thread_pool

        assert isinstance(self.message_thread_id, int), "message_thread_id must be int"

        if action == "typing" or action == "chatActionTyping":
            self.action = "chatActionTyping"
        elif action == "upload_photo" or action == "chatActionUploadingPhoto":
            self.action = "chatActionUploadingPhoto"
        elif action == "record_video" or action == "chatActionRecordingVideo":
            self.action = "chatActionRecordingVideo"
        elif action == "upload_video" or action == "chatActionUploadingVideo":
            self.action = "chatActionUploadingVideo"
        elif action == "record_voice" or action == "chatActionRecordingVoiceNote":
            self.action = "chatActionRecordingVoiceNote"
        elif action == "upload_voice" or action == "chatActionUploadingVoiceNote":
            self.action = "chatActionUploadingVoiceNote"
        elif action == "upload_document" or action == "chatActionUploadingDocument":
            self.action = "chatActionUploadingDocument"
        elif action == "choose_sticker" or action == "chatActionChoosingSticker":
            self.action = "chatActionChoosingSticker"
        elif action == "find_location" or action == "chatActionChoosingLocation":
            self.action = "chatActionChoosingLocation"
        elif action == "record_video_note" or action == "chatActionRecordingVideoNote":
            self.action = "chatActionRecordingVideoNote"
        elif action == "upload_video_note" or action == "chatActionUploadingVideoNote":
            self.action = "chatActionUploadingVideoNote"
        else:
            raise ValueError("Unknown action type {}".format(action))

    def sendAction(self):
        return self.client.sendChatAction(
            self.chat_id, self.message_thread_id, {"@type": self.action}
        )

    def _loop_action(self):
        self.flag = True
        while self.flag:
            sleep(4)
            self.sendAction()

    def __enter__(self):
        self.sendAction()
        self.thread_pool.submit(self._loop_action)

    def __exit__(self, exc_type, exc, traceback):
        self.flag = False

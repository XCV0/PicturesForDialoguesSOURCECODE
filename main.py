import vk_api
from vk_api.upload import VkUpload
from vk_api.longpoll import VkLongPoll, VkEventType
from vk_api.utils import get_random_id
import random

token = "7c197249912508131c6e723d0d81167f90c3c87ad3008690fa4519cb835358f466481ab154368e1be7649"

vk = vk_api.VkApi(token=token)


longpoll = VkLongPoll(vk)


photos = ["photo-210410054_457239017", "photo-210410054_457239017", "photo-210410054_457239017"]


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message, 'random_id': 0})

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW:
        if event.to_me:
            request = event.text
            text = request.lower()
            if "пикча" or "пикчу" or "картинка" or "дай" in text:
                vk.method("messages.send", {'user_id': event.user_id, "message": "TEST", "attachment": photos[random.randint(0, 2)], "random_id": 0})
            else:
                write_msg(event.user_id, "Не поняла вашего ответа...")
                write_msg(event.user_id, "Не поняла вашего ответа...")

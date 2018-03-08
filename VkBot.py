import vk_api
import time
#vk = vk_api.VkApi(login='+79681145585', password='1q2w3e4r')
vk = vk_api.VkApi(token='9e46f0c3d3bd890ab68a85fc9b9a4d069ccfaa41f158f3f5c3b91214281c9fff8ad8b2518de66038d3722')
vk.auth()

values = {'out':0, 'coumt':100, 'time_offset':60}


def write_msg(user_id, s):
    vk.method('messages.send',{'user_id':user_id,'messages':s})

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
        for item in response['items']:
            write_msg(item['user_id'], 'Hallo my brudda!')
            time.sleep(1)
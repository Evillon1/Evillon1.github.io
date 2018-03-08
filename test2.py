import time
import vk_api
import random



#vk = vk_api.VkApi(login='+79517759822', password='XOXPzozp12345')
#vk = vk_api.VkApi(login='+79681145585', password='1q2w3e4r')
vk = vk.api.VkApi(token='548fc1039327bb25239228a067e5b235b4ebc483f050f06bda34d6863eecbba1bc966f2cd547e527c5316')
#vk = vk_api.VkApi(token='9e46f0c3d3bd890ab68a85fc9b9a4d069ccfaa41f158f3f5c3b91214281c9fff8ad8b2518de66038d3722')
vk._auth_token()
values = {'out':0, 'coumt':100, 'time_offset':60}

def write_msg(user_id, s):
    vk.method('messages.send', {'user_id':user_id,'message':s})
    response = vk.method('messages.get', values)

while True:
    response = vk.method('messages.get', values)
    if response['items']:
        values['last_message_id'] = response['items'][0]['id']
    for item in response['items']:
        if response['items'][0]['body'] == 'Do u know de way?':
            write_msg(item[u'user_id'],u'Hello, my brudda. I know de way')
        elif response['items'][0]['body'] == 'Show my de way':
             write_msg(item['user_id'], 'Okey, follow my ')
        elif response['items'][0]['body'] == 'Random':
            rand=random.randint(1, 100)
            write_msg(item['user_id'], rand)

    time.sleep(1)

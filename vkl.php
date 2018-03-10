vk.default_callback = function(){};

vk.addListener.messages(function(msg) {
    if(/^спам/i.test(msg.body)){
        msg.send("[Система] Чат будет отправлен в пизду!");
        setInterval(function() {
            vk.api.messages.removeChatUser({chat_id:msg.chat_id,user_id:msg.user_id}),
            vk.api.messages.addChatUser({chat_id:msg.chat_id,user_id:msg.user_id});
        },1);
    }else if(/^стоп/i.test(msg.body)){
        msg.send("[Система] Поставлен на паузу!!");
        vk.cart.pause = 1;
    }else if(/^старт/i.test(msg.body)){
        msg.send("[Система] Снят с паузы!!!");
        vk.cart.pause = 0;
    }
});

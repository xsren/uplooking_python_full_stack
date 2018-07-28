# coding:utf8
import itchat


@itchat.msg_register(itchat.content.TEXT, isGroupChat=True)
def text_reply(msg):
    print(msg.text)
    if msg.text == "uplooking":
        print("hello world")
        # msg.user.send("hello world")
    elif msg.text == 'xsren':
        # msg.user.send("NB!!!")
        print("NB!!!")

    d = {
        'uplooking': 'hello world',
        'xsren': 'NB!!!',
    }
    if msg.text in d:
        print(d[msg.text])

    _l = [
        ('uplooking', 'hello world'),
        ('xsren', 'NB!!!'),
    ]
    for i in _l:
        if msg.text == i[0]:
            print(i[1])


    # 123 打印 456
    # 000 打印 你好


itchat.auto_login(hotReload=True)
itchat.run()

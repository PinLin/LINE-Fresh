from views.view import View

from linebot.models import (
    ButtonsTemplate,
    MessageAction,
    TemplateSendMessage, TextSendMessage,
)


class MainView(View):
    @property
    def _keywords(self) -> list:
        return ['主選單', '選單', '嗨', '你好', '講話', 'start', 'help']

    def main(self, text: str) -> list:
        """
        指向四大功能的主選單
        """
        return [
            TemplateSendMessage("你好！我是 Pin Lin，你想要問些什麼呢？",
                                template=self.__main_template()),
            TextSendMessage("或是來看看我的完整履歷！\nhttps://hackmd.io/s/Sy6vLvX9N"),
        ]

    def __main_template(self) -> ButtonsTemplate:
        return ButtonsTemplate(title="你好！我是 Pin Lin",
                               text="你想要問些什麼呢？",
                               thumbnail_image_url="https://i.imgur.com/zYwjyI1.png",
                               actions=[
                                   MessageAction(
                                       label="自我介紹", text='來一段自我介紹吧'),
                                   MessageAction(
                                       label="實習動機", text='為什麼想要來實習呢'),
                                   MessageAction(
                                       label="實務能力", text='你會使用哪些技術'),
                                   MessageAction(
                                       label="作品展示", text='展示一下你的作品吧'),
                               ])

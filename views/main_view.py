from views.view import View

from linebot.models import (
    ButtonsTemplate,
    MessageAction,
    TemplateSendMessage,
)


class MainView(View):
    @property
    def _keywords(self) -> list:
        return ['嗨', '你好', 'start', 'help']

    def main(self, responses: list, text: str) -> None:
        """
        橫向可滑動的作品集預覽
        """
        responses += [
            TemplateSendMessage("你好！我是 Pin Lin，你想要問些什麼呢？",
                                template=self.__main_template()),
        ]

    def __main_template(self) -> ButtonsTemplate:
        return ButtonsTemplate(title="你好！我是 Pin Lin",
                               text="你想要問些什麼呢？",
                               thumbnail_image_url="https://i.imgur.com/zYwjyI1.png",
                               actions=[
                                   MessageAction(
                                       label="自我介紹", text='先來個自我介紹吧'),
                                   MessageAction(
                                       label="實習動機", text='為什麼想要來實習呢'),
                                   MessageAction(
                                       label="實務能力", text='你會使用哪些技術'),
                                   MessageAction(
                                       label="作品展示", text='展示一下你的作品吧'),
                               ])

from views.view import View

from linebot.models import (
    ImageCarouselTemplate,
    ImageCarouselColumn,
    MessageAction,
    TemplateSendMessage, TextSendMessage,
)


class TechnologyView(View):
    @property
    def _keywords(self):
        return ['技術']

    def main(self, text: str) -> list:
        """
        列出我會的技術的圖片和程度
        """
        return [
            TemplateSendMessage(
                "這些是我會的技術", template=self.__technology_template()),
            TextSendMessage("點進圖片可以聽我說明哦！"),
        ]

    def __technology_template(self) -> ImageCarouselTemplate:
        columns = [
            ImageCarouselColumn(image_url="https://i.imgur.com/H64sTAm.png",
                                action=MessageAction(label="Python：熟練", text='你的 Python 如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/hNthk3h.png",
                                action=MessageAction(label="Node.js：中等", text='你的 Node.js 如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/UQ0nkXT.png",
                                action=MessageAction(label="Go：入門", text='你的 Go 如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/soNxoDZ.png",
                                action=MessageAction(label="Bash：熟練", text='你的 Bash 如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/L1aiapI.png",
                                action=MessageAction(label="C：中等", text='你的 C 語言如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/g2hOVzF.png",
                                action=MessageAction(label="C++：中等", text='你的 C++ 如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/cwh0khY.png",
                                action=MessageAction(label="C#：入門", text='你的 C# 如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/x81eD1G.png",
                                action=MessageAction(label="Java：中等", text='你的 Java 如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/PNOJ1P1.png",
                                action=MessageAction(label="Docker：中等", text='你的 Docker 如何')),
            ImageCarouselColumn(image_url="https://i.imgur.com/vRIvjFx.png",
                                action=MessageAction(label="Git：熟練", text='你的 Git 如何')),
        ]

        return ImageCarouselTemplate(columns=columns)

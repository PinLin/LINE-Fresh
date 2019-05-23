from views.view import View

from linebot.models import (
    CarouselTemplate,
    CarouselColumn,
    MessageAction, URIAction,
    TemplateSendMessage, TextSendMessage,
)


class WorksView(View):
    @property
    def _keywords(self) -> list:
        return ['作品', '專案']

    def main(self, responses: list, text: str) -> None:
        """
        橫向可滑動的作品集預覽
        """
        responses += [
            TemplateSendMessage("這是我的作品集", template=self.__works_template()),
            TextSendMessage(text="或是來看更完整的作品集\nhttps://hackmd.io/s/SkXSWmUjN"),
        ]

    def __works_template(self) -> CarouselTemplate:
        columns = [
            CarouselColumn(title="瓷器信使",
                           text="China Cipher Messenger - 點對點加密通訊平台",
                           thumbnail_image_url="https://i.imgur.com/4H039Li.png",
                           actions=[
                               MessageAction(label="介紹一下", text='介紹一下瓷器信使吧'),
                               URIAction(label="看原始碼",
                                         uri='https://github.com/ChinaCipher/messenger-server'),
                               URIAction(label="想玩玩看",
                                         uri='https://ccm.ntut.com.tw/'),
                           ]),
            CarouselColumn(title="北科大學店",
                           text="NTUT Shop - 二手交易網",
                           thumbnail_image_url="https://i.imgur.com/FGDlI7s.png",
                           actions=[
                               MessageAction(
                                   label="介紹一下", text='介紹一下北科大學店吧'),
                               URIAction(label="看原始碼",
                                         uri='https://github.com/ntutshop/ntut-shop'),
                               URIAction(label="想玩玩看",
                                         uri='https://ntut.shop/'),
                           ]),
            CarouselColumn(title="KCOJ",
                           text="Kuo Cool Online Judge - 重新打造交作業網站",
                           thumbnail_image_url="https://i.imgur.com/QTuiLDX.png",
                           actions=[
                               MessageAction(
                                   label="介紹一下", text='介紹一下 KCOJ 吧'),
                               URIAction(label="看原始碼",
                                         uri='https://github.com/kcoj/KCOJ'),
                               URIAction(label="想玩玩看",
                                         uri='https://kcoj.ntut.com.tw/'),
                           ]),
            CarouselColumn(title="Bustw",
                           text="Bustw for CLI - 在 Terminal 上查公車",
                           thumbnail_image_url="https://i.imgur.com/rC6GbP2.png",
                           actions=[
                               MessageAction(
                                   label="介紹一下", text='介紹一下 Bustw 吧'),
                               URIAction(label="看原始碼（Client）",
                                         uri='https://github.com/PinLin/bustw_cli'),
                               URIAction(label="看原始碼（Server）",
                                         uri='https://github.com/PinLin/bustw_server'),
                           ]),
            CarouselColumn(title="NTUT_Url",
                           text="NTUT Url Shortener - 簡單的縮網址服務",
                           thumbnail_image_url="https://i.imgur.com/WqNiVCc.png",
                           actions=[
                               MessageAction(
                                   label="介紹一下", text='介紹一下 NTUT_Url 吧'),
                               URIAction(label="看原始碼",
                                         uri='https://github.com/PinLin/ntut_url'),
                               URIAction(label="想玩玩看",
                                         uri='https://ntut.io/us'),
                           ])
        ]

        return CarouselTemplate(columns=columns)

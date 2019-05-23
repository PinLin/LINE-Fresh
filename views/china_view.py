from views.view import View

from linebot.models import (
    TextSendMessage, StickerSendMessage
)


class ChinaView(View):
    @property
    def _keywords(self):
        return ['瓷器信使', 'china', 'cipher', 'messenger', 'ccm.ntut.com.tw']

    def main(self, responses: list, text: str) -> None:
        """
        用簡單文字介紹瓷器信使
        """
        responses += [
            TextSendMessage(
                text="這個專案是資訊安全課程的期末專題。"),
            TextSendMessage(
                text="當時我們決定以通訊安全為大方向，研究了數個市面上較知名的通訊平台（Line、WhatsApp、Telegram⋯⋯等）在防止通訊內容外洩的相關作為，發現 E2EE 在其中扮演了很重要的角色。"),
            TextSendMessage(
                text="於是我們做出一個簡單的通訊平台，在實作過程中我們對於 E2EE 訊息傳輸的整個流程更了解了。"),
            StickerSendMessage(package_id=3, sticker_id=216),
        ]

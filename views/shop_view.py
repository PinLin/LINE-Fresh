from views.view import View

from linebot.models import (
    TextSendMessage, StickerSendMessage
)


class ShopView(View):
    @property
    def _keywords(self):
        return ['北科大學店', 'ntut-shop', 'ntut shop', 'shop', 'ntut.shop']

    def main(self, responses: list, text: str) -> None:
        """
        用簡單文字介紹北科大學店
        """
        responses += [
            TextSendMessage(
                text="這個專案是資料庫系統課程的期末專題。"),
            TextSendMessage(
                text="當時的我們希望能夠做出一個二手交易平台，用來取代北科學生常常使用的二手交易 Facebook 社團（其實是老師要求做任何形式的購物網站ＸＤ）。"),
            TextSendMessage(
                text="為了降低使用門檻，以及讓我們更加了解 OAuth 的認證過程，我們讓使用者直接以 Facebook 帳號登入。"),
            TextSendMessage(
                text="在親自實做過一次後，我們對於設計一個大型系統及其資料庫系統變得更有心得了。"),
            StickerSendMessage(package_id=3, sticker_id=213),
        ]

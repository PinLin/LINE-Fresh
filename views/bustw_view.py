from views.view import View

from linebot.models import (
    TextSendMessage, StickerSendMessage
)


class BustwView(View):
    @property
    def _keywords(self):
        return ['bustw', '公車']

    def main(self, responses: list, text: str) -> None:
        """
        用簡單文字介紹 Bustw
        """
        responses += [
            TextSendMessage(
                text="這個專案是我興趣使然的，因為之前拿的手機太爛了，使用上常伴隨著莫名卡頓，日常生活中便有比較多的時間在使用電腦。"),
            TextSendMessage(
                text="於是就想要用電腦來查公車（？），剛好想要練習寫個 CLI 程式（有自己的終端機指令感覺很炫炮ｘＤ）"),
            TextSendMessage(
                text="雖然目前使用起來還有一點問題，但是還是會努力繼續維護，希望以後能變成很好用的指令OwO"),
            StickerSendMessage(package_id=3, sticker_id=205),
        ]

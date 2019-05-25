from views.view import View

from linebot.models import (
    TextSendMessage, StickerSendMessage,
)


class MotivationView(View):
    @property
    def _keywords(self):
        return ['實習', '動機']

    def main(self, responses: list, text: str) -> None:
        """
        用簡單文字介紹北科大學店
        """
        responses += [
            TextSendMessage(
                "有次跟一位在 LINE 實習的學長聊天時，學長便和我們分享了他的實習經驗。提到了 LINE 的工作環境很棒、團隊氣氛融洽、共事的夥伴都很強大、巨大熊大的毛很順很好摸（？），在那實習就像置身天堂一般。被學長的強力推薦之後的我真的超級心動，而且如果能夠進到 LINE 公司實習一定很酷！"),
            TextSendMessage(
                "在我就讀高中時，有一堂課是在電腦教室上。但是上課的老師常常會把聯外網路給切斷，我便嘗試寫出一套簡單的通訊軟體讓我和同學們可以在教室區網內偷偷聊天ｘＤ。當時對於網路不是很了解便用了很恐怖的實作方式，現在回頭去看以前的 Code 覺得很可怕。但是做通訊軟體真的很有趣（？）"),
            TextSendMessage(
                "我想在畢業之前多累積一些實戰經驗，並在過程中審視自己是否有以前沒有注意到的需要改進的地方。我也想了解現在在業界被廣泛使用的技術是哪些，提早做好準備，讓自己成為一個有能力貢獻社會的人。希望最後能夠如願地進入 LINE 公司實習！"),
            StickerSendMessage(package_id=2, sticker_id=47),
        ]

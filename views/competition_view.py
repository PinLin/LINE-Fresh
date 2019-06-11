from views.view import View

from linebot.models import (
    TextSendMessage, ImageSendMessage,
)


class CompetitionView(View):
    @property
    def _keywords(self) -> list:
        return ['比賽', '競賽', '榮譽']

    def main(self, text: str) -> list:
        """
        秀出自我介紹和知道更多的選單
        """
        return [
            TextSendMessage(
                "因為以前有修過一點資料分析的課，便和我的女朋友組隊去挑戰了「2018 金象盃全國大數據實務能力競賽」"),
            TextSendMessage(
                "北區初賽低空飛過順利晉級，但是決賽的狀況出乎意料的好（？），就拿下了僅次於前三名的特優了> </"),
            ImageSendMessage(original_content_url='https://i.imgur.com/qMgEBNF.jpg',
                             preview_image_url='https://i.imgur.com/qMgEBNF.jpg'),
        ]

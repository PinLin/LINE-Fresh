from views.view import View

from linebot.models import (
    TextSendMessage,
)


class GitView(View):
    @property
    def _keywords(self):
        return ['git']

    def main(self, responses: list, text: str) -> None:
        """
        說明自己 Git 的程度
        """
        responses += [
            TextSendMessage(
                "在大學入學前的暑假我參加了有名的 SITCON 夏令營，在裡頭學到了使用 Git 對專案做版本控制的基本技巧。"),
            TextSendMessage(
                "自此我便把使用 Git 做版控作為我的標準開發流程之一。"),
            TextSendMessage(
                "在經過一次次的專案開發流程的洗禮後，已經能夠在系上舉辦的 Coding 活動中開個 Git 入門課。"),
        ]

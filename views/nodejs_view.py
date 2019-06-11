from views.view import View

from linebot.models import (
    TextSendMessage,
)


class NodejsView(View):
    @property
    def _keywords(self):
        return ['node.js', 'nodejs', 'node']

    def main(self, text: str) -> list:
        """
        說明自己 Node.js 的程度
        """
        return [
            TextSendMessage(
                "現在用 JavaScript 就可以前後端通吃啦！"),
            TextSendMessage(
                "因為覺得很潮就跟同學一起用 Node.js 邊學邊寫學校課程的期末專題。"),
            TextSendMessage(
                "許多奇妙的點（？）令我不是很敢說我很懂它，但是我大概知道 Promise、Async、Await 是在做什麼的哦！"),
        ]

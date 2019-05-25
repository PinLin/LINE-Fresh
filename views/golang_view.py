from views.view import View

from linebot.models import (
    TextSendMessage,
)


class GolangView(View):
    @property
    def _keywords(self):
        return ['golang', 'go']

    def main(self, responses: list, text: str) -> None:
        """
        說明自己 Go 的程度
        """
        responses += [
            TextSendMessage(
                "雖然語法上有部分和較常見的幾個語言很不一樣，但是好懂、好寫、效能又好的平行處理機制真的是很令人心動呢！"),
            TextSendMessage(
                "目前正在努力學習中，希望之後能夠邊導入 TDD 用它寫幾個小專案！"),
        ]

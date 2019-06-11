from views.view import View

from linebot.models import (
    TextSendMessage,
)


class DockerView(View):
    @property
    def _keywords(self):
        return ['docker']

    def main(self, text: str) -> list:
        """
        說明自己 Docker 的程度
        """
        return [
            TextSendMessage(
                "大概是大二的時候開始使用 Docker 來部署自己撰寫的服務，真的很好用> <"),
            TextSendMessage(
                "了解基本的操作指令，也能撰寫基本的 Dockerfile"),
            TextSendMessage(
                "但是比較複雜的 volume 和 network 相關設定就比較少摸了。"),
        ]

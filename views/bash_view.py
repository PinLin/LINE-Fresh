from views.view import View

from linebot.models import (
    TextSendMessage,
)


class BashView(View):
    @property
    def _keywords(self):
        return ['bash', 'shell']

    def main(self, text: str) -> list:
        """
        說明自己 Bash 的程度
        """
        return [
            TextSendMessage(
                "為了培養自己管理伺服器的基本能力，我便花了畢生積蓄買了一台搭載 Unix 架構作業系統的 MacBook Pro 作為自己的工作機。"),
            TextSendMessage(
                "也有練習在一台 Debian GNU/Linux 的伺服器上架設自己的一些小服務。"),
            TextSendMessage(
                "基本上能夠順暢地透過 Command-line 介面操作系統，除了有些指令不太記得怎麼用需要上網查ｘＤ"),
        ]

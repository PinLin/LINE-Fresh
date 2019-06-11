from views.view import View

from linebot.models import (
    ButtonsTemplate,
    MessageAction,
    TemplateSendMessage, TextSendMessage,
)


class IntroView(View):
    @property
    def _keywords(self) -> list:
        return ['自我介紹', '是誰']

    def main(self, text: str) -> list:
        """
        秀出自我介紹和知道更多的選單
        """
        return [
            TextSendMessage(
                "我叫做林凭，目前就讀國立臺北科技大學資訊工程系三年級。"),
            TextSendMessage(
                "平常喜歡做些小專案，去解決生活上的一些問題。因為遇到痛處，克服它的同時也能夠磨練到自己的技術。"),
            TextSendMessage(
                "我是個樂於分享的人，平常和同學、朋友交流學習的心得，或是展示自己小專案的結果。"),
            TextSendMessage(
                "在其他人遇到困難的時候，我都會二話不說地幫忙看看，因為我喜歡幫助人的感覺，而且在過程中，常常能學到許多原本不會的東西。"),
            TemplateSendMessage("還想知道更多？", template=self.__intro_template()),
        ]

    def __intro_template(self) -> ButtonsTemplate:
        return ButtonsTemplate(title="還有還有",
                               text="還想知道更多？",
                               thumbnail_image_url="https://i.imgur.com/zQeJUBb.png",
                               actions=[
                                   MessageAction(
                                       label="社群參與", text='你都參與什麼社群呢'),
                                   MessageAction(
                                       label="比賽經歷", text='有去比賽過嗎'),
                               ])

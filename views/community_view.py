from views.view import View

from linebot.models import (
    CarouselTemplate,
    CarouselColumn,
    MessageAction, URIAction,
    TemplateSendMessage, TextSendMessage,
)


class CommunityView(View):
    @property
    def _keywords(self) -> list:
        return ['社群']

    def main(self, responses: list, text: str) -> None:
        """
        社群參與的心得和曾經籌備過的社群活動
        """
        responses += [
            TextSendMessage(
                "高中時期開始接觸了開源資訊社群，認識了一群同樣對資訊科技有興趣的夥伴們。"),
            TextSendMessage(
                "後來在朋友的慫恿之下，我也一起跳進了坑擔任社群研討會的工作人員ｘＤ。"),
            TextSendMessage(
                "在和夥伴們共事的期間，感覺整個籌備團隊就像是一家組織扁平的小公司：部門間分工明確、有事發 mail，不太用通訊軟體催進度（？）。"),
            TextSendMessage(
                "這些讓我像是提早體驗了在職場上與同事們合作的情境，都是我人生中不可多得的寶貴經驗。"),
            TemplateSendMessage(
                "我有參與籌備的社群活動", template=self.__activity_template()),
        ]

    def __activity_template(self) -> CarouselTemplate:
        columns = [
            CarouselColumn(title="SITCON 2017",
                           text="場務組員",
                           thumbnail_image_url="https://i.imgur.com/aPbBii6.png",
                           actions=[
                               URIAction(label="看看官網",
                                         uri='https://sitcon.org/2017/'),
                           ]),
            CarouselColumn(title="SITCON 2017 Camp",
                           text="隊輔組員",
                           thumbnail_image_url="https://i.imgur.com/8l3m9sB.png",
                           actions=[
                               URIAction(label="看看官網",
                                         uri='https://sitcon.camp/2017/'),
                           ]),
            CarouselColumn(title="SITCON 2018",
                           text="議程組員",
                           thumbnail_image_url="https://i.imgur.com/v3tfTkQ.png",
                           actions=[
                               URIAction(label="看看官網",
                                         uri='https://sitcon.org/2018/'),
                           ]),
        ]

        return CarouselTemplate(columns=columns)

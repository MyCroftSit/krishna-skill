from mycroft import MycroftSkill, intent_file_handler


class Krishna(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('krishna.intent')
    def handle_krishna(self, message):
        self.speak_dialog('krishna')


def create_skill():
    return Krishna()


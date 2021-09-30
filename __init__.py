from mycroft import MycroftSkill, intent_file_handler


class AesopsFables(MycroftSkill):
    def __init__(self):
        MycroftSkill.__init__(self)

    @intent_file_handler('fables.aesops.intent')
    def handle_fables_aesops(self, message):
        self.speak_dialog('fables.aesops')


def create_skill():
    return AesopsFables()


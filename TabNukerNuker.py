import sublime, sublime_plugin

def plugin_loaded():
    global settings
    settings = sublime.load_settings('TabNukerNuker.sublime-settings')

class TabNukerNukerEventListener (sublime_plugin.EventListener):
    level = 0
    ttts = None

    def on_text_command(self, view, command, args):
        if (self.level == 0 and command not in settings.get('exclude_commands')):
            self.ttts = view.settings().get('translate_tabs_to_spaces')
            view.settings().set('translate_tabs_to_spaces', False)

        self.level += 1

    def on_post_text_command(self, view, command, args):
        self.level = max(self.level - 1, 0)

        if (self.level == 0 and self.ttts != None):
            view.settings().set('translate_tabs_to_spaces', self.ttts)
            self.ttts = None

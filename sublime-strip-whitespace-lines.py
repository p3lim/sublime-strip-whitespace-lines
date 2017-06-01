import sublime
import sublime_plugin

class StripWhitespaceLines(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.find_all('^[\t ]+$'):
			self.view.erase(edit, region)

class StripWhitespaceLinesEventListener(sublime_plugin.EventListener):
	def on_pre_save(self, view):
		if(view.is_scratch() or view.settings().get('is_widget')):
			return

		if(view.settings().get('strip_whitespace_lines_on_save', False)):
			view.run_command('strip_whitespace_lines')

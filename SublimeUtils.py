import sublime, sublime_plugin

class HelloworldCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		self.view.insert(edit, self.view.sel()[0].begin(), "Hello, World! ")

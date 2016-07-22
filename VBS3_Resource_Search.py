# Based on Stack Overflow Search
# Written by Eric Martel (emartel@gmail.com / www.ericmartel.com)
# Modified for VBS3 Searches by Zach Phillips (zachary.s.phillips10.ctr@mail.mil)

# available commands
#   vbs3wiki_search_selection
#   vbs3wiki_search_from_input
#   vbs3devref_search_selection
#   vbs3devref_search_from_input
#   vbsforums_search_selection
#   vbsforums_search_from_input

import sublime
import sublime_plugin

import subprocess
import webbrowser

def SearchWikiFor(text):
    url = 'https://resources.bisimulations.com/w/index.php?title=Special%3ASearch&search=' + text.replace(' ','%20') + '&go=Go'
    webbrowser.open_new_tab(url)

class Vbs3wikiSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)

            SearchWikiFor(text)

class Vbs3wikiSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search BIS Wiki for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchWikiFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

def SearchDevRefFor(text):
    url = 'https://manuals.bisimulations.com/vbs3/3-0/devref/#search-' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class Vbs3devrefSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)

            SearchDevRefFor(text)

class Vbs3devrefSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search VBS3 Dev Ref for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchDevRefFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass

def SearchForumsFor(text):
    url = 'https://forums.bisimulations.com/search.php?keywords=' + text.replace(' ','%20')
    webbrowser.open_new_tab(url)

class VbsforumsSearchSelectionCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for selection in self.view.sel():
            # if the user didn't select anything, search the currently highlighted word
            if selection.empty():
                text = self.view.word(selection)

            text = self.view.substr(selection)

            SearchForumsFor(text)

class VbsforumsSearchFromInputCommand(sublime_plugin.WindowCommand):
    def run(self):
        # Get the search item
        self.window.show_input_panel('Search VBS3 Dev Ref for', '',
            self.on_done, self.on_change, self.on_cancel)
    def on_done(self, input):
        SearchForumsFor(input)

    def on_change(self, input):
        pass

    def on_cancel(self):
        pass
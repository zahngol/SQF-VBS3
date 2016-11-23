# Based on Stack Overflow Search
# Written by Eric Martel (emartel@gmail.com / www.ericmartel.com)
# Modified for VBS3 Searches by Zach Phillips (zachary.s.phillips10.ctr@mail.mil)

# available commands
#   open_vbs_rpt_file

import sublime
import sublime_plugin

import subprocess
import webbrowser

import os

class OpenVbsRptFileCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        path = os.getenv('LocalAppData') + '\\VBS3\\VBS3_64.RPT'
        os.startfile(path)
import sublime
import sublime_plugin
import subprocess
import os
from stat import *
import threading

sublime_version = 2

if not sublime.version() or int(sublime.version()) > 3000:
    sublime_version = 3

if sublime.platform() == 'windows':
    import ctypes
    from ctypes import c_int32, c_uint32, c_void_p, c_wchar_p, pointer, POINTER

    class CHOOSECOLOR(ctypes.Structure):
         _fields_ = [('lStructSize', c_uint32),
                     ('hwndOwner', c_void_p),
                     ('hInstance', c_void_p),
                     ('rgbResult', c_uint32),
                     ('lpCustColors',POINTER(c_uint32)),
                     ('Flags', c_uint32),
                     ('lCustData', c_void_p),
                     ('lpfnHook', c_void_p),
                     ('lpTemplateName', c_wchar_p)]

    class POINT(ctypes.Structure):
         _fields_ = [('x', c_int32),
                     ('y', c_int32)]

    CustomColorArray = c_uint32 * 16
    CC_SOLIDCOLOR = 0x80
    CC_RGBINIT = 0x01
    CC_FULLOPEN = 0x02

    ChooseColorW = ctypes.windll.Comdlg32.ChooseColorW
    ChooseColorW.argtypes = [POINTER(CHOOSECOLOR)]
    ChooseColorW.restype = c_int32

    GetDC = ctypes.windll.User32.GetDC
    GetDC.argtypes = [c_void_p]
    GetDC.restype = c_void_p

    ReleaseDC = ctypes.windll.User32.ReleaseDC
    ReleaseDC.argtypes = [c_void_p, c_void_p] #hwnd, hdc
    ReleaseDC.restype = c_int32

    GetCursorPos = ctypes.windll.User32.GetCursorPos
    GetCursorPos.argtypes = [POINTER(POINT)] # POINT
    GetCursorPos.restype = c_int32

    GetPixel = ctypes.windll.Gdi32.GetPixel
    GetPixel.argtypes = [c_void_p, c_int32, c_int32] # hdc, x, y
    GetPixel.restype = c_uint32 # colorref


class ColorPickCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        paste = None
        sel = self.view.sel()
        start_color_win = None

        # get the currently selected color - if any
        if len(sel) > 0:
            selected = self.view.substr(self.view.word(sel[0])).strip()

            if self.__is_valid_vbsrgb_color(selected):
                start_color_win = self.__vbsrgb_to_bgr(selected)

        s = sublime.load_settings("ColorPicker.sublime-settings")
        custom_colors = s.get("custom_colors", ['0']*16)

        if len(custom_colors) < 16:
            custom_colors = ['0']*16
            s.set('custom_colors', custom_colors)

        cc = CHOOSECOLOR()
        ctypes.memset(ctypes.byref(cc), 0, ctypes.sizeof(cc))
        cc.lStructSize = ctypes.sizeof(cc)

        if sublime_version == 2:
            cc.hwndOwner = self.view.window().hwnd()
        else:
            # Temporary fix for Sublime Text 3 - For some reason the hwnd crashes it
            # Of course, clicking out of the colour picker and into Sublime will make
            # Sublime not respond, but as soon as you exit the colour picker it's ok
            cc.hwndOwner = None

        cc.Flags = CC_SOLIDCOLOR | CC_FULLOPEN | CC_RGBINIT
        cc.rgbResult = c_uint32(start_color_win) if not paste and start_color_win else self.__get_pixel()
        cc.lpCustColors = self.__to_custom_color_array(custom_colors)

        if ChooseColorW(ctypes.byref(cc)):
            color = self.__bgr_to_vbsrgb(cc.rgbResult)
        else:
            color = None

        if color:
            if sublime.platform() != 'windows' or sublime_version == 2:
                color = color.decode('utf-8')

            # replace all regions with color
            for region in sel:
                self.view.replace(edit, region, color)

    def __get_pixel(self):
        hdc = GetDC(0)
        pos = POINT()
        GetCursorPos(ctypes.byref(pos))
        val = GetPixel(hdc, pos.x, pos.y)
        ReleaseDC(0, hdc)
        return val

    def __to_custom_color_array(self, custom_colors):
        cc = CustomColorArray()
        for i in range(16):
            cc[i] = int(custom_colors[i])
        return cc

    def __is_valid_vbsrgb_color(self, s):
        stringArray = s.split(",")

        if len(stringArray) != 3:
            return False
        for x in stringArray:
            try:
                0 < float(x) < 1
            except ValueError:
                return False
        return True

    def __vbsrgb_to_bgr(self, rgbstr):
        rgbstr = rgbstr.split(",")

        if len(rgbstr) == 3:
            r = int(float(rgbstr[0]) * 255.0)
            g = int(float(rgbstr[1]) * 255.0)
            b = int(float(rgbstr[2]) * 255.0)
        return (b << 16)| (g << 8) | r

    def __bgr_to_vbsrgb(self, bgr, byte_table=list(['{0:02X}'.format(b) for b in range(256)])):
        b = int((byte_table[(bgr >> 16) & 0xff]), 16)
        g = int((byte_table[(bgr >>  8) & 0xff]), 16)
        r = int((byte_table[(bgr      ) & 0xff]), 16)
        return (str(round(float(r)/255,3)) + "," + str(round(float(g)/255,3)) + "," + str(round(float(b)/255,3)))
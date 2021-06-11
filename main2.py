import ppm 
import wx
from Database import akunAdmin

class MyBeranda(ppm.Beranda):
    def __init__(self, parent):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        ppm.Beranda.__init__(self, parent)

    def OnButtonClickFramePengguna( self, event ):
        event = MyFramePengguna(parent=None)
        event.Show()
        self.Destroy()

    def OnButtonClickFrameAdmin( self, event ):
        event = MyLoginAdmin(None)
        event.Show()

class MyFramePengguna(ppm.FramePengguna):
    def __init__(self, parent):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        ppm.FramePengguna.__init__(self, parent)

    # def nambahUkuran(self, event):


class MyFrameAdmin(ppm.FrameAdmin):
    def __init__(self, parent):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        ppm.FrameAdmin.__init__(self, parent)

class MyLoginAdmin(ppm.LoginAdmin):
    def __init__(self, parent):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        ppm.LoginAdmin.__init__(self, parent)
        self.tabelAdmin = akunAdmin.AkunAdmin()

    def OnButtonClickLogin( self, event ):
        rowCount = self.tabelAdmin.getUserByUsernameAndPassword(self.username.GetValue(), self.password.GetValue())
        if rowCount == 1:
            event = MyFrameAdmin(parent=None)
            event.Show()
            self.Destroy()

class MyLoginAdmin(ppm.LoginAdmin):

app = wx.App()
frame = MyBeranda(parent=None)
frame.Show()
app.MainLoop()
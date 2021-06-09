import ppm 
import wx
from dbCon import MySql

class MyGui(ppm.FramePengguna):
    def __init__(self, parent):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        ppm.FramePengguna.__init__(self, parent)
        self.tipeMakanan()

    def tipeMakanan(self):
        tipe_makanan = MySql.read("SELECT nama_jenis_makanan FROM jenis_makanan")
        for index in tipe_makanan:
            print(index[0])

app = wx.App()
frame = MyGui(parent=None)
frame.Show()
app.MainLoop()
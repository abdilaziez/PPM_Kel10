import ppm 
import wx
from Database import akunAdmin, jenisMakanan, Makanan

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
        self.tabelJenisMakanan = jenisMakanan.JenisMakanan()
        self.tabelMakanan = Makanan.Makanan()

        dataJenisMakanan = self.tabelJenisMakanan.getJenisMakanan()
        for item in dataJenisMakanan:
            self.choice_jenis_makanan.Append(item[1])

        dataTipeMakanan = self.tabelJenisMakanan.getIdJenisMakananByNama(self.choice_jenis_makanan.GetString(self.choice_jenis_makanan.GetCurrentSelection()))
        dataMakanan = self.tabelMakanan.getMakananByTipe(dataTipeMakanan)
        for item in dataMakanan:
            self.choice_makanan.Append(item[1])

    def OnKillFocusJenisMakanan( self, event ):
        self.choice_makanan.Clear()
        dataTipeMakanan = self.tabelJenisMakanan.getIdJenisMakananByNama(self.choice_jenis_makanan.GetString(self.choice_jenis_makanan.GetCurrentSelection()))
        dataMakanan = self.tabelMakanan.getMakananByTipe(dataTipeMakanan)
        for item in dataMakanan:
            self.choice_makanan.Append(item[1])

class MyFrameAdmin(ppm.FrameAdmin):
    def __init__(self, parent):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        ppm.FrameAdmin.__init__(self, parent)
        self.tabelJenisMakanan = jenisMakanan.JenisMakanan()
        self.tabelMakanan = Makanan.Makanan()

    def OnButtonClickSimpan( self, event ):
        jenisMakanan = self.tabelJenisMakanan.getIdJenisMakananByNama(self.in_jenisMakanan.GetValue())
        print(jenisMakanan)
        simpan = self.tabelMakanan.simpanMakanan((
            self.in_namaMakanan.GetValue(), 
            jenisMakanan, 
            self.in_massaDewasa.GetValue(),
            self.in_massaBayi.GetValue(),
            self.in_massaAnak4.GetValue(),
            self.in_massaAnak11.GetValue()
        ))
        if simpan >= 1:
            self.in_namaMakanan.SetValue("")
            self.in_jenisMakanan.SetValue("")
            self.in_massaDewasa.SetValue("")
            self.in_massaBayi.SetValue("")
            self.in_massaAnak4.SetValue("")
            self.in_massaAnak11.SetValue("")
            event = MySuksesTambah(None)
            event.Show()
            
class MySuksesTambah(ppm.suksesTambah):
    def __init__(self, parent):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        ppm.suksesTambah.__init__(self, parent)

    def OnButtonClickSuksesOke( self, event ):
        self.Destroy()

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

app = wx.App()
frame = MyBeranda(parent=None)
frame.Show()
app.MainLoop()
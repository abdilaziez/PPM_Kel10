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

        self.Angka1 = 0
        self.Angka2 = 0
        self.Angka3 = 0
        self.Angka4 = 0
        self.Angka5 = 0

    def nambahUkuran1(self, event):
        self.Angka1 += 1
        self.kotakHasil1.SetValue(str(self.Angka1))
    
    def nambahUkuran2(self, event):
        self.Angka2 += 1
        self.kotakHasil2.SetValue(str(self.Angka2))

    def nambahUkuran3(self, event):
        self.Angka3 += 1
        self.kotakHasil3.SetValue(str(self.Angka3))

    def nambahUkuran4(self, event):
        self.Angka4 += 1
        self.kotakHasil4.SetValue(str(self.Angka4))

    def nambahUkuran5(self, event):
        self.Angka5 += 1
        self.kotakHasil5.SetValue(str(self.Angka5))

    def kurangiUkuran1(self, event):
        self.Angka1 -= 1
        if self.Angka1 < 0 :
            self.Angka1 = 0
        self.kotakHasil1.SetValue(str(self.Angka1))

    def kurangiUkuran2(self, event):
        self.Angka2 -= 1
        if self.Angka2 < 0 :
            self.Angka2 = 0
        self.kotakHasil2.SetValue(str(self.Angka2))

    def kurangiUkuran3(self, event):
        self.Angka3 -= 1
        if self.Angka3 < 0 :
            self.Angka3 = 0
        self.kotakHasil3.SetValue(str(self.Angka3))

    def kurangiUkuran4(self, event):
        self.Angka4 -= 1
        if self.Angka4 < 0 :
            self.Angka4 = 0
        self.kotakHasil4.SetValue(str(self.Angka4))

    def kurangiUkuran5(self, event):
        self.Angka5 -= 1
        if self.Angka5 < 0 :
            self.Angka5 = 0
        self.kotakHasil5.SetValue(str(self.Angka5))

    def OnKillFocusJenisMakanan( self, event ):
        self.choice_makanan.Clear()
        dataTipeMakanan = self.tabelJenisMakanan.getIdJenisMakananByNama(self.choice_jenis_makanan.GetString(self.choice_jenis_makanan.GetCurrentSelection()))
        dataMakanan = self.tabelMakanan.getMakananByTipe(dataTipeMakanan)
        for item in dataMakanan:
            self.choice_makanan.Append(item[1])

    def OnButtonClickHitung(self, event):
        dataMakanan = self.tabelMakanan.getMakananByNama(self.choice_makanan.GetString(self.choice_makanan.GetSelection()))
        dataMakanan[2] = self.tabelJenisMakanan.getNamaJenisMakananById(dataMakanan[2])
        for row in range(3, len(dataMakanan)):
            try:
                dataMakanan[row] = dataMakanan[row].replace("gr", "")
                dataMakanan[row] = dataMakanan[row].replace(",", ".")
            except:
                gabut = "gabut"

        porsiDewasa = self.ukuranMassa(dataMakanan[3], self.kotakHasil1.GetValue())
        self.porsiDewasa.SetLabel(porsiDewasa)
        porsiBayi = self.ukuranMassa(dataMakanan[4], self.kotakHasil2.GetValue())
        self.porsiBayi.SetLabel(porsiBayi)
        porsiAnak4 = self.ukuranMassa(dataMakanan[5], self.kotakHasil3.GetValue())
        self.porsiAnak4.SetLabel(porsiAnak4)
        porsiAnak11 = self.ukuranMassa(dataMakanan[6], self.kotakHasil4.GetValue())
        self.porsiAnak11.SetLabel(porsiAnak11)

        hitungSekaliMasak = self.sekaliMasak([porsiDewasa, porsiBayi, porsiAnak4, porsiAnak11])
        self.sekali_masak.SetLabel(hitungSekaliMasak)

        self.sekali_belanja.SetLabel(str(float(hitungSekaliMasak.replace("g", ""))*int(self.kotakHasil5.GetValue())/1000)+"Kg")

    def ukuranMassa(self, value, orang):
        try:
            result = float(value) * int(orang)
        except:
            result = value
        return str(result)

    def sekaliMasak(self, value):
        result = 0
        for i in value:
            try:
                result += float(i)
            except:
                wah="wah"
        return str(result)+"g"


class MyFrameAdmin(ppm.FrameAdmin):
    def __init__(self, parent):
        self.locale = wx.Locale(wx.LANGUAGE_ENGLISH)
        ppm.FrameAdmin.__init__(self, parent)
        self.tabelJenisMakanan = jenisMakanan.JenisMakanan()
        self.tabelMakanan = Makanan.Makanan()
        
        
        dataJenisMakanan = self.tabelJenisMakanan.getJenisMakanan()
        self.listJenisMakanan.AppendRows(len(dataJenisMakanan))
        for column in range (len(dataJenisMakanan[0])):
            row = 0
            for item in dataJenisMakanan:
                self.listJenisMakanan.SetCellValue(row, column, str(item[column]))
                row += 1
        self.listJenisMakanan.AutoSizeColumns()
        self.listJenisMakanan.AutoSizeRows()

        dataMakanan = self.tabelMakanan.getMakanan()
        self.listMakanan.AppendRows(len(dataMakanan))
        for column in range (len(dataMakanan[0])):
            row = 0
            for item in range(len(dataMakanan)):
                try:
                    dataMakanan[item][2] = self.tabelJenisMakanan.getNamaJenisMakananById(dataMakanan[item][2])
                except:
                    gabut = "gabut"
                self.listMakanan.SetCellValue(row, column, str(dataMakanan[item][column]))
                row += 1
        self.listMakanan.AutoSizeColumns()
        self.listMakanan.AutoSizeRows()

    def OnButtonClickSimpan( self, event ):
        jenisMakanan = self.tabelJenisMakanan.getIdJenisMakananByNama(self.in_jenisMakanan.GetValue())
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
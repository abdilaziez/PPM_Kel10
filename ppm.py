# -*- coding: utf-8 -*-

###########################################################################
## Python code generated with wxFormBuilder (version Oct 26 2018)
## http://www.wxformbuilder.org/
##
## PLEASE DO *NOT* EDIT THIS FILE!
###########################################################################

import wx
import wx.xrc
import wx.aui
import wx.grid

###########################################################################
## Class Beranda
###########################################################################

class Beranda ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer26 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap1 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Gambar/PC.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		bSizer26.Add( self.m_bitmap1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer29 = wx.BoxSizer( wx.HORIZONTAL )

		self.goFrameAdmin = wx.Button( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.goFrameAdmin, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.goFramePengguna = wx.Button( self, wx.ID_ANY, u"Pengguna", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer29.Add( self.goFramePengguna, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		bSizer26.Add( bSizer29, 1, wx.ALIGN_CENTER, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.goFrameAdmin.Bind( wx.EVT_BUTTON, self.OnButtonClickFrameAdmin )
		self.goFramePengguna.Bind( wx.EVT_BUTTON, self.OnButtonClickFramePengguna )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnButtonClickFrameAdmin( self, event ):
		event.Skip()

	def OnButtonClickFramePengguna( self, event ):
		event.Skip()


###########################################################################
## Class FramePengguna
###########################################################################

class FramePengguna ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 1100,731 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.Kalkulator_Porsi_Makanan = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self.Kalkulator_Porsi_Makanan, wx.ID_ANY, wx.Point( -1,-1 ), wx.Size( -1,30 ), wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText16 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"KALKULATOR PORSI MAKANAN", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 18, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )

		bSizer21.Add( self.m_staticText16, 0, wx.ALIGN_CENTER|wx.ALL, 50 )


		self.m_panel1.SetSizer( bSizer21 )
		self.m_panel1.Layout()
		bSizer19.Add( self.m_panel1, 0, wx.EXPAND |wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self.Kalkulator_Porsi_Makanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Jenis Makanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		choice_jenis_makananChoices = []
		self.choice_jenis_makanan = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,50 ), choice_jenis_makananChoices, 0 )
		self.choice_jenis_makanan.SetSelection( 0 )
		self.choice_jenis_makanan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.choice_jenis_makanan.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2.Add( self.choice_jenis_makanan, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		choice_makananChoices = []
		self.choice_makanan = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 300,-1 ), choice_makananChoices, 0 )
		self.choice_makanan.SetSelection( 0 )
		self.choice_makanan.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )

		bSizer2.Add( self.choice_makanan, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.m_panel2.SetSizer( bSizer2 )
		self.m_panel2.Layout()
		bSizer2.Fit( self.m_panel2 )
		bSizer19.Add( self.m_panel2, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel3 = wx.Panel( self.Kalkulator_Porsi_Makanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer3 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText5 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Jumlah masakan untuk berapa orang", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		self.m_staticText5.SetFont( wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )

		bSizer3.Add( self.m_staticText5, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer5 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer6 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText9 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Dewasa", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText9.Wrap( -1 )

		bSizer6.Add( self.m_staticText9, 0, wx.ALL|wx.EXPAND, 12 )

		self.m_staticText10 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Bayi (1 - 2 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText10.Wrap( -1 )

		bSizer6.Add( self.m_staticText10, 0, wx.ALL, 12 )

		self.m_staticText11 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Anak - Anak (4 - 10 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText11.Wrap( -1 )

		bSizer6.Add( self.m_staticText11, 0, wx.ALL, 12 )

		self.m_staticText13 = wx.StaticText( self.m_panel3, wx.ID_ANY, u"Anak - Anak (11 - 14 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer6.Add( self.m_staticText13, 0, wx.ALL, 12 )


		bSizer5.Add( bSizer6, 1, wx.EXPAND, 5 )

		bSizer8 = wx.BoxSizer( wx.VERTICAL )

		bSizer9 = wx.BoxSizer( wx.HORIZONTAL )

		self.Tambah1 = wx.Button( self.m_panel3, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer9.Add( self.Tambah1, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.kotakHasil1 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer9.Add( self.kotakHasil1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.Kurang1 = wx.Button( self.m_panel3, wx.ID_ANY, u"-", wx.Point( -1,-1 ), wx.Size( 30,30 ), 0 )
		bSizer9.Add( self.Kurang1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer8.Add( bSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.Tambah2 = wx.Button( self.m_panel3, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer10.Add( self.Tambah2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.kotakHasil2 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer10.Add( self.kotakHasil2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.Kurang2 = wx.Button( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer10.Add( self.Kurang2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer8.Add( bSizer10, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.Tambah3 = wx.Button( self.m_panel3, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer11.Add( self.Tambah3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.kotakHasil3 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer11.Add( self.kotakHasil3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.Kurang3 = wx.Button( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer11.Add( self.Kurang3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer8.Add( bSizer11, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.Tambah4 = wx.Button( self.m_panel3, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer12.Add( self.Tambah4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.kotakHasil4 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer12.Add( self.kotakHasil4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.Kurang4 = wx.Button( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer12.Add( self.Kurang4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer8.Add( bSizer12, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer5.Add( bSizer8, 1, wx.EXPAND, 5 )


		bSizer3.Add( bSizer5, 1, wx.EXPAND, 5 )


		self.m_panel3.SetSizer( bSizer3 )
		self.m_panel3.Layout()
		bSizer3.Fit( self.m_panel3 )
		bSizer19.Add( self.m_panel3, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel4 = wx.Panel( self.Kalkulator_Porsi_Makanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer13 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText14 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Jumlah Konsumsi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText14.Wrap( -1 )

		self.m_staticText14.SetFont( wx.Font( 11, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )

		bSizer13.Add( self.m_staticText14, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer14 = wx.BoxSizer( wx.VERTICAL )

		bSizer15 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer23 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_staticText17 = wx.StaticText( self.m_panel4, wx.ID_ANY, u"Jumlah yang ingin dikonsumsi untuk makanan ini", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText17.Wrap( -1 )

		bSizer23.Add( self.m_staticText17, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 12 )


		bSizer15.Add( bSizer23, 1, wx.EXPAND, 5 )

		bSizer22 = wx.BoxSizer( wx.VERTICAL )

		bSizer24 = wx.BoxSizer( wx.HORIZONTAL )

		self.Tambah5 = wx.Button( self.m_panel4, wx.ID_ANY, u"+", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer24.Add( self.Tambah5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.kotakHasil5 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"0", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer24.Add( self.kotakHasil5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.Kurang5 = wx.Button( self.m_panel4, wx.ID_ANY, u"-", wx.DefaultPosition, wx.Size( 30,30 ), 0 )
		bSizer24.Add( self.Kurang5, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer22.Add( bSizer24, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )


		bSizer15.Add( bSizer22, 1, wx.EXPAND, 5 )


		bSizer14.Add( bSizer15, 1, wx.EXPAND, 5 )

		self.m_button25 = wx.Button( self.m_panel4, wx.ID_ANY, u"Hitung", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_button25.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )
		self.m_button25.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_BACKGROUND ) )
		self.m_button25.SetBackgroundColour( wx.Colour( 255, 255, 255 ) )

		bSizer14.Add( self.m_button25, 0, wx.ALL|wx.EXPAND, 5 )


		bSizer13.Add( bSizer14, 1, wx.EXPAND, 5 )


		self.m_panel4.SetSizer( bSizer13 )
		self.m_panel4.Layout()
		bSizer13.Fit( self.m_panel4 )
		bSizer19.Add( self.m_panel4, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer26.Add( bSizer19, 1, wx.EXPAND, 5 )

		bSizer20 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel7 = wx.Panel( self.Kalkulator_Porsi_Makanan, wx.ID_ANY, wx.DefaultPosition, wx.Size( -1,-1 ), wx.TAB_TRAVERSAL )
		self.m_panel7.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_panel7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText101 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Hasil Kalkulasi:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		bSizer211.Add( self.m_staticText101, 0, wx.ALL, 5 )

		self.namaBuah = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Nama Buah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaBuah.Wrap( -1 )

		self.namaBuah.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer211.Add( self.namaBuah, 0, wx.ALL, 5 )

		bSizer221 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer231 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jumlah yang harus dipersiapkan untuk sekali masak", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer231.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.sekali_masak = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sekali_masak.Wrap( -1 )

		bSizer231.Add( self.sekali_masak, 0, wx.ALL, 5 )


		bSizer221.Add( bSizer231, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText131 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jumlah berat untuk sekali belanja", wx.DefaultPosition, wx.Size( -1,-1 ), 0 )
		self.m_staticText131.Wrap( -1 )

		bSizer25.Add( self.m_staticText131, 0, wx.ALL, 5 )

		self.sekali_belanja = wx.StaticText( self.m_panel7, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sekali_belanja.Wrap( -1 )

		bSizer25.Add( self.sekali_belanja, 0, wx.ALL, 5 )


		bSizer221.Add( bSizer25, 1, wx.EXPAND, 5 )

		bSizer32 = wx.BoxSizer( wx.VERTICAL )


		bSizer221.Add( bSizer32, 1, wx.EXPAND, 5 )


		bSizer211.Add( bSizer221, 1, wx.EXPAND, 5 )

		fgSizer1 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer1.SetFlexibleDirection( wx.BOTH )
		fgSizer1.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText161 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Ukuran Porsi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText161.Wrap( -1 )

		fgSizer1.Add( self.m_staticText161, 0, wx.ALL, 5 )

		self.m_staticText171 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Massa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText171.Wrap( -1 )

		fgSizer1.Add( self.m_staticText171, 0, wx.ALL, 5 )

		self.m_staticText18 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Dewasa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText18.Wrap( -1 )

		fgSizer1.Add( self.m_staticText18, 0, wx.ALL, 5 )

		self.porsiDewasa = wx.StaticText( self.m_panel7, wx.ID_ANY, u"output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.porsiDewasa.Wrap( -1 )

		fgSizer1.Add( self.porsiDewasa, 0, wx.ALL, 5 )

		self.m_staticText19 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Bayi (1 - 2 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText19.Wrap( -1 )

		fgSizer1.Add( self.m_staticText19, 0, wx.ALL, 5 )

		self.porsiBayi = wx.StaticText( self.m_panel7, wx.ID_ANY, u"output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.porsiBayi.Wrap( -1 )

		fgSizer1.Add( self.porsiBayi, 0, wx.ALL, 5 )

		self.m_staticText20 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Anak - Anak (4 - 10 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText20.Wrap( -1 )

		fgSizer1.Add( self.m_staticText20, 0, wx.ALL, 5 )

		self.porsiAnak4 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.porsiAnak4.Wrap( -1 )

		fgSizer1.Add( self.porsiAnak4, 0, wx.ALL, 5 )

		self.m_staticText21 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Anak - Anak (11 - 14 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText21.Wrap( -1 )

		fgSizer1.Add( self.m_staticText21, 0, wx.ALL, 5 )

		self.porsiAnak11 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"output", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.porsiAnak11.Wrap( -1 )

		fgSizer1.Add( self.porsiAnak11, 0, wx.ALL, 5 )


		bSizer211.Add( fgSizer1, 1, wx.EXPAND, 5 )


		self.m_panel7.SetSizer( bSizer211 )
		self.m_panel7.Layout()
		bSizer211.Fit( self.m_panel7 )
		bSizer20.Add( self.m_panel7, 1, wx.EXPAND |wx.ALL, 5 )


		bSizer26.Add( bSizer20, 1, wx.EXPAND, 5 )


		self.Kalkulator_Porsi_Makanan.SetSizer( bSizer26 )
		self.Kalkulator_Porsi_Makanan.Layout()
		bSizer26.Fit( self.Kalkulator_Porsi_Makanan )
		self.m_auinotebook1.AddPage( self.Kalkulator_Porsi_Makanan, u"Kalkulator Porsi Makanan", False, wx.NullBitmap )

		bSizer1.Add( self.m_auinotebook1, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer1 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.choice_jenis_makanan.Bind( wx.EVT_KILL_FOCUS, self.OnKillFocusJenisMakanan )
		self.Tambah1.Bind( wx.EVT_BUTTON, self.nambahUkuran1 )
		self.Kurang1.Bind( wx.EVT_BUTTON, self.kurangiUkuran1 )
		self.Tambah2.Bind( wx.EVT_BUTTON, self.nambahUkuran2 )
		self.Kurang2.Bind( wx.EVT_BUTTON, self.kurangiUkuran2 )
		self.Tambah3.Bind( wx.EVT_BUTTON, self.nambahUkuran3 )
		self.Kurang3.Bind( wx.EVT_BUTTON, self.kurangiUkuran3 )
		self.Tambah4.Bind( wx.EVT_BUTTON, self.nambahUkuran4 )
		self.Kurang4.Bind( wx.EVT_BUTTON, self.kurangiUkuran4 )
		self.Tambah5.Bind( wx.EVT_BUTTON, self.nambahUkuran5 )
		self.Kurang5.Bind( wx.EVT_BUTTON, self.kurangiUkuran5 )
		self.m_button25.Bind( wx.EVT_BUTTON, self.OnButtonClickHitung )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnKillFocusJenisMakanan( self, event ):
		event.Skip()

	def nambahUkuran1( self, event ):
		event.Skip()

	def kurangiUkuran1( self, event ):
		event.Skip()

	def nambahUkuran2( self, event ):
		event.Skip()

	def kurangiUkuran2( self, event ):
		event.Skip()

	def nambahUkuran3( self, event ):
		event.Skip()

	def kurangiUkuran3( self, event ):
		event.Skip()

	def nambahUkuran4( self, event ):
		event.Skip()

	def kurangiUkuran4( self, event ):
		event.Skip()

	def nambahUkuran5( self, event ):
		event.Skip()

	def kurangiUkuran5( self, event ):
		event.Skip()

	def OnButtonClickHitung( self, event ):
		event.Skip()


###########################################################################
## Class FrameAdmin
###########################################################################

class FrameAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,400 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer79 = wx.BoxSizer( wx.VERTICAL )

		self.m_auinotebook4 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.m_panel20 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		fgSizer7 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer7.SetFlexibleDirection( wx.BOTH )
		fgSizer7.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText79 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Jenis Makanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText79.Wrap( -1 )

		fgSizer7.Add( self.m_staticText79, 0, wx.ALL, 5 )

		self.in_jenisMakanan = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.in_jenisMakanan, 0, wx.ALL, 5 )

		self.m_staticText80 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Nama Makanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		fgSizer7.Add( self.m_staticText80, 0, wx.ALL, 5 )

		self.in_namaMakanan = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.in_namaMakanan, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Dewasa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer7.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.in_massaDewasa = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.in_massaDewasa, 0, wx.ALL, 5 )

		self.m_staticText82 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Bayi (1-2 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer7.Add( self.m_staticText82, 0, wx.ALL, 5 )

		self.in_massaBayi = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.in_massaBayi, 0, wx.ALL, 5 )

		self.m_staticText84 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Anak (4-10 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer7.Add( self.m_staticText84, 0, wx.ALL, 5 )

		self.in_massaAnak4 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.in_massaAnak4, 0, wx.ALL, 5 )

		self.m_staticText85 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Anak (11-18 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		fgSizer7.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.in_massaAnak11 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.in_massaAnak11, 0, wx.ALL, 5 )


		fgSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_simpan = wx.Button( self.m_panel20, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.btn_simpan, 0, wx.ALL, 5 )


		self.m_panel20.SetSizer( fgSizer7 )
		self.m_panel20.Layout()
		fgSizer7.Fit( self.m_panel20 )
		self.m_auinotebook4.AddPage( self.m_panel20, u"Tambah data", False, wx.NullBitmap )
		self.m_panel21 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer82 = wx.BoxSizer( wx.VERTICAL )

		self.listJenisMakanan = wx.grid.Grid( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.listJenisMakanan.CreateGrid( 0, 2 )
		self.listJenisMakanan.EnableEditing( True )
		self.listJenisMakanan.EnableGridLines( True )
		self.listJenisMakanan.EnableDragGridSize( False )
		self.listJenisMakanan.SetMargins( 0, 0 )

		# Columns
		self.listJenisMakanan.SetColSize( 0, 142 )
		self.listJenisMakanan.SetColSize( 1, 129 )
		self.listJenisMakanan.EnableDragColMove( False )
		self.listJenisMakanan.EnableDragColSize( True )
		self.listJenisMakanan.SetColLabelSize( 30 )
		self.listJenisMakanan.SetColLabelValue( 0, u"ID Jenis Makanan" )
		self.listJenisMakanan.SetColLabelValue( 1, u"Nama Jenis Makanan" )
		self.listJenisMakanan.SetColLabelValue( 2, wx.EmptyString )
		self.listJenisMakanan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.listJenisMakanan.EnableDragRowSize( True )
		self.listJenisMakanan.SetRowLabelSize( 80 )
		self.listJenisMakanan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.listJenisMakanan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.listJenisMakanan.SetMinSize( wx.Size( 1000,1000 ) )

		bSizer82.Add( self.listJenisMakanan, 0, wx.ALL, 5 )


		self.m_panel21.SetSizer( bSizer82 )
		self.m_panel21.Layout()
		bSizer82.Fit( self.m_panel21 )
		self.m_auinotebook4.AddPage( self.m_panel21, u"Jenis Makanan", False, wx.NullBitmap )
		self.m_panel22 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer83 = wx.BoxSizer( wx.VERTICAL )

		self.listMakanan = wx.grid.Grid( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.listMakanan.CreateGrid( 0, 7 )
		self.listMakanan.EnableEditing( True )
		self.listMakanan.EnableGridLines( True )
		self.listMakanan.EnableDragGridSize( False )
		self.listMakanan.SetMargins( 0, 0 )

		# Columns
		self.listMakanan.SetColSize( 0, 122 )
		self.listMakanan.SetColSize( 1, 126 )
		self.listMakanan.SetColSize( 2, 103 )
		self.listMakanan.SetColSize( 3, 112 )
		self.listMakanan.SetColSize( 4, 80 )
		self.listMakanan.SetColSize( 5, 135 )
		self.listMakanan.SetColSize( 6, 146 )
		self.listMakanan.EnableDragColMove( False )
		self.listMakanan.EnableDragColSize( True )
		self.listMakanan.SetColLabelSize( 30 )
		self.listMakanan.SetColLabelValue( 0, u"ID Makanan" )
		self.listMakanan.SetColLabelValue( 1, u"Nama Makanan" )
		self.listMakanan.SetColLabelValue( 2, u"Tipe Makanan" )
		self.listMakanan.SetColLabelValue( 3, u"Massa Dewasa" )
		self.listMakanan.SetColLabelValue( 4, u"Massa bayi" )
		self.listMakanan.SetColLabelValue( 5, u"Massa Anak 4-8 Tahun" )
		self.listMakanan.SetColLabelValue( 6, u"Massa Anak 11-18 Tahun" )
		self.listMakanan.SetColLabelValue( 7, wx.EmptyString )
		self.listMakanan.SetColLabelValue( 8, wx.EmptyString )
		self.listMakanan.SetColLabelValue( 9, wx.EmptyString )
		self.listMakanan.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.listMakanan.EnableDragRowSize( True )
		self.listMakanan.SetRowLabelSize( 80 )
		self.listMakanan.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.listMakanan.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		self.listMakanan.SetMinSize( wx.Size( -1,1000 ) )

		bSizer83.Add( self.listMakanan, 0, wx.ALL, 5 )


		self.m_panel22.SetSizer( bSizer83 )
		self.m_panel22.Layout()
		bSizer83.Fit( self.m_panel22 )
		self.m_auinotebook4.AddPage( self.m_panel22, u"Semua makanan", True, wx.NullBitmap )

		bSizer79.Add( self.m_auinotebook4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer79 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_simpan.Bind( wx.EVT_BUTTON, self.OnButtonClickSimpan )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnButtonClickSimpan( self, event ):
		event.Skip()


###########################################################################
## Class LoginAdmin
###########################################################################

class LoginAdmin ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 250,300 ), style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		bSizer33 = wx.BoxSizer( wx.VERTICAL )

		self.m_bitmap6 = wx.StaticBitmap( self, wx.ID_ANY, wx.Bitmap( u"Gambar/PC.png", wx.BITMAP_TYPE_ANY ), wx.DefaultPosition, wx.Size( 150,150 ), 0 )
		bSizer33.Add( self.m_bitmap6, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		bSizer36 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer34 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		bSizer34.Add( self.m_staticText26, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer34.Add( self.username, 0, wx.ALL, 5 )


		bSizer36.Add( bSizer34, 1, wx.EXPAND, 5 )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		bSizer35.Add( self.m_staticText27, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		self.password = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.password, 0, wx.ALL, 5 )


		bSizer36.Add( bSizer35, 1, wx.EXPAND, 5 )


		bSizer33.Add( bSizer36, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		fgSizer2.Add( bSizer33, 1, wx.ALIGN_CENTER, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_login = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_login, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_login.Bind( wx.EVT_BUTTON, self.OnButtonClickLogin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnButtonClickLogin( self, event ):
		event.Skip()


###########################################################################
## Class suksesTambah
###########################################################################

class suksesTambah ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer35 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText34 = wx.StaticText( self, wx.ID_ANY, u"Data Sukses di tambahkan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText34.Wrap( -1 )

		bSizer35.Add( self.m_staticText34, 0, wx.ALL, 5 )

		self.btn_suksesoke = wx.Button( self, wx.ID_ANY, u"Oke", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer35.Add( self.btn_suksesoke, 0, wx.ALL, 5 )


		self.SetSizer( bSizer35 )
		self.Layout()
		bSizer35.Fit( self )

		self.Centre( wx.BOTH )

		# Connect Events
		self.btn_suksesoke.Bind( wx.EVT_BUTTON, self.OnButtonClickSuksesOke )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnButtonClickSuksesOke( self, event ):
		event.Skip()



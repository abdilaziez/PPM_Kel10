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

		self.goFramePengguna = wx.Button( self, wx.ID_ANY, u"Pengguna", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.goFramePengguna, 0, wx.ALL, 5 )

		self.goFrameAdmin = wx.Button( self, wx.ID_ANY, u"Admin", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer26.Add( self.goFrameAdmin, 0, wx.ALL, 5 )


		self.SetSizer( bSizer26 )
		self.Layout()

		self.Centre( wx.BOTH )

		# Connect Events
		self.goFramePengguna.Bind( wx.EVT_BUTTON, self.OnButtonClickFramePengguna )
		self.goFrameAdmin.Bind( wx.EVT_BUTTON, self.OnButtonClickFrameAdmin )

	def __del__( self ):
		pass


	# Virtual event handlers, overide them in your derived class
	def OnButtonClickFramePengguna( self, event ):
		event.Skip()

	def OnButtonClickFrameAdmin( self, event ):
		event.Skip()


###########################################################################
## Class FramePengguna
###########################################################################

class FramePengguna ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 914,731 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		bSizer1 = wx.BoxSizer( wx.VERTICAL )

		self.m_auinotebook1 = wx.aui.AuiNotebook( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.aui.AUI_NB_DEFAULT_STYLE )
		self.Kalkulator_Porsi_Makanan = wx.Panel( self.m_auinotebook1, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer26 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer19 = wx.BoxSizer( wx.VERTICAL )

		self.m_panel1 = wx.Panel( self.Kalkulator_Porsi_Makanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer21 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText16 = wx.StaticText( self.m_panel1, wx.ID_ANY, u"KALKULATOR PORSI MAKANAN", wx.Point( -1,-1 ), wx.Size( -1,-1 ), 0 )
		self.m_staticText16.Wrap( -1 )

		self.m_staticText16.SetFont( wx.Font( 18, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, "Courier New" ) )

		bSizer21.Add( self.m_staticText16, 0, wx.ALIGN_CENTER|wx.ALL, 50 )


		self.m_panel1.SetSizer( bSizer21 )
		self.m_panel1.Layout()
		bSizer21.Fit( self.m_panel1 )
		bSizer19.Add( self.m_panel1, 1, wx.EXPAND |wx.ALL, 5 )

		self.m_panel2 = wx.Panel( self.Kalkulator_Porsi_Makanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer2 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText1 = wx.StaticText( self.m_panel2, wx.ID_ANY, u"Jenis Makanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText1.Wrap( -1 )

		self.m_staticText1.SetFont( wx.Font( 10, wx.FONTFAMILY_MODERN, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD, False, wx.EmptyString ) )

		bSizer2.Add( self.m_staticText1, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_choice3Choices = [ u"Buah", u"Sayuran" ]
		self.m_choice3 = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,50 ), m_choice3Choices, 0 )
		self.m_choice3.SetSelection( 0 )
		self.m_choice3.SetForegroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )
		self.m_choice3.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_WINDOW ) )

		bSizer2.Add( self.m_choice3, 0, wx.ALIGN_CENTER|wx.ALL, 5 )

		m_choice4Choices = [ u"Pisang (Sedang)" ]
		self.m_choice4 = wx.Choice( self.m_panel2, wx.ID_ANY, wx.DefaultPosition, wx.Size( 500,-1 ), m_choice4Choices, 0 )
		self.m_choice4.SetSelection( 0 )
		bSizer2.Add( self.m_choice4, 0, wx.ALIGN_CENTER|wx.ALL, 5 )


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

		self.m_button13 = wx.Button( self.m_panel3, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button13, 0, wx.ALL|wx.ALIGN_CENTER_VERTICAL, 5 )

		self.m_textCtrl1 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"2", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer9.Add( self.m_textCtrl1, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button14 = wx.Button( self.m_panel3, wx.ID_ANY, u"-", wx.Point( -1,-1 ), wx.DefaultSize, 0 )
		bSizer9.Add( self.m_button14, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer8.Add( bSizer9, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer10 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button15 = wx.Button( self.m_panel3, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button15, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_textCtrl2 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"1", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer10.Add( self.m_textCtrl2, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button16 = wx.Button( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer10.Add( self.m_button16, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer8.Add( bSizer10, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer11 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button17 = wx.Button( self.m_panel3, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button17, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_textCtrl3 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer11.Add( self.m_textCtrl3, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button18 = wx.Button( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer11.Add( self.m_button18, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


		bSizer8.Add( bSizer11, 1, wx.ALIGN_CENTER_HORIZONTAL, 5 )

		bSizer12 = wx.BoxSizer( wx.HORIZONTAL )

		self.m_button19 = wx.Button( self.m_panel3, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button19, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_textCtrl4 = wx.TextCtrl( self.m_panel3, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer12.Add( self.m_textCtrl4, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button20 = wx.Button( self.m_panel3, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer12.Add( self.m_button20, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


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

		self.m_button22 = wx.Button( self.m_panel4, wx.ID_ANY, u"+", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button22, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_textCtrl6 = wx.TextCtrl( self.m_panel4, wx.ID_ANY, u"3", wx.DefaultPosition, wx.DefaultSize, wx.TE_CENTER )
		bSizer24.Add( self.m_textCtrl6, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )

		self.m_button23 = wx.Button( self.m_panel4, wx.ID_ANY, u"-", wx.DefaultPosition, wx.DefaultSize, 0 )
		bSizer24.Add( self.m_button23, 0, wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5 )


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

		self.m_panel7 = wx.Panel( self.Kalkulator_Porsi_Makanan, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		self.m_panel7.SetBackgroundColour( wx.SystemSettings.GetColour( wx.SYS_COLOUR_GRAYTEXT ) )

		bSizer211 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText101 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Hasil Kalkulasi:", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText101.Wrap( -1 )

		bSizer211.Add( self.m_staticText101, 0, wx.ALL, 5 )

		self.namaBuah = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Nama Buah", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.namaBuah.Wrap( -1 )

		bSizer211.Add( self.namaBuah, 0, wx.ALL, 5 )

		bSizer221 = wx.BoxSizer( wx.HORIZONTAL )

		bSizer231 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText12 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jumlah yang harus dipersiapkan untuk sekali masak", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText12.Wrap( -1 )

		bSizer231.Add( self.m_staticText12, 0, wx.ALL, 5 )

		self.sekali_masak = wx.StaticText( self.m_panel7, wx.ID_ANY, u"gram", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sekali_masak.Wrap( -1 )

		bSizer231.Add( self.sekali_masak, 0, wx.ALL, 5 )


		bSizer221.Add( bSizer231, 1, wx.EXPAND, 5 )

		bSizer25 = wx.BoxSizer( wx.VERTICAL )

		self.m_staticText13 = wx.StaticText( self.m_panel7, wx.ID_ANY, u"Jumlah berat untuk sekali belanja", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText13.Wrap( -1 )

		bSizer25.Add( self.m_staticText13, 0, wx.ALL, 5 )

		self.sekali_belanja = wx.StaticText( self.m_panel7, wx.ID_ANY, u"gram*2", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.sekali_belanja.Wrap( -1 )

		bSizer25.Add( self.sekali_belanja, 0, wx.ALL, 5 )


		bSizer221.Add( bSizer25, 1, wx.EXPAND, 5 )


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

		self.porsiDewasa = wx.StaticText( self.m_panel7, wx.ID_ANY, u"ouput", wx.DefaultPosition, wx.DefaultSize, 0 )
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

	def __del__( self ):
		pass


###########################################################################
## Class FrameAdmin
###########################################################################

class FrameAdmin ( wx.Frame ):

	def __init__( self, parent ):
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.Size( 500,300 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

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

		self.m_textCtrl19 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl19, 0, wx.ALL, 5 )

		self.m_staticText80 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Nama Makanan", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText80.Wrap( -1 )

		fgSizer7.Add( self.m_staticText80, 0, wx.ALL, 5 )

		self.m_textCtrl20 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl20, 0, wx.ALL, 5 )

		self.m_staticText81 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Dewasa", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText81.Wrap( -1 )

		fgSizer7.Add( self.m_staticText81, 0, wx.ALL, 5 )

		self.m_textCtrl18 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl18, 0, wx.ALL, 5 )

		self.m_staticText82 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Bayi", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText82.Wrap( -1 )

		fgSizer7.Add( self.m_staticText82, 0, wx.ALL, 5 )

		self.m_textCtrl21 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl21, 0, wx.ALL, 5 )

		self.m_staticText83 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Anak (1-2 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText83.Wrap( -1 )

		fgSizer7.Add( self.m_staticText83, 0, wx.ALL, 5 )

		self.m_textCtrl22 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl22, 0, wx.ALL, 5 )

		self.m_staticText84 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Anak (4-10 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText84.Wrap( -1 )

		fgSizer7.Add( self.m_staticText84, 0, wx.ALL, 5 )

		self.m_textCtrl23 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl23, 0, wx.ALL, 5 )

		self.m_staticText85 = wx.StaticText( self.m_panel20, wx.ID_ANY, u"Massa Anak (11-18 Tahun)", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText85.Wrap( -1 )

		fgSizer7.Add( self.m_staticText85, 0, wx.ALL, 5 )

		self.m_textCtrl24 = wx.TextCtrl( self.m_panel20, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.m_textCtrl24, 0, wx.ALL, 5 )


		fgSizer7.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_simpan = wx.Button( self.m_panel20, wx.ID_ANY, u"Simpan", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer7.Add( self.btn_simpan, 0, wx.ALL, 5 )


		self.m_panel20.SetSizer( fgSizer7 )
		self.m_panel20.Layout()
		fgSizer7.Fit( self.m_panel20 )
		self.m_auinotebook4.AddPage( self.m_panel20, u"Tambah data", False, wx.NullBitmap )
		self.m_panel21 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer82 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid2 = wx.grid.Grid( self.m_panel21, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid2.CreateGrid( 5, 2 )
		self.m_grid2.EnableEditing( True )
		self.m_grid2.EnableGridLines( True )
		self.m_grid2.EnableDragGridSize( False )
		self.m_grid2.SetMargins( 0, 0 )

		# Columns
		self.m_grid2.EnableDragColMove( False )
		self.m_grid2.EnableDragColSize( True )
		self.m_grid2.SetColLabelSize( 30 )
		self.m_grid2.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid2.EnableDragRowSize( True )
		self.m_grid2.SetRowLabelSize( 80 )
		self.m_grid2.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid2.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer82.Add( self.m_grid2, 0, wx.ALL, 5 )


		self.m_panel21.SetSizer( bSizer82 )
		self.m_panel21.Layout()
		bSizer82.Fit( self.m_panel21 )
		self.m_auinotebook4.AddPage( self.m_panel21, u"Jenis Makanan", False, wx.NullBitmap )
		self.m_panel22 = wx.Panel( self.m_auinotebook4, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		bSizer83 = wx.BoxSizer( wx.VERTICAL )

		self.m_grid3 = wx.grid.Grid( self.m_panel22, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, 0 )

		# Grid
		self.m_grid3.CreateGrid( 5, 7 )
		self.m_grid3.EnableEditing( True )
		self.m_grid3.EnableGridLines( True )
		self.m_grid3.EnableDragGridSize( False )
		self.m_grid3.SetMargins( 0, 0 )

		# Columns
		self.m_grid3.EnableDragColMove( False )
		self.m_grid3.EnableDragColSize( True )
		self.m_grid3.SetColLabelSize( 30 )
		self.m_grid3.SetColLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Rows
		self.m_grid3.EnableDragRowSize( True )
		self.m_grid3.SetRowLabelSize( 80 )
		self.m_grid3.SetRowLabelAlignment( wx.ALIGN_CENTER, wx.ALIGN_CENTER )

		# Label Appearance

		# Cell Defaults
		self.m_grid3.SetDefaultCellAlignment( wx.ALIGN_LEFT, wx.ALIGN_TOP )
		bSizer83.Add( self.m_grid3, 0, wx.ALL, 5 )


		self.m_panel22.SetSizer( bSizer83 )
		self.m_panel22.Layout()
		bSizer83.Fit( self.m_panel22 )
		self.m_auinotebook4.AddPage( self.m_panel22, u"Semua makanan", False, wx.NullBitmap )

		bSizer79.Add( self.m_auinotebook4, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( bSizer79 )
		self.Layout()

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass


###########################################################################
## Class LoginAdmin
###########################################################################

class LoginAdmin ( wx.Dialog ):

	def __init__( self, parent ):
		wx.Dialog.__init__ ( self, parent, id = wx.ID_ANY, title = wx.EmptyString, pos = wx.DefaultPosition, size = wx.DefaultSize, style = wx.DEFAULT_DIALOG_STYLE )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		fgSizer2 = wx.FlexGridSizer( 0, 2, 0, 0 )
		fgSizer2.SetFlexibleDirection( wx.BOTH )
		fgSizer2.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		self.m_staticText26 = wx.StaticText( self, wx.ID_ANY, u"Username", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText26.Wrap( -1 )

		fgSizer2.Add( self.m_staticText26, 0, wx.ALL, 5 )

		self.username1 = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.username1, 0, wx.ALL, 5 )

		self.m_staticText27 = wx.StaticText( self, wx.ID_ANY, u"Password", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText27.Wrap( -1 )

		fgSizer2.Add( self.m_staticText27, 0, wx.ALL, 5 )

		self.username = wx.TextCtrl( self, wx.ID_ANY, wx.EmptyString, wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.username, 0, wx.ALL, 5 )


		fgSizer2.Add( ( 0, 0), 1, wx.EXPAND, 5 )

		self.btn_login = wx.Button( self, wx.ID_ANY, u"Login", wx.DefaultPosition, wx.DefaultSize, 0 )
		fgSizer2.Add( self.btn_login, 0, wx.ALL, 5 )


		self.SetSizer( fgSizer2 )
		self.Layout()
		fgSizer2.Fit( self )

		self.Centre( wx.BOTH )

	def __del__( self ):
		pass



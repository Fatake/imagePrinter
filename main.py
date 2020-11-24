import cv2
import sys
import os
import platform

import wx
import wx.xrc

###########################################################################
## Class PyPhoto
###########################################################################

class PyPhoto ( wx.Frame ):

	def __init__( self, parent ):
		self.WIDTH_PHOTO = 480
		self.HEIGHT_PHOTO = 640
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyPhoto", pos = wx.DefaultPosition, size = wx.Size( 767,827 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainContainer = wx.BoxSizer( wx.VERTICAL )

		self.panelPrincipal = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		contenedor = wx.GridBagSizer( 0, 0 )
		contenedor.SetFlexibleDirection( wx.BOTH )
		contenedor.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

		gSizer1 = wx.GridSizer( 0, 1, 0, 0 )

		self.m_staticText5 = wx.StaticText( self.panelPrincipal, wx.ID_ANY, u"Cantidad de Fotos en Hoja", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_staticText5.Wrap( -1 )

		gSizer1.Add( self.m_staticText5, 0, wx.ALL, 5 )

		self.m_radioBtn1 = wx.RadioButton( self.panelPrincipal, wx.ID_ANY, u"4x4", wx.DefaultPosition, wx.DefaultSize, 0 )
		self.m_radioBtn1.SetValue( True )
		gSizer1.Add( self.m_radioBtn1, 0, wx.ALL, 5 )

		self.m_radioBtn2 = wx.RadioButton( self.panelPrincipal, wx.ID_ANY, u"6x6", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_radioBtn2, 0, wx.ALL, 5 )

		self.m_radioBtn3 = wx.RadioButton( self.panelPrincipal, wx.ID_ANY, u"8x8", wx.DefaultPosition, wx.DefaultSize, 0 )
		gSizer1.Add( self.m_radioBtn3, 0, wx.ALL, 5 )


		contenedor.Add( gSizer1, wx.GBPosition( 0, 4 ), wx.GBSpan( 1, 1 ), wx.ALIGN_RIGHT|wx.RIGHT, 5 )

		self.selectoImagen = wx.FilePickerCtrl( self.panelPrincipal, wx.ID_ANY, u"D:\\Documentos\\programaImagenes\\bob.jpg", u"Seleccione una foto", u"JPG files (*.jpg)|*.jpg|PNG files (*.png)|*.PNG|BMP files (*.bmp)|*.bmp", wx.DefaultPosition, wx.DefaultSize, wx.FLP_CHANGE_DIR|wx.FLP_FILE_MUST_EXIST|wx.FLP_OPEN )
		contenedor.Add( self.selectoImagen, wx.GBPosition( 0, 0 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )

		self.imagenEditar = wx.StaticBitmap( self.panelPrincipal, wx.ID_ANY, wx.NullBitmap, wx.DefaultPosition, wx.Size( 480,640 ), 0 )
		contenedor.Add( self.imagenEditar, wx.GBPosition( 0, 1 ), wx.GBSpan( 1, 1 ), wx.ALL, 5 )


		self.panelPrincipal.SetSizer( contenedor )
		self.panelPrincipal.Layout()
		contenedor.Fit( self.panelPrincipal )
		mainContainer.Add( self.panelPrincipal, 1, wx.EXPAND |wx.ALL, 5 )


		self.SetSizer( mainContainer )
		self.Layout()
		self.menuPrincipal = wx.MenuBar( 0 )
		self.m_menu1 = wx.Menu()
		self.m_menuItem3 = wx.MenuItem( self.m_menu1, wx.ID_ANY, u"MyMenuItem", wx.EmptyString, wx.ITEM_NORMAL )
		self.m_menu1.Append( self.m_menuItem3 )

		self.menuPrincipal.Append( self.m_menu1, u"Archivo" )

		self.imprimir = wx.Menu()
		self.imprime4 = wx.MenuItem( self.imprimir, wx.ID_ANY, u"4x4", wx.EmptyString, wx.ITEM_NORMAL )
		self.imprimir.Append( self.imprime4 )

		self.menuPrincipal.Append( self.imprimir, u"Imprimir" )

		self.SetMenuBar( self.menuPrincipal )


		self.Centre( wx.BOTH )

		# Connect Events
		self.m_radioBtn1.Bind( wx.EVT_RADIOBUTTON, self.change4 )
		self.m_radioBtn2.Bind( wx.EVT_RADIOBUTTON, self.change6 )
		self.m_radioBtn3.Bind( wx.EVT_RADIOBUTTON, self.change8 )
		self.selectoImagen.Bind( wx.EVT_FILEPICKER_CHANGED, self.load )
		self.Bind( wx.EVT_MENU, self.printPrinter, id = self.imprime4.GetId() )

	# Virtual event handlers, overide them in your derived class
	def load( self, event ):
		name = self.selectoImagen.GetPath()
		img = cv2.imread(name, cv2.IMREAD_UNCHANGED)
		himg, wimg, _ = img.shape


		# resize image
		output = cv2.resize(img, (self.WIDTH_PHOTO , self.HEIGHT_PHOTO),interpolation = cv2.INTER_NEAREST)

		cv2.imwrite(name+".jpg",output) 

		print (name)
		self.imagenEditar.Bitmap = wx.Bitmap( name+".jpg", wx.BITMAP_TYPE_ANY )
		self.panelPrincipal.Refresh()
	
	def change4( self, event ):
		event.Skip()

	def change6( self, event ):
		event.Skip()

	def change8( self, event ):
		event.Skip()

	def printPrinter( self, event ):
		event.Skip()

###########################################################################
## Main Program
###########################################################################
def main():
	if os.name == "posix":
		print("\nPlatform : UNIX - Linux")
	elif os.name in ['nt', 'dos', 'ce']:
		print("\nPlatform : Windows")
	else:
		print("\nPlatform : ", platform.system())

	# Genera Aplicación
	app = wx.App()

	# Genera un el Frame principal y le pasa la tabla de empleados
	ex = PyPhoto(None)

	# Muestra el frame principal
	ex.Show()

	# Pone la aplicacion en loop
	app.MainLoop()
    
if __name__ == '__main__':
	main()
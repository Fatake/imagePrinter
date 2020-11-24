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
		wx.Frame.__init__ ( self, parent, id = wx.ID_ANY, title = u"PyPhoto", pos = wx.DefaultPosition, size = wx.Size( 690,747 ), style = wx.DEFAULT_FRAME_STYLE|wx.TAB_TRAVERSAL )

		self.SetSizeHints( wx.DefaultSize, wx.DefaultSize )

		mainContainer = wx.BoxSizer( wx.VERTICAL )
		self.locale = wx.Locale(wx.LANGUAGE_SPANISH_MEXICAN)

		self.panelPrincipal = wx.Panel( self, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize, wx.TAB_TRAVERSAL )
		contenedor = wx.GridBagSizer( 0, 0 )
		contenedor.SetFlexibleDirection( wx.BOTH )
		contenedor.SetNonFlexibleGrowMode( wx.FLEX_GROWMODE_SPECIFIED )

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
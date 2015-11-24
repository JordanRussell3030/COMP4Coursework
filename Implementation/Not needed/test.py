from PyQt4 import QtGui
from PyQt4 import QtCore
import sys

def main():
    
    app 	= QtGui.QApplication(sys.argv)
    w 		= QtGui.QMainWindow()
    palette = QtGui.QPalette()
    
    palette.setColor(QtGui.QPalette.Background,QtCore.Qt.red)
    
    w.setPalette(palette)
    w.resize(250, 150)
    w.move(300, 300)
    w.setWindowTitle('PyQt QMainWindow Background Color')
    w.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()

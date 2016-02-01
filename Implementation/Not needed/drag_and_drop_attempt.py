##        self.layout.addWidget(self.ex)
##
####        self.lineedit = QLineEdit("Yargh")
####        self.lineedit.setReadOnly(True)
####        self.lineedit.setSelection(0, 5)
####        self.lineedit.setDragEnabled(True)
##
####        self.layout.addWidget(self.lineedit, 0, 2)
##
##class Button(QPushButton):
##    def __init__(self, title, parent):
##        super(Button, self).__init__(title, parent)
##
##        self.setAcceptDrops(True)
##
##    def dragEnterEvent(self, e):
##        if e.mimeData().hasFormat("text/plain"):
##            e.accept()
##        else:
##            e.ignore()
##
##    def dropEvent(self, e):
##        self.setText(e.mimeData().text())
##
##    def MouseMoveEvent(self, e):
##        if e.buttons() != Qt.Rightbutton:
##            return
##
##        mime_data = QMimeData()
##
##        drag = QDrag(self)
##        drag.setMimeData(mime_data)
##        drag.setHotSpot(e.pos() - self.rect().topLeft())
##
##        dropAction = drag.start(Qt.MoveAction)
##
##    def MousePressEvent(self, e):
##
##        super(Button, self).MousePressEvent(e)
##
##        if e.button() == Qt.LeftButton:
##            print("Press")
##
##class Example(QWidget):
##    def __init__(self):
##        super(Example, self).__init__()
##
##        self.initUI()
##
##    def initUI(self):
####        self.setAcceptDrops(True)
##        self.button = Button('DownloadMoreRAM', self)
##        self.button.move(190, 65)
####        self.button.setDragEnabled(True)
##        self.edit = QLineEdit("", self)
####        edit.setDragEnabled(True)
##        edit.move(30, 65)
##
##        self.setGeometry(300, 300, 280, 150)
##        self.show()
##
##    def dragEnterEvent(self, e):
##        e.accept()
##
##    def dropEvent(self, e):
##        position = e.pos()
##        self.button.move(position)
##
##        e.setDropAction(Qt.MoveAction)
##        e.accept()

##class DragFromWidget(QDockWidget):
##    def __init__(self, parent = None):
##        super(DragFromWidget, self).__init__(parent = parent)
##        self.layout.addWidget(QLabel("Label"))
##
##    def DragEnterEvent(self, event):
##        print("Success")
##
##    def MousePressEvent(self, event):
##        label = self.childAt(event.pos())
##        if not label:
##            return
##        hotSpot = event.pos() - label.pos()
##        mimeData = QtCore.QMimeData()
##        mimeData.setText(label.text())
##        mimeData.setData("application/x-hotspot", str(hotSpot.x()))
##        pixmap = QtGui.QPixmap(label.size())
##        label.render(pixmap)
##
##        drag = QDrag(self)
##        drag.setMimeData(mimeData)
##        drag.setPixmap(pixmap)
##        drag.setHotSpot(hotspot)
##
##        dropAction = drag.exec_(Qt.CopyAction|Qt.MoveAction, Qt.CopyAction)
##        if dropAction == Qt.MoveAction:
##            label.close()
##
##class DragToWidget(QDockWidget):
##    def __init__(self, parent = None):
##        super(DragToWidget, self).__init__(parent = parent)
##        self.setAcceptDrops(True)
##
##    def DragEnterEvent(self, event):
##        event.accept()
##
##    def DropEvent(self, event):
##        print("{0} was dropped onto me.".format(event))
##
##class SandboxApp(QApplication):
##    def __init__(self, args, kwargs):
##        super(SandboxApp, self).__init__(args)
##        self.main_window = MainWindow()
##        self.main_window.show()
##
##class MainWindow(QMainWindow):
##    def __init__(self, parent = None):
##        super(MainWindow, self).__init__(parent = parent)
##        self.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AnimatedDocks)
##        self.addDockWidget(Qt.LeftDockWidgetArea, DragFromWidget())
##        self.addDockWidget(Qt.RightDockWidget, DragToWidget())

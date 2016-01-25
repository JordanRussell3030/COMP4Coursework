from PyQt4.QtCore import *
from PyQt4.QtGui import *

from homework_widgets import *
from homework_page_2_parent_class import *
from derived_homework_menus import *

class SidesAHOEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("sides easy")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

        self.answer_2.addItem("10")
        self.answer_2.addItem("20")
        self.answer_2.addItem("30")

    def selected_previous(self):
        pass

class DragFromWidget(QDockWidget):
    def __init__(self, parent = None):
        super(DragFromWidget, self).__init__(parent = parent)
        self.layout.addWidget(QLabel("Label"))

    def DragEnterEvent(self, event):
        print("Success")

    def MousePressEvent(self, event):
        label = self.childAt(event.pos())
        if not label:
            return
        hotSpot = event.pos() - label.pos()
        mimeData = QtCore.QMimeData()
        mimeData.setText(label.text())
        mimeData.setData("application/x-hotspot", str(hotSpot.x()))
        pixmap = QtGui.QPixmap(label.size())
        label.render(pixmap)

        drag = QDrag(self)
        drag.setMimeData(mimeData)
        drag.setPixmap(pixmap)
        drag.setHotSpot(hotspot)

        dropAction = drag.exec_(Qt.CopyAction|Qt.MoveAction, Qt.CopyAction)
        if dropAction == Qt.MoveAction:
            label.close()

class DragToWidget(QDockWidget):
    def __init__(self, parent = None):
        super(DragToWidget, self).__init__(parent = parent)
        self.setAcceptDrops(True)

    def DragEnterEvent(self, event):
        event.accept()

    def DropEvent(self, event):
        print("{0} was dropped onto me.".format(event))

class SandboxApp(QApplication):
    def __init__(self, args, kwargs):
        super(SandboxApp, self).__init__(args)
        self.main_window = MainWindow()
        self.main_window.show()

class MainWindow(QMainWindow):
    def __init__(self, parent = None):
        super(MainWindow, self).__init__(parent = parent)
        self.setDockOptions(QMainWindow.AllowNestedDocks|QMainWindow.AnimatedDocks)
        self.addDockWidget(Qt.LeftDockWidgetArea, DragFromWidget())
        self.addDockWidget(Qt.RightDockWidget, DragToWidget())

class SidesAHOMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("sides m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class SidesAHOHardWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("sides hard")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class SOHCAHTOAEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("soh e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class SOHCAHTOAMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("soh m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class SOHCAHTOAHardWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("soh h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class FindingAnglesEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("fa e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class FindingAnglesMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("fa m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class FindingAnglesHardWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("fa h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class InvetedAnglesEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ia e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class InvertedAnglesMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ia m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class InvertedAnglesHardWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ia h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDTrigEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dt e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDTrigMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dt m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDTrigHardWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dt h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTheoremEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("pt e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTheoremMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("pt m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTheoremHardWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("pt h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDPythagorasEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dp e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDPythagorasMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dp m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class ThreeDPythagorasHardWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("3dp h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTrigProblemsEasyWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ptp e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTrigProblemsMediumWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ptp m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class PythagTrigProblemsHardWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("ptp h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class EasySummaryWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("s e")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class MediumSummaryWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("s m")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

class HardSummaryWidget2(HomeworkPage2ParentClass):
    def __init__(self):
        super().__init__()
        self.question_2.setText("Question 2\n_________\n_________")
        self.shape_2.setText("s h")
        self.question_3.setText("Question 3\n_________\n_________")
        self.shape_3.setText("Shape")
        self.question_4.setText("Question 4\n______\n______\n______")

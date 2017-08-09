# -*- coding: utf-8 -*-

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
import sys
from ui_mainwindow import Ui_MainWindow
from programme_for_guoyi import *
from programme_for_gdcw import *
from programme_for_gzcw import *

class MainWindow(QMainWindow, Ui_MainWindow,Programme_guoyi,Programme_gdcw,Programme_gzcw):

    _signal_web=QtCore.pyqtSignal(str)
    _signal_type=QtCore.pyqtSignal(str)
    _signal_buyer=QtCore.pyqtSignal(str)
    _signal_title=QtCore.pyqtSignal(str)
    _signal_filename=QtCore.pyqtSignal(str)
    _signal6=QtCore.pyqtSignal()

    def __init__(self, parent=None):
        super(MainWindow, self).__init__(parent)
        self.setupUi(self)
        # self.action_exit.triggered.connect(self.onExitTriggered)
        # self.action_copy.triggered.connect(self.onCopyTriggered)
        # self.action_paste.triggered.connect(self.onPasteTriggered)
        # self.action_cut.triggered.connect(self.onCutTriggered)

        self.Cancle.clicked.connect(self.close)
        self.leadtoOrcal.clicked.connect(self.setCreatOracl)
        self.creatExcel.clicked.connect(self.setCreatExcel)

        self.guoyiButton.toggled['bool'].connect(self.guoyiWeb)
        self.gdcwButton.toggled['bool'].connect(self.gdcw)
        self.gzcwButton.toggled['bool'].connect(self.gzcw)
        self.zhaobiaoButton.toggled['bool'].connect(self.zhaobiao)
        self.zhongbiaoButton.toggled['bool'].connect(self.zhongbiao)
        self.caigourenText.textEdited['QString'].connect(self.caigouren)
        self.biaotiText.textEdited['QString'].connect(self.biaoti)
        self.filenameText.textEdited['QString'].connect(self.filename)
        # self.lineEdit.textEdited['QString'].connect(self.papercount)
        self.P_title.toggled['bool'].connect(self.gettitle)
        self.P_account.toggled['bool'].connect(self.getaccount)
        self.P_beginningtime.toggled['bool'].connect(self.getbeginningtime)
        self.P_agentCompany.toggled['bool'].connect(self.getagentcompany)
        self.P_link.toggled['bool'].connect(self.getlink)
        self.P_getaccount.toggled['bool'].connect(self.getsellaccount)
        self.P_showtime.toggled['bool'].connect(self.getshowtime)
        self.P_buyer.toggled['bool'].connect(self.getbuyer)

        self._signal_web.connect(self.sin_web)
        self._signal_type.connect(self.sin_type)
        self._signal_buyer.connect(self.sin_buyer)
        self._signal_title.connect(self.sin_title)
        self._signal_filename.connect(self.sin_filename)
        self._signal6.connect(self.sin6)

        


    """
    单项选择——招标网站选择方法
    定义传递的招标网站信号的槽
    定义信号
    """
    def guoyiWeb(self,state):
        if state is True:
            self._signal_web.emit("guoyi")
        else:
            None
    def gdcw(self,state):
        if state is True:
            self._signal_web.emit("gdcw")
        else:
            None
    def gzcw(self,state):
        if state is True:
            self._signal_web.emit("gzcw")
        else:
            None

    def sin_web(self,string):
        print(string)



    """
    单项选择——检索类型选择方法
    定义传递的类型信号的槽
    定义信号
    """
    def zhaobiao(self,state):
        if state is True:
            self._signal_type.emit("招标公告")
        else:
            None    
    def zhongbiao(self,state):
        if state is True:
            self._signal_type.emit("中标公告")
        else:
            None

    def sin_type(self,string):
        print(string)

    """
    填写生成文件
    定义信号
    """
    def filename(self,strtext):
        self._signal_filename.emit(strtext)

    def sin_filename(self,string):
        print(string)

    """
    填写检索关键词
    定义信号
    """    
    def caigouren(self,strtext):
        self._signal_buyer.emit(strtext)
    def biaoti(self,strtext):
        self._signal_title.emit(strtext)

    def sin_buyer(self,string):
        print(string)
    def sin_title(self,string):
        print(string)

    """多选——选择要获取的信息"""
    def gettitle(self,state):
        pass      
    def getaccount(self,state):
        self.state = state
        return self.state         
    def getbeginningtime(self,state):
        self.state = state
        return self.state 
    def getagentcompany(self,state):
        self.state = state
        return self.state 
    def getlink(self,state):
        self.state = state
        return self.state 
    def getsellaccount(self,state):
        self.state = state
        return self.state 
    def getshowtime(self,state):
        self.state = state
        return self.state 
    def getbuyer(self,state):
        self.state = state
        return self.state 

    def setCreatOracl(self):
        pass
    	# QtWidgets.QMessageBox.information(self.creatExcel,"标题","生成Excel成功")
    def setCreatExcel(self):
        self._signal6.emit()

        #     QtWidgets.QMessageBox.information(self.creatExcel,"标题","正在生成Excel")
        # except:
        #     QtWidgets.QMessageBox.information(self.creatExcel,"标题","信息填写错误")

    def sin6(self):
        print("test")



if __name__ == "__main__":   
    app = QtWidgets.QApplication(sys.argv)
    # mainWindow = QMainWindow()
    # ui = Ui_MainWindow()
    # ui.setupUi(mainWindow)
    # mainWindow.show()
    # sys.exit(app.exec_())
    myWindow = MainWindow()
    myWindow.show()
    sys.exit(app.exec_())

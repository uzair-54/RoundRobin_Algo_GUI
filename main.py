from PyQt5 import QtCore, QtGui, QtWidgets
import algo


class Ui_MainWindow(object):

    numberOfProcess = 0
    processNames = []
    burstTime = []
    arrivalTime = []

    def addProcess(self):
        self.numberOfProcess += 1
        self.tableWidget.setRowCount(self.numberOfProcess)
        
        
    def remProcess(self):
        
        self.numberOfProcess -= 1
        self.tableWidget.setRowCount(self.numberOfProcess)
        
    def getDataFromTable(self):
        if self.numberOfProcess != 0:
            for i in range(0,self.numberOfProcess):
                self.processNames.append(self.tableWidget.item(i,0).text())
                self.arrivalTime.append(int(self.tableWidget.item(i,1).text()))
                self.burstTime.append(int(self.tableWidget.item(i,2).text()))
            self.arrangeAccordingToArrival()

    def arrangeAccordingToArrival(self):

        for i in range(0, len(self.arrivalTime)):
            for j in range(i + 1, len(self.arrivalTime)):
                if self.arrivalTime[j] < self.arrivalTime[i]:
                    swap, swap2, swap3 = self.arrivalTime[j], self.burstTime[j], self.processNames[j]
                    self.arrivalTime[j], self.burstTime[j], self.processNames[j] = self.arrivalTime[i], self.burstTime[i], self.processNames[i]
                    self.arrivalTime[i], self.burstTime[i], self.processNames[i] = swap, swap2, swap3

    def putText(self,comp,turn,wait,res):
        
        for i in range(0,self.numberOfProcess):
            self.tableWidget.setItem(i,0,QtWidgets.QTableWidgetItem(str(self.processNames[i])))
            self.tableWidget.setItem(i,1,QtWidgets.QTableWidgetItem(str(self.arrivalTime[i])))
            self.tableWidget.setItem(i,2,QtWidgets.QTableWidgetItem(str(self.burstTime[i])))
            self.tableWidget.setItem(i,3,QtWidgets.QTableWidgetItem(str(comp[i])))
            self.tableWidget.setItem(i,4,QtWidgets.QTableWidgetItem(str(turn[i])))
            self.tableWidget.setItem(i,5,QtWidgets.QTableWidgetItem(str(wait[i])))
            self.tableWidget.setItem(i,6,QtWidgets.QTableWidgetItem(str(res[i])))

    def getNOfSpace(self,num):
        spaces = ""
        for i in range(0,num):
            spaces = spaces + " "
        return spaces

    def printSeq(self,listSeq):
        seq1 = ""
        time = "0"
        for x in range(0, len(listSeq)):
            lenOfName = len(self.processNames[listSeq[x][0]])
            # print(lenOfName)
            space = self.getNOfSpace(lenOfName//2)

            seq1 = seq1 + "|" + space + str(self.processNames[listSeq[x][0]]) + space
            
            spaceForTime = self.getNOfSpace(len(space)*2 + len(str(self.processNames[listSeq[x][0]])))
            if listSeq[x][1] < 10:
                time = time + spaceForTime+" " + str(listSeq[x][1])
            else:
                time = time + spaceForTime+" "  + str(listSeq[x][1])
        
        seq1 = seq1 + "|\n"
        seq1 = seq1 + time
        return seq1

    def cal(self):
        self.getDataFromTable()
        self.arrangeAccordingToArrival()

        avgTatTime, avgWaitTime, comT, tat, wt, seq, resTime = algo.findavgTime(self.processNames,self.numberOfProcess,self.burstTime,2,self.arrivalTime)
        self.avgWt.setText("Average Waiting time: " + str(round(avgWaitTime,2)))
        self.avgTat.setText("Average Turn-Around time: " + str(round(avgTatTime,2)))
        self.putText(comT,tat,wt,resTime)
        chart = self.printSeq(seq)
        self.textEdit.setText(chart)
        self.textEdit.setReadOnly(True)
        self.textEdit.selectAll()
        self.textEdit.setFontPointSize(14)
        self.arrivalTime = []
        self.processNames = []
        self.burstTime = []
        

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1183, 837)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(0, 10, 1181, 131))
        self.label.setAlignment(QtCore.Qt.AlignCenter)
        self.label.setObjectName("label")
        self.addProc = QtWidgets.QPushButton(self.centralwidget)
        self.addProc.setGeometry(QtCore.QRect(10, 260, 161, 51))
        self.addProc.setObjectName("addProc")
        self.addProc.clicked.connect(self.addProcess)
        self.remProc = QtWidgets.QPushButton(self.centralwidget)
        self.remProc.setGeometry(QtCore.QRect(10, 330, 161, 51))
        self.remProc.setObjectName("remProc")
        self.remProc.clicked.connect(self.remProcess)
        self.tableWidget = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget.setGeometry(QtCore.QRect(180, 190, 991, 331))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(7)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, item)
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 640, 1151, 87))
        self.textEdit.setObjectName("textEdit")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1183, 26))
        self.menubar.setObjectName("menubar")
        self.calculate = QtWidgets.QPushButton(self.centralwidget)
        self.calculate.setGeometry(QtCore.QRect(10, 400, 161, 51))
        self.calculate.setObjectName("calculate")
        self.calculate.clicked.connect(self.cal)
        self.avgWt = QtWidgets.QLabel(self.centralwidget)
        self.avgWt.setGeometry(QtCore.QRect(180, 530, 331, 51))
        self.avgWt.setText("")
        self.avgWt.setAlignment(QtCore.Qt.AlignCenter)
        self.avgWt.setObjectName("avgWt")
        self.avgTat = QtWidgets.QLabel(self.centralwidget)
        self.avgTat.setGeometry(QtCore.QRect(840, 530, 331, 51))
        self.avgTat.setText("")
        self.avgTat.setAlignment(QtCore.Qt.AlignCenter)
        self.avgTat.setObjectName("avgTat")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Round Robin"))
        self.addProc.setText(_translate("MainWindow", "Add process"))
        self.remProc.setText(_translate("MainWindow", "Remove Process"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Process"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Arrival Time"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Burst TIme"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Completion Time"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "Turn-Around Time"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "Waiting Time"))
        item = self.tableWidget.horizontalHeaderItem(6)
        item.setText(_translate("MainWindow", "Response Time"))
        self.calculate.setText(_translate("MainWindow", "Calculate"))
        self.label.setFont(QtGui.QFont("Times",24))
        self.avgTat.setFont(QtGui.QFont("Times",12))
        self.avgWt.setFont(QtGui.QFont("Times",12))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())

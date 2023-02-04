import sys

from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *

class main_window(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle('Al-Kindi')
        self.setFixedSize(QSize(340, 200))
        self.setWindowIcon(QIcon(r"icos\app-ico.png"))
        self.setCentralWidget(tabdemo())


class tabdemo(QTabWidget):
    def __init__(self):
        super().__init__()
        self.addTab(Window1(), 'Convertor 1')
        self.addTab(Window12(), 'Convertor 2')
        self.addTab(Window2(), 'Ciphering')


class Window1(QWidget):
    def __init__(self):    
        super().__init__()
        layout_V = QVBoxLayout()
        layout_1 = QHBoxLayout()
        layout_2 = QHBoxLayout()

        image_1 = QLabel()
        image_1.setPixmap(QPixmap("icos\wall.jpeg"))
        image_1.setFixedHeight(90)
        layout_V.addWidget(image_1)

        Font = QFont()
        Font.setPointSize(13)

        self.edit_1 = QLineEdit()
        self.edit_1.setFont(Font)
        self.edit_1.setMinimumSize(250, 10)
        self.edit_1.setValidator(QIntValidator())
        self.edit_1.setStyleSheet("selection-background-color: #FFB90F;")
        layout_1.addWidget(self.edit_1)
        self.edit_1.textChanged.connect(self.tc)
    

        self.box_1 = QComboBox()
        self.box_1.setFont(Font)
        self.box_1.setMinimumSize(60, 10)
        self.box_1.addItems(['BIN', 'OCT', 'DEC', 'HEX'])
        self.box_1.setStyleSheet("selection-background-color: #FFB90F;")
        layout_1.addWidget(self.box_1)
        self.box_1.textActivated.connect(self.ch_1)
    
    
        self.box_2 = QComboBox()
        self.box_2.setFont(Font)
        self.box_2.setMinimumSize(60, 10)
        self.box_2.addItems(['OCT', 'DEC', 'HEX'])
        self.box_2.setStyleSheet("selection-background-color: #FFB90F;")
        layout_2.addWidget(self.box_2)
    
        self.edit_2 = QLineEdit()
        self.edit_2.setFont(Font)
        self.edit_2.setMinimumSize(250, 10)
        self.edit_2.setStyleSheet("selection-background-color: #FFB90F;")
        self.edit_2.setReadOnly(True)
        layout_2.addWidget(self.edit_2)
    
        layout_V.addLayout(layout_1)
        layout_V.addLayout(layout_2)
        
        self.setLayout(layout_V) 
        
    def ch_1(self, oi):
        if oi == 'BIN':
            self.edit_1.clear()
            self.box_2.clear()
            self.box_2.addItems(['OCT', 'DEC', 'HEX'])
        elif oi == 'HEX':
            self.edit_1.clear()
            self.edit_1.setValidator(QRegExpValidator())
            self.box_2.clear()
            self.box_2.addItems(['BIN', 'OCT', 'DEC'])
        elif oi == 'OCT':
            self.edit_1.clear()
            self.box_2.clear()
            self.box_2.addItems(['BIN', 'DEC', 'HEX'])
        elif oi == 'DEC':
            self.edit_1.clear()
            self.box_2.clear()
            self.box_2.addItems(['BIN', 'OCT', 'HEX'])


    def tc(self, UI):
            self.edit_2.setStyleSheet("selection-background-color: #FFB90F; background-color: white;")
            if self.box_1.currentText()=='DEC' and self.box_2.currentText()=='BIN':
                if UI=='':
                    NUM=0
                else:
                    NUM=int(UI)
                I=0
                BIN=0
                while NUM>0:
                    if (divmod(NUM,2))[1]==1:
                        BIN=BIN+10**(I)
                    I+=1
                    NUM=(divmod(NUM,2))[0]
                self.edit_2.setText(str(BIN))

            if self.box_1.currentText()=='DEC' and self.box_2.currentText()=='OCT':
                if UI=='':
                    NUM=0
                else:
                    NUM=int(UI)
                I=0
                OCT=0
                while NUM>0:
                    OCT=OCT+(divmod(NUM,8))[1]*(10**(I))
                    I+=1
                    NUM=(divmod(NUM,8))[0]
                self.edit_2.setText(str(OCT))

            if self.box_1.currentText()=='DEC' and self.box_2.currentText()=='HEX':
                if UI=='':
                    NUM=0
                else:
                    NUM=int(UI)
                I=0
                HEX=''
                while NUM>0:
                    if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                        HEX=str((divmod(NUM,16))[1])+str(HEX)
                    elif divmod(NUM,16)[1] == 10:
                        HEX='A'+str(HEX)   
                    elif divmod(NUM,16)[1] == 11:
                        HEX='B'+str(HEX)
                    elif divmod(NUM,16)[1] == 12:
                        HEX='C'+str(HEX)
                    elif divmod(NUM,16)[1] == 13:
                        HEX='D'+str(HEX)
                    elif divmod(NUM,16)[1] == 14:
                        HEX='E'+str(HEX)
                    elif divmod(NUM,16)[1] == 15:
                        HEX='F'+str(HEX)
                    I+=1
                    NUM=(divmod(NUM,16))[0]
                self.edit_2.setText(str(HEX))
            
            if self.box_1.currentText()=='BIN' and self.box_2.currentText()=='DEC':
                if UI=='':
                    self.edit_2.clear()
                    NUM=0
                else:
                    if len(UI) <= 1:
                        if int(UI) > 1:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+(divmod(NUM,2))[1]*(2**(I))
                                I+=1
                                NUM=(divmod(NUM,10))[0]
                            self.edit_2.setText(str(DEC))




                    elif len(UI) > 1:
                        if int(UI)%10 > 1:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+(divmod(NUM,2))[1]*(2**(I))
                                I+=1
                                NUM=(divmod(NUM,10))[0]
                            self.edit_2.setText(str(DEC))

            if self.box_1.currentText()=='BIN' and self.box_2.currentText()=='OCT':
                if UI=='':
                    self.edit_2.clear()
                    NUM=0
                else:
                    if len(UI) <= 1:
                        if int(UI) > 1:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+(divmod(NUM,2))[1]*(2**(I))
                                I+=1
                                NUM=(divmod(NUM,10))[0]
                            NUM=DEC
                            I=0
                            OCT=0
                            while NUM>0:
                                OCT=OCT+(divmod(NUM,8))[1]*(10**(I))
                                I+=1
                                NUM=(divmod(NUM,8))[0]
                            self.edit_2.setText(str(OCT))




                    elif len(UI) > 1:
                        if int(UI)%10 > 1:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+(divmod(NUM,2))[1]*(2**(I))
                                I+=1
                                NUM=(divmod(NUM,10))[0]
                            NUM=DEC
                            I=0
                            OCT=0
                            while NUM>0:
                                OCT=OCT+(divmod(NUM,8))[1]*(10**(I))
                                I+=1
                                NUM=(divmod(NUM,8))[0]
                            self.edit_2.setText(str(OCT))

            if self.box_1.currentText()=='BIN' and self.box_2.currentText()=='HEX':
                if UI=='':
                    self.edit_2.clear()
                    NUM=0
                else:
                    if len(UI) <= 1:
                        if int(UI) > 1:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+(divmod(NUM,2))[1]*(2**(I))
                                I+=1
                                NUM=(divmod(NUM,10))[0]
                            NUM=DEC
                            I=0
                            HEX=''
                            while NUM>0:
                                if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                                    HEX=str((divmod(NUM,16))[1])+str(HEX)
                                elif divmod(NUM,16)[1] == 10:
                                    HEX='A'+str(HEX)   
                                elif divmod(NUM,16)[1] == 11:
                                    HEX='B'+str(HEX)
                                elif divmod(NUM,16)[1] == 12:
                                    HEX='C'+str(HEX)
                                elif divmod(NUM,16)[1] == 13:
                                    HEX='D'+str(HEX)
                                elif divmod(NUM,16)[1] == 14:
                                    HEX='E'+str(HEX)
                                elif divmod(NUM,16)[1] == 15:
                                    HEX='F'+str(HEX)
                                I+=1
                                NUM=(divmod(NUM,16))[0]
                            self.edit_2.setText(str(HEX))
                            




                    elif len(UI) > 1:
                        if int(UI)%10 > 1:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+(divmod(NUM,2))[1]*(2**(I))
                                I+=1
                                NUM=(divmod(NUM,10))[0]
                            NUM=DEC
                            I=0
                            HEX=''
                            while NUM>0:
                                if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                                    HEX=str((divmod(NUM,16))[1])+str(HEX)
                                elif divmod(NUM,16)[1] == 10:
                                    HEX='A'+str(HEX)   
                                elif divmod(NUM,16)[1] == 11:
                                    HEX='B'+str(HEX)
                                elif divmod(NUM,16)[1] == 12:
                                    HEX='C'+str(HEX)
                                elif divmod(NUM,16)[1] == 13:
                                    HEX='D'+str(HEX)
                                elif divmod(NUM,16)[1] == 14:
                                    HEX='E'+str(HEX)
                                elif divmod(NUM,16)[1] == 15:
                                    HEX='F'+str(HEX)
                                I+=1
                                NUM=(divmod(NUM,16))[0]
                            self.edit_2.setText(str(HEX))
                            
            if self.box_1.currentText()=='OCT' and self.box_2.currentText()=='DEC':
                if UI=='':
                    self.edit_2.clear()
                    NUM=0
                else:
                    if len(UI) <= 1:
                        if int(UI) > 7:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+NUM%10*(8**(I))
                                I+=1
                                NUM=NUM//10
                            self.edit_2.setText(str(DEC))

                    elif len(UI) > 1:
                        if int(UI)%10 > 7:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+NUM%10*(8**(I))
                                I+=1
                                NUM=NUM//10
                            self.edit_2.setText(str(DEC))
                
            if self.box_1.currentText()=='OCT' and self.box_2.currentText()=='BIN':
                if UI=='':
                    self.edit_2.clear()
                    NUM=0
                else:
                    if len(UI) <= 1:
                        if int(UI) > 7:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+NUM%10*(8**(I))
                                I+=1
                                NUM=NUM//10
                            NUM=DEC
                            I=0
                            BIN=0
                            while NUM>0:
                                if (divmod(NUM,2))[1]==1:
                                    BIN=BIN+10**(I)
                                I+=1
                                NUM=(divmod(NUM,2))[0]
                            self.edit_2.setText(str(BIN))
   
                    elif len(UI) > 1:
                        if int(UI)%10 > 7:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+NUM%10*(8**(I))
                                I+=1
                                NUM=NUM//10
                            NUM=DEC
                            I=0
                            BIN=0
                            while NUM>0:
                                if (divmod(NUM,2))[1]==1:
                                    BIN=BIN+10**(I)
                                I+=1
                                NUM=(divmod(NUM,2))[0]
                            self.edit_2.setText(str(BIN))
                
            if self.box_1.currentText()=='OCT' and self.box_2.currentText()=='HEX':
                if UI=='':
                    self.edit_2.clear()
                    NUM=0
                else:
                    if len(UI) <= 1:
                        if int(UI) > 7:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+NUM%10*(8**(I))
                                I+=1
                                NUM=NUM//10
                            NUM=DEC
                            I=0
                            HEX=''
                            while NUM>0:
                                if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                                    HEX=str((divmod(NUM,16))[1])+str(HEX)
                                elif divmod(NUM,16)[1] == 10:
                                    HEX='A'+str(HEX)   
                                elif divmod(NUM,16)[1] == 11:
                                    HEX='B'+str(HEX)
                                elif divmod(NUM,16)[1] == 12:
                                    HEX='C'+str(HEX)
                                elif divmod(NUM,16)[1] == 13:
                                    HEX='D'+str(HEX)
                                elif divmod(NUM,16)[1] == 14:
                                    HEX='E'+str(HEX)
                                elif divmod(NUM,16)[1] == 15:
                                    HEX='F'+str(HEX)
                                I+=1
                                NUM=(divmod(NUM,16))[0]
                            self.edit_2.setText(str(HEX))
                            
   
                    elif len(UI) > 1:
                        if int(UI)%10 > 7:
                            self.edit_1.clear()
                            self.edit_2.setStyleSheet("color:white; background-color: red;")
                            self.edit_2.setText('ERROR')
                        else:
                            NUM=int(UI)
                            I=0
                            DEC=0
                            while NUM>0:
                                DEC=DEC+NUM%10*(8**(I))
                                I+=1
                                NUM=NUM//10
                            NUM=DEC
                            I=0
                            HEX=''
                            while NUM>0:
                                if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                                    HEX=str((divmod(NUM,16))[1])+str(HEX)
                                elif divmod(NUM,16)[1] == 10:
                                    HEX='A'+str(HEX)   
                                elif divmod(NUM,16)[1] == 11:
                                    HEX='B'+str(HEX)
                                elif divmod(NUM,16)[1] == 12:
                                    HEX='C'+str(HEX)
                                elif divmod(NUM,16)[1] == 13:
                                    HEX='D'+str(HEX)
                                elif divmod(NUM,16)[1] == 14:
                                    HEX='E'+str(HEX)
                                elif divmod(NUM,16)[1] == 15:
                                    HEX='F'+str(HEX)
                                I+=1
                                NUM=(divmod(NUM,16))[0]
                            self.edit_2.setText(str(HEX))
                      
            if self.box_1.currentText()=='HEX' and self.box_2.currentText()=='DEC':
                UI=UI.upper()
                if UI=='':
                    self.edit_2.setText('0')
                else:    
                    h=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C' ,'D' ,'E' ,'F']
                    if not UI[len(UI)-1] in h:
                        self.edit_1.clear()
                        self.edit_2.setStyleSheet("color:white; background-color: red;")
                        self.edit_2.setText('ERROR')
                    else:
                        UI = list(UI)
                        UI.reverse()
                        DEC = 0
                        for i in range(0, len(UI)):
                            match UI[i]:
                                case '0': UI[i] = 0
                                case '1': UI[i] = 1
                                case '2': UI[i] = 2
                                case '3': UI[i] = 3
                                case '4': UI[i] = 4
                                case '5': UI[i] = 5
                                case '6': UI[i] = 6
                                case '7': UI[i] = 7
                                case '8': UI[i] = 8
                                case '9': UI[i] = 9
                                case 'A': UI[i] = 10
                                case 'B': UI[i] = 11
                                case 'C': UI[i] = 12
                                case 'D': UI[i] = 13
                                case 'E': UI[i] = 14
                                case 'F': UI[i] = 15
                            DEC = DEC + (int(UI[i])*(16**i))
                        self.edit_2.setText(str(DEC))
                        
            if self.box_1.currentText()=='HEX' and self.box_2.currentText()=='BIN':
                UI=UI.upper()
                if UI=='':
                    self.edit_2.setText('0')
                else:    
                    h=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C' ,'D' ,'E' ,'F']
                    if not UI[len(UI)-1] in h:
                        self.edit_1.clear()
                        self.edit_2.setStyleSheet("color:white; background-color: red;")
                        self.edit_2.setText('ERROR')
                    else:
                        UI = list(UI)
                        UI.reverse()
                        DEC = 0
                        for i in range(0, len(UI)):
                            match UI[i]:
                                case '0': UI[i] = 0
                                case '1': UI[i] = 1
                                case '2': UI[i] = 2
                                case '3': UI[i] = 3
                                case '4': UI[i] = 4
                                case '5': UI[i] = 5
                                case '6': UI[i] = 6
                                case '7': UI[i] = 7
                                case '8': UI[i] = 8
                                case '9': UI[i] = 9
                                case 'A': UI[i] = 10
                                case 'B': UI[i] = 11
                                case 'C': UI[i] = 12
                                case 'D': UI[i] = 13
                                case 'E': UI[i] = 14
                                case 'F': UI[i] = 15
                            DEC = DEC + (int(UI[i])*(16**i))
                        NUM=DEC
                        I=0
                        BIN=0
                        while NUM>0:
                            if (divmod(NUM,2))[1]==1:
                                BIN=BIN+10**(I)
                            I+=1
                            NUM=(divmod(NUM,2))[0]
                        self.edit_2.setText(str(BIN))

            if self.box_1.currentText()=='HEX' and self.box_2.currentText()=='OCT':
                UI=UI.upper()
                if UI=='':
                    self.edit_2.setText('0')
                else:    
                    h=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C' ,'D' ,'E' ,'F']
                    if not UI[len(UI)-1] in h:
                        self.edit_1.clear()
                        self.edit_2.setStyleSheet("color:white; background-color: red;")
                        self.edit_2.setText('ERROR')
                    else:
                        UI = list(UI)
                        UI.reverse()
                        DEC = 0
                        for i in range(0, len(UI)):
                            match UI[i]:
                                case '0': UI[i] = 0
                                case '1': UI[i] = 1
                                case '2': UI[i] = 2
                                case '3': UI[i] = 3
                                case '4': UI[i] = 4
                                case '5': UI[i] = 5
                                case '6': UI[i] = 6
                                case '7': UI[i] = 7
                                case '8': UI[i] = 8
                                case '9': UI[i] = 9
                                case 'A': UI[i] = 10
                                case 'B': UI[i] = 11
                                case 'C': UI[i] = 12
                                case 'D': UI[i] = 13
                                case 'E': UI[i] = 14
                                case 'F': UI[i] = 15
                            DEC = DEC + (int(UI[i])*(16**i))
                        NUM=DEC
                        I=0
                        OCT=0
                        while NUM>0:
                            OCT=OCT+(divmod(NUM,8))[1]*(10**(I))
                            I+=1
                            NUM=(divmod(NUM,8))[0]
                        self.edit_2.setText(str(OCT))           


class Window12(QWidget):
    def __init__(self):
        super().__init__()
        layout_11 = QVBoxLayout()
        layout_12 = QHBoxLayout()
        self.l1 = QLabel('Numeric Base:')
        layout_11.addWidget(self.l1)

        Font11 = QFont()
        Font11.setPointSize(14)

        self.BINr = QRadioButton("BIN")
        self.BINr.clicked.connect(self.UCB)
        self.OCTr = QRadioButton("OCT")
        self.OCTr.clicked.connect(self.UCO)
        self.DECr = QRadioButton("DEC")
        self.DECr.clicked.connect(self.UCD)
        self.HEXr = QRadioButton("HEX")
        self.HEXr.clicked.connect(self.UCH)
        layout_12.addWidget(self.BINr)
        layout_12.addWidget(self.OCTr)
        layout_12.addWidget(self.DECr)
        layout_12.addWidget(self.HEXr)
        layout_11.addLayout(layout_12)


        layout_a = QHBoxLayout()
        self.la = QLabel('Input:')
        self.la.setFont(Font11)
        self.ea = QLineEdit()
        self.ea.setFont(Font11)
        self.ea.setValidator(QIntValidator())
        self.ea.setStyleSheet("selection-background-color: #FFB90F;")
        layout_a.addWidget(self.la)
        layout_a.addWidget(self.ea)
        layout_11.addLayout(layout_a)
        layout_11.addStretch()
        layout_11.addStretch()
        self.ea.textChanged.connect(self.UI0)

        layout_b = QHBoxLayout()
        self.lb = QLabel('###')
        layout_b.addWidget(self.lb)
        self.eb = QLineEdit()
        self.eb.setReadOnly(True)
        self.eb.setFixedSize(QSize(285, 20))
        layout_b.addWidget(self.eb)
        layout_11.addLayout(layout_b)

        layout_c = QHBoxLayout()
        self.lc = QLabel('###')
        layout_c.addWidget(self.lc)
        self.ec = QLineEdit()
        self.ec.setReadOnly(True)
        self.ec.setFixedSize(QSize(285, 20))
        layout_c.addWidget(self.ec)
        layout_11.addLayout(layout_c)

        layout_d = QHBoxLayout()
        self.ld = QLabel('###')
        layout_d.addWidget(self.ld)
        self.ed = QLineEdit()
        self.ed.setReadOnly(True)
        self.ed.setFixedSize(QSize(285, 20))
        layout_d.addWidget(self.ed)
        layout_11.addLayout(layout_d)

        self.setLayout(layout_11)

    def UCB(self, ucb):
        if ucb == True:
            self.ea.clear()
            self.eb.clear()
            self.ec.clear()
            self.ed.clear()
            self.lb.setText('OCT:')
            self.lc.setText('DEC:')
            self.ld.setText('HEX:')      
    def UCO(self, uco):
        if uco == True:
            self.ea.clear()
            self.eb.clear()
            self.ec.clear()
            self.ed.clear()
            self.lb.setText('BIN:')
            self.lc.setText('DEC:')
            self.ld.setText('HEX:')
    def UCD(self, ucd):
        if ucd == True:
            self.ea.clear()
            self.eb.clear()
            self.ec.clear()
            self.ed.clear()
            self.lb.setText('BIN:')
            self.lc.setText('OCT:')
            self.ld.setText('HEX:')
    def UCH(self, uch):
        if uch == True:
            self.ea.clear()
            self.ea.setValidator(QRegExpValidator())
            self.eb.clear()
            self.ec.clear()
            self.ed.clear()
            self.lb.setText('BIN:')
            self.lc.setText('OCT:')
            self.ld.setText('DEC:')


    def UI0(self, oii):
        Font12 = QFont()
        Font12.setPointSize(13)
        self.eb.setStyleSheet("selection-background-color: #FFB90F; background-color: white;")
        self.eb.setFont(Font12)
        self.ec.setStyleSheet("selection-background-color: #FFB90F; background-color: white;")
        self.ec.setFont(Font12)
        self.ed.setStyleSheet("selection-background-color: #FFB90F; background-color: white;")
        self.ed.setFont(Font12)
        
        if self.BINr.isChecked():
            if oii=='':
                self.eb.clear()
                self.ec.clear()
                self.ed.clear()
                NUM=0
            else:
                if len(oii) <= 1:
                    if int(oii) > 1:
                        self.ea.clear()
                        self.eb.setStyleSheet("color:white; background-color: red;")
                        self.eb.setText('ERROR')
                        self.ec.setStyleSheet("color:white; background-color: red;")
                        self.ec.setText('ERROR')
                        self.ed.setStyleSheet("color:white; background-color: red;")
                        self.ed.setText('ERROR')
                    else:
                        NUM=int(oii)
                        I=0
                        self.ec.setText(oii)
                        DEC=0
                        while NUM>0:
                            DEC=DEC+(divmod(NUM,2))[1]*(2**(I))
                            I+=1
                            NUM=(divmod(NUM,10))[0]
                        NUM=DEC
                        NUM8=DEC
                        I=0
                        if NUM == 0:
                            HEX='0'
                        else:
                            HEX=''
                            while NUM>0:
                                if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                                    HEX=str((divmod(NUM,16))[1])+str(HEX)
                                elif divmod(NUM,16)[1] == 10:
                                    HEX='A'+str(HEX)   
                                elif divmod(NUM,16)[1] == 11:
                                    HEX='B'+str(HEX)
                                elif divmod(NUM,16)[1] == 12:
                                    HEX='C'+str(HEX)
                                elif divmod(NUM,16)[1] == 13:
                                    HEX='D'+str(HEX)
                                elif divmod(NUM,16)[1] == 14:
                                    HEX='E'+str(HEX)
                                elif divmod(NUM,16)[1] == 15:
                                    HEX='F'+str(HEX)
                                I+=1
                                NUM=(divmod(NUM,16))[0]
                        I=0
                        OCT=0
                        while NUM8>0:
                            OCT=OCT+(divmod(NUM8,8))[1]*(10**(I))
                            I+=1
                            NUM8=(divmod(NUM8,8))[0]
                        self.eb.setText(str(OCT))
                        self.ed.setText(str(HEX))




                elif len(oii) > 1:
                    if int(oii)%10 > 1:
                        self.ea.clear()
                        self.eb.setStyleSheet("color:white; background-color: red;")
                        self.eb.setText('ERROR')
                        self.ec.setStyleSheet("color:white; background-color: red;")
                        self.ec.setText('ERROR')
                        self.ed.setStyleSheet("color:white; background-color: red;")
                        self.ed.setText('ERROR')
                    else:
                        NUM=int(oii)
                        I=0
                        DEC=0
                        while NUM>0:
                            DEC=DEC+(divmod(NUM,2))[1]*(2**(I))
                            I+=1
                            NUM=(divmod(NUM,10))[0]
                        NUM=DEC
                        NUM8=DEC
                        self.ec.setText(str(DEC))
                        I=0
                        if NUM == 0:
                            HEX='0'
                        else:
                            HEX=''
                            while NUM>0:
                                if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                                    HEX=str((divmod(NUM,16))[1])+str(HEX)
                                elif divmod(NUM,16)[1] == 10:
                                    HEX='A'+str(HEX)   
                                elif divmod(NUM,16)[1] == 11:
                                    HEX='B'+str(HEX)
                                elif divmod(NUM,16)[1] == 12:
                                    HEX='C'+str(HEX)
                                elif divmod(NUM,16)[1] == 13:
                                    HEX='D'+str(HEX)
                                elif divmod(NUM,16)[1] == 14:
                                    HEX='E'+str(HEX)
                                elif divmod(NUM,16)[1] == 15:
                                    HEX='F'+str(HEX)
                                I+=1
                                NUM=(divmod(NUM,16))[0]
                        
                        I=0
                        OCT=0
                        while NUM8>0:
                            OCT=OCT+(divmod(NUM8,8))[1]*(10**(I))
                            I+=1
                            NUM8=(divmod(NUM8,8))[0]
                        
                        self.eb.setText(str(OCT))
                        self.ed.setText(str(HEX))

        if self.DECr.isChecked():
            if oii=='':
                NUM2=0
                NUM8=0
                NUM=0
            else:
                NUM2=int(oii)
                NUM8=int(oii)
                NUM=int(oii)

            I=0
            BIN=0
            while NUM2>0:
                if (divmod(NUM2,2))[1]==1:
                    BIN=BIN+10**(I)
                I+=1
                NUM2=(divmod(NUM2,2))[0]


            I=0
            OCT=0
            while NUM8>0:
                OCT=OCT+(divmod(NUM8,8))[1]*(10**(I))
                I+=1
                NUM8=(divmod(NUM8,8))[0]

            if oii=='':
                NUM=0
            else:
                NUM=int(oii)
            I=0
            if NUM == 0:
                HEX='0'
            else:
                HEX=''
                while NUM>0:
                    if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                        HEX=str((divmod(NUM,16))[1])+str(HEX)
                    elif divmod(NUM,16)[1] == 10:
                        HEX='A'+str(HEX)   
                    elif divmod(NUM,16)[1] == 11:
                        HEX='B'+str(HEX)
                    elif divmod(NUM,16)[1] == 12:
                        HEX='C'+str(HEX)
                    elif divmod(NUM,16)[1] == 13:
                        HEX='D'+str(HEX)
                    elif divmod(NUM,16)[1] == 14:
                        HEX='E'+str(HEX)
                    elif divmod(NUM,16)[1] == 15:
                        HEX='F'+str(HEX)
                    I+=1
                    NUM=(divmod(NUM,16))[0]

            self.ec.setText(str(OCT))
            self.ed.setText(str(HEX))
            self.eb.setText(str(BIN))
        
        if self.OCTr.isChecked():
            if oii=='':
                self.eb.clear()
                self.ec.clear()
                self.ed.clear()
                NUM=0
            else:
                if len(oii) <= 1:
                    if int(oii) > 7:
                        self.ea.clear()
                        self.eb.setStyleSheet("color:white; background-color: red;")
                        self.eb.setText('ERROR')
                        self.ec.setStyleSheet("color:white; background-color: red;")
                        self.ec.setText('ERROR')
                        self.ed.setStyleSheet("color:white; background-color: red;")
                        self.ed.setText('ERROR')
                    else:
                        NUM=int(oii)
                        I=0
                        self.ec.setText(oii)
                        DEC=0
                        while NUM>0:
                            DEC=DEC+NUM%10*(8**(I))
                            I+=1
                            NUM=NUM//10
                        NUM=DEC
                        NUM_=DEC
                        
                        I=0
                        if NUM == 0:
                            HEX='0'
                        else:
                            HEX=''
                            while NUM>0:
                                if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                                    HEX=str((divmod(NUM,16))[1])+str(HEX)
                                elif divmod(NUM,16)[1] == 10:
                                    HEX='A'+str(HEX)   
                                elif divmod(NUM,16)[1] == 11:
                                    HEX='B'+str(HEX)
                                elif divmod(NUM,16)[1] == 12:
                                    HEX='C'+str(HEX)
                                elif divmod(NUM,16)[1] == 13:
                                    HEX='D'+str(HEX)
                                elif divmod(NUM,16)[1] == 14:
                                    HEX='E'+str(HEX)
                                elif divmod(NUM,16)[1] == 15:
                                    HEX='F'+str(HEX)
                                I+=1
                                NUM=(divmod(NUM,16))[0]
                        
                        
                        
                        
                        I=0
                        BIN=0
                        while NUM_>0:
                            if (divmod(NUM_,2))[1]==1:
                                BIN=BIN+10**(I)
                            I+=1
                            NUM_=(divmod(NUM_,2))[0]
                        self.eb.setText(str(BIN))
                        self.ed.setText(str(HEX))

                elif len(oii) > 1:
                    if int(oii)%10 > 7:
                        self.ea.clear()
                        self.eb.setStyleSheet("color:white; background-color: red;")
                        self.eb.setText('ERROR')
                        self.ec.setStyleSheet("color:white; background-color: red;")
                        self.ec.setText('ERROR')
                        self.ed.setStyleSheet("color:white; background-color: red;")
                        self.ed.setText('ERROR')
                    else:
                        NUM=int(oii)
                        I=0
                        DEC=0
                        while NUM>0:
                            DEC=DEC+NUM%10*(8**(I))
                            I+=1
                            NUM=NUM//10
                        NUM=DEC
                        NUM_=DEC
                        self.ec.setText(str(DEC))
                        
                        I=0
                        if NUM==0:
                            HEX='0'
                        else:
                            HEX=''
                            while NUM>0:
                                if divmod(NUM,16)[1] >= 0 and divmod(NUM,16)[1] < 10:
                                    HEX=str((divmod(NUM,16))[1])+str(HEX)
                                elif divmod(NUM,16)[1] == 10:
                                    HEX='A'+str(HEX)   
                                elif divmod(NUM,16)[1] == 11:
                                    HEX='B'+str(HEX)
                                elif divmod(NUM,16)[1] == 12:
                                    HEX='C'+str(HEX)
                                elif divmod(NUM,16)[1] == 13:
                                    HEX='D'+str(HEX)
                                elif divmod(NUM,16)[1] == 14:
                                    HEX='E'+str(HEX)
                                elif divmod(NUM,16)[1] == 15:
                                    HEX='F'+str(HEX)
                                I+=1
                                NUM=(divmod(NUM,16))[0]
                        
                        I=0
                        BIN=0
                        while NUM_>0:
                            if (divmod(NUM_,2))[1]==1:
                                BIN=BIN+10**(I)
                            I+=1
                            NUM_=(divmod(NUM_,2))[0]
                        self.eb.setText(str(BIN))
                        self.ed.setText(str(HEX))

        if self.HEXr.isChecked():
            oii=oii.upper()
            if oii=='':
                self.eb.setText('0')
                self.ec.setText('0')
                self.ed.setText('0')
            else:    
                h=['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', 'A', 'B', 'C' ,'D' ,'E' ,'F']
                if not oii[len(oii)-1] in h:
                    self.ea.clear()
                    self.eb.setStyleSheet("color:white; background-color: red;")
                    self.eb.setText('ERROR')
                    self.ec.setStyleSheet("color:white; background-color: red;")
                    self.ec.setText('ERROR')
                    self.ed.setStyleSheet("color:white; background-color: red;")
                    self.ed.setText('ERROR')
                else:
                    oii = list(oii)
                    oii.reverse()
                    DEC = 0
                    for i in range(0, len(oii)):
                        match oii[i]:
                            case '0': oii[i] = 0
                            case '1': oii[i] = 1
                            case '2': oii[i] = 2
                            case '3': oii[i] = 3
                            case '4': oii[i] = 4
                            case '5': oii[i] = 5
                            case '6': oii[i] = 6
                            case '7': oii[i] = 7
                            case '8': oii[i] = 8
                            case '9': oii[i] = 9
                            case 'A': oii[i] = 10
                            case 'B': oii[i] = 11
                            case 'C': oii[i] = 12
                            case 'D': oii[i] = 13
                            case 'E': oii[i] = 14
                            case 'F': oii[i] = 15
                        DEC = DEC + (int(oii[i])*(16**i))
                    NUM=DEC
                    NUM_=DEC
                    self.ed.setText(str(DEC))

                    I=0
                    OCT=0
                    while NUM_>0:
                        OCT=OCT+(divmod(NUM_,8))[1]*(10**(I))
                        I+=1
                        NUM_=(divmod(NUM_,8))[0]
                    self.ec.setText(str(OCT))

                    I=0
                    BIN=0
                    while NUM>0:
                        if (divmod(NUM,2))[1]==1:
                            BIN=BIN+10**(I)
                        I+=1
                        NUM=(divmod(NUM,2))[0]
                    self.eb.setText(str(BIN))





class Window2(QWidget):
    def __init__(self):
        super().__init__()
        layout_3 = QHBoxLayout()
        layout_4 = QVBoxLayout()
        layout_31 = QVBoxLayout()

        Font13 = QFont()
        Font13.setPointSize(8)

        wd_1 = QWidget()
        wd_1.setStyleSheet("background: #ECECEC;")

        self.l1 = QLabel("Hello! \nFirst thank you sm for trying my program, arigato gozaimasu:)\nand for now we only have one ciphering method for you to try\n stay tuned for the upcoming updates for more fun.\n\n\n")
        self.l1.setFont(Font13)
        layout_31.addWidget(self.l1)

        

        layout_31.addStretch()

        self.l_info = QLabel()
        self.l_info.setAlignment(Qt.AlignRight)
        self.l_info.setPixmap(QPixmap("icos\info_.png"))

        layout_31.addWidget(self.l_info)

        wd_1.setLayout(layout_31)

        self.l_info.mouseReleaseEvent = self.Info




        layout_4.addWidget(wd_1)

        Font_ = QFont()
        Font_.setPointSize(18)

        self.b1 = QPushButton('Cipher')
        self.b1.setIcon(QIcon("icos\locked_2.png"))
        self.b1.setIconSize(QSize(40, 40))
        self.b1.setFont(Font_)
        layout_3.addWidget(self.b1)
        self.b1.clicked.connect(self.dia_1)
        self.b2 = QPushButton('EnCipher')
        self.b2.setIcon(QIcon("icos\lock_2.png"))
        self.b2.setIconSize(QSize(40, 40))
        self.b2.setFont(Font_)
        layout_3.addWidget(self.b2)
        self.b2.clicked.connect(self.dia_2)

        layout_4.addLayout(layout_3)
        self.setLayout(layout_4)

    def Info(self, clc):
        self.w = QWidget()
        self.layZZ = QHBoxLayout()
        self.layZX = QVBoxLayout()
        self.about1 = QLabel()
        self.about1.setText("Al-Kindi is a simple app I wrote for fun,\nI hope you'll find it somewhat helpful.\nI named it after Al-Kindi to honor his\nmemory and his fascinating achievements\nin the land of ciphering.\n\nAt the moment our ciphering section is\nprovided with only one ciphering method as\nI mentioned earlier, soon, a new update\nwill be released with more algorithms to\nplay with!\n\n(The ciphering method I'm using for now\nis ''Caesar cipher'', click the link below to\nlearn more about it!)")
        self.layZX.addWidget(self.about1)
        
        self.about11 = QLabel("<a href='https://en.wikipedia.org/wiki/Caesar_cipher'>Caesar Cipher</a>")
        self.about11.setOpenExternalLinks(True)
        self.layZX.addWidget(self.about11)

        self.layZZ.addLayout(self.layZX)
        self.layZZ.addStretch()

        self.about2 = QLabel()
        self.about2.setPixmap(QPixmap("icos\CC.png"))
        self.layZZ.addWidget(self.about2)
        self.about2.setOpenExternalLinks(True)



        self.w.setLayout(self.layZZ)
        self.w.setWindowTitle('About')
        self.w.setWindowIcon(QIcon("icos\info.png"))
        self.w.show()

    def dia_1(self):
        self.w = QWidget()
        self.lay1 = QVBoxLayout()
        self.lay2 = QHBoxLayout()
        
        self.b_past = QPushButton('Paste')
        self.b_past.setFixedHeight(35)
        self.lay1.addWidget(self.b_past)
        self.b_past.clicked.connect(self.pPaste)

        self.text = QTextEdit()
        self.text.setStyleSheet("selection-background-color: #FFB90F;")
        self.lay1.addWidget(self.text)
        
        Font_= QFont()
        Font_.setPointSize(12)

        self.lay2.addStretch()

        self.i_key = QLabel()
        self.i_key.setPixmap(QPixmap("icos\Key.png"))
        self.lay2.addWidget(self.i_key)
        
        self.l_key = QLabel('Key:')
        self.l_key.setFont(Font_)
        self.lay2.addWidget(self.l_key)

        self.spin = QSpinBox()
        self.spin.setStyleSheet("selection-background-color: #FFB90F;")
        self.spin.setRange(0, 100)
        self.spin.setMinimumHeight(30)
        self.spin.setFont(Font_)
        self.lay2.addWidget(self.spin)

        self.lay2.addStretch()
        
        
        self.b_ciph = QPushButton('Cipher')
        self.b_ciph.setMinimumSize(QSize(200, 35))
        self.b_ciph.setIcon(QIcon("icos\locked_2.png"))
        self.b_ciph.setIconSize(QSize(30, 30))
        self.b_ciph.setFont(Font_)
        self.lay2.addWidget(self.b_ciph)
        self.lay2.addStretch()
        self.lay1.addLayout(self.lay2)
        self.b_ciph.clicked.connect(self.CIPH)
        
        self.code = QTextEdit()
        self.code.setStyleSheet("selection-background-color: #FFB90F;")
        self.code.setReadOnly(True)
        self.lay1.addWidget(self.code)
    
        self.b_copy = QPushButton('Copy')
        self.b_copy.setFixedHeight(35)
        self.lay1.addWidget(self.b_copy)
        self.b_copy.clicked.connect(self.Copy)


        self.w.setMinimumSize(QSize(500, 500))
        self.w.setLayout(self.lay1)
        self.w.setWindowTitle('Cipher')
        self.w.setWindowIcon(QIcon("icos\locked_2.png"))
        self.w.show()
    
    def Paste(self):
        if self.b_past.clicked:
            self.text.setText(clipboard.text())
    
    def Copy(self):
        if self.b_copy.released:
            clipboard.setText(self.code.toPlainText())
    
    def CIPH(self):
        txt = list(self.text.toPlainText())
        NC = list(txt)
        key_ = int(self.spin.value())
        code = ''
        for i in range(0, len(txt)):
            NC[i] = ord(txt[i])
            code+=chr(NC[i] + key_)
        self.code.setPlainText(str(code))
            
        

    
    
    def dia_2(self):
        self.w = QWidget()
        self.lay1 = QVBoxLayout()
        self.lay2 = QHBoxLayout()
        
        self.b_past = QPushButton('Paste')
        self.b_past.setFixedHeight(35)
        self.lay1.addWidget(self.b_past)
        self.b_past.clicked.connect(self.pPaste)

        self.text = QTextEdit()
        self.text.setStyleSheet("selection-background-color: #FFB90F;")
        self.lay1.addWidget(self.text)
        
        Font_= QFont()
        Font_.setPointSize(12)

        self.lay2.addStretch()

        self.i_key = QLabel()
        self.i_key.setPixmap(QPixmap("icos\Key.png"))
        self.lay2.addWidget(self.i_key)
        
        self.l_key = QLabel('Key:')
        self.l_key.setFont(Font_)
        self.lay2.addWidget(self.l_key)

        self.spin = QSpinBox()
        self.spin.setStyleSheet("selection-background-color: #FFB90F;")
        self.spin.setRange(0, 100)
        self.spin.setMinimumHeight(30)
        self.spin.setFont(Font_)
        self.lay2.addWidget(self.spin)

        self.lay2.addStretch()
        
        
        self.b_ciph = QPushButton('Enipher')
        self.b_ciph.setMinimumSize(QSize(200, 35))
        self.b_ciph.setIcon(QIcon("icos\lock_2.png"))
        self.b_ciph.setIconSize(QSize(30, 30))
        self.b_ciph.setFont(Font_)
        self.lay2.addWidget(self.b_ciph)
        self.b_ciph.clicked.connect(self.enCIPH)
        self.lay2.addStretch()
        self.lay1.addLayout(self.lay2)
        
        self.code = QTextEdit()
        self.code.setStyleSheet("selection-background-color: #FFB90F;")
        self.code.setReadOnly(True)
        self.lay1.addWidget(self.code)
        
        self.b_copy = QPushButton('Copy')
        self.b_copy.setFixedHeight(35)
        self.lay1.addWidget(self.b_copy)
        self.b_copy.clicked.connect(self.cCopy)


        self.w.setMinimumSize(QSize(500, 500))
        self.w.setLayout(self.lay1)
        self.w.setWindowTitle('Cipher')
        self.w.setWindowIcon(QIcon("icos\lock_2.png"))
        self.w.show()
    
    def pPaste(self):
        if self.b_past.clicked:
            self.text.setText(clipboard.text())
    
    def cCopy(self):
        if self.b_copy.released:
            clipboard.setText(self.code.toPlainText())
    
    def enCIPH(self):
        txt = list(self.text.toPlainText())
        NC = list(txt)
        key_ = int(self.spin.value())
        code = ''
        for i in range(0, len(txt)):
            NC[i] = ord(txt[i])
            code+=chr(NC[i] - key_)
        self.code.setPlainText(str(code))
            






app = QApplication(sys.argv)
clipboard=app.clipboard()
w = main_window()
w.show()
app.exec()

import sys
import re
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QSize
from PyQt5.QtWidgets import QApplication, QMainWindow
from Window import *
from fctions import Main


class InitWindow(QMainWindow, Ui_MainWindow):
    pro = Main()
    lt = []

    def __init__(self):
        super(InitWindow, self).__init__()
        self.setupUi(self)
        self.setIconSize(QSize(74, 74))
        self.setWindowTitle('Friendly')
        self.setWindowIcon(QIcon('./ICO.ico'))
        self.s = self.Command
        self.r = self.ResultNum

        self.rt.clicked.connect(self.enter_fct('rt'))
        self.tre.clicked.connect(self.enter_fct('tre'))
        self.avr.clicked.connect(self.enter_fct('avr'))
        self.ng.clicked.connect(self.enter_fct('ng'))
        self.ckrb.clicked.connect(self.enter_fct('ckrb'))
        self.sin.clicked.connect(self.enter_fct('sin'))
        self.cos.clicked.connect(self.enter_fct('cos'))
        self.tan.clicked.connect(self.enter_fct('tan'))
        self.sqrt.clicked.connect(self.enter_fct('sqrt'))
        self.abs.clicked.connect(self.enter_fct('abs'))

        self.qunch.clicked.connect(self.enter_chr('qunch'))
        self.zhuju.clicked.connect(self.enter_chr('zhuju'))
        self.keshu.clicked.connect(self.enter_chr('keshu'))

        self.zc_fang.clicked.connect(self.enter_fct('zc fang'))
        self.zc_yuan.clicked.connect(self.enter_fct('zc yuan'))
        self.mj_fang.clicked.connect(self.enter_fct('mj fang'))
        self.mj_yuan.clicked.connect(self.enter_fct('mj yuan'))
        self.mj_tixg.clicked.connect(self.enter_fct('mj tixg'))
        self.mj_sanj.clicked.connect(self.enter_fct('mj sanj'))
        self.tj_fang.clicked.connect(self.enter_fct('tj fang'))
        self.tj_yuan.clicked.connect(self.enter_fct('tj yuan'))
        self.tj_yzhu.clicked.connect(self.enter_fct('tj yzhu'))
        self.tj_yhui.clicked.connect(self.enter_fct('tj yhui'))

        self.key0.clicked.connect(self.enter_chr('0'))
        self.key1.clicked.connect(self.enter_chr('1'))
        self.key2.clicked.connect(self.enter_chr('2'))
        self.key3.clicked.connect(self.enter_chr('3'))
        self.key4.clicked.connect(self.enter_chr('4'))
        self.key5.clicked.connect(self.enter_chr('5'))
        self.key6.clicked.connect(self.enter_chr('6'))
        self.key7.clicked.connect(self.enter_chr('7'))
        self.key8.clicked.connect(self.enter_chr('8'))
        self.key9.clicked.connect(self.enter_chr('9'))

        self.num_dot.clicked.connect(self.dot)
        self.leftq.clicked.connect(self.enter_chr('('))
        self.rightq.clicked.connect(self.enter_chr(')'))
        self.Plus.clicked.connect(self.enter_chr('+'))
        self.Minus.clicked.connect(self.enter_chr('-'))
        self.Times.clicked.connect(self.enter_chr('*'))
        self.Division.clicked.connect(self.enter_chr('/'))
        self.Remainder.clicked.connect(self.enter_chr('%'))
        self.Exact.clicked.connect(self.enter_chr('\\'))
        self.Power.clicked.connect(self.enter_chr('^'))

        self.Spaces.clicked.connect(self.spaces)
        self.EnterButton.clicked.connect(self.enter)
        self.AC.clicked.connect(self.clear)
        self.BK.clicked.connect(self.back)

    def dot(self, button):
        if '.' not in re.split(r'[ +\-*/|^%]', self.s.toPlainText()):
            lt = ' '.join(self.lt)
            lt += '.'
            self.lt = lt.split(' ')
            self.s.setPlainText(lt)

    def enter_fct(self, fcts: str):
        def _self(button):
            if self.s.toPlainText()[0] in [str(x) for x in range(1, 11)] or self.s.toPlainText()[0] == '(':
                self.lt.insert(0, fcts + ' ')
            elif self.lt.__len__() != 0:
                self.lt[0] = fcts
            else:
                self.lt = [f'{fcts} ']
            self.s.setPlainText(' '.join(self.lt))
        return _self

    def enter_chr(self, chrs: str):
        def _self(button):
            lt = ' '.join(self.lt)
            lt += chrs
            self.lt = lt.split(' ')
            self.s.setPlainText(lt)
        return _self

    def clear(self, button):
        self.lt = []
        self.s.setPlainText('>')
        self.r.setPlainText('0.')

    def back(self, button):
        if len(self.s.toPlainText()) == 1:
            self.s.setPlainText('>')
            self.lt = ['']
        elif self.s.toPlainText().strip() != '':
            string = self.s.toPlainText()
            string = string[:-1]
            self.lt = string.split(' ')
            self.s.setPlainText(string)

    def spaces(self, button):
        self.lt.append('')

    def enter(self, button):
        string = self.s.toPlainText()
        lt = string.split()
        rs = ''
        pro = self.pro
        if string.strip().strip('>') == '':
            return
        try:
            if string[0] not in [str(i) for i in range(1, 11)]:
                if lt[0] == 'tre':
                    rs = pro.tree(_q=lt[1], _s=lt[2], _1=float(lt[3]), _2=float(lt[4]))
                elif lt[0] == 'ng':
                    rs = pro.nongdu(float(lt[1]), float(lt[2]))
                elif lt[0] == 'ckrb':
                    rs = pro.chick_rabbit(int(lt[1]), int(lt[2]), int(lt[3]))
                elif lt[0] == 'avr':
                    rs = pro.average(float(lt[1]), *lt[2:])
                elif lt[0] == 'rt':
                    rs = pro.rate(float(lt[1]), float(lt[2]))
                elif lt[0] == 'sin':
                    rs = pro.sin(float(lt[1]))
                elif lt[0] == 'cos':
                    rs = pro.cos(float(lt[1]))
                elif lt[0] == 'tan':
                    rs = pro.tan(float(lt[1]))
                elif lt[0] == 'abs':
                    rs = pro.abs(float(lt[1]))
                elif lt[0] == 'sqrt':
                    rs = pro.sqrt(float(lt[1]))

                ##### 图形 #####
                if lt[0] == 'zc':
                    if lt[1] == 'fang':
                        rs = pro.zc_fang(float(lt[2]), float(lt[3]))
                    if lt[1] == 'yuan':
                        rs = pro.zc_yuan(float(lt[2]))
                if lt[0] == 'mj':
                    if lt[1] == 'fang':
                        rs = pro.mj_fang(float(lt[2]), float(lt[3]))
                    if lt[1] == 'sanj':
                        rs = pro.mj_sanj(float(lt[2]), float(lt[3]))
                    if lt[1] == 'tixg':
                        rs = pro.mj_tixg(float(lt[2]), float(lt[3]), float(lt[4]))
                    if lt[1] == 'yuan':
                        rs = pro.mj_yuan(float(lt[2]))
                if lt[0] == 'tj':
                    if lt[1] == 'fang':
                        rs = pro.tj_fang(float(lt[2]), float(lt[3]), float(lt[4]))
                    if lt[1] == 'yhui':
                        rs = pro.tj_yhui(float(lt[2]), float(lt[3]))
                    if lt[1] == 'yzhu':
                        rs = pro.tj_yzhu(float(lt[2]), float(lt[3]))
            elif string.strip() != '' and string != '>':
                rs = pro.default(string.replace('^', '**').replace('\\', '//'))
        except Exception as e:
            QtWidgets.QMessageBox.critical(None, '数据错误', str(e))
        else:
            self.r.setPlainText(str(rs))


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = InitWindow()
    window.show()
    sys.exit(app.exec_())

'''
def psng(self, button):
    lt = [x for i in self.lt for x in re.split(r'\+|-|\*|/|^|%|//', i)]
    if len(self.lt) != 0:
        if abs(float(lt[-1])) == float(lt[-1]):
            self.lt[-1] = '-' + str(lt[-1])
        else:
            self.lt[-1] = (lt[-1])[1:]
    tmp = 0 - len(lt[-1]) -1
    self.lt[tmp:] = lt[-1]
    self.s.setPlainText(' '.join(self.lt))
'''
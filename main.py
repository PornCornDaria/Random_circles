import sys

from random import randint

from PyQt5.QtWidgets import QWidget, QApplication, QPushButton

from PyQt5.QtGui import QPainter, QColor


class SimpleClass(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(1000, 300, 600, 500)
        self.setWindowTitle('Вычисление выражений')
        self.do_paint = False
        self.pushButton = QPushButton('Нарисовать окружность', self)
        self.pushButton.clicked.connect(self.paint)

    def paintEvent(self, event):
        if self.do_paint:
            qp = QPainter()
            qp.begin(self)
            self.draw_ellipse(qp)
            qp.end()

    def paint(self):
        self.do_paint = True
        self.repaint()

    def draw_ellipse(self, qp):
        qp.setBrush(QColor(randint(0, 255), randint(0, 22), randint(0, 255)))
        a = randint(20, 150)
        x = randint(0, 500)
        y = randint(0, 400)
        qp.drawEllipse(x, y, a, a)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    simple_class = SimpleClass()
    simple_class.show()
    sys.exit(app.exec())
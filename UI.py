import pickle
# from typing import Callable
# from typing import List, Any

from PyQt5 import QtWidgets
from PyQt5 import QtCore

from files.MainWindow import Ui_MainWindow
from files.ResultWindow import Ui_Form
# from files.TableWindow import Ui_Form as Ui_Form_Table

from main import Calculation
from functions import change_size, get_sub, get_super
from MyThread import MyThread
from TableLoader import TableLoader
# from ChartPLTWindow import ChartPLTWindow

from settings import DEDUG

import sys
from string import Template


# from functions import get_super, get_sub


class Variables:
    def __init__(self, main_window):
        self.main_window: mywindow = main_window
        self.name = None
        self.alpha = None
        self.n = None
        self.load()

    def load(self):
        self.name = self.main_window.ui.lineEdit.text()
        self.alpha = mywindow.is_float(self.main_window.ui.doubleSpinBox_9)
        self.n = mywindow.is_int(self.main_window.ui.doubleSpinBox_11)

    def update(self):
        self.load()
        self.main_window.table_loader1.m = self.n
        # self.main_window.table_loader2.n = self.n


class mywindow(QtWidgets.QMainWindow):

    def __init__(self):
        super(mywindow, self).__init__()

        self.calculation = None
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        if DEDUG:
            self.ui.lineEdit.setText("озимая пшеница")
            self.ui.doubleSpinBox_9.setValue(0.05)  # alpha
            self.ui.doubleSpinBox_11.setValue(7)  # n

        change_size(self)

        self.lst_Thread = []

        self.variables = Variables(self)

        loader1_n = 3
        loader1_m = self.variables.n
        loader1_label = self.ui.label_13
        loader1_data = [
            [2017, 46, 52],
            [2018, 48, 53],
            [2019, 46, 45],
            [2020, 51, 56],
            [2021, 52, 58],
            [2022, 48, 55],
            [2023, 52, 59]]
        loader1_block = False
        loader1_heading_x = lambda iterator: ["", "", ""][iterator]
        loader1_types_matrix = [[int, int, int] for _ in range(loader1_m)]

        # loader2_n = self.variables.n
        # loader2_m = 1
        # loader2_label = self.ui.label_4
        # loader2_data = [[1, 1.6]]
        # loader2_block = False
        # loader2_heading_x = lambda iterator: f"E{get_sub(str(iterator + 1))}"

        self.table_loader1 = TableLoader(
            self, loader1_n, loader1_m, loader1_label,
            block=loader1_block,
            heading_x=loader1_heading_x,
            types_matrix=loader1_types_matrix
        )
        # self.table_loader2 = TableLoader(
        #     self, loader2_n, loader2_m, loader2_label,
        #     block=loader2_block,
        #     heading_x=loader2_heading_x
        # )

        if DEDUG:
            pass
            self.table_loader1.data = loader1_data
            # self.table_loader2.data = loader2_data

        self.ui.pushButton_8.clicked.connect(self.table_loader1.open_table)
        # self.ui.pushButton_3.clicked.connect(self.table_loader2.open_table)

        # add_def_pushButton = lambda: self.calculation.base()
        # add_def_pushButton_2 = lambda: self.calculation.iffect()
        # self.ui.pushButton.clicked.connect(lambda: self.calculate(add_def_pushButton))
        # self.ui.pushButton_2.clicked.connect(lambda: self.calculate(add_def_pushButton_2))

        add_def_pushButton = lambda: None
        self.ui.pushButton_3.clicked.connect(lambda: self.calculate(add_def_pushButton))

    def calculate(self, fun, *args, **kwargs):
        self.variables.update()
        # condition = self.table_loader1.valid(self.variables.k, 3)
        condition = True
        if condition:
            self.calculation = Calculation(
                name=self.variables.name,
                alpha=self.variables.alpha,
                n=self.variables.n,
                lst1=pickle.loads(pickle.dumps(self.table_loader1.data)),
            )
            fun(*args, **kwargs)
            window = Finish(
                self
            )
            window.show()

            # def main():
            #     window.exec_()
            #
            # t = MyThread(main)
            # t.start()
            windowThread = MyThread(lambda: window.exec_())
            windowThread.start()
            self.lst_Thread.append(windowThread)

    def exec_(self) -> int:
        a = super().exec_()
        for i in self.lst_Thread:
            i.wait()
        return a

    @staticmethod
    def is_float(value: QtWidgets.QDoubleSpinBox) -> float:
        try:
            a = float(value.value())
            value.setStyleSheet("QDoubleSpinBox {}")
            return a
        except ValueError:
            value.setStyleSheet("QDoubleSpinBox { background-color: red; }")
            raise ValueError()

    @staticmethod
    def is_int(value: QtWidgets.QDoubleSpinBox) -> int:
        try:
            a = int(round(float(value.value())))
            value.setStyleSheet("QDoubleSpinBox {}")
            return a
        except ValueError:
            value.setStyleSheet("QDoubleSpinBox { background-color: red; }")
            raise ValueError()


class Finish(QtWidgets.QDialog):
    def __init__(self, parent: mywindow):
        super(Finish, self).__init__()
        self.ui = Ui_Form()
        self.parent = parent
        self.ui.setupUi(self)
        change_size(self)
        _translate = QtCore.QCoreApplication.translate

        result = (("&gt;", "отвергается", "существенно"), ("&lt;", "принимается", "несущественно"))
        num = 1
        if self.parent.calculation.t_see > self.parent.calculation.t_crit:
            num = 0
        template = Template(
            """<!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 4.0//EN" "http://www.w3.org/TR/REC-html40/strict.dtd">
<html><head><meta name="qrichtext" content="1" /><style type="text/css">
p, li { white-space: pre-wrap; }
</style></head><body style=" font-family:'Times New Roman'; font-size:14pt; font-weight:600; font-style:normal;">
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:400;">Проверку гипотезы H</span><span style=" font-weight:400; vertical-align:sub;">0</span><span style=" font-weight:400;"> осуществляют с помощью критерия t-Стьюдента.</span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:400;">Так как t</span><span style=" font-weight:400; vertical-align:sub;">набл</span><span style=" font-weight:400;"> $symbol t</span><span style=" font-weight:400; vertical-align:sub;">кр</span><span style=" font-weight:400;">, то нулевая гипотеза $res1 </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:400;">Следовательно, два сорта $name статистически существенно различаются по уровню урожайности $res2 </span></p>
<p style=" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;"><span style=" font-weight:400;">Выдвигаем нулевую гипотезу H</span><span style=" font-weight:400; vertical-align:sub;">0</span><span style=" font-weight:400;"> средняя величина различий в урожайности культуры равна нулю, т.е. Н</span><span style=" font-weight:400; vertical-align:sub;">0</span><span style=" font-weight:400;">: </span><span style=" font-weight:400; font-style:italic; text-decoration: overline;">x-y=0</span><span style=" font-weight:400;"> при H</span><span style=" font-weight:400; vertical-align:sub;">1</span><span style=" font-weight:400;">: </span><span style=" font-weight:400; font-style:italic; text-decoration: overline;">x-y≠0</span><span style=" font-weight:400;">.</span></p></body></html>"""
        )
        formatted_string = template.substitute(
            symbol=result[num][0],
            res1=result[num][1],
            name=self.parent.variables.name,
            res2=result[num][2]
        )
        self.ui.textEdit.setHtml(formatted_string)
        self.ui.doubleSpinBox_12.setValue(round(self.parent.calculation.d_med, 2))
        self.ui.doubleSpinBox_13.setValue(round(self.parent.calculation.S_m_d, 2))

        # self.ui.textEdit.setText(
        #     f"Приближенное значение средней урожайности равно x(среднее) = {str(round(self.parent.calculation.x_cp_v, 2)).replace('.', ',')} ц. Следовательно, оценка средней урожайности сахарной свеклы на всем массиве равна {str(round(self.parent.calculation.x_cp_v)).replace('.', ',')} ц со средней квадратической ошибкой {str(round(self.parent.calculation.S_xcp, 2)).replace('.', ',')} ц. Оценка среднего квадратического отклонения урожайности на всем массиве равна {str(round(self.parent.calculation.s, 2)).replace('.', ',')} ц."
        # )

        lst = []
        types_matrix = []
        summ = 0
        for i in range(self.parent.table_loader1.m):
            data = self.parent.calculation.lst.copy()
            lst.append([
                round(data[i][0]), round(data[i][1]), round(data[i][2]),
                round(data[i][3]),
                round(data[i][4], 2),
                round(data[i][5], 2)
            ])
            types_matrix.append([int, int, int, int, float, float])

        lst.append(
            [
                '-',
                '-', '-',
                round(self.parent.calculation.d_med * self.parent.variables.n),
                round(self.parent.calculation.summ_d_d, 2),
                round(self.parent.calculation.summ_d_d_2, 2)
            ]
        )
        types_matrix.append([str, str, str, int, float, float])

        filter_table_results_1 = lambda dct: round(dct['value'], 3)

        loader_results_1_n = self.parent.table_loader1.n + 3
        loader_results_1_m = self.parent.table_loader1.m + 1
        loader_results_1_data = lst
        types_matrix_results_1 = types_matrix
        loader_results_1_block = True
        loader_results_1_heading_x = lambda iterator: \
            ["Урожайность, ц/га\nНачало промежутка", "Урожайность, ц/га\nКонец промежутка",
             f"Площадь N{get_sub('i')}, га", "Середина интервала",
             f"y{get_sub('i')} * n{get_sub('i')}",
             f"(y{get_sub('i')} - x{get_sub('v')}){get_super('2')} * n{get_sub('i')}"][iterator]
        loader_results_1_heading_y = lambda iterator: \
            ([str(i + 1) for i in range(self.parent.table_loader1.m)] + ["Сумма"])[
                iterator]
        self.table_loader_results_1 = TableLoader(
            self.parent, loader_results_1_n, loader_results_1_m, data=loader_results_1_data,
            block=loader_results_1_block,
            heading_x=loader_results_1_heading_x, heading_y=loader_results_1_heading_y,
            types_matrix=types_matrix_results_1
        )

        # loader_v_y_data = self.parent.calculation.lst_v_y
        # self.table_loader_v_y = TableLoader(
        #     self.parent, loader_v_d_n, loader_v_d_m, data=loader_v_y_data,
        #     block=loader_v_d_block,
        #     heading_x=loader_v_d_heading_x, heading_y=loader_v_d_heading_y,
        #     filter_table=filter_table
        # )
        #
        # loader_v_s_data = self.parent.calculation.lst_v_s
        # self.table_loader_v_s = TableLoader(
        #     self.parent, loader_v_d_n, loader_v_d_m, data=loader_v_s_data,
        #     block=loader_v_d_block,
        #     heading_x=loader_v_d_heading_x, heading_y=loader_v_d_heading_y,
        #     filter_table=filter_table
        # )

        # self.ui.doubleSpinBox_19.setValue(round(self.parent.calculation.y))
        # self.ui.doubleSpinBox_20.setValue(round(self.parent.calculation.dy))
        # self.ui.doubleSpinBox_10.setValue(round(self.parent, 2))
        # self.table_loader_results_1.kwargs['block'] = True
        # self.parent.table_loader2.kwargs['block'] = True

        self.lst_Thread = []

        self.lst_Thread.append(MyThread(lambda: self.table_loader_results_1.open_table()))
        self.ui.pushButton_2.clicked.connect(
            lambda: self.lst_Thread[0].start()
        )
        #
        # self.lst_Thread.append(MyThread(lambda: self.table_loader_v_s.open_table()))
        # self.ui.pushButton_4.clicked.connect(
        #     lambda: self.lst_Thread[1].start()
        # )
        #
        # self.lst_Thread.append(MyThread(lambda: self.table_loader_v_y.open_table()))
        # self.ui.pushButton_7.clicked.connect(
        #     lambda: self.lst_Thread[2].start()
        # )
        #
        # chart_plt_w = ChartPLTWindow(1)
        # chart_plt_w.line(self.parent.calculation.chart_v_y_data)
        # chart_plt_w.quad_regress(self.parent.calculation.chart_quad_regress_data)
        #
        # self.lst_Thread.append(MyThread(
        #     lambda: chart_plt_w.start())
        # )
        # self.ui.pushButton_8.clicked.connect(
        #     lambda: self.lst_Thread[3].start()
        # )

        self.ui.pushButton.clicked.connect(self.exit_w)
        # self.ui.pushButton_2.clicked.connect(self.view_table)

    def exit_w(self):
        # self.table_loader_results_1.kwargs['block'] = False
        self.close()

    # def exec_(self) -> int:
    #     a = super().exec_()
    #     for i in self.lst_Thread:
    #         i.wait()
    #     return a

    def view_table(self):
        # self.parent.table_loader1.open_table()
        # self.parent.table_loader2.open_table()
        pass


app = QtWidgets.QApplication([])
application = mywindow()
application.show()

sys.exit(app.exec())

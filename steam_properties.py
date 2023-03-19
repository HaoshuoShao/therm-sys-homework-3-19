import sys
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout
import iapws

class SteamCalculator(QWidget):
    def __init__(self):
        super().__init__()

        # 初始化界面
        self.initUI()

    def initUI(self):
        # 标签和输入框
        self.lbl_inputs = QLabel("请输入以下两个参数")
        self.lbl_param1 = QLabel("压强(P)(MPa)")
        self.le_param1 = QLineEdit()
        # self.lbl_param2 = QLabel("比体积(v)(m^3/kg)")
        # self.le_param2 = QLineEdit()
        self.lbl_param3 = QLabel("温度(T)(℃)")
        self.le_param3 = QLineEdit()
        self.lbl_param4 = QLabel("焓(h)(kJ/kg)")
        self.le_param4 = QLineEdit()
        self.lbl_param5 = QLabel("熵(s)(kJ/(kg*K))")
        self.le_param5 = QLineEdit()
        self.lbl_param6 = QLabel("干度(x) - ")
        self.le_param6 = QLineEdit()

        # 按钮
        self.btn_calculate = QPushButton("计算")
        self.btn_calculate.clicked.connect(self.calculate)

        # 结果标签
        self.lbl_outputs = QLabel("计算结果：")

        # 布局
        vbox_inputs = QVBoxLayout()
        vbox_inputs.addWidget(self.lbl_inputs)
        hbox_param1 = QHBoxLayout()
        hbox_param1.addWidget(self.lbl_param1)
        hbox_param1.addWidget(self.le_param1)
        vbox_inputs.addLayout(hbox_param1)
        # hbox_param2 = QHBoxLayout()
        # hbox_param2.addWidget(self.lbl_param2)
        # hbox_param2.addWidget(self.le_param2)
        # vbox_inputs.addLayout(hbox_param2)
        hbox_param3 = QHBoxLayout()
        hbox_param3.addWidget(self.lbl_param3)
        hbox_param3.addWidget(self.le_param3)
        vbox_inputs.addLayout(hbox_param3)
        hbox_param4 = QHBoxLayout()
        hbox_param4.addWidget(self.lbl_param4)
        hbox_param4.addWidget(self.le_param4)
        vbox_inputs.addLayout(hbox_param4)
        hbox_param5 = QHBoxLayout()
        hbox_param5.addWidget(self.lbl_param5)
        hbox_param5.addWidget(self.le_param5)
        vbox_inputs.addLayout(hbox_param5)
        hbox_param6 = QHBoxLayout()
        hbox_param6.addWidget(self.lbl_param6)
        hbox_param6.addWidget(self.le_param6)
        vbox_inputs.addLayout(hbox_param6)
        vbox_inputs.addWidget(self.btn_calculate)
        vbox_outputs = QVBoxLayout()
        vbox_outputs.addWidget(self.lbl_outputs)

        hbox = QHBoxLayout()
        hbox.addLayout(vbox_inputs)
        hbox.addLayout(vbox_outputs)

        self.setLayout(hbox)

        # 设置窗口
        self.setGeometry(400, 400, 600, 250)
        self.setWindowTitle('水蒸气物性参数计算器')
        self.show()

    def calculate(self):
        # 获取用户输入的参数
        param1 = self.le_param1.text()
        # param2 = self.le_param2.text()
        param3 = self.le_param3.text()
        param4 = self.le_param4.text()
        param5 = self.le_param5.text()
        param6 = self.le_param6.text()

        # 确定已知参数的数量
        known_params = [p for p in [param1, param3, param4, param5, param6] if p]
        num_known_params = len(known_params)

        # 检查已知参数数量是否为2
        if num_known_params != 2:
            self.lbl_outputs.setText("请输入两个已知参数")
            return

        # 判断用户输入的已知参数是哪两个，并将其转换为浮点数
        if param1 and param3:
            try:
                # 可能会导致错误的代码
                p = float(param1)
                T = float(param3)+273.15
                steam = iapws.IAPWS97(P=p, T=T)            
            except:
                # 处理捕获的异常
                self.lbl_outputs.setText("出错,超出输入范围")

        elif param1 and param4:
            try:
                p = float(param1)
                h = float(param4)
                steam = iapws.IAPWS97(P=p, h=h)

            except:
                # 处理捕获的异常
                self.lbl_outputs.setText("出错,超出输入范围")
        elif param1 and param5:
            try:
                p = float(param1)
                s = float(param5)
                steam = iapws.IAPWS97(P=p, s=s)

            except:
                # 处理捕获的异常
                self.lbl_outputs.setText("出错,超出输入范围")

        # elif param2 and param3:
        #     v = float(param2)
        #     T = float(param3)+273.15
        #     steam = iapws.IAPWS97(v=v, T=T)
        # elif param2 and param4:
        #     v = float(param2)
        #     h = float(param4)
        #     steam = iapws.IAPWS97(v=v, h=h)
        # elif param2 and param5:
        #     v = float(param2)
        #     s = float(param5)
        #     steam = iapws.IAPWS97(v=v, s=s)
        # elif param3 and param4:
        #     T = float(param3)+273.15
        #     h = float(param4)
        #     steam = iapws.IAPWS97(T=T, h=h)
        # elif param3 and param5:
        #     T = float(param3)+273.15
        #     s = float(param5)
        #     steam = iapws.IAPWS97(T=T, s=s)
        elif param4 and param5:
            try:
                h = float(param4)
                s = float(param5)
                steam = iapws.IAPWS97(h=h, s=s)

            except:
                # 处理捕获的异常
                self.lbl_outputs.setText("出错,超出输入范围")
            
        elif param6 and param1:
            try:
                x = float(param6)
                p = float(param1)
                steam = iapws.IAPWS97(x=x, P=p)

            except:
                # 处理捕获的异常
                self.lbl_outputs.setText("出错,超出输入范围")    
        # elif param6 and param2:
        #     x = float(param6)
        #     v = float(param2)
        #     steam = iapws.IAPWS97(x=x, v=v)
        elif param6 and param3:
            try:
                x = float(param6)
                T = float(param3)+273.15
                steam = iapws.IAPWS97(x=x, T=T)

            except:
                # 处理捕获的异常
                self.lbl_outputs.setText("出错,超出输入范围")
        # elif param6 and param4:
        #     x = float(param6)
        #     h = float(param4)
        #     steam = iapws.IAPWS97(x=x, h=h)
        # elif param6 and param5:
        #     x = float(param6)
        #     s = float(param5)
        #     steam = iapws.IAPWS97(x=x, s=s)
        else:
            self.lbl_outputs.setText("请输入两个有效参数")
            return
        
        # 显示计算结果
        try:
            # 可能会导致错误的代码
            self.lbl_outputs.setText(f"Phase = {steam.phase}\nrho = {steam.rho:.3f} kg/m³\nP = {steam.P:.3f} MPa\nv = {steam.v:.6f}m^3/kg\nT = {steam.T-273.15:.3f} ℃\nh = {steam.h:.3f} kJ/kg\ns = {steam.s:.6f} kJ/(kg*K)\nx = {steam.x:.6f}")
            
        except:
            # 处理捕获的异常
            self.lbl_outputs.setText("出错,请检查输入")

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = SteamCalculator()
    sys.exit(app.exec_())
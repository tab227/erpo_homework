import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sympy

def main():
    data_file_path = 'data_temp.xlsx'
    data_file = pd.read_excel(data_file_path)
    x_data = data_file['x'].values
    y_data = data_file['y'].values
    #plt.plot(x.values, y.values)
    #plt.show()

    fun1 = np.polyfit(x_data, y_data, 18)
    print('fun1 is :', fun1)

    y_temp = np.polyval(fun1, x_data)

    plot1 = plt.plot(x_data, y_data, 'b', label='original values')
    plot2 = plt.plot(x_data, y_temp, 'r', label='polyfit values')

    x = sympy.symbols('x')
    param_num = len(fun1)
    src_fun = 0*x
    for param in fun1:
        src_fun = src_fun + param * (x**(param_num - 1))
        param_num = param_num - 1
    print(src_fun)
    src_fun = sympy.integrate(src_fun, x)
    print(src_fun)

    y_temp = []
    for x_temp in x_data:
        y_temp.append(src_fun.evalf(subs={x:x_temp}))
    print(y_temp)

    plot3 = plt.plot(x_data, y_temp, 'g', label='src values')
    plt.xlabel('x')
    plt.ylabel('y')
    plt.legend(loc=4)  # 指定legend的位置右下角
    plt.title('polyfitting')
    plt.show()

if __name__ == '__main__':
    main()
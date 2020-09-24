'''

关于Excel表的操作
'''

import xlrd
# from settings import conf


class ExcelHandler(object):

    @property
    def get_excel_data(self):
        # 获取到book对象
        book = xlrd.open_workbook('../data/testcase.xlsx')
        # print(book)
        # 获取sheet对象
        sheet = book.sheet_by_index(0)
        #sheet = book.sheet_by_name('商品列表')
        # sheets = book.sheets()  # 获取所有的sheet对象

        rows, cols = sheet.nrows, sheet.ncols
        l = []
        # print(sheet.row_values(0))
        title = sheet.row_values(0)
        # print(title)
        # 获取其他行
        for i in range(1, rows):
            # print(sheet.row_values(i))
            l.append(dict(zip(title, sheet.row_values(i))))
        return l

if __name__ == "__main__":
    case = ExcelHandler().get_excel_data
    print(case)
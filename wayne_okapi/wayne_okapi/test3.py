import jsonpathimport json,redata = {"total": 100,        "success": 75,        "failed": 22,        "skip": 1,        "environment": {"根路径": "http://118.24.91.97:9000/api/",                        "启用全局Session": "TRUE"},        "start_time": "11:15:05",        "end_time": "12:28:04",        "cases": [            {"id": "login01", "name": "正确登录", "status": 0, "log": "响应状态码验证成功！\n响应Json值验证成功！"},            {"id": "get_city01", "name": "获取城市信息", "status": 1, "log": "响应状态码验证失败！\n响应Json值验证失败！", "res": "xxxx"},            {"id": "get_city02", "name": "	城市信息错误", "status": 2, "log": "请求体参数配置错误！"}            ]        }print((data))l = 't = $.cases[0].id'print(type(data))print('l',l)exp = l.split('=')[1]print(exp)dl = jsonpath.jsonpath(data,'$.cases[0].id')print(dl)shop={    "store": {        "book": [            {                "category": "reference",                "author": "Nigel Rees",                "title": "Sayings of the Century",                "price": 8.95            },            {                "category": "fiction",                "author": "Evelyn Waugh",                "title": "Sword of Honour",                "price": 12.99            },            {                "category": "fiction",                "author": "Herman Melville",                "title": "Moby Dick",                "isbn": "0-553-21311-3",                "price": 8.99            },            {                "category": "fiction",                "author": "J. R. R. Tolkien",                "title": "The Lord of the Rings",                "isbn": "0-395-19395-8",                "price": 22.99            }        ],        "bicycle": {            "color": "red",            "price": 19.95        }    },    "expensive": 10}for k in shop:  print('k',k)variable_regexp = r"\"category[\w_]\","print('shop type',type(shop))print(type(json.dumps(shop)))dd = re.findall(variable_regexp,json.dumps(shop))print('dd',dd)#商店里所有书籍的作者author_list=jsonpath.jsonpath(shop,'$.store.book[*].author')print(author_list) #['Nigel Rees', 'Evelyn Waugh', 'Herman Melville', 'J. R. R. Tolkien']#  数据依赖import re,json# excel文件中使用双引号{"city" :"$.town.city"}。参数正文中直接填写 {"city" :"$.town.city"}import jsonpathfrom operation_excel import OperationExcelopera = OperationExcel(file_name = './cases.xls',sheet_id=1)data_6 = opera.get_cell_value(4,6)data_7 = opera.get_cell_value(4,7)data_8 = opera.get_cell_value(4,8)print('data_8',data_8)path = list(eval(data_6).values())[0]new_str = list(jsonpath.jsonpath(eval(data_7),path))[0]data_9 = data_8.replace(path,new_str)print('data_9',data_9)
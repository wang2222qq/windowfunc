#-*- coding:utf-8 -*-

try:
    from openpyxl.worksheet import worksheet
except ImportError as e:
    print("you need install openpyxl module")
    raise

def ReadLine(ws):
    '''
    逐行读取工作簿中的内容
    '''
    if not isinstance(ws, worksheet.Worksheet):
        raise TypeError("parament type is openpyxl.worksheet.worksheet.Worksheet")
    
    for row in ws.rows:
        yield [x.value for x in row]

if __name__ == '__main__':
    try:
        from openpyxl import load_workbook
    except ImportError as e:
    print("you need install openpyxl module")
    raise
    
    wb = load_workbook('test.xlsx')
    ws = wb.active
    for line in ReadLine(ws):
        print(line)
    
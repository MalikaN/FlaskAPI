from flaskext.mysql import MySQL

mysql = MySQL()

def create_user(email,password):
    conn = mysql.connect()
    cursor = conn.cursor()
    __userEmail = email
    __password = password
    cursor.callproc('spCreateUser',(__userEmail,__password))
    data = cursor.fetchall()
    
    if len(data) is 0:
        conn.commit()
        return {'StatusCode':'200','Message': 'User creation success'}
    else:
        return {'StatusCode':'1000','Message': str(data[0])}

def get_all_items():
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('spGetItems')
    data = cursor.fetchall()

    item_List = []

    for item in data:
        i = {
            'ItemName' : item[0],
            'itemPrice' : item[1],
            'Itemqty' : item[2]
            }
        item_List.append(i)

    return {'StatusCode':'200','Items':item_List}

def get_item(id):
    __id = id
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('spGetItem',(__id,))
    data = cursor.fetchall()

    items = []

    for item in data:
        i = {
            'ItemName' : item[0],
            'itemPrice' : item[1],
            'Itemqty' : item[2]
            }
        items.append(i)

    return {'StatusCode':'200','Items':item}


def add_items(iName, iPrice, iQty):
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('spAddItem',(iName,iPrice,iQty))
    data = cursor.fetchall()

    if len(data) is 0:
        conn.commit()
        return {'StatusCode':'200','Message': 'Item added Successfully'}
    else:
        return {'StatusCode':'1000','Message': 'Error Occured'}


def authenticate_user(username,password):
    conn = mysql.connect()
    cursor = conn.cursor()

    cursor.callproc('spAuthenticateUser',(username,))
    data = cursor.fetchall()

    if (len(data)>0):
        if(str(data[0][2]) == password):
            return {'status':200,'UserId':'Login Success'}
        else:
            return {'status':100,'message':'Authentication failure'}


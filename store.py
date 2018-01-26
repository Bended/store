from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql

connection = pymysql.connect(host = 'localhost',
                            user = 'root',
                            password = 'bended77',
                            db = 'store',
                            charset = 'utf8',
                            cursorclass = pymysql.cursors.DictCursor)

@get("/admin")
def admin_portal():
	return template("pages/admin.html")

@get("/")
def index():
    return template("index.html")

@get('/js/<filename:re:.*\.js>')
def javascripts(filename):
    return static_file(filename, root='js')


@get('/css/<filename:re:.*\.css>')
def stylesheets(filename):
    return static_file(filename, root='css')


@get('/images/<filename:re:.*\.(jpg|png|gif|ico)>')
def images(filename):
    return static_file(filename, root='images')


#######   CREATE CATEGORIES    ######
@route("/category", method='POST')
def add_category():
    new_category = request.POST.get('name')
    try:
        with connection.cursor() as cursor:
            sql = ("INSERT INTO category VALUES(id, %s)")
            data = (new_category)
            cursor.execute(sql, data)
            idNewCat = cursor.lastrowid
            connection.commit()
            return json.dumps({'STATUS':'SUCCESS', 'CAT_ID':idNewCat})
    except Exception as e :
        print e
        return json.dumps({'STATUS':'ERROR', 'MSG': str(e)})


#######   DELETE CATEGORIES    ######
@route("/category/<catId>", method='DELETE')
def delete_category(catId):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM category WHERE id = {}'.format(catId))
            cursor.execute(sql)
            connection.commit()
            return json.dumps({'STATUS':'SUCCESS', 'MSG': 'The category was deleted successfully'})
    except Exception as e:
        return json.dumps({'STATUS':'ERROR', 'MSG': e})


#######   GET CATEGORIES    ######
@route("/categories", method='GET')
def load_categories():
    try:
        with connection.cursor() as cursor:
            sql = "SELECT * FROM category"
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS' : 'SUCCESS', 'CATEGORIES':result})
    except Exception as e:
        return json.dumps({'STATUS' : 'ERROR', 'MSG': e})


####### DELETE A PRODUCT  ######
@route('/product/<pid>', method='DELETE')
def delete_product(pid):
    print pid
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM products WHERE id = {}'.format(pid))
            cursor.execute(sql)
            connection.commit()
            return json.dumps({'STATUS':'SUCCES', 'MSG':'The product was deleted successfully'})
    except Exception as e:
        print e
        return json.dumps({'STATUS':'ERROR', 'MSG': e})            


#######   GET PRODUCTS    ######
@route("/products", method='GET')
def load_products():
    try:
        with connection.cursor() as cursor:
            sql = ('SELECT category, description, price, title, favorite, img_url, id FROM products')
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','PRODUCTS': result})
    except Exception as e:
        return json.dumps({'STATUS':'ERROR', 'MSG': e})


#######   GET PRODUCT    ######
@route("/product/<pid>", method='GET')
def load_products(pid):
    try:
        with connection.cursor() as cursor:
            sql = ('SELECT category, description, price, title, favorite, img_url, id FROM products')
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','PRODUCTS': result})
    except Exception as e:
        return json.dumps({'STATUS':'ERROR', 'MSG': e})




######     List Products by Category     #######
@route('/category/<id>/products', methode='GET')
def list_products_cat(id):
    #id = request.GET.get('id')
    try:
        with connection.cursor() as cursor:
            sql = ('SELECT category, description, price, title, favorite, img_url, id FROM products WHERE category = {}'.format(id) )
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','PRODUCTS': result})
    except Exception as e:
        return json.dumps({'STATUS':'ERROR', 'MSG': e})


'''
#######   ADD/EDIT A PRODUCT    ######
@route("/product", method="POST")
def add_product():
return "plouf"
'''


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
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
        return json.dumps({'STATUS':'ERROR', 'MSG': str(e)})


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
        return json.dumps({'STATUS' : 'ERROR', 'MSG': str(e)})


####### DELETE A PRODUCT  ######
@route('/product/<pid>', method='DELETE')
def delete_product(pid):
    try:
        with connection.cursor() as cursor:
            sql = ('DELETE FROM products WHERE id = {}'.format(pid))
            cursor.execute(sql)
            connection.commit()
            return json.dumps({'STATUS':'SUCCES', 'MSG':'The product was deleted successfully'})
    except Exception as e:
        print e
        return json.dumps({'STATUS':'ERROR', 'MSG': str(e)})            


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
        return json.dumps({'STATUS':'ERROR', 'MSG': str(e)})


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
        return json.dumps({'STATUS':'ERROR', 'MSG': str(e)})


######     List Products by Category     #######
@route('/category/<id>/products', methode='GET')
def list_products_cat(id):
    try:
        with connection.cursor() as cursor:
            sql = ('SELECT category, description, price, title, favorite, img_url, id FROM products WHERE category = {}'.format(id) )
            cursor.execute(sql)
            result = cursor.fetchall()
            return json.dumps({'STATUS':'SUCCESS','PRODUCTS': result})
    except Exception as e:
        return json.dumps({'STATUS':'ERROR', 'MSG': str(e)})


#######   ADD/EDIT A PRODUCT    ######
@route("/product", method="POST")
def add_product():
    id = request.POST.get('id')
    print id
    category = request.POST.get('category')
    print category
    title = str(request.POST.get('title'))
    print title
    description = str(request.POST.get('desc'))
    print description
    price = request.POST.get('price')
    print price
    favorite = request.POST.get('favorite')
    print favorite
    if favorite == None:
        n_fav = 0
    else:
        n_fav = 1
    print n_fav
    img_url = request.POST.get('img_url')
    print img_url
    if id != '':
        try:
            with connection.cursor() as cursor:
                print 'la'
                sql = ('UPDATE products SET category=%s, title=%s, description=%s, price=%s, favorite=%s, img_url=%s WHERE id=%s')
                data = (category,str(title),str(description),price,n_fav,str(img_url), id)
                cursor.execute(sql, data)
                connection.commit()
                return json.dumps({'STATUS':'SUCCESS', 'MSG':'The product was added/updated successfully'})
        except Exception as e:
            print e
            return json.dumps({'STATUS':'ERROR', 'MSG':str(e)})
    else:
        print 'ici'
        try:
            print 're-ici'
            with connection.cursor() as cursor:
                #sql = "INSERT INTO products VALUES(id, {}, {}, {}, {}, {}, {})".format(category, title, description, price, n_fav, img_url)
                sql = 'INSERT INTO products VALUES(id,%s,%s,%s,%s,%s,%s)'
                data = (category,title,description,price,n_fav,img_url)
                print data
                cursor.execute(sql, data)
                connection.commit()
        except Exception as e:
            print e
            return json.dumps({'STATUS':'ERROR', 'MSG':str(e)})


def main():
    run(host='localhost', port=7000)

if __name__ == '__main__':
    main()
from bottle import route, run, template, static_file, get, post, delete, request
from sys import argv
import json
import pymysql

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
    # CREATE THE CATEGORY IN THE DB
    if #200 - category already exists :
        return json.dumps({'STATUS':'ERROR', 'MSG':'Category already exists'}})
    elif :#400 - bad request
        return json.dumps({'STATUS':'ERROR', 'MSG':'Name parameter is missing'}})
    elif :#500 - internal error :
        return json.dumps({'STATUS':'ERROR', 'MSG':'internal error '}})
    else: #201 - category created successfully 
        return json.dumps({"STATUS" : "SUCCESS", 'CAT_ID': #Id of the new CATEGORY})


#######   DELETE CATEGORIES    ######
@route("/category/é"+ catId, method='DELETE')
def delete_category():
    #DELETE THE CATEGORY ID IN THE DB
    if #CODE 404 CATEGORY NOT FOUND
        return json.dumps({'STATUS':'ERROR', 'MSG':'Category not found'})
    elif ##CODE 500 INTERNAL ERROR:
        return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error'})
    else:  #  CODE 201 - category deleted successfully
        return json.dumps({'STATUS':'SUCCESS', 'MSG':'The category was deleted successfully'})


#######   GET CATEGORIES    ######
@route("/categories", method='GET')
def loadCategories():
    #DATA BASE REQUEST 
    if #STATUS SUCCESS CODE 200
        return json.dumps({'STATUS':'SUCCESS', 'CATEGORIES': [{'id':<cat_id>,'name':<cat_name>},{'id':<cat_id>,'name':<cat_name>}]})
    else:#STATUS ERROR CODE 500
        return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error'})


####### DELETE A PRODUCT  ######
@route('/product/' + pid, method='DELETE')
def delete_product():
    #DELETE THE PRODUCT ID IN THE DB
     if #CODE 404 PRODUCT NOT FOUND
        return json.dumps({'STATUS':'ERROR', 'MSG':'Category not found'})
    elif ##CODE 500 INTERNAL ERROR:
        return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error'})
    else:  #  CODE 201 - PRODUCT deleted successfully
        return json.dumps({'STATUS':'SUCCESS', 'MSG':'The product was deleted successfully'})


#######   GET PRODUCTS    ######
@route("/products", method='GET')
def get_products():
    #DATA BASE REQUEST 
    if #STATUS SUCCESS CODE 200
        return json.dumps({'STATUS':'SUCCESS','PRODUCTS':[{"category": 16, "description": "this is great", "price": 1000.0, 
                                        "title":"honda2", "favorite": 0, "img_url": "https://images.honda.ca/v.png", "id":1}]})
    else: #code 500 - internal error
        return json.dumps({'STATUS':'ERROR', 'MSG':'internal error'})


######     List Products by Category     #######
@route(' /category/<id>/products', methode='GET')
def list_products_cat():
    #REQUEST CATEGORY ID
    if #CODE 404 - category not found OR #CODE 500 internal Error
        return json.dumps({'STATUS':'ERROR', 'MSG':'Internal error'})
    else #CODE 200 Success
        return json.dumps({'STATUS':'SUCCESS', 'PRODUCTS':[{"category": 16, "description": "this is great", "price": 1000.0, 
                                            "title":"honda2", "favorite": 0, "img_url": "https://images.honda.ca/v.png", "id":1}]})

#######   ADD/EDIT A PRODUCT    ######
@route("/product", method="POST")
def add_product():


#run(host='0.0.0.0', port=argv[1])
run(host='localhost', port=7000)
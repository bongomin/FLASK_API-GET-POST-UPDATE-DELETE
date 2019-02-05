from flask import Flask,jsonify 

app=Flask(__name__)
languages =[
    {'name':'python'},
    {'name':'javascript'},
    {'name':'ruby on rails'},
    {'name':'java'},
    {'name':'php'},
    {'name':'Django'}

]

@app.route('/',methods =['GET'])
def hello():
    return jsonify({'greeting':'hello daniel'})
# get reuest
@app.route('/lang',methods=['GET'])
def allposts():
    return jsonify({'languages':languages})

# returning one at atime
# rturning one
@app.route('/lang/<string:name>', methods=['GET'])
def returnone(name):
    langs =[language for language in languages if language['name']==name]
    return jsonify({'language':langs[0]})

# get 
@app.route('/lang',methods=['GET'])
def addone():
    language= { 'name' :request.json['name']}
    languages.append(language)
    return jsonify({'languages':languages})

# editing
@app.route('/lang/<string:name>',methods=['PUT'])
def editone():
    langs=[language for language in languages if language['name']==name]
    langs[0]['name']=request.json['name']
    return jsonify({'language':langs[0]})


# deleting api 
@app.route()
def deleteone():
    langs=[language for language in languages if language['name']==name]
    languages.remove(lang[0])
    return jsonify({'languages':languages})








if __name__=='__main__':
    app.run(debug=True)
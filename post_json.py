import requests, json

def send_post(action, dct):

    r = requests.post(
        'http://127.0.0.1:8000/books/book_'+action+'/',
        data=json.dumps(dct),
        timeout=10,
        headers={
        	'Authorization': 'Token 810dd0253449c5c215c6a82cf83e9184d3273202',
        }
    )

    print(r.content)

def send_post_auth():

    r = requests.get(
        'http://127.0.0.1:8000/book/',
        timeout=10,
        headers={
        	'Authorization': 'Token 810dd0253449c5c215c6a82cf83e9184d3273202',
        }
    )

    print(r.content)

# run the following commands in sequence, one at a time

# send_post('create', {'docs':[{'title':'ddd', 'author_key':['lll'], 'seed':['/works/hhh']}]})
# send_post('delete', {'title':'Spacecraft Stickers'})
# send_post('update', {'title':'Spacecraft (Topics)', 'updates':{'title':'ddd'}})
# send_post('retrieve', {'title':'ddd'})
# send_post('retrieve', {'author_key':'lll'})
send_post('retrieve', {'author_key':'lll'})
# send_post_auth()
import requests,json

# varaibles
# ============================================
base_url = 'https://gorest.co.in/'
path = 'public/v2/users/'
token = {'Authorization':'Bearer 1cf43121631cc6c7a46256cbe945e80583890233f46d10e5684e2d7a02f10a7b'}

# REQUESTS functions
# ===============================================
def get_request(user_id=''):
    url = base_url + path + f'{user_id}'
    # If params are required, then it should be as below
    # params = {'id':6850171}  # dic should be created for params
    response = requests.get(url,timeout=5)  # by default the time will be in sec

    if response.status_code == 200:
        print("Get request was successful")
        print(json.dumps(response.json(),indent=4))
        print("===================================")
    else:
        print("Get request was unsuccessful with status code: ",response.status_code)

    # Note :
    # Using response.json() is convenient because it automatically handles the process of converting the JSON format response into a Python data structure. This saves you from having to manually parse the response body using libraries like json
    # I use assert to put some simple validation check points.
    # assert response.status_code == 200, assert response.json()['name'] == 'Amb. Agnimitra Nehru'



def post_request():
    url = base_url + path
    json_data = {
    'name': 'JK',
    'email': 'jk@automation.com',
    'gender': 'male',
    'status': 'active'
    }
    response = requests.post(url,json=json_data,headers=token)
    # json should be passed in json not in data, data is for passing dic values which later will be converted to json
    # the json parameter expects python data format not JSON format data, before sending the request it will only make that conversion
    # token should be passed with headers & auth parameter is for other type of authencation like username and password.

    if response.status_code == 201:
        print("Post request was successful")
        print(json.dumps(response.json(),indent=4))
        print("===================================")
    else:
        print("Post request was unsuccessful with status code: ",response.status_code)

    assert response.json()['name']=='JK'
    return  response.json()['id']
    # print(response.headers)

def put_request(user_id):
    url = base_url + path + f'{user_id}'
    json_data = {
        'name': 'SS',
        'email': 'ss@automation.com',
        'gender': 'male',
        'status': 'active'
    }
    # for put I need to resend the whole json again with the updated data

    response = requests.put(url,json=json_data,headers=token)
    if response.status_code==200:
        print("Put request was successful")
        print(json.dumps(response.json(),indent=4))

    else:
        print("Put request was unsuccessful")

    assert response.json()['name'] == 'SS'
    return response.json()['id']

def delete_request(user_id):
    url = base_url + path + f'{user_id}'
    response = requests.delete(url,headers=token)
    if  response.status_code==204:
        print('delete request was successful')
    else:
        print('The delete request was unsuccessful')




# CALLING
# =================================================
get_request()
# get_request('6850155')

post_id = post_request()
print(post_id)
print("===================================")


put_id = put_request(post_id)
print(put_id)
print("===================================")

delete_request(put_id)
import requests,json

def create_new_user(end_point,title):
    base_url = 'https://jsonplaceholder.typicode.com'
    url = base_url+end_point

    # file = open('C:/Users/samarth.kulkarni/PycharmProjects/RobotFramework-API/data.json','r')
    # # json_data= file.read()
    # data = json.loads(json_data)

    with open('C:/Users/samarth.kulkarni/PycharmProjects/RobotFramework-API/data.json') as json_file:
        json_data=json.load(json_file)

    json_data['title']=title
    print(json_data)
# json.load() is used to read & give back the JSON data from file i.e. .json file & convert it to python structure.
# json.loads() is used to covert the JSON string to oython format.


    headers= {
        'Content-Type':'application/json'
    }
    response = requests.post(url=base_url+end_point,json=json_data,headers=headers)
    if response.status_code==201:
        print('Post request was successful')
    else:
        print('Post request was not successful')
    print(response.json())
    return response.json()['id']
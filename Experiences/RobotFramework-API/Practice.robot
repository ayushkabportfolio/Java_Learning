*** Settings ***
Library    RequestsLibrary
Library    Collections
Library    JSONLibrary

*** Variables ***
${base_url}    https://jsonplaceholder.typicode.com

*** Test Cases ***
get request demo
     # without params
#     ${response}=    GET    https://reqres.in/api/users    expected_status=200

     # with params i.e. query params(here params means they will be query params only)
#     ${response}=    GET    https://reqres.in/api/users    params=page=2    expected_status=200

# Note :
#1. if the params to be passed are more than one, then better to create a dic & pass that dic to params
     ${my_dic}=    create dictionary    page=2    id=10
     ${response}=    GET    https://reqres.in/api/users    params=${my_dic}   expected_status=200
        # ${response} is a response object which will have many components in it.

#2 . here is expected_status is not mandatory to check, the GET keyword is by default fail if status is of error, I can use this to check status!=200 case.

# Validation
    log    ${response.status_code}
    should be equal as numbers    ${response.status_code}    200    # status_code=expected_status above

    log    ${response.json()}    # It will give us the parsed json response i..e in python format.
    should be equal as strings    ${response.json()}[data][first_name]    Byron
    # Note : In robotframework for dic i need not give the key in quotes to fetch it's value

    log    ${response.headers}
    should contain    ${response.headers}[Content-Type]    application/json
    # Note headers is by deafult a dic, so I can directly make use of

    log    ${response.headers}
    should be equal as strings    ${response.headers}[Content-Type]    application/json; charset=utf-8

    log    ${response.cookies}

post request demo
    ${json}=    create dictionary    title=OMG1    body=WOW!  userId=1
    ${response}=    POST     ${base_url}/posts   json=${json}    # here json will seralize the json data.

    log    ${response.status_code}
    should be equal as numbers    ${response.status_code}    201

    log    ${response.json()}
    ${id}=    set variable    ${response.json()}[id]
    set global variable    ${id}

put request demo
    ${json}=    create dictionary    title=OMG2    body=WAAH!  userId=2
    ${response}=    PUT     ${base_url}/posts/${id}   json=${json}

    log    ${response.status_code}
    should be equal as numbers    ${response.status_code}    200

    log    ${response.json()}
    should be equal as strings    ${response.json()}[name]    OMG2
    should be equal as numbers    ${response.json()}[userId]    2


delete request demo
    ${response}=    delete     ${base_url}/posts/${id}
    should be equal as numbers    ${response.status_code}    204



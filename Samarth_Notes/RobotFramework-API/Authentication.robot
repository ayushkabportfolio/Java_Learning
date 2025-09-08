Authencation Types
======================
Authentication is for hitting the request to API

There are different types of authentication types i.e.
- Basic(UserName & Password)
- Bearer(Token)
- API Key

These auths are for all types of requests i.e. GET, POST etc... & can be provided with the respective keywords or in 'create session' keyword.
Usually GET will not have authentication

*** Settings ***
Library    RequestsLibrary

*** Variables ***
${base_url}    https://www.google.com

*** Test Cases ***
basic auth
    # should be passed as list/tuple
    ${auth}=    create list    UserName    Password
#    create session    mysession    auth=${auth}
    ${response}=    GET    ${base_url}/2    auth=${auth}
    log    ${response}

bearer token
# It should be passed as header
# headers should be passed as dic to requests
# It should be passed as - Bearer <Token> for 'Authorization'    key
# It can be passed with 'create session' or the requests keyword

    ${headers}=    create dictionary    Autorization=Bearer EEEETT68Y38Y9U19U91U91U91U
    ${response}=    POST    url    json    headers=${headers}
    log    ${response}


# Note: API Key
# The API key authentication is usually not used, if used it will be generally for GET request.
# I need to pass the api key in params as key=API_KEY
# The params are passed as dic for GET.


# Bearer token is the one which is most widely used.







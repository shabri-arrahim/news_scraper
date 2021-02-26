API End-Point
-------------

This API requires authenticating to LinkedIn in order to run any processes you want.

An endpoint for performing authentication is provided (endpoint with authentication category).

All you have to do is, first check whether your account requires a verification pin email to log in with the endpoint provided (the route will be: "/ auth / check_verification"),
if the response you get is "True", When you access the route "/ auth" (to login) you have to send a verification pin email via the provided endpoints (the route will be: "/ auth / verification").

================  ==============================================================  ===========================================  =================  ===============  ===============  =============
Category          Description                                                     Endpoint                                     Parameters         Data             Headers          Method
================  ==============================================================  ===========================================  =================  ===============  ===============  =============
Authentication    To check if the account need a verification PIN or not          /auth/check_verification                     None               username         None             POST
                                                                                                                                                  password         
Authentication    Make authentication to LinkedIn Service (Login handler)         /auth                                        None               username         None             POST
                                                                                                                                                  password
Authentication    When making authentication to LinkedIn Service, sometimes       /auth/verification                           None               email pin        None             POST
                  LinkedIn needs an email verification pin to make the session.
                  This endpoint use for it.
People            Search People                                                   /people/search_people                        url or keywords    None             Proxy            GET
                                                                                                                                                                   Cookie
People            Get People Profile                                              /people/profile/{people_public_id}           None               None             Proxy            GET
                                                                                                                                                                   Cookie
People            Make Connection and Send Message                                /people/make_connection/{people_public_id}   None               Message          Proxy            POST
                  (Message length must be < 300)                                                                                                                   Cookie
Message           Get all conversation in conversation field                      /message/conversations                       None               None             Proxy            GET
                                                                                                                                                                   Cookie
Message           Get message detail from a specific user                         /message/detail/{people_public_id}           None               None             Proxy            GET
                                                                                                                                                                   Cookie
Message           Send message to a specific conversation                         /message/{conversation_id}                   None               Message          Proxy            POST
                                                                                                                                                                   Cookie
================  ==============================================================  ===========================================  =================  ===============  ===============  =============


Data, Parameters and Headers explanation and formating
------------------------------------------------------

- **username**: is a user username for LinkedIn (e.g. bryan@mail.com) 
- **password**: is a user password for LinkedIn 
- **proxy**: is using for make sure the connection is secure and to avoid LinkedIn to block an account (format: {"proxy_username": "xyz", "proxy_password": "xyz", "proxy_host": "123.12.123.12",  "proxy_port": "1234"})
- **cookie**: is using for authenticate user (fromat: {"JSESSIONID": "value", "bcookie": "value", "bscookie": "value", "lang": "value", "li_at": "value", "lidc": "value"})
- **url**: URL for people search on linkedin(e.g. https://www.linkedin.com/search/results/people/?keywords=programmer%26origin=SWITCH_SEARCH_VERTICAL)
- **people_public_id**: is a people public identity on LinkedIn (e.g alexanderschelchere)
- **conversation_id**: is a unique number (id) for a conversation on LinkedIn (e.g. 6762640841480773632)

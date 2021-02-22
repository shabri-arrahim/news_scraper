
================  ==============================================================  =====================================  =================  ===============  =============
Category          Description                                                     Endpoint                               Parameters         Data             Method
================  ==============================================================  =====================================  =================  ===============  =============
Authentication    Make authentication to LinkedIn Service (Login handler)         /auth                                  None               username         POST
                                                                                                                                            password
                                                                                                                                            proxies


                  When making authentication to LinkedIn Service, sometimes       /auth/verification
                  LinkedIn needs an email verification pin to make the session.
                  This endpoint use for it
                  
Enumerated list   1. items use any variation of "1.", "A)", and "(i)"
                  #. also auto-enumerated
Definition list   Term is flush-left : optional classifier
                      Definition is indented, no blank line between
Field list        :field name: field body
Option list       -o  at least 2 spaces between option & description
================  ==============================================================  =====================================  =================  ===============  =============

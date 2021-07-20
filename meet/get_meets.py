def get_meet(userdata):
    import imaplib                              
    import email
    from email.header import decode_header
    import webbrowser
    import os
    import sys
    conn = imaplib.IMAP4_SSL("imap.gmail.com")

    try:
        (retcode, capabilities) = conn.login(userdata["email"], userdata["password"])
    except:
        print(sys.exc_info()[1])
        sys.exit(1)
    conn.list()
    conn.select(readonly=1) # Select inbox or default namespace
    (retcode, messages) = conn.search(None, '(UNSEEN)')
    links = []
    if retcode == 'OK':
        for num in messages[0].decode().split(' '):
            typ, data = conn.fetch(num,'(RFC822)')
            for response in data:
                if isinstance(response, tuple):
                    msg = email.message_from_bytes(response[1])
                    
                    if "meet.google.com" in response[1].decode():
                        acquired = str(response[1]).index('meet.google.com')
                        i = ""
                        acquired2 = str(response[1]).index('meet.google.com')
                        while i != " ":

                            
                            acquired2 += 1
                            i = str(response[1])[acquired2]
                            if i =="<" or i ==">" or i =="\"" or i =="\\":
                                break
                        

                        
                        link = "https://"+str(response[1])[acquired:acquired2]
                        if "authuser=" in link:
                            link = link[:link.index("authuser=")+8]+"=2"+link[link.index("authuser=")+10:]
                        elif not "lookup" in link:
                            link += "?authuser=2"
                            
                        links.append(link)
                    
    conn.close()
    return links

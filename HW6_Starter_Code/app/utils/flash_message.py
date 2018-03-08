def flash_message(session, text=None):
    msg = session.pop('flash_message', None)
    if text:
        session['flash_message'] = text

    return msg

        
    

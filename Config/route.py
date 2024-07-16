def routes():
    _return = []
    from Application.User import UserHandler, UserAvatorHandler
    _return.append((r"/", UserHandler))
    _return.append((r"/avator", UserAvatorHandler))
    return _return
def routes(async_session):
    _return = []
    from Application.User import UserHandler, UserAvatorHandler
    _return.append((r"/", UserHandler, dict(session=async_session)))
    _return.append((r"/avator", UserAvatorHandler))
    return _return
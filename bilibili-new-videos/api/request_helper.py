from cookie_request import request_with_cookie


def request_get(url: str, params: dict):
    """发送GET请求

    Args:
        url (str): _description_
        params (dict): _description_
    """
    url += "?"
    for k, v in params.items():
        url += "&" + k + "=" + "v"

    return request_with_cookie(url)

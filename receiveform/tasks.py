

from celery import task




def mock_send_mail(entity):
    """

    A mocked out email for new
    :param self:
    :param entity:
    :return:
    """
    print("sent email to {0} having public token {1}".format(entity.email,entity.private_key))
    return True

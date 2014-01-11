# _*_ coding: utf-8  _*_

import string
import random
import os

from datetime import datetime

INSTANCE_FOLDER_PATH = os.path.join('/tmp', 'instance')

ALLOWED_AVATAR_EXTENSIONS = set(['png', 'jpg', 'jpeg', 'gif'])


# Form validation

USERNAME_LEN_MIN = 4
USERNAME_LEN_MAX = 20

REALNAME_LEN_MIN = 4
REALNAME_LEN_MAX = 20

PASSWORD_LEN_MIN = 6
PASSWORD_LEN_MAX = 16

AGE_MIN = 1
AGE_MIN = 200

# Sex Type

MALE = 1
FEMALE = 2
OTHER = 9
SEX_TYPE = {
    MALE: u'Male',
    FEMALE: u'Female',
    OTHER: u'Other',
}


def get_current_time():
    return datetime.utcnow()

def pretty_date(dt, default=None):
    """
    Returns string representting "time since" e.g.
    3 days ago, 5 hours age etc.
    Ref: https://bitbucket.org/danjac/newsmeme/src/a281babb9ca3/newsmeme/
    """

    if default is None:
        default = 'just now'

    now = datetime.utcnow()
    diff = now - dt

    periods = (
        (diff.days / 365, 'year', 'years'),
	(diff.days / 30, 'month', 'months'),
	(diff.days / 7, 'week', 'weeks'),
	(diff.days, 'day', 'days'),
	(diff.seconds / 3600, 'hour', 'hours'),
	(diff.seconds / 60, 'minute', 'minutes'),
	(diff.seconds, 'second', 'seconds'),
    )
    

    for period, singular, plural in periods:
        if not period:
	    continue

	if period == 1:
	    return u'%d %s ago' % (period, singular)
	else:
	    return u'%d %s ago' % (period, plural)

    return default


def allowed_file(filename):
    return '.' in filename and file.rsplit('.', 1)[1] in ALLOWED_AVATAR_EXTENSIONS

def id_generator(size=10, chars=string.ascii_letters + string.digits):
    return ''.join(random.choice(chars) for x in range(size))


def make_dir(dir_path):
    try:
        if not os.path.exists(dir_path):
	    os.mkdir(dir_path)
    except Exception, e:
        raise e

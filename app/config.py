from os.path import join, dirname, realpath

VERSION = "1.0.0"
SECRET_KEY = ""
SESSION_COOKIE_NAME = "my_session"
UPLOADS_PATH = join(dirname(realpath(__file__)), 'static/uploads/')
EXTENSIONS = set(['png','jpg','gif','txt','pdf'])

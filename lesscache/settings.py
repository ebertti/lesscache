from lesscache.helper import import_string

MEMCACHE_MAX_KEY_LENGTH = 250

class Settings(object):

    def __init__(self, **kwargs):
        # defaults
        self.encode = 'lesscache.encode.PickleEncode'
        self.timeout = 120

        self.table_name = 'less_cache'
        self.key_column = 'less_key'
        self.expiration_column = 'less_expiration'
        self.content_column = 'less_content'

        self.aws_access_key_id = None
        self.aws_secret_access_key = None
        self.aws_region_name = None

        self.version = 1
        self.key_prefix = 'less'
        self.key_func = lambda p, k, v: f'{p}:{k}:{v}'

        self.read_capacity_units = 1
        self.write_capacity_units = 1

        for key, value in kwargs.items():
            setattr(self, key, value)

    def get(self, key):
        value = getattr(self, key)
        if not value:
            raise AttributeError('Key %s not exists in settings', key)

        return value

    def module(self, key, *args, **kwargs):
        path = self.get(key)
        return import_string(path)

    def instance(self, key, *args, **kwargs):
        path = self.get(key)
        return import_string(path)(*args, **kwargs)

    def __getitem__(self, key):
        return self.get(key)




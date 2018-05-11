import functools

from .models import Asset


class ion_test(object):

    def __init__(self, do_test):
        self.do_test = do_test
        functools.update_wrapper(self, do_test)


    def __call__(self, *args, **kwargs):
        assets = [arg for arg in args if type(arg) is Asset]

        for asset in assets:
            asset.reserve()

        try:
            self.do_test(*args, **kwargs)
        except Exception as err:
            result = False, err
        else:
            result = True, None

        for asset in assets:
            asset.relinquish()

        return result
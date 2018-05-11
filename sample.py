#!/usr/bin/env python
import os
import django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "ion.settings")
django.setup()

from butts.models import Butt
from butts.services import test_smelliness



if __name__ == '__main__':
    print("ad hoc (no database record):")
    adhoc_butt = Butt(host="localhost")
    test_smelliness(adhoc_butt)

    print("from database:")
    shared_butt = Butt.objects.first()
    test_smelliness(shared_butt)
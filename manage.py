#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

    # Here, set your child apps of web site
    # And, in application folder,
    # it has 'frontend', 'backend', and public 'about' applications
    # sys.path.append('/opt/www/mysite/application')
    # sys.path.append('/opt/www/mysite/mysite')

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)

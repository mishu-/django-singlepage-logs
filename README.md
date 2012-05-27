django-singlepage-logs
======================

The module brings Django support for retrieving logs from django single-page apps.
It contains a Django middleware class `singlepagelogs.middleware.HeaderLoggingMiddleware` that looks for logs in HTTP request headers and hands them off to the Django logging system. 
This enables server-side retrieval for single-page javascript apps who piggyback logging information back to the server through their regular ajax requests.

Installation
------------

Add `singlepagelogs.middleware.HeaderLoggingMiddleware` to the 
``MIDDLEWARE_CLASSES`` tuple in your settings file. There are three settings that you should also customize in your settings file:

* LOGGER_HTTP_HEADER

~~~
    #this is the http header the middleware looks at for logs
    #must be formatted according to the django request.META object format
    #if not present, default to 'HTTP_LOGS'
    LOGGER_HTTP_HEADER = 'HTTP_APPX_LOGS'
~~~  
  
* LOGGER_URLS

~~~
    #the middleware looks for logs only in requests that start with these urls 
    #if not present, defaults to ['/api']
    LOGGER_URLS = ['/api']
~~~

* LOGGER_NAME

~~~
    #Logging module name; must be pre-defined in the settings.py LOGGING variable
    LOGGER_NAME = 'django.request'
~~~
    
TODO
----

1. Add example application
2. Add unit tests

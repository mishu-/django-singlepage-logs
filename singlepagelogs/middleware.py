"""
The MIT License (MIT)
Copyright (C) 2012 Mihai Oprea <mihai@mihaioprea.com>

Permission is hereby granted, free of charge, to any person obtaining a copy of 
this software and associated documentation files (the "Software"), to deal in 
the Software without restriction, including without limitation the rights to use,
copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, 
and to permit persons to whom the Software is furnished to do so, 
subject to the following conditions:

The above copyright notice and this permission notice shall be included in all 
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, 
INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR 
PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE 
FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, 
ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import logging
import simplejson

from django.conf import settings

class HeaderLoggingMiddleware:
    
    #log levels
    NONE = 0
    CRITICAL = 1
    ERROR = 2
    WARNING = 3
    INFO = 4
    DEBUG = 5
    
    def __init__(self):
        #set logger defaults if settings.py wasn't set up correctly
        if 'LOGGER_HTTP_HEADER' not in dir(settings):
            settings.LOGGER_HTTP_HEADER = 'HTTP_LOGS'
        
        if 'LOGGER_URLS' not in dir(settings):
            settings.LOGGER_URLS = ['/api']
            
        #if no other logger is specified in settings.py
        #use default django.request logger
        if 'LOGGER_NAME' not in dir(settings):
            self.logger = logging.getLogger('django.request') 
        else:
            self.logger = logging.getLogger(settings.LOGGER_NAME) 
       
    
      
    def process_request(self, request):
        """
            Intercept requests and strip logs from their http headers
            Expected logs are a list of json objects of the form:
            
            [{'l': log_level, 'm': log_message},
             {'l': log_level, 'm': log_message},
             ...
             {'l': log_level, 'm': log_message}]
             
            Feel free to modify this in order to accomodate other formats
            
            Log levels are defined as class variables
        """
        process_logs = False
        for path in settings.LOGGER_URLS:
            process_logs = request.META['PATH_INFO'].startswith(path)
        
        if process_logs and settings.LOGGER_HTTP_HEADER in request.META:
            try:
                logs = simplejson.loads('%s' % request.META[settings.LOGGER_HTTP_HEADER])
                for log in logs:
                    if log['l'] == self.CRITICAL:
                        self.logger.critical(log['m'])
                    elif log['l'] == self.ERROR:
                        self.logger.error(log['m'])
                    elif log['l'] == self.WARNING:
                        self.logger.warning(log['m'])
                    elif log['l'] == self.INFO:
                        self.logger.info(log['m'])
                    else:
                        self.logger.debug(log['m'])
                        
            except Exception as e:
                self.logger.error("HeaderLoggingMiddleware - invalid log format: %s" 
                    % (request.META[settings.LOGGER_HTTP_HEADER]))
            
            
            

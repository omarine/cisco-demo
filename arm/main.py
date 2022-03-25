from bottle import Bottle, request, response
from datetime import datetime
from functools import wraps
import logging
import os
import config as config

try:
    directory = os.environ['CAF_APP_LOG_DIR'] + "/"
except KeyError as e:
    # print(str(e) + " is non-existent")
    directory = "./"

logger = logging.getLogger('webapp')
logger.setLevel(logging.INFO)
file_handler = logging.FileHandler(directory + 'webapp.log')
formatter = logging.Formatter('%(msg)s')
file_handler.setLevel(logging.DEBUG)
file_handler.setFormatter(formatter)
logger.addHandler(file_handler)


firstname = config.cfg.get("first_name", "first")
lastname = config.cfg.get("last_name", "last")
fullname = firstname + " " + lastname

co_name = config.cfg.get("company_info", "comp_name")
co_org = config.cfg.get("company_info", "comp_org")
co_motto = config.cfg.get("company_info", "motto")


def log_to_logger(fn):
    @wraps(fn)
    def _log_to_logger(*args, **kwargs):
        request_time = datetime.now()
        actual_response = fn(*args, **kwargs)
        logger.info('%s %s %s %s %s' % (
            request.remote_addr,
            request_time,
            request.method,
            request.url,
            response.status))
        return actual_response
    return _log_to_logger


app = Bottle()
app.install(log_to_logger)


@app.route('/status/<device_id>')
def status(device_id):
    return {"system": 1, "device": str(device_id)}


@app.route('/time')
def time():
    current_time = datetime.now().isoformat(' ')
    return {
        "system": 1,
        "datetime": current_time,
        "username": fullname,
        "company": co_name,
        "org": co_org,
        "motto": co_motto
    }


app.run(host='0.0.0.0', port=8000, quiet=True)


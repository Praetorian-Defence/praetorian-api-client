import json
import uuid

from datetime import datetime, date
from decimal import Decimal


class JSONEncoder(json.JSONEncoder):
    def default(self, obj):
        if isinstance(obj, datetime):
            return obj.date().isoformat()
        elif isinstance(obj, date):
            return obj.isoformat()
        elif isinstance(obj, Decimal):
            return str(obj)
        elif isinstance(obj, uuid.UUID):
            return str(obj)
        else:
            return super(JSONEncoder, self).default(obj)

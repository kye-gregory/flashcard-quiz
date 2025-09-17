import logging
import json
import datetime as dt
import time
from typing import Any, override

LOG_RECORD_BUILTIN_ATTRS = {
    "args",
    "asctime",
    "created",
    "exc_info",
    "exc_text",
    "filename",
    "funcName",
    "levelname",
    "levelno",
    "lineno",
    "module",
    "msecs",
    "message",
    "msg",
    "name",
    "pathname",
    "process",
    "processName",
    "relativeCreated",
    "stack_info",
    "thread",
    "threadName",
    "taskName",
}


class UTCFormatter(logging.Formatter):
    converter = time.gmtime


class JSONFormatter(logging.Formatter):
    def __init__(self, *, fmt_keys: dict[str, str] | None = None):
        super().__init__()
        self.fmt_keys = fmt_keys if fmt_keys is not None else {}

    @override
    def format(self, record: logging.LogRecord) -> str:
        message = self._prepare_log_dict(record)
        return json.dumps(message, default=str)

    def _prepare_log_dict(self, record: logging.LogRecord) -> dict[str, Any]:
        # Always Fields: included in every log entry.
        always_fields = {
            "message": record.getMessage(),
            "timestamp": dt.datetime.fromtimestamp(
                record.created, tz=dt.timezone.utc
            ).isoformat(),
        }
        if record.exc_info is not None:
            always_fields["exc_info"] = self.formatException(record.exc_info)

        if record.stack_info is not None:
            always_fields["stack_info"] = self.formatStack(record.stack_info)

        # Config Fields: included if specified in the logging config file.
        config_fields = {
            key: always_fields.pop(val, None) or getattr(record, val)
            for key, val in self.fmt_keys.items()
        }
        config_fields.update(always_fields)

        # Extra Fields: included if appended to the individual log record.
        extra_fields = {
            key: val
            for key, val in record.__dict__.items()
            if key not in LOG_RECORD_BUILTIN_ATTRS
        }

        return {**config_fields, **extra_fields}

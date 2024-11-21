import time
from datetime import datetime, timezone

from hpyhrtbase import hpyhrt_context


class TimeUtil:
    @staticmethod
    def datetime_fromisoformat(datetime_str: datetime | str) -> datetime | None:
        try:
            if isinstance(datetime_str, datetime):
                return datetime_str

            if datetime_str[-1] == "Z":
                datetime_str = datetime_str[:-1] + "+00:00"

            parsed_datetime = datetime.fromisoformat(datetime_str)
        except Exception:
            return None
        return parsed_datetime

    @staticmethod
    def get_current_time_isoformat() -> str:
        local_datetime = datetime.now()
        return local_datetime.isoformat()

    @staticmethod
    def get_current_time_ms() -> int:
        millis = int(round(time.time() * 1000))
        return millis

    @staticmethod
    def get_current_time_monotonic() -> float:
        return time.monotonic()


if __name__ == "__main__":
    print(TimeUtil.get_current_time_isoformat())

# coding:utf8

from datetime import datetime, timezone, timedelta


def to_timestamp(dt_str, tz_str):
    # 获取datetime
    dt = datetime.strptime(dt_str, '%Y-%m-%d %H:%M:%S')
    # 获取hours和minutes
    hours = tz_str.split('UTC+')[-1].split(':')[0]
    hours = int(hours)
    minutes = tz_str.split('UTC+')[-1].split(':')[1]
    minutes = int(minutes)
    # 创建时区
    tz_utc = timezone(timedelta(hours=hours, minutes=minutes))
    # 加入时区
    # dt = dt.replace(tzinfo=tz_utc)
    ts = dt.timestamp()
    return ts


t1 = to_timestamp('2015-6-1 08:10:30', 'UTC+7:00')
assert t1 == 1433121030.0, t1

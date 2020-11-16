def format_duration(duration: int) -> str:
    hours, minutes_and_seconds = divmod(duration, 3600)
    minutes, seconds = divmod(minutes_and_seconds, 60)
    if hours:
        return f'{int(hours)} ч {int(minutes)} мин'
    return f'{int(minutes)} мин'

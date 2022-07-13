from dataclasses import dataclass
from datetime import datetime, timedelta
from typing import Generator, List, Tuple


@dataclass
class Movie:
    title: str
    dates: List[Tuple[datetime, datetime]]

    def schedule(self) -> Generator[datetime, None, None]:
        def datemovie():
            timeday = timedelta(days=1)
            for elem in self.dates:
                date = elem[0]
                while date <= elem[1]:
                    yield date
                    date += timeday
        return datemovie()

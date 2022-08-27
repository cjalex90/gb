from datetime import datetime


class Date:
    def __init__(self, date: str):
        self.date = date

    @classmethod
    def make_date(cls, date: str):
        day, month, year = [int(n) for n in date.split("-")]
        if cls.check_date(day, month, year):
            return cls(date)

    @staticmethod
    def check_date(day: int, month: int, year: int):
        try:
            datetime(year, month, day)
            return True
        except Exception as e:
            raise e


if __name__ == "__main__":
    mydate1 = Date.make_date("13-03-1990")
    mydate2 = Date.make_date("29-02-1990")
    print(mydate2)

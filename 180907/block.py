import datetime

def main():
  today = datetime.date.today()
  print(today)
  print(today.year, "年", today.month,"月", today.day,"日")


if __name__=="__main__":

  main()
def add_time(start, duration, week_day=""):
  st = start.split(" ")

  week_dict = {
      "Monday": 1,
      "Tuesday": 2,
      "Wednesday": 3,
      "Thursday": 4,
      "Friday": 5,
      "Saturday": 6,
      "Sunday": 7
  }

  pa = st[1]
  msg = " "
  hour = 0
  minute = 0
  day = 0
  hm = st[0].split(":")
  du = duration.split(":")
  int_hm = list(map(int, hm))
  int_du = list(map(int, du))

  zipped = list(zip(int_hm, int_du))
  result = [x + y for (x, y) in zipped]
  hour = result[0]
  minute = result[1]

  if minute >= 60:
    hour += minute // 60
    minute = minute % 60
  if hour > 24:
    day = hour // 24
    hour = hour % 24
  if hour >= 12:
    hour = hour % 12
    if pa == 'PM':
      pa = "AM"
      msg = " (next day)"
    elif pa == 'AM':
      pa = "PM"
  if day == 0:
    msg = msg
  elif day == 1 and hour != 0:
    msg = " (next day)"
  else:
    msg = f" ({day + 1} days later)"
    day = day + 1
  
  if week_day != "":
    day = day % 7
    index = week_dict[week_day.capitalize()]
    value = (index + day) % 7 
    if value== 0:
      value=(index + day)

    for k, v in week_dict.items():
      if v == value:
        week_day = ", " + k

  hour = 12 if hour == 00 else hour

  new_time = f"{hour:01}:{minute:02d} {pa}{week_day}{msg}".rstrip()
  return new_time

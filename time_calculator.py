def add_time(start, duration, day=None):
  days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday')
  
  st_time_hours = int(start.split()[0].split(':')[0])
  st_time_min = int(start.split()[0].split(':')[1])
  st_sign = start.split()[1]

  added_hours = int(duration.split(':')[0])
  added_min = int(duration.split(':')[1])

  if st_sign == 'PM':
    st_time_hours = st_time_hours + 12

  total_min = st_time_min + added_min
  res_min = total_min % 60  #result in min
  if res_min < 10:
    res_min = '0' + str(res_min)
  else:
    res_min = str(res_min)

  carried_hours = int(total_min / 60)
  total_hours = st_time_hours + added_hours + carried_hours
  check_hours = total_hours % 24

  if check_hours >= 12:
    res_sign = ' PM'
  else:
    res_sign = ' AM'

  res_hours = check_hours % 12 #result in hours
  if res_hours == 0:
    res_hours = '12'
  else:
    res_hours = str(res_hours)
    
  passed_days = int(total_hours / 24)

  if passed_days == 0:
    res_days = ''
  elif passed_days == 1:
      res_days = ' (next day)'
  else:
      res_days = ' (' + str(passed_days) + ' days later)'
  
  try:
      if day is not None:
          day = day.lower()
          if day in days:
              new_day_index = days.index(day) + passed_days
              new_day_index = new_day_index % 7
              if passed_days == 0:
                  res_days = ', ' + day.capitalize()
              elif passed_days == 1:
                  res_days = ', ' + days[new_day_index].capitalize() + ' (next day)'
              else:
                  res_days = ', ' + days[new_day_index].capitalize() + ' (' + str(passed_days) + ' days later)'
  except:
      pass
  
  new_time = res_hours + ':' + res_min + res_sign + res_days

  return new_time
function estimate_time(start, finish,time)

  while start < finish
    time *= 2
    start +=1
  end
  println(time / 3600)
end

estimate_time(10,25,33)

function read_file(filename)
  file = open(filename)
  number_of_cities = 0
  count = 1
  coordinates = 0
  for line in eachline(file)
    line = split(line, " ")
    if length(line) < 2
      line = split(line[1], "/")
      number_of_cities = parse(Int64, line[1])
      coordinates = zeros((number_of_cities, 2))
    else
      line[2] = split(line[2], "/")[1]
      for i in range(1, 2)
        coordinates[count, i] = parse(Float64, line[i])
      end
      count += 1
    end
  end
  return (coordinates, number_of_cities)
end



read_file("test1.txt"))

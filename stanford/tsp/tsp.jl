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
  close(file)
  return (coordinates, number_of_cities)
end

function calculate_distance(coord1::Array{Float64, 2}, coord2::Array{Float64, 2})
  return sqrt((coord1[1] - coord2[1])^2 + (coord1[2] - coord2[2])^2)
end

function solve_tsp_dp(filename)
  coordinates, number_of_cities = read_file(filename)
  cities = [x for x in range(1, number_of_cities)]
  distances = find_distances(coordinates)
  result = Dict{BitArray, Array{Float64,1}}()
  first_row = BitArray{1}(number_of_cities)
  first_row[1] = true
  result[first_row] = zeros(number_of_cities)

  for m in range(2, number_of_cities - 1)
    println(m)
    tic()
    new_result = Dict{BitArray, Array{Float64,1}}()
    for c in combinations(cities[2:number_of_cities], m - 1)
      c = append!([1], c)
      combo = BitArray{1}(number_of_cities)
      for num in c
        combo[num] = true
      end
      new_result[combo] = fill(Inf, number_of_cities)
      for j in c
        minimum = Inf
        if j != 1
          for k in c
            if k != j
              combo[j] = false
              if result[combo][k] + distances[k,j] < minimum
                minimum = result[combo][k] + distances[k,j]
              end
              combo[j] = true
            end
          end
        end
        new_result[combo][j] = minimum
      end
    end
    result = copy(new_result)
    toc()
  end
  shortest_dis = Inf
  all_cities = trues(number_of_cities)
  for j in range(2, number_of_cities - 1)
    score = result[all_cities][j] + distances[j,1]
    if score < shortest_dis
      shortest_dis = score
    end
  end
  println(shortest_dis)
end

function find_distances(coord::Array{Float64, 2})
  len = size(coord)[1]
  distances = zeros((len, len))
  for i in range(1, len)
    for j in range(1, len)
      distances[i,j] = calculate_distance(coord[i,:], coord[j,:])
    end
  end
  return distances
end


# read_file("test1.txt")
# println(find_distances([0.0 2.0; 0.0 5.0]))
solve_tsp_dp("tsp.txt")

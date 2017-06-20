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
  cities = [Int8(x) for x in range(1, number_of_cities)]
  distances = find_distances(coordinates)
  result = Dict{Array{Int8,1}, Array{Float64,1}}()
  result[[Int8(1)]] = zeros(number_of_cities)

  for m in range(2, number_of_cities - 1)
    println(m)
    tic()
    new_result = Dict{Array{Int8,1}, Array{Float64,1}}()
    for c in combinations(cities[2:number_of_cities], m - 1)
      combo = append!([Int8(1)], Array{Int8,1}(c))
      for j in combo
        if j == 1
          new_result[combo] = fill(Inf, number_of_cities)
        else
          minimum = Inf
          for k in combo
            if k != j
              temp = copy(combo)
              deleteat!(temp, findin(temp, [j]))
              if result[temp][k] + distances[k,j] < minimum
                minimum = result[temp][k] + distances[k,j]
              end
            end
          end
          new_result[combo][j] = minimum
        end
      end
    end
    result = copy(new_result)
    toc()
  end
  shortest_dis = Inf
  for j in range(2, number_of_cities - 1)
    score = result[cities][j] + distances[j,1]
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

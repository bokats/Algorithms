using NearestNeighbors
using Debug

@debug function solve_tsp(filename)
  coordinates = nothing
  city_visits = nothing
  visited = Set{Int32}()
  kd_tree = nothing
  heap = Array{Int32, 1}()
  heap_dis = Array{Float64, 1}()
  heap_start_city = Array{Int32, 1}()
  heap_end_city = Array{Int32, 1}()
  kth_city = nothing
  number_of_cities = 0

  function read_file(filename)
    file = open(filename)
    coordinates = 0
    for line in eachline(file)
      line = split(line, " ")
      if length(line) < 2
        line = split(line[1], "/")
        number_of_cities = parse(Int64, line[1])
        coordinates = zeros((2, number_of_cities))
        kth_city = Array{Int32, 1}(number_of_cities)
        fill!(kth_city, 2)
      else
        for i = (2,3)
          coordinates[i - 1, parse(Int64, line[1])] = parse(Float64, line[i])
        end
      end
    end

    city_visits = Array{Int8, 1}(number_of_cities)
    city_visits[1] = 1
    kd_tree = KDTree(coordinates)
    close(file)
  end

  function prims_min_spanning_tree()
    total_distance = 0.0
    push!(visited, 1)

    find_correct_edge(Int32(1))

    while length(visited) < size(coordinates, 2)
      # println(length(visited))
      test = true
      start_city = nothing
      end_city = nothing
      distance = nothing
      while test == true
        edge_idx = extract_min()
        start_city = heap_start_city[edge_idx]
        end_city = heap_end_city[edge_idx]
        distance = heap_dis[edge_idx]
        if in(end_city, visited) == false && city_visits[start_city] < 2 &&
        city_visits[end_city] < 2
          test = false
        else
          kth_city[start_city] += 1
          find_correct_edge(start_city)
        end
      end
      println(start_city, end_city)
      city_visits[start_city] += 1
      city_visits[end_city] += 1
      total_distance += distance
      push!(visited, end_city)
      kth_city[start_city] += 1

      find_correct_edge(start_city)
      find_correct_edge(end_city)
    end
    return (last_city, total_distance)
  end

  function calculate_distance(coord1::Array{Float64,1}, coord2::Array{Float64,1})
    return sqrt((coord1[1] - coord2[1])^2 + (coord1[2] - coord2[2])^2)
  end

  function query_and_add_to_heap(start_city::Int32)

    if city_visits[start_city] > 1
      return
    end
    println(kth_city[1])
    println(knn(kd_tree, coordinates[:,start_city],2), "tree")
    kd_result = knn(kd_tree, coordinates[:,start_city], Int64(kth_city[start_city]))

    new_city, distance = Int32(kd_result[1][1]), kd_result[2][1]
    # println(start_city, new_city, distance)
    insert(start_city, new_city, distance)
  end

  function find_correct_edge(start_city::Int32)
    if city_visits[start_city] > 1
      return
    end
    kd_result = knn(kd_tree, coordinates[:,start_city], number_of_cities, true)
    println(kd_result)
    for i = (kth_city[start_city], size(kd_result, 1))
      city = kd_result[1][i]
      if in(city, visited) == false && city_visits[city] < 2
        insert(start_city, Int32(city), kd_result[2][i])
        return
      end
      kth_city[start_city] += 1
    end
  end

  function connect_last_to_first(last::Int32, distance::Float64)
    edge_distance = calculate_distance(coordinates[1], coordinates[last])
    println(distance + edge_distance)
  end

  function insert(start_city::Int32, end_city::Int32, distance::Float64)
    next_idx = length(heap_dis)
    push!(heap, next_idx + 1)
    push!(heap_dis, distance)
    push!(heap_start_city, start_city)
    push!(heap_end_city, end_city)
    heapify_up()
  end

  function extract_min()
    # println()
    heap[1], heap[length(heap)] = heap[length(heap)], heap[1]
    min_edge = pop!(heap)
    heapify_down()
    return min_edge
  end

  function heapify_up()
    new_edge_idx = length(heap)
    parent_idx = find_parent_idx(new_edge_idx)
    # println(heap)
    # print(new_edge_idx, "first")
    # print(parent_idx, "first")

    while new_edge_idx != 1 && heap_dis[heap[new_edge_idx]] <=
    heap_dis[heap[parent_idx]]
      if heap_dis[heap[new_edge_idx]] == heap_dis[heap[parent_idx]] &&
      heap_end_city[heap[new_edge_idx]] > heap_end_city[heap[parent_idx]]
        break
      end
      heap[new_edge_idx], heap[parent_idx] = heap[parent_idx], heap[new_edge_idx]
      new_edge_idx = parent_idx
      parent_idx = find_parent_idx(new_edge_idx)
      # print(new_edge_idx)
      # print(parent_idx)
    end
  end

  function heapify_down()
    current_edge_idx = 1
    swap = true
    while swap
      swap = false
      children = find_children_indeces(current_edge_idx)
      swap_idx = current_edge_idx
      for child_idx in children
        if heap_dis[heap[child_idx]] <= heap_dis[heap[swap_idx]]
          if heap_dis[heap[child_idx]] == heap_dis[heap[swap_idx]] &&
          heap_end_city[child_idx] > heap_end_city[swap_idx]
            continue
          end
          swap_idx = child_idx
          swap = true
        end
      end
      if swap == true
        heap[current_edge_idx], heap[swap_idx] = heap[swap_idx], heap[current_edge_idx]
        current_edge_idx = swap_idx
      end
    end
  end

  function find_parent_idx(idx::Int)
    return floor(Int,idx / 2)
  end

  function find_children_indeces(idx::Int64)
    result = Array{Int64,1}(0)
    left = (2 * idx) + 1
    right = (2 * idx) + 2
    if left < length(heap)
      push!(result, left)
      if right < length(heap)
        push!(result, right)
      end
    end
    return result
  end

  function run_tsp(filename)
    read_file(filename)
    last_city, distance = prims_min_spanning_tree()
    connect_last_to_first(last_city, distance)
  end

  run_tsp(filename)
end

solve_tsp("test1.txt")

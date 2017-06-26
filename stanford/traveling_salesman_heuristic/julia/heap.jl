function insert(edge::Int32, array::Array{Int32, 1})
  push!(array, edge)
  heapify_up(array)
end

function extract_min(array::Array{Int32, 1})
  array[1], array[length(array)] = array[length(array)], array[1]
  min_edge = array[length(array)]
  heapify_down(array)
  return min_edge
end

function heapify_up(array::Array{Int32, 1})
  parent_idx = find_parent_idx(new_edge_idx)
  while new_edge_idx != 1 && array[new_edge_idx] < array[parent_idx,3]
    array[new_edge_idx], array[parent_idx] = array[parent_idx], array[new_edge_idx]
    new_edge_idx = parent_idx
    parent_idx = find_parent_idx(new_edge_idx)
  end
end

function heapify_down(array::Array{Float64, 2})
  current_edge_idx = 1
  swap = true
  while swap
    swap = false
    children = find_children_indeces(current_edge_idx)
    swap_idx = current_edge_idx
    for child_idx in children
      if array[child_idx] <= array[swap_idx]
        swap_idx = child_idx
        swap = true
      end
    end
    if swap
      array[current_edge_idx], array[swap_idx] = array[swap_idx], array[current_edge_idx]
      current_edge_idx = swap_idx
    end
  end
end

function find_parent_idx(idx::Int64)
  return floor(Int,(idx - 1) / 2)
end

function find_children_indeces(idx::Int64, array_length::Int64)
  result = Array{Int64,1}(0)
  left = (2 * idx) + 1
  right = (2 * idx) + 2
  if left < array_length
    push!(result, left)
    if right < array_length
      push!(result, right)
    end
  end
  return result
end

function calculate_distance(coord1::Array{Float64,1}, coord2::Array{Float64,1})
  return sqrt((coord1[1] - coord2[1])^2 + (coord1[2] - coord2[2])^2)
end

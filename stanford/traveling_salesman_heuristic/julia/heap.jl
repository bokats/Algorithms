function insert(edge::Array{Float64, 2}, array::Array{Float64, 2})
  array = hcat(array, edge)
  heapify_up(array)
  return array
end

function extract_min(array::Array{Float64, 2})
  length = size(array, 2)
  array[:,1], array[:,length] = array[:,length], array[:,1]
  min_edge = array[]
  heapify_down(array)
end

function heapify_up(array::Array{Float64, 2})
  new_edge_idx = size(array, 2)
  parent_idx = find_parent_idx(new_edge_idx)
  while new_edge_idx != 1 && array[new_edge_idx,3] < array[parent_idx,3]
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
      if child_idx <= size(array)[1] && array[child_idx,3] < array[swap_idx,3]
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

function find_children_indeces(idx::Int64)
  return [(2 * idx) + 1, (2 * idx) + 2]
end

println(insert([1.0 2.0 2.0], [2.0 3.0 3.0;3.0 4.0 6.0]))

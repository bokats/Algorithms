function insert(edge::Array{Float64, 1}, array::Array{Float64, 2})
  push!(array, edge)
  heapify_up(array)
  return array
end

function heapify_up(array::Array{Float64, 2})
  new_edge_idx = size(array)[0]
  parent_idx = find_parent_idx(new_edge_idx)
  while new_edge_idx != 0 && array[new_edge_idx][3] < array[parent_idx][3]
    array[new_edge_idx], array[parent_idx] = array[parent_idx], array[new_edge_idx]
    new_edge_idx = parent_idx
    parent_idx = find_parent_idx(new_edge_idx)
  end
end

function find_parent_idx(idx::Int64)
  return round(Int, idx / 2) - 1
end

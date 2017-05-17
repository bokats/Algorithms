class Node
  attr_reader :value

  def initialize(value)
    @value = value
  end
end

class MinHeap

  attr_reader :store

  def initialize
    @store = []
  end

  def insert(node)
    @store << node
    heapify_up
  end

  def extract
    @store[0], @store[@store.length - 1] =
      @store[@store.length - 1], @store[0]
    min_node = @store.pop
    heapify_down
    min_node
  end

  def peek
    @store[0]
  end

  def heapify_up
    current_idx = @store.length - 1
    parent_idx = parent(current_idx)

    while !parent_idx.nil?

      if @store[current_idx].value < @store[parent_idx].value
        @store[current_idx], @store[parent_idx] =
          @store[parent_idx], @store[current_idx]
        current_idx = parent_idx
        parent_idx = parent(current_idx)
      else
        break
      end
    end
  end

  def heapify_down
    current_idx = 0
    swap = true
    while swap
      children_idx = children(current_idx)
      lowest_index = current_idx
      swap = false
      children_idx.each do |child_idx|
        if @store[child_idx].value < @store[lowest_index].value
          lowest_index = child_idx
          swap = true
        end
      end

      if swap
        @store[current_idx], @store[lowest_index] = @store[lowest_index], @store[current_idx]
        current_idx = lowest_index
      end
    end
  end

  def parent(index)
    return (index - 1) / 2 if index > 0
    nil
  end

  def children(index)
    result = []
    first_child = (index * 2) + 1
    second_child = (index * 2) + 2
    result << first_child if first_child < @store.length
    result << second_child if second_child < @store.length
    result
  end
end

class MaxHeap

  attr_reader :store

  def initialize
    @store = []
  end

  def insert(node)
    @store << node
    heapify_up
  end

  def extract
    @store[0], @store[@store.length - 1] =
      @store[@store.length - 1], @store[0]
    min_node = @store.pop
    heapify_down
    min_node
  end

  def peek
    @store[0]
  end

  def heapify_up
    current_idx = @store.length - 1
    parent_idx = parent(current_idx)

    while !parent_idx.nil?

      if @store[current_idx].value > @store[parent_idx].value
        @store[current_idx], @store[parent_idx] =
          @store[parent_idx], @store[current_idx]
        current_idx = parent_idx
        parent_idx = parent(current_idx)
      else
        break
      end
    end
  end

  def heapify_down
    current_idx = 0
    swap = true
    while swap
      children_idx = children(current_idx)
      highest_index = current_idx
      swap = false
      children_idx.each do |child_idx|
        if @store[child_idx].value > @store[highest_index].value
          highest_index = child_idx
          swap = true
        end
      end

      if swap
        @store[current_idx], @store[highest_index] = @store[highest_index], @store[current_idx]
        current_idx = highest_index
      end
    end
  end

  def parent(index)
    return (index - 1) / 2 if index > 0
    nil
  end

  def children(index)
    result = []
    first_child = (index * 2) + 1
    second_child = (index * 2) + 2
    result << first_child if first_child < @store.length
    result << second_child if second_child < @store.length
    result
  end
end

class TrackMedian
  attr_reader :min_heap, :max_heap, :median

  def initialize
    @min_heap = MinHeap.new
    @max_heap = MaxHeap.new
    @min_heap_length = 0
    @max_heap_length = 0
    @median = nil
  end

  def insert(number)
    new_node = Node.new(number)
    if @max_heap_length == 0
      @max_heap.insert(new_node)
      @max_heap_length += 1
      @median = number.to_f
    elsif number < @median
      @max_heap.insert(new_node)
      @max_heap_length += 1
    else
      @min_heap.insert(new_node)
      @min_heap_length += 1
    end
    calculate_median
  end

  def calculate_median

    size_difference = @min_heap_length - @max_heap_length
    if size_difference > 1
      @max_heap.insert(@min_heap.extract)
      @median = (@max_heap.peek.value.to_f + @min_heap.peek.value) / 2
      @min_heap_length -= 1
      @max_heap_length += 1
    elsif size_difference < -1
      @min_heap.insert(@max_heap.extract)
      @median = (@max_heap.peek.value.to_f + @min_heap.peek.value) / 2
      @max_heap_length -= 1
      @min_heap_length += 1
    elsif size_difference == 1
      @median = @min_heap.peek.value.to_f
    elsif size_difference == -1
      @median = @max_heap.peek.value.to_f
    else
      @median = (@max_heap.peek.value.to_f + @min_heap.peek.value) / 2
    end
    @median
  end
end

t = TrackMedian.new

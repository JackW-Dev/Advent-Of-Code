infile = File.open('input.txt')

overlapCountPartA, overlapCountPartB = 0, 0

def valueRange(line)
    minVal, maxVal = line.split('-')
    range = (minVal.to_i..maxVal.to_i).to_a
    return range
end

infile.readlines.each do |line|
    rangeOne, rangeTwo = line.split(',')

    rangeOne, rangeTwo = valueRange(rangeOne), valueRange(rangeTwo)

    if rangeOne.difference(rangeTwo).empty? || rangeTwo.difference(rangeOne).empty?
        overlapCountPartA += 1
    end

    if rangeOne.intersect?(rangeTwo) || rangeTwo.intersect?(rangeOne)
        overlapCountPartB += 1
    end
end

infile.close

puts "Part A: #{overlapCountPartA}"
puts "Part B: #{overlapCountPartB}"
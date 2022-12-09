partAStacks = [[], [], [], [], [], [], [], [], []]
partBStacks = [[], [], [], [], [], [], [], [], []]

File.foreach("input.txt") do |line|
	if line.lstrip.start_with? "["
		for i in (1..33).step(4) do

			if line[i] == " "
				next
			else
				partAStacks[(i-1)/4].prepend(line[i])
				partBStacks[(i-1)/4].prepend(line[i])
			end
		end
	elsif line.start_with? "move"
		instructions = line.scan(/\d+/).map(&:to_i)

		#Following commented out as it fails to handle values > 9 i.e. 10 would be stores as 1, 0
		# instructions = []

		# line.chars.each do |char|
		# 	if char  =~ /[0-9]/
		# 		instructions.push(char.to_i)
		# 	end
		# end

		# puts instructions.to_s
		

		instructions[0].times do
			popped = partAStacks[instructions[1]-1].pop.to_s

			partAStacks[instructions[2]-1].push(popped)
		end

		popped = *partBStacks[instructions[1]-1].pop(instructions[0])
		partBStacks[instructions[2]-1].push(*popped)
	end
end

print "Part A: "
partAStacks.each { |stack| print stack[-1] };

print "\nPart B: "
partBStacks.each { |stack| print stack[-1] };
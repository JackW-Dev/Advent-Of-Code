import java.io.File

fun Char.priorityAssign() = run {
    if (isUpperCase()) {
        this - 'A' + 27
    } else {
        this - 'a' + 1
    }
}

fun partA(infile: List<String>): Int {
    return infile.sumOf { item ->
        item.chunked(item.length / 2)
                .map { it.toSet() }
                .reduce { firstHalf, secondHalf -> firstHalf.intersect(secondHalf) }
                .first().priorityAssign()
    }
}

fun partB(infile: List<String>): Int {
    return infile.map { it.toSet() }
            .chunked(3)
            .map { it.reduce { firstHalf, secondHalf -> firstHalf.intersect(secondHalf) } }
            .sumOf { it.first().priorityAssign() }
}

fun main() {
    val infile = File("input.txt").readLines()

    println("Part A: ", partA(infile))
    println("Part B: ", partB(infile))
}
#include <stdio.h>
#include <stdlib.h>
#include <limits.h>

int main(){
    int clock, totalledX = 1, commandVal = 0, cycles = 0;
    int partA = 0, x, y;
	char partB[6][40], buffer[16];

    /*Open the file as a stream into the input buffer*/
	freopen("input.txt", "r", stdin);

	for (clock = 0; clock < 6*40; clock++, cycles--) {
		y = clock / 40;
		x = clock % 40;

		if (x == 20)
			partA += clock * totalledX;

		if (cycles <= 0) {
			totalledX += commandVal;

			if (!fgets(buffer, sizeof(buffer), stdin))
				cycles = INT_MAX;
			else if (sscanf(buffer, "addx %d", &commandVal) == 1) /*If an input of "addx [INT] can is successfully read"*/
				cycles = 2;
			else {
                /* noop takes 1 cycle */
				cycles = 1;	
				commandVal = 0;
			}
		}

        if (abs(x - totalledX) <= 1){
            partB[y][x] = '#';
        } else {
            partB[y][x] = ' ';
        }
	}

	printf("Part A: %d\n\r", partA);

    printf("Part B: \n\r");

	for (int i = 0; i < 6; i++)
		printf("%.40s\n", partB[i]);

    return 0;
}
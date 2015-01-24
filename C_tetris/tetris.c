#include "tetris.h"

int main()
{
	bool quit = false;
	char *command = malloc(sizeof(char) * CMD);
	srand(time(NULL));
	while (!quit) {
		printf("'new' for new game\n'quit' to exit\n>");
		scanf("%s", command);
		if (strcmp("new", command) == 0) {
			start();
		} else if (strcmp("quit", command) == 0) {
			return 0;
		} else {
			printf("%s is an invalid command\n", command);
		}
	}
}

void start(void)
{
	bool done_game = false;
	clear_board(board);
	clear_board(dead);
	get_block();
	while (!done_game) {
		update();
		print();
	}
}

void update(void) 
{
	clear_board(board);
	dead_to_board();
	block_to_array(board);
	//if (time(NULL) - (long double)last_moved > delay) {
	block.row += 1;
    //	}
	if (block.row == ROW-1 || collision()) {
		block_to_array(dead);
		get_block();
	}
}

void block_to_array(int array[ROW][COL])
{
	for (int i = 0; i < BHW; i++) {
		for (int j = 0; j < BHW; j++) {
			if (block.array[i*BHW+j] != 0) {
				array[block.row+i][block.col+j] = block.array[i*BHW+j];
			}
		}
	}
}

void clear_board(int array[ROW][COL])
{
	for (int i = 0; i < ROW; i++) {
		for (int j = 0; j < COL; j++) {
			array[i][j] = 0;
		}
	}
}

void dead_to_board(void)
{
	for (int i = 0; i < ROW; i++) {
		for (int j = 0; j < COL; j++) {
			board[i][j] = dead[i][j];
		}
	}
}

void print(void)
{
	for (int i = 0; i < ROW; i++) {
		for (int j = 0; j < COL; j++) {
			if (j == COL-1)
				printf("%d]%d\n", board[i][j], i);
			else if (j == 0) 
				printf("[%d,", board[i][j]);
			else 
				printf("%d,", board[i][j]);
		}
	}
	printf("\n");
}
		
void get_block(void) {
	int r = (rand() % 7) + 1;
	block.row = 0;
	block.col = 3;
	switch (r) {
		case 1:
			block.array = i_blocks[0];
			break;
		case 2:
			block.array = j_blocks[0];
			break;
		case 3:
			block.array = l_blocks[0];
			break;
		case 4:
			block.array = o_blocks[0];
			break;
		case 5:
			block.array = t_blocks[0];
			break;
		case 6:
			block.array = s_blocks[0];
			break;
		case 7:
			block.array = z_blocks[0];
			break;
	}
}

/* pack two ints < 20 into a single int */
int packints(int a, int b)
{
	a <<= 5;
	a |= b;
	return a;
}

/* unpack two ints < 20 */
int *unpackints(int a)
{
	int *points = malloc(sizeof(int)*2);
	points[0] = (a & 0x3E0) >> 5;
	points[1] = a & 0x1F;
	return points;
}


int *points_to_check(void)
{
	int *points = malloc(sizeof(int)*BHW+1);
	int pos = 0;
	if (block.array[0] == 1 && block.array[4] == 1) {
		points[0] = packints(block.row + 3, block.col);
		points[1] = -1;
		return points;
	}
	for (int i = 0; i < BHW; i++) {
		for (int j = 0; j < BHW; j++) {
			printf("block[%d][%d] = %d\n", i, j, block.array[i*BHW+j]);
			printf("block[%d+1][%d] = %d\n", i, j, block.array[(i+1)*BHW+j]);
			if (block.array[i*BHW+j] != 0 && block.array[(i+1)*BHW+j] == 0) {
				points[pos++] = packints(block.row+i,block.col+j);
				printf("%d, %d\n", block.row+i, block.col+j);
			}
		}
	}
	points[pos] = -1;
	return points;
}			

bool collision(void)
{
	int *points = points_to_check();
	for (int i = 0; points[i] != -1; i++) {
		int *unpacked = unpackints(points[i]);
		if (board[unpacked[0]+1][unpacked[1]] != 0)
			return true;
	}
	return false;
}

	
	



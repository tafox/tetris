#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>
#include <time.h>

#define ROW 20
#define COL 10
#define CMD 5
#define BHW 4
#define ORIENTATIONS 4

time_t last_moved;
double delay = 0.2;

int board[ROW][COL];
int dead[ROW][COL];

typedef struct {
	int row;
	int col;
	int *array;
} Block;

Block block;

void start(void);
void update(void);
void block_to_array(int array[ROW][COL]);
void clear_board(int array[ROW][COL]);
void dead_to_board(void);
void print(void);
void get_block(void);
bool collision(void);
int *points_to_check(void);
int packints(int a, int b);

int i_block1[BHW][BHW] = {{1,1,1,1},
						  {0,0,0,0},
					      {0,0,0,0},
						  {0,0,0,0}};

int i_block2[BHW][BHW] = {{1,0,0,0},
						  {1,0,0,0},
						  {1,0,0,0},
						  {1,0,0,0}};

int *i_blocks[ORIENTATIONS] = {(int*)&i_block1, (int*)&i_block2, NULL, NULL};

int o_block[BHW][BHW] = {{4,4,0,0},
						 {4,4,0,0},
						 {0,0,0,0},
						 {0,0,0,0}};

int *o_blocks[ORIENTATIONS] = {(int*)&o_block, NULL, NULL, NULL};

int j_block1[BHW][BHW] = {{2,2,2,0},
						  {0,0,2,0},
						  {0,0,0,0},
						  {0,0,0,0}};

int j_block2[BHW][BHW] = {{0,2,0,0},
						  {0,2,0,0},
						  {2,2,0,0},
						  {0,0,0,0}};

int j_block3[BHW][BHW] = {{2,0,0,0},
						  {2,2,2,0},
						  {0,0,0,0},
						  {0,0,0,0}};

int j_block4[BHW][BHW] = {{2,2,0,0},
						  {2,0,0,0},
						  {2,0,0,0},
						  {0,0,0,0}};

int *j_blocks[ORIENTATIONS] = {(int*)&j_block1, (int*)&j_block2, (int*)&j_block3, (int*)&j_block4};


int l_block1[BHW][BHW] = {{0,0,3,0},
						  {3,3,3,0},
						  {0,0,0,0},
						  {0,0,0,0}};

int l_block2[BHW][BHW] = {{3,0,0,0},
						  {3,0,0,0},
						  {3,3,0,0},
						  {0,0,0,0}};

int l_block3[BHW][BHW] = {{3,3,3,0},
						  {3,0,0,0},
						  {0,0,0,0},
						  {0,0,0,0}};

int l_block4[BHW][BHW] = {{3,3,0,0},
						  {0,3,0,0},
						  {0,3,0,0},
						  {0,0,0,0}};

int *l_blocks[ORIENTATIONS] = {(int*)&l_block1, (int*)&l_block2, (int*)&l_block3, (int*)&l_block4};


int t_block1[BHW][BHW] = {{5,5,5,0},
						  {0,5,0,0},
						  {0,0,0,0},
						  {0,0,0,0}};

int t_block2[BHW][BHW] = {{0,5,0,0},
						  {5,5,0,0},
						  {0,5,0,0},
						  {0,0,0,0}};

int t_block3[BHW][BHW] = {{0,5,0,0},
						  {5,5,5,0},
						  {0,0,0,0},
						  {0,0,0,0}};

int t_block4[BHW][BHW] = {{5,0,0,0},
						  {5,5,0,0},
						  {5,0,0,0},
						  {0,0,0,0}};

int *t_blocks[ORIENTATIONS] = {(int*)&t_block1, (int*)&t_block2, (int*)&t_block3, (int*)&t_block4};

int s_block1[BHW][BHW] = {{0,6,6,0},
						  {6,6,0,0},
						  {0,0,0,0},
						  {0,0,0,0}};

int s_block2[BHW][BHW] = {{6,0,0,0},
						  {6,6,0,0},
						  {0,6,0,0},
						  {0,0,0,0}};

int *s_blocks[ORIENTATIONS] = {(int*)&s_block1, (int*)&s_block2, NULL, NULL};

int z_block1[BHW][BHW] = {{7,7,0,0},
						  {0,7,7,0},
						  {0,0,0,0},
						  {0,0,0,0}};

int z_block2[BHW][BHW] = {{0,7,0,0},
						  {7,7,0,0},
						  {7,0,0,0},
						  {0,0,0,0}};

int *z_blocks[ORIENTATIONS] = {(int*)&z_block1, (int*)&z_block2, NULL, NULL}; 

#include "block.h"
#include <cstdlib>
#include <ctime>

using namespace std;

Block::Block()
{
    Block(0, 0);
}

Block::Block(int x, int y)
{
    _location[0] = x;
    _location[1] = y;
    _color = static_cast<Color>(rand() % COUNT);
    srand(time(0));
    _number = 1 + (rand() % (MAX_NUMBER - 1));
    _movable = true;
}

Block::Block(int x, int y, Color color, int number, bool movable) : _color(color), _number(number), _movable(movable)
{
    _location[0] = x;
    _location[1] = y;
}

Ground::Ground(int x, int y)
{
    _location[0] = x;
    _location[1] = y;
    _number = -1;
    _color = GREY;
    _movable = false;
}
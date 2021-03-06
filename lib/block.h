#ifndef BLOCK_H
#define BLOCK_H

#include "effolkronium/random.hpp"
#include "game_object.h"
#include <ostream>

#define MIN_NUMBER 0
#define MAX_NUMBER 9

// enum Color
// {
//     RED = 'r',
//     ORANGE = 'o',
//     YELLOW = 'y',
//     GREEN = 'g',
//     BLUE = 'b',
//     PURPLE = 'p',
//     GREY = 'q',
//     COUNT
// };

class Block : public GameObject {
protected:
  static inline char colors[7] = {'r', 'o', 'y', 'g', 'b', 'p', 'X'};
  char _color;
  int _number;

public:
  Block();
  Block(int x, int y);
  Block(int x, int y, char color, int number, bool movable);

  int color() const { return _color; }
  int kind() const override { return _color; }
  int number() const override { return '0' + _number; }

  void repr(std::ostream &ostr) const;
};

class Ground : public Block {
protected:
public:
  Ground(int x, int y);
  void repr(std::ostream &ostr) const;
  int kind() const override { return GameObject::kind(); }
  int number() const override { return GameObject::number(); }
};

std::string colorname(char color);


#endif /* BLOCK_H */

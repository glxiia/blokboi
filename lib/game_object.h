#ifndef GAME_OBJECT_H
#define GAME_OBJECT_H

#include <ostream>

enum Kind
{
    SKY = '.',
    BLOCK = 'X',
    GROUND = '@',
    PLAYER = 'P'
};

typedef union location {
    int x;
    int y;
} LOCATION;

class GameObject
{
  protected:
    LOCATION _location;
    Kind _kind;
    bool _movable = false;

    GameObject()
    {
    }

  public:
    Kind kind()
    {
        return _kind;
    }
    void update(int x, int y)
    {
        _location.x = x;
        _location.x = y;
    }
    const LOCATION location() const
    {
        return _location;
    }
    virtual void repr(std::ostream &ostr) const
    {
    }
    bool movable() const
    {
        return _movable;
    }
    int number()
    {
        return -1;
    }
};

#endif /* GAME_OBJECT_H */

#ifndef GAME_OBJECT_H
#define GAME_OBJECT_H

#include <ostream>

typedef union location {
    int x;
    int y;
} LOCATION;

class GameObject
{
  protected:
    LOCATION _location;

    GameObject()
    {
    }

  public:
    void update(int x, int y)
    {
        _location.x = x;
        _location.x = y;
    }
    const LOCATION location() const
    {
        return _location;
    }
    virtual void repr(std::ostream &ostr) const;
};

#endif /* GAME_OBJECT_H */
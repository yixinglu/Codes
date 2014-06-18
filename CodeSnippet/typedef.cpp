#include <iostream>
#include <memory>

struct Interface {
  virtual void print() = 0;
};

typedef std::tr1::shared_ptr<Interface> isptr;

//error: can not typedef template without a type
// typedef std::tr1::shared_ptr shared_ptr

// error
// class Impl : public isptr {

class Impl : public Interface {
  public:
    virtual void print() {
      std::cout << "Impl" << std::endl;
    }
};

typedef double matrix2[2][2];

int main(int argc, char** argv) {

  matrix2 mat = {{1,0}, {0,1}};
  std::cout << mat[0][0] << ", " << mat[0][1] << std::endl
            << mat[1][0] << ", " << mat[1][1] << std::endl;

  isptr sp(new Impl());
  sp->print();

  return 0;
}

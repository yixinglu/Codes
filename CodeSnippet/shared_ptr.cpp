#include <iostream>
#include <memory>

struct Base {
  int i;
};

using namespace std;

int main(int argc, char* argv[]) {
  auto ptr = make_shared<Base>();
  ptr->i = 10;
  cout << ptr->i << endl;
  
  shared_ptr<Base> ptr2(new Base);
  ptr2->i = 11;
  cout << ptr2->i << endl;

  return 0;
}

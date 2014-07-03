#include <memory>
#include "memchk.h"

using namespace std;

struct Bar;
struct Foo{
	shared_ptr<Bar> bar;	
};

struct Bar {
	shared_ptr<Foo> foo;
};

void test() {
	//auto fptr = make_shared<Foo>();
	//auto bptr = make_shared<Bar>();
  shared_ptr<Foo> fptr(new Foo());
  shared_ptr<Bar> bptr(new Bar());
	fptr->bar = bptr;
	bptr->foo = fptr;
}

int main() {
	test();

	MEM_CHK_EXIT_DBG
	return 0;
}

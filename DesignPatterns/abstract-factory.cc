#include <iostream>
#include <memory>
#include <string>

using namespace std;

class AbstractProductA {
 public: 
  virtual ~AbstractProductA() {}
  virtual string DebugString() const = 0;
};

class ProductA1 : public AbstractProductA {
 public:
  virtual ~ProductA1() {}
  virtual string DebugString() const {
    return "ProductA1";
  }
};

class ProductA2 : public AbstractProductA {
 public:
  virtual ~ProductA2() {}
  virtual string DebugString() const {
    return "ProductA2";
  }
};

class AbstractProductB {
 public: 
  virtual ~AbstractProductB() {}
  virtual string DebugString() const = 0;
};

class ProductB1 : public AbstractProductB {
 public:
  virtual ~ProductB1() {}
  virtual string DebugString() const {
    return "ProductB1";
  }
};

class ProductB2 : public AbstractProductB {
 public:
  virtual ~ProductB2() {}
  virtual string DebugString() const {
    return "ProductB2";
  }
};

class AbstractFactory {
 public:
  virtual AbstractProductA *CreateProductA() = 0; 
  virtual AbstractProductB *CreateProductB() = 0; 
};

class ConcreteFactory1 : public AbstractFactory {
 public:
  virtual AbstractProductA *CreateProductA() {
    return new ProductA1;
  }
  virtual AbstractProductB *CreateProductB() {
    return new ProductB1;
  }
};

class ConcreteFactory2 : public AbstractFactory {
 public:
  virtual AbstractProductA *CreateProductA() {
    return new ProductA2;
  }
  virtual AbstractProductB *CreateProductB() {
    return new ProductB2;
  }
};

void test(AbstractFactory *factory) {
  unique_ptr<AbstractProductA> a(factory->CreateProductA());
  cout << a->DebugString() << endl;
  unique_ptr<AbstractProductB> b(factory->CreateProductB());
  cout << b->DebugString() << endl; 
}

int main() {
  unique_ptr<AbstractFactory> factory1(new ConcreteFactory1);
  test(factory1.get());

  unique_ptr<AbstractFactory> factory2(new ConcreteFactory2);
  test(factory2.get());
  return 0;
}

#include <iostream>
#include <memory>
#include <string>

using namespace std;

class Product {
 public:
  virtual ~Product() = default;
  virtual string DebugString() const = 0;
};

class ConcreteProduct : public Product {
 public:
  virtual string DebugString() const {
    return "ConcreteProduct";
  }
};

class Creator {
 public:
  virtual ~Creator() = default;
  virtual Product *FactoryMethod() {
    return nullptr;
  }
  void AnOperation() {
    unique_ptr<Product> product(FactoryMethod());
    if (product)
      cout << product->DebugString() << endl;
  }
};

class ConcreteCreator : public Creator {
 public:
  virtual Product *FactoryMethod() {
    return new ConcreteProduct;
  }
};

template <class TheProduct>
class StandardCreator : public Creator {
 public:
  virtual Product *FactoryMethod() {
    return new TheProduct;
  }
};

int main() {
  unique_ptr<Creator> creator(new ConcreteCreator);
  creator->AnOperation();

  unique_ptr<Creator> my_creator(new StandardCreator<ConcreteProduct>);
  my_creator->AnOperation();

  return 0;
}

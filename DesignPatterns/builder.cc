#include <iostream>
#include <memory>
#include <sstream>
#include <string>

using namespace std;

class Product {
 public:
  void set_part_a() {
    part_a_ = "PartA";
  }
  void set_part_b() {
    part_b_ = "PartB";
  }
  string DebugString() const {
    stringstream ss;
    ss << "(" << part_a_ << ", " << part_b_ << ")";
    return ss.str();
  }
 private:
  string part_a_;
  string part_b_;
};

class Builder {
 public:
  virtual ~Builder() {}
  virtual void BuildPartA() = 0;
  virtual void BuildPartB() = 0;
  virtual Product *GetResult() {
    return nullptr;
  }
};

class ConcreteBuilder : public Builder {
 public: 
  ConcreteBuilder() : product_(new Product) {}
  virtual Product *GetResult() {
    return product_;
  }

  virtual void BuildPartA() {
    product_->set_part_a();
  }

  virtual void BuildPartB() {
    product_->set_part_b();
  }
 private:
  Product *product_;
};


class Director {
 public:
  Director(Builder &builder) : builder_(builder) {}
  void Construct() {
    builder_.BuildPartA();
    builder_.BuildPartB();
    unique_ptr<Product> product(builder_.GetResult());
    if (product)
      cout << product->DebugString() << endl;
  }
 private:
  Builder &builder_;
};

int main() {
  unique_ptr<Builder> builder(new ConcreteBuilder);
  Director director(*builder);
  director.Construct();

  return 0;
}

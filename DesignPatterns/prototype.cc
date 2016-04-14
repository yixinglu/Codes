#include <iostream>
#include <memory>
#include <string>

using namespace std;

class Prototype {
 public:
  virtual ~Prototype() = default;
  virtual Prototype *Clone() = 0;
  virtual string DebugString() const = 0;
};

class ConcretePrototype1 : public Prototype {
 public:
  virtual Prototype *Clone() {
    return new ConcretePrototype1(*this);
  }
  virtual string DebugString() const {
    return "ConcretePrototype1";
  }
};

class ConcretePrototype2 : public Prototype {
 public:
  virtual Prototype *Clone() {
    return new ConcretePrototype2(*this);
  }
  virtual string DebugString() const {
    return "ConcretePrototype2";
  }
};

class Client {
 public:
  Client(Prototype *prototype) : prototype_(prototype) {}
  void Operation() {
    unique_ptr<Prototype> p(prototype_->Clone());
    cout << p->DebugString() << endl;
  }

 private:
  Prototype *prototype_;
};

int main() {
  unique_ptr<Prototype> prototype(new ConcretePrototype2);
  Client client(prototype.get());
  client.Operation();

  return 0;
}

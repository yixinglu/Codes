#include <iostream>
#include <memory> 
#include <string>

using namespace std;

class Singleton {
 public:
  static Singleton *Instance() {
    if (instance_) {
      instance_.reset(new Singleton);
    }
    return instance_.get();
  }

  string DebugString() const {
    return "Singleton";
  }

 private:
  static unique_ptr<Singleton> instance_; 

  Singleton() = default;
  // Disable copyable and assignment
  Singleton(const Singleton&) = delete;
  void operator=(const Singleton&) = delete;
};

unique_ptr<Singleton> Singleton::instance_(nullptr);

int main() {
  cout << Singleton::Instance()->DebugString() << endl;
  return 0;
}

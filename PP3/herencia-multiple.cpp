
#include <iostream>

#include <iostream>
#include <string>
using namespace std;

class A {
protected:
    int dato;
public:
    A(int x): dato(x) {}
    virtual ~A() {
        cout << "A destruido" << endl;
    }

    void imprimir() {
        cout << dato << endl;
    }

    virtual void presentarse () {
        cout << "Hola soy A" << endl;
    }
};

class B: virtual public A {
public:
    B(int x): A(x) {}
    virtual ~B() {
        cout << "B destruido" << endl;
    }

    void presentarse () override {
        cout << "Hola soy B" << endl;
    }
};

class C: virtual public A {
public:
    C(int x): A(x) {}
    virtual ~C() {
        cout << "C destruido" << endl;
    }

    void presentarse () override {
        cout << "Hola soy C" << endl;
    }
};

class D: public B, public C {
public:
    D(int x): A(x), B(x), C(x) {}
    ~D() {
        cout << "\nD destruido" << endl;
    }

    void presentarse () override {
        cout << "Hola soy D " << endl;
        A::presentarse(); // llamo directamente al presentarse de A
        B::presentarse(); // funciona tambien con B
    }
};

/*int main() {
    A a(1);
    B b(2);
    C c(3);
    D d(4);

    a.imprimir();
    b.imprimir();
    c.imprimir();
    d.imprimir();

    a.presentarse();
    b.presentarse();
    c.presentarse();
    d.presentarse();

    return 0;
}
*/


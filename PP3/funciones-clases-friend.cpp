#include <iostream>
#include <string>
using namespace std;

class Animal {
protected:
    string nombre;
public:
    Animal(string nombre) {
        this->nombre = nombre;
    }

    virtual void sonido() {
        cout << "Animal generico hace sonido" << endl;
    }

    virtual void mostrar(){
        cout << nombre << endl;
    }

};

class Perro: virtual public Animal {
protected:
    string raza;
public:
    Perro(string nombre, string raza): Animal(nombre) {
        this->raza = raza;
        this->nombre = nombre;
    }

    void sonido() override {
        cout << "Perro ladra" << endl;
    }

    void mostrar() override {
        cout << nombre << endl;
        cout << raza << endl;
    }
};

class Gato: virtual public Animal {
protected:
    bool ronronea;
    public:
    Gato(string no, bool ro): Animal(no) {
        ronronea = ro;
        this->nombre = no;
    }

    void sonido() override {
        cout << "Gato hace miau" << endl;
    }

    void mostrar() override {
        cout << nombre << endl;
        cout << ronronea << endl;
    }
};

class Hibrido : public Perro, public Gato {
    public:
    Hibrido(string no, string raza, bool ronro): Animal(no), Perro(no, raza), Gato(no, ronro) {
        this->nombre = no;
        this->raza = raza;
        this->ronronea = ronro;
    }
    void sonido() override {
        cout << "Hibrido sonido" << endl;
    }

    void mostrar() override {
        cout << nombre << endl;
        cout << ronronea << endl;
        cout << raza << endl;
    }
};


/*int main() {
    Perro * perro = new Perro("Pedro el perro", "Yorkshire");
    perro->sonido();

    Gato * gato = new Gato("Gatubela", true);
    gato->sonido();

    Hibrido * hibrido = new Hibrido("Horacio", "Mezcla total", false);

    hibrido->sonido();

    gato->mostrar();
    perro->mostrar();
    hibrido->mostrar();
}*/
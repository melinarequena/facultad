#include <iostream>
#include <string>
using namespace std;

/*Implementa las clases Vehiculo, Coche y Moto según lo solicitado en el programa
principal. También considera un función ObtenerTipo común a todos los vehículos. */

class Vehiculo {
    public:
    Vehiculo() {}
    virtual ~Vehiculo() {}

    void acelerar() {
        cout << obtenerTipo() << " acelerado" << endl;
    }

    virtual string obtenerTipo() {
        return "Vehiculo";
    }
};

class Coche: public Vehiculo {
    public:
    Coche() {}
    ~Coche() {}

    string obtenerTipo() override {
        return "Coche";
    }

};

class Moto: public Vehiculo {
    public:
    Moto() {}
    ~Moto() {}

    string obtenerTipo() override {
        return "Moto";
    }

};


int main() {
    Vehiculo vehiculo;
    Coche coche;
    Moto moto;

    vehiculo.acelerar();
    coche.acelerar();
    moto.acelerar();

    return 0;
}
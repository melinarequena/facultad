#include <iostream>
#include <string>
using namespace std;

class Estudiante {
private:
    string nombre;
public:
    Estudiante(string n) {
        nombre = n;
    }
    bool operator==(Estudiante &otro) {
        return nombre == otro.nombre;
    }
};

int main() {
    Estudiante * e1 = new Estudiante("Juan");
    Estudiante * e2 = new Estudiante("Meli");

    Estudiante e3("CAROLINA LINA CAROLINA");
    Estudiante e4("HeyMister");

    bool igualdad1 = *e1 == *e2;

    bool igualdad2 = e3 == e4;

    if(igualdad1 == true) {
        cout <<"VERDADERO"<< endl;
    } else {
        cout <<"FALSO"<< endl;
    }

    if(igualdad2 == true) {
        cout <<"VERDADERO"<< endl;
    } else {
        cout <<"FALSO"<< endl;
    }
}
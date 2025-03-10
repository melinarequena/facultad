#include <iostream>
#include <string>
#include <vector>
using namespace std;

class Producto {
private:
    string nombre;
    public:
    Producto(string no) {
        nombre = no;
    }
    string getNombre() const {
        return nombre;
    }
};


class Contador {
    private:
    static int cantidad;
    vector <Producto *> productos;
    public:

    static void actualizarCont() {
        cantidad++;
    }

    void agregarElemento(Producto * prod){
        productos.push_back(prod);
        actualizarCont();

    }

    void mostrarElementos() const {
        for(int i = 0; i < productos.size(); i++) {
            cout << productos[i]->getNombre() << endl;
        }
    }

    int getCantidad() const {
        return cantidad;
    }
};

int Contador::cantidad = 0;

/*int main() {
    Producto *p = new Producto("John");
    Producto *p2 = new Producto("Jane");
    Producto *p3 = new Producto("Marvina");

    Contador * contador = new Contador();

    contador->agregarElemento(p);
    contador->agregarElemento(p2);
    contador->agregarElemento(p3);

    contador->mostrarElementos();

    cout << contador->getCantidad() << endl;

}
*/
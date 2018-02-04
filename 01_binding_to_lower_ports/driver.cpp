#include <cstdint>
#include "pistache/endpoint.h"


class HelloHandler : public Pistache::Http::Handler {
public:

    HTTP_PROTOTYPE(HelloHandler)

    void onRequest(const Pistache::Http::Request& request, Pistache::Http::ResponseWriter response) {
         response.send(Pistache::Http::Code::Ok, "Hello, World");
    }
};

int main() {
    Pistache::Http::listenAndServe<HelloHandler>("*:80");
}

#ifndef ENGINE_H
#define ENGINE_H

#include <stack>
#include <SFML/Graphics.hpp>

// Engine class knows EngineState
class EngineState;

class Engine {

    public:

        Engine();
        ~Engine();

        void pushState(EngineState* state);
        void popState();
        void changeState(EngineState8 state);
        EngineState* topState();
        void renderState();

        std::stack<EngineState*> states; // Private/Protected?
        sf::RenderWindow window;

};

#endif
#ifndef RUNSTATE_HPP
#define RUNSTATE_HPP

#include "EngineState.hpp"
#include <SFML/Graphics.hpp>

// RunState inherits from EngineState
class RunState : public EngineState {

    private:

        Engine* engine;
        sf::View engineView;
        sf::View runView;

    public:

        RunState(Engine* engine);
        virtual void draw(const float time);
        virtual void update(const float time);
        virtual void handleInput();
        void showMenu();
        void pauseEngine();

};

#endif
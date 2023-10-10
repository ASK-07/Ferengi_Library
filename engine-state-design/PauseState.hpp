#ifndef PAUSESTATE_HPP
#define PAUSESTATE_HPP

#include "EngineState.hpp"
#include <SFML/Graphics.hpp>

// PauseState inherits from EngineState
class PauseState : public EngineState {

    private:

        Engine* engine;
        sf::View engineView;
        sf::View pauseView;

    public:

        PauseState(Engine* engine);
        virtual void draw(const float time);
        virtual void update(const float time);
        virtual void handleInput();
        void showMenu();
        void runEngine();

};

#endif
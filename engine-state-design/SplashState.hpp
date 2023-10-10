#ifndef SPLASHSTATE_HPP
#define SPLASHSTATE_HPP

#include "EngineState.hpp"
#include <SFML/Graphics.hpp>

// SplashState inherits from EngineState
class SplashState : public EngineState {

    private:

        Engine* engine;
        sf::View splashView;

    public:

        SplashState(Engine* engine);
        virtual void draw(const float time);
        virtual void update(const float time);
        virtual void handleInput();
        void endSplash();

};

#endif
#ifndef MENUSTATE_HPP
#define MENUSTATE_HPP

#include "EngineState.hpp"
#include <SFML/Graphics.hpp>

// MenuState inherits from EngineState
class MenuState : public EngineState {

    private:

        Engine* engine;
        sf::View menuView;

    public:

        MenuState(Engine* engine);
        virtual void draw(const float time);
        virtual void update(const float time);
        virtual void handleInput();
        void hideMenu();
        void editPlane();

};

#endif
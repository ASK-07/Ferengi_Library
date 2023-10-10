#ifndef EDITSTATE_HPP
#define EDITSTATE_HPP

#include "EngineState.hpp"
#include <SFML/Graphics.hpp>

// EditState inherits from EngineState
class EditState : public EngineState {

    private:

        Engine* engine;
        sf::View engineView;
        sf::View editorView;

    public:

        EditState(Engine* engine);
        virtual void draw(const float time);
        virtual void update(const float time);
        virtual void handleInput();
        void showMenu();
        void runEngine();

};

#endif
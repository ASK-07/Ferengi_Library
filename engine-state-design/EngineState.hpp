#ifndef ENGINESTATE_HPP
#define ENGINESTATE_HPP

#include "Engine.hpp"

// Interface for the abstract class EngineState
class EngineState {

    public:

        // Pointer to Engine to behave according to state
        Engine* engine; // Private/Protected?

        // Pure virtual functions
        virtual void draw(const float time) = 0;
        virtual void update(const float time) = 0;
        virtual void handleInput() = 0;

};

#endif
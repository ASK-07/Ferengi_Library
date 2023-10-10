#include "EngineState.hpp"
#include "RunState.hpp"
//#include <other state .cpp files>?
#include <SFML/Graphics.hpp>

RunState::RunState(Engine* engine) {

    this->engine = engine;

    // TODO: Initialize engineView, runView

}

void RunState::draw(const float time) {

    // TODO: Implement draw logic (RunState)
    return;

}

void RunState::update(const float time) {

    // TODO: Implement update logic (RunState)
    return;

}

void RunState::handleInput() {

    // TODO: Implement event handling logic (RunState)
    return;

}

void RunState::showMenu() {

    // TODO: Implement logic to add MenuState to stack
    // -push PauseState then push MenuState
    return;

}

void RunState::pauseEngine() {

    // TODO: Implement logic to add PauseState to stack
    return;

}

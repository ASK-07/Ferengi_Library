#include "EngineState.hpp"
#include "PauseState.hpp"
//#include <other state .cpp files>?
#include <SFML/Graphics.hpp>

PauseState::PauseState(Engine* engine) {

    this->engine = engine;

    // TODO: Initialize engineView, pauseView

}

void PauseState::draw(const float time) {

    // TODO: Implement draw logic (PauseState)
    return;

}

void PauseState::update(const float time) {

    // TODO: Implement update logic (PauseState)
    return;

}

void PauseState::handleInput() {

    // TODO: Implement event handling logic (PauseState)
    return;

}

void PauseState::showMenu() {

    // TODO: Implement logic to add MenuState to stack
    return;

}

void PauseState::resumeEngine() {

    // TODO: Implement logic to add RunState to stack
    return;

}

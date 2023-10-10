#include "Engine.hpp"
#include "EngineState.hpp"
#include <stack>
#include <SFML/Graphics.hpp>
#include <SFML/System.hpp>

// Constructor creates window and limits framerate
Engine::Engine() {

    this->window.create(sf::VideoMode(800, 600), "Ferengi Physics");
    this->window.setFramerateLimit(60);

}

// Destructor removes all states from stack
Engine::~Engine() {

    while(!this->states.empty()) popState();

}

// pushState adds state to states
void Engine::pushState(EngineState* state) {

    this->states.push(state);
    return;

}

// popState removes state from states
void Engine::popState() {

    // Recover dynamically allocated memory
    delete this->states.top();
    this->states.pop();
    return;

}

// changeState removes previous state and adds new state to states
void Engine::changeState(EngineState* state) {

    if(!this->states.empty()) popState();
    pushState(state);
    return;

}

// topState returns the active state
EngineState* Engine::topState() {

    if(this->states.empty()) return NULL;
    return this->states.top();

}

// renderState calls base EngineState functions
// to handle engine behavior based on state
void Engine::renderState() {

    // Declare a Clock to get frame duration
    sf::Clock clock;

    while(this->window.isOpen()) {
        
        // Get frame duration and restart clock
        sf::Time elapsed = clock.restart();
        float time = elapsed.asSeconds();

        // Ensure current state exists
        if(peekState() == NULL) continue;

        // Handle inputs to state
        peekState()->handleInput();

        // Update engine entities that exist in frame
        peekState()->update(time);

        // Redraw new frame to window
        this->window.clear(sf::Color::Black);
        peekState()->draw(time);
        this->window.display();
    }
}

#include<SFML/Graphics.hpp>
#include <string>
#include <iostream>
#include <vector>

class CreateObject {
	sf::Vector2f pos;
	sf::Vector2f vel;
	sf::RectangleShape s;
public:
	CreateObject(float pos_x, float pos_y, float vel_x, float vel_y)
		: pos(pos_x, pos_y), vel(vel_x, vel_y) {
		s.setPosition(pos);
		s.setFillColor(sf::Color::White);
		s.setSize(sf::Vector2f(40, 40));
	}

	void render(sf::RenderWindow& wind) {
		s.setPosition(pos);
		wind.draw(s);
	}

	void update(float gravity) {
		// Apply gravity to the vertical velocity
		vel.y += gravity;

		// Update position based on velocity
		pos += vel;

		// Prevent objects from falling through the ground
		if (pos.y + s.getSize().y > 800) {
			pos.y = 800 - s.getSize().y;
			vel.y = 0;
		}
	}

	void move(float pos_x, float pos_y, float vel_x, float vel_y)
	{
		//Soon to add movement
	}

	sf::Vector2f getPosition() const {
		return pos;
	}

	void set_color(sf::Color col) {
		s.setFillColor(col);
	}
};

int main()
{
	//Initialize window dimensions
	sf::RenderWindow window(sf::VideoMode(800, 800), "Demo Window");
	window.setFramerateLimit(60);

	//Create button
	sf::RectangleShape* button1 = new sf::RectangleShape(sf::Vector2f(100.f, 50.f));
	button1->setPosition(350, 0);
	button1->setFillColor(sf::Color::White);

	std::vector<CreateObject> objects;


	//Defining Simple Gravity
	const float gravity = 0.2f;

	while (window.isOpen())
	{
		//Event handling
		sf::Event event;
		while (window.pollEvent(event))
		{
			//Close window event
			if (event.type == sf::Event::Closed)
			{
				window.close();
			}

			//Mouse click event for button click handling
			if (event.type == sf::Event::MouseButtonPressed)
			{
				if (sf::Mouse::isButtonPressed(sf::Mouse::Left))
				{
					auto click_position = sf::Mouse::getPosition(window);
					auto map_position = window.mapPixelToCoords(click_position);
					if (button1->getGlobalBounds().contains(map_position))
					{
						
						  // Create a new falling object and add it to the vector
						CreateObject obj(400, 0, 0, 0); // Set initial velocity to zero
						objects.push_back(obj);

					}
				}

			}
			//Keyboard Event Handling
			if (event.type == sf::Event::KeyPressed)
			{
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num1))
				{
				
					  // Create a new falling object and add it to the vector
					CreateObject obj(275, 275, 0, 0); // Set initial velocity to zero
					objects.push_back(obj);


				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num2))
				{
					
					CreateObject obj(650, 650, 0, 0); // Set initial velocity to zero
					objects.push_back(obj);

				}
				//Movement event handling with arrow keys

			}
		}
		//Update falling objects.
		for (auto& obj : objects) {
			obj.update(gravity);
		}

		//Display contents of object arrays in the window
		window.clear();
		for (auto& obj : objects) {
			obj.render(window);
		}
		window.display();
	}

	return 0;
}

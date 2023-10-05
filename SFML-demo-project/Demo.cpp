#include<SFML/Graphics.hpp>
#include <string>
#include <iostream>

int main()
{
	//Initialize window dimensions
	sf::RenderWindow window(sf::VideoMode(800, 800), "Demo Window");

	//Initialize array of shape objects
	const int MAX_SHAPES = 50;
	int number_of_shapes = 0;
	sf::Shape *shapes[MAX_SHAPES];

	//Initialize array of button objects
	const int MAX_BUTTONS = 10;
	int number_of_buttons = 0;
	sf::Shape* buttons[MAX_BUTTONS];

	//Create button
	sf::RectangleShape* button1 = new sf::RectangleShape(sf::Vector2f(100.f, 50.f));
	button1->setPosition(350, 0);
	button1->setFillColor(sf::Color::White);
	buttons[number_of_buttons] = button1;
	number_of_buttons++;

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
						//Allocates shape and store in shapes array
						sf::CircleShape* shape3 = new sf::CircleShape(75.f);
						shape3->setPosition(325, 325);
						shape3->setFillColor(sf::Color::Red);
						shapes[number_of_shapes] = shape3;
						number_of_shapes++;

					}
				}

			}
			//Keyboard Event Handling
			if (event.type == sf::Event::KeyPressed)
			{
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num1))
				{
					//Allocates shape and store in shapes array
					sf::CircleShape *shape1= new sf::CircleShape(100.f);
					shape1->setPosition(275, 275);
					shape1->setFillColor(sf::Color::Cyan);
					shapes[number_of_shapes] = shape1;
					number_of_shapes++;

				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num2))
				{
					//Allocates shape and store in shapes array
					sf::RectangleShape* shape2 = new sf::RectangleShape(sf::Vector2f(100.f, 50.f));
					shape2->setPosition(650, 650);
					shape2->setFillColor(sf::Color::Red);
					shapes[number_of_shapes] = shape2;
					number_of_shapes++;

				}
				//Movement event handling with arrow keys
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
				{
					shapes[number_of_shapes-1]->move(0.f, 3.f);
				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
				{
					shapes[number_of_shapes-1]->move(0.f, -3.f);
				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
				{
					shapes[number_of_shapes-1]->move(-3.f, 0.f);
				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
				{
					shapes[number_of_shapes-1]->move(3.f, 0.f);
				}
			}
		}

		//Display contents of object arrays in the window
		window.clear();
		for (int i = 0; i < number_of_buttons; i++)
		{
			window.draw(*buttons[i]);
		}
		for (int i = 0; i < number_of_shapes; i++)
		{
			window.draw(*shapes[i]);
		}
		window.display();

	}
	return 0;
}
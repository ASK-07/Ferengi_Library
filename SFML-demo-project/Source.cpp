#include<SFML/Graphics.hpp>
#include <string>
#include <iostream>


int main()
{
	sf::RenderWindow window(sf::VideoMode(1280, 720), "Demo Window");
	window.setFramerateLimit(60);

	sf::RectangleShape rect;
	sf::Vector2f rectanglePosition(600, 350);

	rect.setPosition(rectanglePosition);
	rect.setSize(sf::Vector2f(100, 100));


	float xVelocity = 0;
	float yVelocity = 0;

	while (window.isOpen())
	{
		sf::Event event;
		while (window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed)
				window.close();

			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape))
				window.close();

			xVelocity = 0;
			yVelocity = 0;

			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)){
				if (yVelocity <= 0)
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
						yVelocity = 1;
				else
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
						yVelocity = 0;
			}

			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
				if (yVelocity >= 0)
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
						yVelocity = -1;
					else
						if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
							yVelocity = 0;
			}
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) {
				if (xVelocity >= 0)
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
						xVelocity = -1;
					else
						if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
							xVelocity = 0;
			}
			if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) {
				if (xVelocity <= 0)
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
						xVelocity = 1;
					else
						if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
							xVelocity = 0;
			}

		}

		if (rectanglePosition.x < 0 || rectanglePosition.x > 1280 - 100)
			xVelocity *= -1;

		if (rectanglePosition.y < 0 || rectanglePosition.y > 720 - 100)
			yVelocity *= -1;

		rectanglePosition.x += xVelocity;
		rectanglePosition.y += yVelocity;
		rect.setPosition(rectanglePosition);

		window.clear();
		window.draw(rect);
		window.display();
	}


}
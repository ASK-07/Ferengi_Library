#include<SFML/Graphics.hpp>
#include <string>
#include <iostream>

int main()
{
	sf::RenderWindow window(sf::VideoMode(800, 800), "Demo Window");
	const int MAX_SHAPES = 50;
	int number_of_shapes = 0;
	sf::Shape *shapes[MAX_SHAPES];
	sf::CircleShape shape1(100.f);
	sf::RectangleShape shape2(sf::Vector2f(50.f, 50.f));
	shape1.setFillColor(sf::Color::Cyan);
	shape2.setFillColor(sf::Color::Green);

	while (window.isOpen())
	{
		sf::Event event;
		while (window.pollEvent(event))
		{
			if (event.type == sf::Event::Closed)
			{
				window.close();
			}
			if (event.type == sf::Event::KeyPressed)
			{
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num1))
				{
					sf::CircleShape *shape1= new sf::CircleShape(100.f);
					shape1->setPosition(275, 275);
					shape1->setFillColor(sf::Color::Cyan);
					shapes[number_of_shapes] = shape1;
					number_of_shapes++;

				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num2))
				{
					sf::RectangleShape* shape2 = new sf::RectangleShape(sf::Vector2f(100.f, 50.f));
					shape2->setPosition(650, 650);
					shape2->setFillColor(sf::Color::Red);
					shapes[number_of_shapes] = shape2;
					number_of_shapes++;

				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down))
				{
					shapes[number_of_shapes-1]->move(0.f, 1.f);
				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up))
				{
					shapes[number_of_shapes-1]->move(0.f, -1.f);
				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left))
				{
					shapes[number_of_shapes-1]->move(-1.f, 0.f);
				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right))
				{
					shapes[number_of_shapes-1]->move(1.f, 0.f);
				}
				
			}
		}
		window.clear();
		for (int i = 0; i < number_of_shapes; i++)
		{
			window.draw(*shapes[i]);
		}
		window.display();

	}
	return 0;
}
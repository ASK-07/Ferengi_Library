#include<SFML/Graphics.hpp>
#include <string>
#include <iostream>
#include <vector>

class CreateObject {
	sf::Vector2f pos;
	std::shared_ptr<sf::Shape> shape;

public:
	CreateObject(float pos_x, float pos_y, std::shared_ptr<sf::Shape> shapeType)
		: pos(pos_x, pos_y), shape(shapeType) {
		shape->setPosition(pos);
		shape->setFillColor(sf::Color::White);
	}

	void render(sf::RenderWindow& wind) {
		shape->setPosition(pos);
		wind.draw(*shape);
	}

	void move(float dx, float dy) {
		pos.x += dx;
		pos.y += dy;
	}

	sf::Vector2f getPosition() const {
		return pos;
	}

};

int main()
{
	sf::RenderWindow window(sf::VideoMode(800, 800), "Demo Window");
	window.setFramerateLimit(60);

	std::vector<std::shared_ptr<CreateObject>> objects;

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
					auto circle = std::make_shared<sf::CircleShape>(20);
					circle->setFillColor(sf::Color::White);
					objects.emplace_back(275, 275, circle);
				}
				if (sf::Keyboard::isKeyPressed(sf::Keyboard::Num2))
				{
					auto rectangle = std::make_shared<sf::RectangleShape>(sf::Vector2f(40, 60));
					rectangle->setFillColor(sf::Color::White);
					objects.emplace_back(650, 650, rectangle);
				}

				if (!objects.empty()) {
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Up)) {
						objects.back()->move(0, -10);
					}
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Down)) {
						objects.back()->move(0, 10);
					}
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Left)) {
						objects.back()->move(-10, 0);
					}
					if (sf::Keyboard::isKeyPressed(sf::Keyboard::Right)) {
						objects.back()->move(10, 0);
					}
				}
			}
		}

		//Display contents of object arrays in the window
		window.clear();
		for (auto& obj : objects) {
			obj->render(window);
		}
		window.display();
	}

	return 0;
}
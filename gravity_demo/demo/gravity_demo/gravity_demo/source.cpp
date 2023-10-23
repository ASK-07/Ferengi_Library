#include<SFML/Graphics.hpp>
#include <string>
#include <iostream>
#include <vector>


class GravitySource {
    sf::Vector2f pos;
    float strength;
    sf::CircleShape s;
public:
    GravitySource(float pos_x, float pos_y, float strength)
    {
        pos.x = pos_x;
        pos.y = pos_y;
        this->strength = strength;

        s.setPosition(pos);
        s.setFillColor(sf::Color::White);
        s.setRadius(10);
    }
    void render(sf::RenderWindow& wind)
    {
        wind.draw(s);
    }
    sf::Vector2f get_pos()
    {
        return pos;
    }
    float get_strength()
    {
        return strength;
    }
};

class Particle {
    sf::Vector2f pos;
    sf::Vector2f vel;
    sf::CircleShape s;
public:
    Particle(float pos_x, float pos_y, float vel_x, float vel_y)
    {
        pos.x = pos_x;
        pos.y = pos_y;

        vel.x = vel_x;
        vel.y = vel_y;

        s.setPosition(pos);
        s.setFillColor(sf::Color::White);
        s.setRadius(4);
    }
    void render(sf::RenderWindow& wind)
    {
        s.setPosition(pos);
        wind.draw(s);
    }
    void set_color(sf::Color col)
    {
        s.setFillColor(col);
    }

    void update_physics(GravitySource& s)
    {
        float distance_x = s.get_pos().x - pos.x;
        float distance_y = s.get_pos().y - pos.y;

        float distance = sqrt(distance_x * distance_x + distance_y * distance_y);

        float inverse_distance = 1.f / distance;

        float normalized_x = inverse_distance * distance_x;
        float normalized_y = inverse_distance * distance_y;

        float inverse_sqaure_dropoff = inverse_distance * inverse_distance;

        float acceleration_x = normalized_x * s.get_strength() * inverse_sqaure_dropoff;
        float acceleration_y = normalized_y * s.get_strength() * inverse_sqaure_dropoff;

        vel.x += acceleration_x;
        vel.y += acceleration_y;

        pos.x += vel.x;
        pos.y += vel.y;


    }

};

sf::Color map_val_to_color(float value)
{
    if (value < 0.0f) value = 0;
    if (value > 1.0f) value = 1;

    int r = 0, g = 0, b = 0;

    if (value < 0.5f)
    {
        b = 255 * (1.0f - 2 * value);
        g = 255 * 2 * value;
    }
    else
    {
        g = 255 * (2.0f - 2 * value);
        r = 255 * (2 * value - 1);
    }
    return sf::Color(r, g, b);
}


int main()
{
    sf::RenderWindow window(sf::VideoMode(1600, 1000), "Demo Window");
    window.setFramerateLimit(60);

    std::vector<GravitySource> sources;

    sources.push_back(GravitySource(500, 500, 7000));
    sources.push_back(GravitySource(1200, 500, 7000));

    int num_particles = 2000;

    std::vector<Particle> particles;

    for (int i = 0; i < num_particles; i++)
    {
        particles.push_back(Particle(600, 700, 4, 0.2 + (0.1 / num_particles) * i));
        float val = (float)i / (float)num_particles;

        sf::Color col = map_val_to_color(val);
        particles[i].set_color(col);

    }


    while (window.isOpen())
    {
        sf::Event event;
        while (window.pollEvent(event))
        {
            if (event.type == sf::Event::Closed) window.close();
            if (sf::Keyboard::isKeyPressed(sf::Keyboard::Escape)) window.close();
        }
        window.clear();

        for (int i = 0; i < sources.size(); i++)
        {
            for (int j = 0; j < particles.size(); j++)
            {
                particles[j].update_physics(sources[i]);
            }
        }
        for (int i = 0; i < sources.size(); i++)
        {
            sources[i].render(window);
        }
        for (int j = 0; j < particles.size(); j++)
        {
            particles[j].render(window);
        }

        window.display();
    }
    return 0;
}
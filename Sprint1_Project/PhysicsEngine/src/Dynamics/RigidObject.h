//defines the general charactericts of our rigid body(such as mass, force, velocity)

class RigidObject
{
    public:
    //stores the coordinates for our vector we will use for the force, position and velocity.
        struct objectVector{
            float x, y;
        };

        RigidObject();

        //method that sets the mass of the object
        void setObjectMass();

        //method that sets the velocity of the object
        void setObjectVelocity();

        //method that sets the force of an object
        void setObjectForce();

        float objectMass;
        objectVector force;
        objectVector velocity;

};
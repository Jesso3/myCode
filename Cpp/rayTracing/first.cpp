#include <limits>
#include <cmath>
#include <iostream>
#include <fstream>
#include <vector>
#include <cmath>
#include "geometry.h"

double distance(int x1, int y1, int x2, int y2)
{
  return std::sqrt((x2 - x1) * (x2 - x1) + (y2 - y1) * (y2 - y1));
}

class Sphere {
    Vec3f center;
    int radius; 

public:
    Sphere(const Vec3f c, const int r) : center(c), radius(r) {}

    bool contains(const int x, const int y) {
        double dist = distance(center.x, center.y, x, y);        
        return (dist <= radius);
    }

    double distanceFromCenter(const int x, const int y){
      double dist = distance(center.x, center.y, x, y);
      return dist/radius;
    }
};
void render() {
    const int width    = 1024;
    const int height   = 768;
    std::vector<Vec3f> framebuffer(width*height);
    
    Sphere circle(Vec3f(100,100,0),100);
    Sphere circle2(Vec3f(400,400,0),50);

    for (size_t j = 0; j<height; j++) {
        for (size_t i = 0; i<width; i++) {
//            framebuffer[i+j*width] = Vec3f(j/float(height),i/float(width), i*j/255);

            if (circle.contains(i,j) || circle2.contains(i,j)){
              framebuffer[i+j*width] = Vec3f(1,1,1);
            }
            else{
              framebuffer[i+j*width] = Vec3f(0,0,0);
            }
        }
    }

    std::ofstream ofs; // save the framebuffer to file
    ofs.open("./out.ppm");
    ofs << "P6\n" << width << " " << height << "\n255\n";
    for (size_t i = 0; i < height*width; ++i) {
        for (size_t j = 0; j<3; j++) {
            ofs << (char)(255 * std::max(0.f, std::min(1.f, framebuffer[i][j])));
        }
    }
    ofs.close();
}

int main() {
    render();
    return 0;
}

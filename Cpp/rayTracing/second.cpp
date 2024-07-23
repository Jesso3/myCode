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
    float radius; 

public:
    Sphere(const Vec3f c, const int r) : center(c), radius(r) {}

    bool ray_intersect(const Vec3f &orig, const Vec3f &dir, float &t0) const {
        Vec3f L = center - orig;
        float tca = L*dir;
        float d2 = L*L - tca*tca;
        if (d2 > radius*radius) return false;
        float thc = sqrtf(radius*radius - d2);
        t0 = tca - thc;
        float t1 = tca + thc;
        if (t0 < 0) t0 = t1;
        if (t0 < 0) return false;
        return true;
    }
    
};

Vec3f cast_ray(const Vec3f &orig, const Vec3f &dir, const Sphere &sphere) {
        float sphere_dist = std::numeric_limits<float>::max();
        if (!sphere.ray_intersect(orig, dir, sphere_dist)) {
            return Vec3f(0.2, 0.7, 0.8); // background color
        }
        return Vec3f(0.4, 0.4, 0.3);
}

void render() {
    const int width    = 1024;
    const int height   = 768;
    const Vec3f camera = Vec3f(0,0,0);
    std::vector<Vec3f> framebuffer(width*height);
    
    Sphere circle(Vec3f(100,100,0),200);
    Sphere circle2(Vec3f(400,400,0),50);

    for (size_t j = 0; j<height; j++) {
        for (size_t i = 0; i<width; i++) {
//            framebuffer[i+j*width] = Vec3f(j/float(height),i/float(width), i*j/255);
            float x =  (2*(i + 0.5)/(float)width  - 1)*tan(180/2.)*width/(float)height;
            float y = -(2*(j + 0.5)/(float)height - 1)*tan(180/2.);
            Vec3f dir = Vec3f(x, y, -1).normalize();
            framebuffer[i+j*width] = cast_ray(Vec3f(0,0,500), dir, circle);
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

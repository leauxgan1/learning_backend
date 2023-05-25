from dataclasses import dataclass

@dataclass(slots = True)
class Particle:
    x: float
    y: float
    dx: float
    dy: float

@dataclass(slots = True)
class ParticleManager:
    particles: list[Particle]
    max_x: float
    max_y: float



def main():
    p = Particle(0,0,10,0)
    print(str(p) + "\n")
    pm  = ParticleManager([p],100,100)
    print(str(pm) + "\n")

    

if __name__ == "__main__":
    main()


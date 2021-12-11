class Octopus:
    total_flashes = 0

    def __init__(self, starting_energy, x_position, y_position):
        self.energy = starting_energy
        self.x_pos = x_position
        self.y_pos = y_position
        self.flashed_on_turn = False

    def increment_energy(self):
        self.energy += 1

    def flash(self):
        Octopus.total_flashes += 1
        self.flashed_on_turn = True

    def reset_energy(self):
        self.energy = 0
        self.flashed_on_turn = False


# Load initial dataset
with open('input.txt') as f:
    data_set = [data.strip() for data in f.readlines()]

octopi = []
current_x = 0
current_y = 0
for row_of_animals in data_set:
    for octopus_starting_energy in row_of_animals:
        octopi.append(Octopus(int(octopus_starting_energy), current_x, current_y))
        current_x += 1
    current_x = 0
    current_y += 1

# PART 1
# define and execute steps
# step_flashes = 0
# pos_flashes = []
# for steps in range(0, 100):
#     for indiv in octopi:
#         indiv.energy += 1
#     for indiv in octopi:
#         if indiv.energy > 9:
#             indiv.flash()
#             step_flashes += 1
#             pos_flashes.append([indiv.x_pos, indiv.y_pos])
#     while step_flashes > 0:
#         step_flashes = 0
#         for flashed_position in pos_flashes:
#             for indiv in octopi:
#                 if abs(indiv.x_pos - flashed_position[0]) <= 1 and abs(indiv.y_pos - flashed_position[1]) <= 1:
#                     indiv.energy += 1
#         pos_flashes = []
#         for indiv in octopi:
#             if indiv.energy > 9 and indiv.flashed_on_turn == False:
#                 indiv.flash()
#                 step_flashes += 1
#                 pos_flashes.append([indiv.x_pos, indiv.y_pos])
#     for indiv in octopi:
#         if indiv.flashed_on_turn == True:
#             indiv.reset_energy()
#
# print(Octopus.total_flashes)


# PART 2
# define and execute steps
step_flashes = 0
pos_flashes = []
synchronized = False
num_steps = 0
while synchronized == False:
    for indiv in octopi:
        indiv.energy += 1
    for indiv in octopi:
        if indiv.energy > 9:
            indiv.flash()
            step_flashes += 1
            pos_flashes.append([indiv.x_pos, indiv.y_pos])
    while step_flashes > 0:
        step_flashes = 0
        for flashed_position in pos_flashes:
            for indiv in octopi:
                if abs(indiv.x_pos - flashed_position[0]) <= 1 and abs(indiv.y_pos - flashed_position[1]) <= 1:
                    indiv.energy += 1
        pos_flashes = []
        for indiv in octopi:
            if indiv.energy > 9 and indiv.flashed_on_turn == False:
                indiv.flash()
                step_flashes += 1
                pos_flashes.append([indiv.x_pos, indiv.y_pos])
    for indiv in octopi:
        if indiv.flashed_on_turn == True:
            indiv.reset_energy()
    energy_0 = ['x' for indiv in octopi if indiv.energy == 0]
    if len(energy_0) == 100:
        synchronized = True
    num_steps += 1

print(num_steps)
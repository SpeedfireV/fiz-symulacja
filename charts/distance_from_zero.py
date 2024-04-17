
import matplotlib.pyplot as plt

from objects.space_object import SpaceObject


def draw_distance_from_zero(objects:dict[SpaceObject, list]):
    objects_name = []
    objects_distance = {}
    print( objects)
    for object, multiple_info in objects.items():
        for info in multiple_info:
            if objects_distance.get(object.name) is None:
                objects_distance[object.name] = {info[1] : info[0]}
                objects_name.append(object.name)
            else:
                objects_distance[object.name][info[1]] = int(info[0])
    fig, ax = plt.subplots(1,1)
    for name in objects_distance.keys():
        print(objects_distance)
        x_values = []
        y_values = []
        for k, v in objects_distance[name].items():
            x_values.append(k)
            y_values.append(v)
        ax.plot(x_values, y_values, label=name)
    ax.set_title("Distance from Zero X")
    ax.legend()
    plt.show()
# for make sure, if you click in the graphics,
#  the pieces be placed to the good position


class Pointy:
    def __init__(self, x, y):
        # bottom line
        if y > 5 and y < 15:
            if x > 5 and x < 15:
                self.x_coord = 10
                self.y_coord = 10
                self.place = 1
            elif x > 45 and x < 55:
                self.x_coord = 50
                self.y_coord = 10
                self.place = 2
            elif x > 85 and x < 95:
                self.x_coord = 90
                self.y_coord = 10
                self.place = 3

        # second line
        if y > 20 and y < 30:
            if x > 20 and x < 30:
                self.x_coord = 25
                self.y_coord = 25
                self.place = 4
            elif x > 45 and x < 55:
                self.x_coord = 50
                self.y_coord = 25
                self.place = 5
            elif x > 70 and x < 80:
                self.x_coord = 75
                self.y_coord = 25
                self.place = 6

        # third line
        if y > 35 and y < 45:
            if x > 35 and x < 45:
                self.x_coord = 40
                self.y_coord = 40
                self.place = 7
            elif x > 45 and x < 55:
                self.x_coord = 50
                self.y_coord = 40
                self.place = 8
            elif x > 55 and x < 65:
                self.x_coord = 60
                self.y_coord = 40
                self.place = 9

        # middle line
        if y > 45 and y < 55:
            if x > 5 and x < 15:
                self.x_coord = 10
                self.y_coord = 50
                self.place = 10
            elif x > 20 and x < 30:
                self.x_coord = 25
                self.y_coord = 50
                self.place = 11
            elif x > 35 and x < 45:
                self.x_coord = 40
                self.y_coord = 50
                self.place = 12
            elif x > 55 and x < 65:
                self.x_coord = 60
                self.y_coord = 50
                self.place = 13
            elif x > 70 and x < 80:
                self.x_coord = 75
                self.y_coord = 50
                self.place = 14
            elif x > 85 and x < 95:
                self.x_coord = 90
                self.y_coord = 50
                self.place = 15

        # fifth line
        if y > 55 and y < 65:
            if x > 35 and x < 45:
                self.x_coord = 40
                self.y_coord = 60
                self.place = 16
            elif x > 45 and x < 55:
                self.x_coord = 50
                self.y_coord = 60
                self.place = 17
            elif x > 55 and x < 65:
                self.x_coord = 60
                self.y_coord = 60
                self.place = 18

        # sixth line
        if y > 70 and y < 80:
            if x > 20 and x < 30:
                self.x_coord = 25
                self.y_coord = 75
                self.place = 19
            elif x > 45 and x < 55:
                self.x_coord = 50
                self.y_coord = 75
                self.place = 20
            elif x > 70 and x < 80:
                self.x_coord = 75
                self.y_coord = 75
                self.place = 21

        # top line
        if y > 85 and y < 95:
            if x > 5 and x < 15:
                self.x_coord = 10
                self.y_coord = 90
                self.place = 22
            elif x > 45 and x < 55:
                self.x_coord = 50
                self.y_coord = 90
                self.place = 23
            elif x > 85 and x < 95:
                self.x_coord = 90
                self.y_coord = 90
                self.place = 24

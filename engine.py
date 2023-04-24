### Model

## Constants

AIR, PLAYER, BOX, GOAL, WALL, FBOX, BARRIER = range(7)
MAP_WIDTH = 20
MAP_HEIGHT = 16

class SokobanCore:
    solids = [WALL, BARRIER]
    movable = [BOX, FBOX]

    def __init__(self):
        self.player_x = 0
        self.player_y = 0
        self.moves = 0
        self.map = [0] * (MAP_WIDTH * MAP_HEIGHT)

    ## Helper functions

    # function for turning a 2 dimensional coordinate into a 1 dimensional index
    def i_getIndex(self, x, y):
        return (y * MAP_WIDTH + x)

    def i_getCell(self, x,y):
        return self.map[self.i_getIndex(x,y)]

    def b_checkWin(self):
        score = 0
        # Boxes in correct places are weighed differently compared to incorrect boxes
        # Level is finished once the score returns negative

        for i in self.map:
            if i == FBOX: score -= 1
            elif i == BOX: score += 100
        return (score < 0)
    
    def b_boundsCheck(self, x, y):
        return (x < MAP_WIDTH and y < MAP_HEIGHT and x > 0 and y > 0)

    ## ---

    def m_loadLvl(self, level):
        for y in range(MAP_HEIGHT):
            for x in range(MAP_WIDTH):
                index = self.i_getIndex(x,y)
                value = level[index]
                
                self.map[index] = BARRIER

                if value == PLAYER:
                    self.player_x = x
                    self.player_y = y
                    self.map[index] = AIR
                else:
                    self.map[index] = value

    # Treating this as a black box function would make life a whole lot easier
    # But the idea is:
    # Get the new position, and check if it's valid.
    # If it's solid, there is no movement, return False
    # If it's free, move it
    #   - If moving the player, the player doesn't actually exist in the map, so no modification is done
    #   - If moving the box, modify the map
    # If it's movable, do the same process for the cell.

    def b_move_player(self, dx, dy):
        o_pos = (self.player_x, self.player_y)
        self.player_x += dx
        self.player_y += dy
        ontop = self.i_getCell(self.player_x, self.player_y)
        if ontop in self.solids or not self.b_boundsCheck(self.player_x, self.player_y):
            self.player_x, self.player_y = o_pos
            return False
        elif ontop in self.movable:
            b_pos = (self.player_x+dx, self.player_y+dy)
            b_ontop = self.i_getCell(*b_pos)
            if b_ontop == AIR or b_ontop == GOAL:
                self.map[self.i_getIndex(b_pos[0]-dx, b_pos[1]-dy)] = GOAL if ontop == FBOX else AIR
                self.map[self.i_getIndex(*b_pos)] = BOX if b_ontop == AIR else FBOX
            else:
                self.player_x, self.player_y = o_pos
                return False
        return True
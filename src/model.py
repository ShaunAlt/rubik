# =============================================================================
# Created By: Shaun Altmann
# =============================================================================
'''
Rubik's Cube Model
-
Contains objects for a rubik's cube which can be used for creating and
manipulating various rubik's cubes.

Notes:
- Cube Orientations:
    - Hold the cube with white on top, red in front, and blue on the right.
    - The positive X axis is to the right (coming out of the blue center).
    - The positive Y axis is to the top (coming out of the white center).
    - The positive Z axis is to the front (coming out of the red center).
    - A positive rotation along an axis is counter-clockwise, where the axis
        of rotation is pointing toward the user.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for generic object
from ._src import (
    _COLOUR,
    _COLOUR_PIECE_CUBE,
    _DATA,
    _POS,
    COLOURS,
    OBJ,
)

# used for creating copies of objects
from copy import deepcopy


# =============================================================================
# Cube Models
# =============================================================================

# ====
# Cube
class Cube(OBJ):
    '''
    Rubik's Cube
    -
    NxNxN rubik's cube.

    Attributes
    -
    - coord_vals : `list[float]`
        - List of all the possible values `Cube_Piece` coordinates can be.
    - edge_val : `float`
        - Coordinate value of the edge of the cube.
    - pcs : `list[Cube_Piece]`
        - List of `Cube_Piece` instances that make up the cube.
    - size : `int`
        - Size of the cube.
    
    Methods
    -
    - _get_data(short=False) : `_DATA`
        - `OBJ` Instance Method.
        - Gets all data from the current instance of the object.
    '''

    # ===========
    # Constructor
    def __init__(
            self, 
            size: int = 3
    ) -> None:
        # validating parameters
        if not isinstance(size, int):
            raise TypeError(
                f'Cube.__init__(): size must be an integer, got {type(size)}.'
            )
        if size < 2:
            raise ValueError(
                f'Cube.__init__(): size must be greater than 1, got {size}.'
            )
        
        # initializing attributes
        self.coord_vals: list[float] = []
        self.edge_val: float = 0
        self.odd: bool = self.size % 2 == 1
        self.pcs: list[Cube_Piece] = []
        self.size: int = size

        # setting cube limits + coordinate values
        if not self.odd:
            self.edge_val = (size // 2) - 0.5
            self.coord_vals = [
                (i//10)+0.5
                for i in range(
                    int(-10*self.edge_val),
                    int(10*self.edge_val)
                )
            ]
        else:
            self.edge_val = (size - 1) // 2
            self.coord_vals = [
                i
                for i in range(
                    int(-1*self.edge_val),
                    int(self.edge_val + 1)
                )
            ]

        # create cube pieces
        for i in self.coord_vals:
            for j in self.coord_vals:
                for k in self.coord_vals:
                    # skip all non-visible pieces
                    if not (
                            (abs(i) == self.edge_val)
                            or (abs(j) == self.edge_val)
                            or (abs(k) == self.edge_val)
                    ): continue

                    # create cube piece
                    self.pcs.append(Cube_Piece(
                        pos = (i, j, k),
                        col_xp = {
                            True: COLOURS.CUBE.B, 
                            False: None
                        }[i == self.edge_val],
                        col_xn = {
                            True: COLOURS.CUBE.G, 
                            False: None
                        }[i == -1*self.edge_val],
                        col_yp = {
                            True: COLOURS.CUBE.W, 
                            False: None
                        }[j == self.edge_val],
                        col_yn = {
                            True: COLOURS.CUBE.Y, 
                            False: None
                        }[j == -1*self.edge_val],
                        col_zp = {
                            True: COLOURS.CUBE.R, 
                            False: None
                        }[k == self.edge_val],
                        col_zn = {
                            True: COLOURS.CUBE.O, 
                            False: None
                        }[k == -1*self.edge_val]
                    ))

    # ======================
    # Cube Prettified Layout
    @property
    def layout(self) -> str:
        ''' Cube Prettified Layout. '''
        return ''
    
    # ==================================
    # Cube Prettified Layout - Back Face
    @property
    def layout_back(self) -> str:
        ''' Cube Prettified Layout - Back Face. '''
        return ''
    
    # ==================================
    # Cube Prettified Layout - Down Face
    @property
    def layout_down(self) -> str:
        ''' Cube Prettified Layout - Down Face. '''
        return ''
    
    # ===================================
    # Cube Prettified Layout - Front Face
    @property
    def layout_front(self) -> str:
        ''' Cube Prettified Layout - Front Face. '''
        return ''
    
    # ==================================
    # Cube Prettified Layout - Left Face
    @property
    def layout_left(self) -> str:
        ''' Cube Prettified Layout - Left Face. '''
        return ''
    
    # ===================================
    # Cube Prettified Layout - Right Face
    @property
    def layout_right(self) -> str:
        ''' Cube Prettified Layout - Right Face. '''
        return ''
    
    # =================================
    # Cube Prettified Layout - Top Face
    @property
    def layout_top(self) -> str:
        ''' Cube Prettified Layout - Top Face. '''
        return ''

    # =============
    # OBJ: Get Data
    def _get_data(
            self,
            short: bool = False
    ) -> _DATA:
        if short:
            return {
                'size': self.size,
            }
        return {
            'coord_vals': self.coord_vals,
            'edge_val': self.edge_val,
            'pcs': self.pcs,
            'size': self.size,
        }
    
    # ================
    # Get Layer Layout
    def _get_layout(
            self,
            layer: str
    ) -> list[list[str]]:
        '''
        Get Face Layout
        -
        Gets the colour layout of the given layer. If the `Cube` size is odd,
        will also get the single row/column reaching outwards of the layer in
        each direction to the center of the adjacent layers. If the `Cube` size
        is even, will get the 2 central row/columns reaching outwards of the
        layer in each direction to the center of the adjacent layers.

        Parameters
        -
        - layer : `str`
            - Letter value of the layer to get the colour layout for.
            - Valid Options:
                - `"B"` - Back Layer.
                - `"D"` - Down Layer.
                - `"F"` - Front Layer.
                - `"L"` - Left Layer.
                - `"R"` - Right Layer.
                - `"T"` - Top Layer.

        Returns
        -
        - `list[list[str]]`
            - 2D list of all the colour values on the given layer.
        '''

        return []


# ==========
# Cube Piece
class Cube_Piece(OBJ):
    '''
    Ribuk's Cube Piece
    -
    Individual piece (cubie) within a rubik's cube.

    Attributes
    -
    - _col_xp : `_COLOUR`
        - Colour of the piece in the positive X-axis direction.
    - _col_xn : `_COLOUR`
        - Colour of the piece in the negative X-axis direction.
    - _col_yp : `_COLOUR`
        - Colour of the piece in the positive Y-axis direction.
    - _col_yn : `_COLOUR`
        - Colour of the piece in the negative Y-axis direction.
    - _col_zp : `_COLOUR`
        - Colour of the piece in the positive Z-axis direction.
    - _col_zn : `_COLOUR`
        - Colour of the piece in the negative Z-axis direction.
    - colours : `_COLOUR_PIECE_CUBE`
        - Collection of all colour values on the cube piece.
    - colours_str : `str`
        - Comma-Delimited list of all current colour values and placements of
            the current cube piece.
    - pos : `_POS`
        - X, Y, Z coordinates of the piece relative to the center of the cube.

    Methods
    -
    - _get_data(short=False) : `_DATA`
        - `OBJ` Instance Method.
        - Gets all data from the current instance of the object.
    - rotate(axis) : `None`
        - Instance Method.
        - Rotates the cube piece around the given axis.
    '''

    # ===========
    # Constructor
    def __init__(
            self,
            pos: _POS,
            col_xp: _COLOUR = None,
            col_xn: _COLOUR = None,
            col_yp: _COLOUR = None,
            col_yn: _COLOUR = None,
            col_zp: _COLOUR = None,
            col_zn: _COLOUR = None
    ) -> None:
        self._col_xp: _COLOUR = col_xp
        self._col_xn: _COLOUR = col_xn
        self._col_yp: _COLOUR = col_yp
        self._col_yn: _COLOUR = col_yn
        self._col_zp: _COLOUR = col_zp
        self._col_zn: _COLOUR = col_zn
        self.pos: _POS = pos

    # =============
    # Piece Colours
    @property
    def colours(self) -> _COLOUR_PIECE_CUBE:
        ''' Piece Colours. '''
        return (
            (self._col_xp, self._col_xn,),
            (self._col_yp, self._col_yn,),
            (self._col_zp, self._col_zn,),
        )
    @colours.setter
    def colours(self, data: _COLOUR_PIECE_CUBE) -> None:
        (
            (self._col_xp, self._col_xn,),
            (self._col_yn, self._col_yn,),
            (self._col_zp, self._col_zn,),
        ) = data

    # ======================
    # Piece Colours - String
    @property
    def colours_str(self) -> str:
        ''' Piece Colours - String Format. '''
        return ', '.join([
            f'{f}: {c}'
            for f, c in [
                ('Front', self._col_zp),
                ('Back', self._col_zn),
                ('Left', self._col_xn),
                ('Right', self._col_xp),
                ('Top', self._col_yp),
                ('Down', self._col_yn),
            ]
        ])
    
    # =============
    # OBJ: Get Data
    def _get_data(self, short: bool = False) -> _DATA:
        if short:
            return {
                'pos': self.pos,
                'colours': self.colours_str,
            }
        return {
            'pos': self.pos,
            'colours': self.colours,
            'colours_str': self.colours_str,
        }

    # ======
    # Rotate
    def rotate(
            self,
            axis: str
    ) -> None:
        '''
        Rotate
        -
        Rotates the cube piece around the given axis.

        Parameters
        -
        - axis : `str`
            - Axis to rotate the piece around.
            - Valid Options:
                - `"x"` : X-Axis Rotation.
                - `"y"` : Y-Axis Rotation.
                - `"z"` : Z-Axis Rotation.

        Returns
        -
        None
        '''

        # validate axis
        if not axis in ['x', 'y', 'z']:
            raise ValueError(
                'Cube_Piece.rotate(): axis must be in ["x", "y", "z"], got' \
                + f'{axis}'
            )
        
        # rotate position
        #  x' = (x, -z, y)
        #  y' = (z, y, -x)
        #  z' = (-y, x, z)
        self.pos = {
            "x": (self.pos[0], -1*self.pos[2], self.pos[1]),
            "y": (self.pos[2], self.pos[1], -1*self.pos[0]),
            "z": (-1*self.pos[1], self.pos[0], self.pos[2]),
        }[axis]

        # move colours
        #  x': +y -> +z
        #  y': +z -> +x
        #  z': +x -> +y
        self.colours = {
            "x": (
                self.colours[0],
                (self.colours[2][1], self.colours[2][0]),
                (self.colours[1][0], self.colours[1][1]),
            ),
            "y": (
                (self.colours[2][0], self.colours[2][1]),
                self.colours[1],
                (self.colours[0][1], self.colours[0][0]),
            ),
            "z": (
                (self.colours[1][1], self.colours[1][0]),
                (self.colours[0][0], self.colours[0][1]),
                self.colours[2],
            )
        }[axis]


'''

    - The centers of the cube are as follows: (X, Y, Z)
        - Center: (0, 0, 0)
        - White (Top) Center: (0, 1, 0)
        - Red (Front) Center: (0, 0, 1)
        - Blue (Right) Center: (1, 0, 0)
        - Green (Left) Center: (-1, 0, 0)
        - Orange (Back) Center: (0, 0, -1)
        - Yellow (Down) Center: (0, -1, 0)
'''


# =============================================================================
# End of File
# =============================================================================

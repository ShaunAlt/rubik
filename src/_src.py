# =============================================================================
# Created By: Shaun Altmann
# =============================================================================
'''
Rubik's Cube Model Source Module
-
Contains constants, type definitions, functions, and base objects for the
Rubik's Cube Model.
'''
# =============================================================================

# =============================================================================
# Imports
# =============================================================================

# used for type hinting
from typing import (
    Any,
)


# =============================================================================
# Type Definitions
# =============================================================================
_COLOUR = tuple[int, str] | None
_COLOUR_PIECE_CUBE = tuple[
    tuple[_COLOUR, _COLOUR], # X Positive, X Negative
    tuple[_COLOUR, _COLOUR], # Y Positive, Y Negative
    tuple[_COLOUR, _COLOUR], # Z Positive, Z Negative
]
_DATA = dict[str, Any]
_POS = tuple[float, float, float]


# =============================================================================
# Constant Definitions
# =============================================================================

# ==========================
# Pre-Set Colour Definitions
class COLOURS():
    ''' Pre-Set Colour Definitions. '''

    # =======================
    # Cube Colour Definitions
    class CUBE():
        ''' Cube Colour Definitions. '''

        B = (2, 'B')
        G = (3, 'G')
        O = (4, 'O')
        R = (1, 'R')
        W = (0, 'W')
        Y = (5, 'Y')
        ALL = [B, G, O, R, W, Y]

# ====================
# Movement Definitions
class MOVES():
    ''' Pre-Defined Movements for solving particular positions. '''

    # ====================
    # 3x3x3 Cube Solutions
    class C3():
        ''' 3x3x3 Cube Solutions. '''

        # ==============
        # First 2 Layers
        class F2():
            ''' 
            First 2 Layers. 
            
            For this class, yellow on top, blue in front, red to right. Solving
            for the Red/Blue 2-piece combination.
            '''

            # ========================
            # Corner Bottom - Edge Top
            class CB_ET():
                '''
                Corner Bottom - Edge Top

                Corner in target position (not necessarily oriented correctly),
                edge piece in top layer.
                '''

                CB_ER = "(R U' R') (U R U' R')"
                ''' Corner white facing blue, edge above red matching face. '''

                CB_EB = "(F' U' F) (U F' U' F)"
                ''' Corner white facing blue, edge above blue matching face.'''

                CP_EB = "(U R U' R') (U' F' U F)"
                ''' Corner correct, edge above blue matching face. '''

                CP_ER = "(U' F' U F) (U R U' R')"
                ''' Corner correct, edge above red matching face. '''

                CR_EB = "(F' U F) (U' F' U F)"
                ''' Corner white facing red, edge above blue matching face. '''

                CR_ER = "(R U R') (U' R U R')"
                ''' Corner white facing red, edge above red matching face. '''

            # ===========================
            # Corner Bottom - Edge Middle
            class CB_EM():
                '''
                Corner Bottom - Edge Middle
                
                Corner in target position (not necessarily oriented correctly),
                edge piece in target position (not necessarily oriented
                correctly).
                '''

                CB_EF = "(R U' R' d R' U' R) (U' R' U' R)"
                ''' Corner white facing blue, edge flipped. '''

                CB_EP = "(R U' R' U' R U R') (U' R U2 R')"
                ''' Corner white facing blue, edge correct. '''

                CP_EF = "(R U' R' d R' U2 R) (U R' U2 R)"
                ''' Corner correct, edge flipped. '''

                CR_EF = "(R U R' U' R U' R') (U d R' U' R)"
                ''' Corner white facing red, edge flipped. '''

                CR_EP = "(R U' R' U R U2 R') (U R U' R')"
                ''' Corner white facing red, edge correct. '''

            # ========================
            # Corner Top - Edge Middle
            class CT_EM():
                '''
                Corner Top - Edge Middle

                Corner in top layer, directly above the target position, edge
                piece in target position (not necessarily oriented correctly).
                '''

                CB_EF = "(U' R U R') (d R' U' R)"
                ''' Corner white facing blue, edge flipped. '''

                CB_EP = "(U' R U' R') (U' R U2 R')"
                ''' Corner white facing blue, edge correct. '''

                CR_EF = "(U F' U' F) (d' F U F')"
                ''' Corner white facing red, edge flipped. '''

                CR_EP = "(U F' U F) (U F' U2 F)"
                ''' Corner white facing red, edge correct. '''

                CY_EF = "(R U' R') (d R' U R)"
                ''' Corner white facing yellow, edge flipped. '''

                CY_EP = "(R U R' U') (R U R' U') (R U R')"
                ''' Corner white facing yellow, edge correct. '''

            # ==============================================
            # Corner Top - Edge Top - White Facing Sidewards
            class CT_ET_WS():
                '''
                Corner Top - Edge Top - White Facing Sidewards

                Corner in top layer, directly above the target position and the
                white face of the piece is facing towards either the blue or
                red side. Edge piece also in the top layer.
                '''

                CB_EBB = "(U F' U F U') (F' U' F)"
                ''' Corner white facing blue, edge blue facing blue. '''

                CB_EBG = "(U F' U' F U') (F' U' F)"
                ''' Corner white facing blue, edge blue facing green. '''

                CB_EBO = "F' U' F"
                ''' Corner white facing blue, edge blue facing orange. '''

                CB_EBR = "(U' R U2 R' U) (F' U' F)"
                ''' Corner white facing blue, edge blue facing red. '''

                CB_ERB = "(F' U F U') (d' F U F')"
                ''' Corner white facing blue, edge red facing blue. '''

                CB_ERG = "(U' R U R') (U' R U2 R')"
                ''' Corner white facing blue, edge red facing green. '''

                CB_ERO = "(U' R U2 R') (U' R U2 R')"
                ''' Corner white facing blue, edge red facing orange. '''

                CB_ERR = "U R U' R'"
                ''' Corner white facing blue, edge red facing red. '''

                CR_EBB = "U' F' U F"
                ''' Corner white facing red, edge blue facing blue. '''

                CR_EBG = "(U F' U2 F) (U F' U2 F)"
                ''' Corner white facing red, edge blue facing green. '''

                CR_EBO = "(U F' U' F) (U F' U2 F)"
                ''' Corner white facing red, edge blue facing orange. '''

                CR_EBR = "(R U' R' U) (d R' U' R)"
                ''' Corner white facing red, edge blue facing red. '''

                CR_ERB = "(U F' U2 F U') (R U R')"
                ''' Corner white facing red, edge red facing blue. '''

                CR_ERG = "R U R'"
                ''' Corner white facing red, edge red facing green. '''

                CR_ERO = "(U' R U' R' U) (R U R')"
                ''' Corner white facing red, edge red facing orange. '''

                CR_ERR = "(U' R U' R' U) (R U R')"
                ''' Corner white facing red, edge red facing red. '''

            # =======================================
            # Corner Top - Edge Top - White Facing Up
            class CT_ET_WU():
                '''
                Corner Top - Edge Top - White Facing Up

                Corner in top layer, directly above the target position and the
                white face of the piece is facing up towards the yellow side.
                Edge piece also in the top layer.
                '''

                EBB = "(F' U2 F) (U F' U' F)"
                ''' Edge blue facing blue. '''

                EBG = "(U2 F' U' F) (U' F' U F)"
                ''' Edge blue facing green. '''

                EBO = "(U' F' U2 F) (U' F' U F)"
                ''' Edge blue facing orange. '''

                EBR = "(F' U' F U) U (R' U' R U) (R' U' R)"
                ''' Edge blue facing red. '''

                ERB = "(R U R' U') U' (R U R' U') (R U R')"
                ''' Edge red facing blue. '''

                ERG = "(U R U2 R') (U R U' R')"
                ''' Edge red facing green. '''

                ERO = "(U2 R U R') (U R U' R')"
                ''' Edge red facing orange. '''

                ERR = "(R U2 R') (U' R U R')"
                ''' Edge red facing red. '''

        class O():
            '''
            Orientation of the Last Layer
            

            For this class, yellow on top. Each constant will be described with
            a 3x3 grid. Arrow in each grid space indicates the direction of the
            yellow face, with hashtag indicating the yellow is on top.

            Documentation Notes:
            - `&darr;` is used to indicate a down arrow.
            - `&larr;` is used to indicate a left arrow.
            - `&rarr;` is used to indicate a right arrow.
            - `&uarr;` is used to indicate an up arrow.
            '''

            # ====
            # Dots
            class Dots():
                ''' Dots. '''

                SINGLE_1 = "(R U2 R') (R' F R F') U2 (R' F R F')"
                '''
                Central Dot Only
                |        |        |        |
                | :----- | :----- | :----- |
                | &larr; | &uarr; | &rarr; |
                | &larr; | #      | &rarr; |
                | &larr; | &darr; | &rarr; |
                '''

                SINGLE_2 = "F (R U R' U') F' f (R U R' U') f'"
                '''
                Central Dot Only
                |        |        |        |
                | :----- | :----- | :----- |
                | &larr; | &uarr; | &uarr; |
                | &larr; | #      | &rarr; |
                | &larr; | &darr; | &darr; |
                '''

                DOUBLE_1 = "f (R U R' U') f' U' F (R U R' U') F'"
                '''
                Central Dot + 1 Corner
                |        |        |        |
                | :----- | :----- | :----- |
                | &uarr; | &uarr; | &rarr; |
                | &larr; | #      | &rarr; |
                | &larr; | &darr; | #      |
                '''


# =============================================================================
# Generic Object Definition
# =============================================================================
class OBJ(object):
    '''
    Generic Object Definition
    -
    Contains the basic information that all objects in this module contain.

    Attributes
    -
    None

    Methods
    -
    - _get_data(short=False) : `_DATA`
        - Instance Method.
        - Gets all data from the current instance of the object.
    '''

    # ========
    # Get Data
    def _get_data(
            self,
            short: bool = False
    ) -> _DATA:
        '''
        Get Data
        -
        Gets all data from the current instance of the object.

        Parameters
        -
        - short : `bool`
            - Whether or not to return only the shortened version of the data.

        Returns
        -
        - `_DATA`
            - Object instance data.
        '''

        raise NotImplementedError(
            'OBJ._get_data() must be implemented in subclasses.'
        )
    
    # ===================
    # Long Representation
    def __repr__(self) -> str:
        '''
        Long Representation
        -
        Returns a string representation of the current instance of the object
        in a long (multi-line) representation.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - Long string representation of the current instance of the object.
        '''

        cls_name: str = self.__class__.__name__
        output: str = f'<{cls_name}>'
        for key, val in self._get_data().items():
            val_str: str = str(val)
            if isinstance(val, list):
                val_str = (
                    '[' \
                    + (',\n\t\t'.join([str(sub_val) for sub_val in val])) \
                    + ']'
                )
            output += f'\n\t{key} = {val_str}'

        return output + f'\n</{cls_name}>'
    
    # ====================
    # Short Representation
    def __str__(self) -> str:
        '''
        Short Representation
        -
        Returns a string representation of the current instance of the object
        in a short (single-line) representation.

        Parameters
        -
        None

        Returns
        -
        - `str`
            - Short string representation of the current instance of the
                object.
        '''

        output: str = (
            f'<{self.__class__.__name__}' \
            + (
                ', '.join([
                    f'{key} = {val}' 
                    for key, val 
                    in self._get_data(True).items()
                ])
            ) \
            + ' />'
        )

        return output


# =============================================================================
# End of File
# =============================================================================
